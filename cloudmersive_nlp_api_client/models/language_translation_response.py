# coding: utf-8

"""
    nlpapiv2

    The powerful Natural Language Processing APIs (v2) let you perform part of speech tagging, entity identification, sentence parsing, and much more to help you understand the meaning of unstructured text.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LanguageTranslationResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'successful': 'bool',
        'translated_text_result': 'str',
        'sentence_count': 'int'
    }

    attribute_map = {
        'successful': 'Successful',
        'translated_text_result': 'TranslatedTextResult',
        'sentence_count': 'SentenceCount'
    }

    def __init__(self, successful=None, translated_text_result=None, sentence_count=None):  # noqa: E501
        """LanguageTranslationResponse - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._translated_text_result = None
        self._sentence_count = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if translated_text_result is not None:
            self.translated_text_result = translated_text_result
        if sentence_count is not None:
            self.sentence_count = sentence_count

    @property
    def successful(self):
        """Gets the successful of this LanguageTranslationResponse.  # noqa: E501

        True if the language detection operation was successful, false otherwise  # noqa: E501

        :return: The successful of this LanguageTranslationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this LanguageTranslationResponse.

        True if the language detection operation was successful, false otherwise  # noqa: E501

        :param successful: The successful of this LanguageTranslationResponse.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def translated_text_result(self):
        """Gets the translated_text_result of this LanguageTranslationResponse.  # noqa: E501

        Translated text in target language  # noqa: E501

        :return: The translated_text_result of this LanguageTranslationResponse.  # noqa: E501
        :rtype: str
        """
        return self._translated_text_result

    @translated_text_result.setter
    def translated_text_result(self, translated_text_result):
        """Sets the translated_text_result of this LanguageTranslationResponse.

        Translated text in target language  # noqa: E501

        :param translated_text_result: The translated_text_result of this LanguageTranslationResponse.  # noqa: E501
        :type: str
        """

        self._translated_text_result = translated_text_result

    @property
    def sentence_count(self):
        """Gets the sentence_count of this LanguageTranslationResponse.  # noqa: E501

        Number of sentences in input text  # noqa: E501

        :return: The sentence_count of this LanguageTranslationResponse.  # noqa: E501
        :rtype: int
        """
        return self._sentence_count

    @sentence_count.setter
    def sentence_count(self, sentence_count):
        """Sets the sentence_count of this LanguageTranslationResponse.

        Number of sentences in input text  # noqa: E501

        :param sentence_count: The sentence_count of this LanguageTranslationResponse.  # noqa: E501
        :type: int
        """

        self._sentence_count = sentence_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LanguageTranslationResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LanguageTranslationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
