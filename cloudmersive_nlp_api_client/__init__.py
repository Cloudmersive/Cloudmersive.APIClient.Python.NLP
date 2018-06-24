# coding: utf-8

# flake8: noqa

"""
    nlpapi

    The powerful Natural Language Processing APIs let you perform part of speech tagging, entity identification, sentence parsing, and much more to help you understand the meaning of unstructured text.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from cloudmersive_nlp_api_client.api.extract_entities_string_api import ExtractEntitiesStringApi
from cloudmersive_nlp_api_client.api.language_detection_api import LanguageDetectionApi
from cloudmersive_nlp_api_client.api.parse_string_api import ParseStringApi
from cloudmersive_nlp_api_client.api.pos_tagger_json_api import PosTaggerJsonApi
from cloudmersive_nlp_api_client.api.pos_tagger_string_api import PosTaggerStringApi
from cloudmersive_nlp_api_client.api.sentences_api import SentencesApi
from cloudmersive_nlp_api_client.api.spell_check_api import SpellCheckApi
from cloudmersive_nlp_api_client.api.words_api import WordsApi

# import ApiClient
from cloudmersive_nlp_api_client.api_client import ApiClient
from cloudmersive_nlp_api_client.configuration import Configuration
# import models into sdk package
from cloudmersive_nlp_api_client.models.check_json_response import CheckJsonResponse
from cloudmersive_nlp_api_client.models.check_sentence_json_response import CheckSentenceJsonResponse
from cloudmersive_nlp_api_client.models.correct_json_response import CorrectJsonResponse
from cloudmersive_nlp_api_client.models.correct_word_in_sentence_json_response import CorrectWordInSentenceJsonResponse
from cloudmersive_nlp_api_client.models.get_words_json_response import GetWordsJsonResponse
from cloudmersive_nlp_api_client.models.language_detection_response import LanguageDetectionResponse
from cloudmersive_nlp_api_client.models.pos_request import PosRequest
from cloudmersive_nlp_api_client.models.pos_response import PosResponse
from cloudmersive_nlp_api_client.models.pos_sentence import PosSentence
from cloudmersive_nlp_api_client.models.pos_tagged_word import PosTaggedWord
from cloudmersive_nlp_api_client.models.word_position import WordPosition