# coding: utf-8

"""
    working library
    version: 0.1
"""

import sys
from setuptools import setup, find_packages

NAME = "working"
VERSION = "0.1"

#REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]
REQUIRES = []

setup(
    name=NAME,
    version=VERSION,
    description="",
    author_email="minoruhiki@gmail.com",
    url="https://github.com/m-hiki/working",
    keywords=["multithread", ""],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    """
)