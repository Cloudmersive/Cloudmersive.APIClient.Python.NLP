# coding: utf-8

"""
    nlpapiv2

    The powerful Natural Language Processing APIs (v2) let you perform part of speech tagging, entity identification, sentence parsing, and much more to help you understand the meaning of unstructured text.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.api.parse_api import ParseApi  # noqa: E501
from cloudmersive_nlp_api_client.rest import ApiException


class TestParseApi(unittest.TestCase):
    """ParseApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_nlp_api_client.api.parse_api.ParseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_parse_parse_string(self):
        """Test case for parse_parse_string

        Parse string to syntax tree  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
