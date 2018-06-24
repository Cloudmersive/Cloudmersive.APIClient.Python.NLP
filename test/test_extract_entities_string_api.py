# coding: utf-8

"""
    nlpapi

    The powerful Natural Language Processing APIs let you perform part of speech tagging, entity identification, sentence parsing, and much more to help you understand the meaning of unstructured text.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.api.extract_entities_string_api import ExtractEntitiesStringApi  # noqa: E501
from cloudmersive_nlp_api_client.rest import ApiException


class TestExtractEntitiesStringApi(unittest.TestCase):
    """ExtractEntitiesStringApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_nlp_api_client.api.extract_entities_string_api.ExtractEntitiesStringApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_extract_entities_string_post(self):
        """Test case for extract_entities_string_post

        Extract entities from string  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
