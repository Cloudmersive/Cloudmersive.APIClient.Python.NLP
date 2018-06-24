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
from cloudmersive_nlp_api_client.api.spell_check_api import SpellCheckApi  # noqa: E501
from cloudmersive_nlp_api_client.rest import ApiException


class TestSpellCheckApi(unittest.TestCase):
    """SpellCheckApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_nlp_api_client.api.spell_check_api.SpellCheckApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_spell_check_check_json(self):
        """Test case for spell_check_check_json

        Spell check word  # noqa: E501
        """
        pass

    def test_spell_check_check_sentence_json(self):
        """Test case for spell_check_check_sentence_json

        Check if sentence is spelled correctly  # noqa: E501
        """
        pass

    def test_spell_check_check_sentence_string(self):
        """Test case for spell_check_check_sentence_string

        Spell check a sentence  # noqa: E501
        """
        pass

    def test_spell_check_correct(self):
        """Test case for spell_check_correct

        Find spelling corrections  # noqa: E501
        """
        pass

    def test_spell_check_correct_json(self):
        """Test case for spell_check_correct_json

        Find spelling corrections  # noqa: E501
        """
        pass

    def test_spell_check_post(self):
        """Test case for spell_check_post

        Spell check a word  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
