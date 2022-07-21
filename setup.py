from setuptools import setup, find_packages  # noqa: H301

NAME = "shotstack-sdk"
VERSION = "0.2.5"
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
    long_description_content_type="text/markdown",
    long_description="""\
    Shotstack is a video, image and audio editing service that allows for the automated generation of videos, images and audio using JSON 
    and a RESTful API. You arrange and configure an edit and POST it to the API which will render your media and provide a file 
    location when complete.
    
    For more details visit [shotstack.io](https://shotstack.io) or checkout our 
    [getting started](https://shotstack.gitbook.io/docs/guides/getting-started) documentation.

    View the GitHub repo for full [SDK documentation](https://github.com/shotstack/shotstack-sdk-python/).
    """
)
