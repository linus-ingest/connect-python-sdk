# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "squareconnect"
VERSION = "0.1.0"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Official Square Connect v2 Client",
    author = "Ti-Fen Pan, James Chang",
    author_email="tpan@squareup.com, jchang@squareup.com",
    url="https://github.com/square/connect-python-sdk",
    keywords=["Swagger", "Square Connect API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    license="http://www.apache.org/licenses/LICENSE-2.0",
    include_package_data=True,
    long_description="""\
    
    """
)

