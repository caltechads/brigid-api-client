from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name="brigid-api-client",
    version="0.1.0",
    description="Python API client library for Brigid",
    url="https://github.com/caltechads/brigid-api-client/",
    author="Caltech IMSS ADS",
    author_email="imss-ads-staff@caltech.edu",
    packages=find_packages(
        exclude=["*.test", "*.test.*", "test.*", "test", "bin", "*.pyc"]
    ),
    include_package_data=True,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    keywords=["devops"],
    classifiers=[
        "Programming Language :: Python :: 3"
        "Programming Language :: Python :: 3.6"
        "Programming Language :: Python :: 3.7"
    ],
    install_requires=["httpx >= 0.15.0", "attrs >= 20.1.0", "python-dateutil >= 2.8.1"],
)
