# coding: utf-8

"""
    nlpapiv2

    The powerful Natural Language Processing APIs (v2) let you perform part of speech tagging, entity identification, sentence parsing, and much more to help you understand the meaning of unstructured text.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "cloudmersive_nlp_api_client"
VERSION = "3.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="nlpapiv2",
    author_email="",
    url="https://www.cloudmersive.com/nlp-api",
    keywords=["Swagger", "nlpapiv2"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown'
    The powerful Natural Language Processing APIs (v2) let you perform part of speech tagging, entity identification, sentence parsing, and much more to help you understand the meaning of unstructured text.  # noqa: E501

)
