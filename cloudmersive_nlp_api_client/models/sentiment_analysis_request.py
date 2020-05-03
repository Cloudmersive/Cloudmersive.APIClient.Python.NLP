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


class SentimentAnalysisRequest(object):
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
        'text_to_analyze': 'str'
    }

    attribute_map = {
        'text_to_analyze': 'TextToAnalyze'
    }

    def __init__(self, text_to_analyze=None):  # noqa: E501
        """SentimentAnalysisRequest - a model defined in Swagger"""  # noqa: E501

        self._text_to_analyze = None
        self.discriminator = None

        if text_to_analyze is not None:
            self.text_to_analyze = text_to_analyze

    @property
    def text_to_analyze(self):
        """Gets the text_to_analyze of this SentimentAnalysisRequest.  # noqa: E501

        Text to analyze  # noqa: E501

        :return: The text_to_analyze of this SentimentAnalysisRequest.  # noqa: E501
        :rtype: str
        """
        return self._text_to_analyze

    @text_to_analyze.setter
    def text_to_analyze(self, text_to_analyze):
        """Sets the text_to_analyze of this SentimentAnalysisRequest.

        Text to analyze  # noqa: E501

        :param text_to_analyze: The text_to_analyze of this SentimentAnalysisRequest.  # noqa: E501
        :type: str
        """

        self._text_to_analyze = text_to_analyze

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
        if issubclass(SentimentAnalysisRequest, dict):
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
        if not isinstance(other, SentimentAnalysisRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
