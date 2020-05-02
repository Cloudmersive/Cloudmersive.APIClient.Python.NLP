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

from cloudmersive_nlp_api_client.models.rephrased_sentence_option import RephrasedSentenceOption  # noqa: F401,E501


class RephrasedSentence(object):
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
        'sentence_index': 'int',
        'original_sentence_text': 'str',
        'rephrasings': 'list[RephrasedSentenceOption]'
    }

    attribute_map = {
        'sentence_index': 'SentenceIndex',
        'original_sentence_text': 'OriginalSentenceText',
        'rephrasings': 'Rephrasings'
    }

    def __init__(self, sentence_index=None, original_sentence_text=None, rephrasings=None):  # noqa: E501
        """RephrasedSentence - a model defined in Swagger"""  # noqa: E501

        self._sentence_index = None
        self._original_sentence_text = None
        self._rephrasings = None
        self.discriminator = None

        if sentence_index is not None:
            self.sentence_index = sentence_index
        if original_sentence_text is not None:
            self.original_sentence_text = original_sentence_text
        if rephrasings is not None:
            self.rephrasings = rephrasings

    @property
    def sentence_index(self):
        """Gets the sentence_index of this RephrasedSentence.  # noqa: E501

        Index of the sentence, 1-based, ordered  # noqa: E501

        :return: The sentence_index of this RephrasedSentence.  # noqa: E501
        :rtype: int
        """
        return self._sentence_index

    @sentence_index.setter
    def sentence_index(self, sentence_index):
        """Sets the sentence_index of this RephrasedSentence.

        Index of the sentence, 1-based, ordered  # noqa: E501

        :param sentence_index: The sentence_index of this RephrasedSentence.  # noqa: E501
        :type: int
        """

        self._sentence_index = sentence_index

    @property
    def original_sentence_text(self):
        """Gets the original_sentence_text of this RephrasedSentence.  # noqa: E501

        Original input sentence text  # noqa: E501

        :return: The original_sentence_text of this RephrasedSentence.  # noqa: E501
        :rtype: str
        """
        return self._original_sentence_text

    @original_sentence_text.setter
    def original_sentence_text(self, original_sentence_text):
        """Sets the original_sentence_text of this RephrasedSentence.

        Original input sentence text  # noqa: E501

        :param original_sentence_text: The original_sentence_text of this RephrasedSentence.  # noqa: E501
        :type: str
        """

        self._original_sentence_text = original_sentence_text

    @property
    def rephrasings(self):
        """Gets the rephrasings of this RephrasedSentence.  # noqa: E501

        Rephrasing text options, candidates of the original input sentence, in order - with best candidate first  # noqa: E501

        :return: The rephrasings of this RephrasedSentence.  # noqa: E501
        :rtype: list[RephrasedSentenceOption]
        """
        return self._rephrasings

    @rephrasings.setter
    def rephrasings(self, rephrasings):
        """Sets the rephrasings of this RephrasedSentence.

        Rephrasing text options, candidates of the original input sentence, in order - with best candidate first  # noqa: E501

        :param rephrasings: The rephrasings of this RephrasedSentence.  # noqa: E501
        :type: list[RephrasedSentenceOption]
        """

        self._rephrasings = rephrasings

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
        if issubclass(RephrasedSentence, dict):
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
        if not isinstance(other, RephrasedSentence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other