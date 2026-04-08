#!/usr/bin/env bash
set -euo pipefail

# Post-generation patches for the Python SDK.
#
# These patches fix issues with openapi-generator v5.4.0's Python output:
# 1. Discriminator safety check: prevents KeyError when discriminator property
#    is not in the attribute_map (happens with certain oneOf compositions).
# 2. Placeholder bypass: allows merge field placeholders like {{ name }} to
#    pass through type validation without errors.
#
# These patches are required until openapi-generator fixes the underlying
# Python oneOf/discriminator handling (tracked upstream).

MODEL_UTILS="shotstack_sdk/model_utils.py"

if [ ! -f "${MODEL_UTILS}" ]; then
  echo "Warning: ${MODEL_UTILS} not found, skipping patches."
  exit 0
fi

echo "Applying post-generation patches to ${MODEL_UTILS}..."

# Patch 1: Add discriminator safety check (two locations)
# Prevents KeyError when discr_propertyname_py is not in cls.attribute_map
python3 << 'PATCH_SCRIPT'
import re

with open("shotstack_sdk/model_utils.py", "r") as f:
    content = f.read()

# The discriminator safety check needs to be added after the line that gets
# discr_propertyname_py, and before accessing cls.attribute_map[discr_propertyname_py]
DISCRIMINATOR_PATTERN = r"(discr_propertyname_py = list\(cls\.discriminator\.keys\(\)\)\[0\])\n(\s+)(discr_propertyname_js = cls\.attribute_map\[discr_propertyname_py\])"

DISCRIMINATOR_REPLACEMENT = r"""\1
\2
\2# DO NOT DELETE #
\2if not discr_propertyname_py in cls.attribute_map:
\2    return None
\2
\2\3"""

patched = re.sub(DISCRIMINATOR_PATTERN, DISCRIMINATOR_REPLACEMENT, content)

# Patch 2: Add placeholder bypass function before validate_and_convert_types
if "is_placeholder" not in patched:
    PLACEHOLDER_FUNC = '''
# DO NOT DELETE
# Custom code checks for placeholders to bypass type checking
def is_placeholder(input_value):
    if isinstance(input_value, str):
        pattern = r'\\{\\{\\s*.*\\s*\\}\\}'
        match = re.search(pattern, input_value)

        if match:
            return True

    return False

'''
    # Insert before validate_and_convert_types function
    patched = patched.replace(
        "\ndef validate_and_convert_types(",
        PLACEHOLDER_FUNC + "\ndef validate_and_convert_types("
    )

# Patch 3: Add placeholder check at start of validate_and_convert_types
if "is_placeholder(input_value)" not in patched:
    patched = patched.replace(
        '    Raises:\n        ApiTypeError\n    """',
        '    Raises:\n        ApiTypeError\n    """\n\n    # DO NO DELETE - runs placeholder check\n    if is_placeholder(input_value):\n        return input_value'
    )

with open("shotstack_sdk/model_utils.py", "w") as f:
    f.write(patched)

print("Patches applied successfully.")
PATCH_SCRIPT

echo "✓ model_utils.py patches applied."

# Patch 4: Fix missing model imports
# openapi-generator v5.4.0 generates imports for inline schemas that don't
# get their own model file (e.g., 'border' instead of 'rich_text_asset_border',
# 'model1' for anonymous inline schemas).
# Fix by commenting out the broken imports — these types are only used for
# validation hints that the discriminator safety check (Patch 1) already bypasses.
echo "Fixing missing model imports..."

python3 << 'FIX_IMPORTS'
import os, re

model_dir = "shotstack_sdk/model"
existing = set()
for f in os.listdir(model_dir):
    if f.endswith(".py") and f != "__init__.py":
        existing.add(f[:-3])

fixed_count = 0
for f in os.listdir(model_dir):
    if not f.endswith(".py"):
        continue
    path = os.path.join(model_dir, f)
    with open(path, "r") as fh:
        content = fh.read()
    original = content

    # Find and comment out imports for non-existent modules
    def fix_import(match):
        mod = match.group(1)
        if mod not in existing:
            return f"# PATCHED: missing module\n    # {match.group(0)}"
        return match.group(0)

    content = re.sub(
        r"from shotstack_sdk\.model\.(\w+) import (\w+)",
        fix_import,
        content
    )

    # Also comment out globals() assignments that reference missing classes
    # e.g., globals()['Border'] = Border
    def fix_globals(match):
        class_name = match.group(1)
        # Check if the import for this class was patched out
        if f"# PATCHED: missing module" in content and \
           f"import {class_name}" in content.split(f"globals()['{class_name}']")[0].split("# PATCHED")[-1]:
            return f"# PATCHED: missing class\n    # {match.group(0)}"
        return match.group(0)

    # Simpler approach: find all class names that were patched out and comment their globals
    patched_classes = set()
    for m in re.finditer(r"# PATCHED: missing module\n\s+# from shotstack_sdk\.model\.\w+ import (\w+)", content):
        patched_classes.add(m.group(1))

    for cls_name in patched_classes:
        content = content.replace(
            f"globals()['{cls_name}'] = {cls_name}",
            f"# PATCHED: missing class — use object as fallback for type refs\n    globals()['{cls_name}'] = object"
        )

    if content != original:
        with open(path, "w") as fh:
            fh.write(content)
        fixed_count += 1
        print(f"  Fixed imports in {f}")

print(f"Fixed {fixed_count} files with missing model imports.")
FIX_IMPORTS

echo "✓ All post-generation patches applied."
