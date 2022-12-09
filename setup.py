from setuptools import setup, find_packages
from pathlib import Path

NAME = "shotstack-sdk"
VERSION = "0.2.6"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name=NAME,
    version=VERSION,
    description="Shotstack",
    author="Shotstack",
    author_email="pypi@shotstack.io",
    url="https://shotstack.io/product/sdk/python/",
    keywords=["shotstack", "video", "video editing", "video editor", "video editing api", "video generation", "video manipulation", "ffmpeg"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown"
)
