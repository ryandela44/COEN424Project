# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Smart Checkout",
    author_email="",
    url="",
    keywords=["Swagger", "Smart Checkout"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    In this course, we are working in groups of 4 or less members on a final project that runs on the Cloud. Our project is to develop a service that has targeted users and with specific functions. This service is accessible on the Internet. Its design follows RESTful architecture style that runs on a Cloud platform and meets the project requirements. The service interface is defined using SwaggerHub open APIs.
    """
)
