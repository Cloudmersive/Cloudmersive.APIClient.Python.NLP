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


class Entity(object):
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
        'entity_type': 'str',
        'entity_text': 'str'
    }

    attribute_map = {
        'entity_type': 'EntityType',
        'entity_text': 'EntityText'
    }

    def __init__(self, entity_type=None, entity_text=None):  # noqa: E501
        """Entity - a model defined in Swagger"""  # noqa: E501

        self._entity_type = None
        self._entity_text = None
        self.discriminator = None

        if entity_type is not None:
            self.entity_type = entity_type
        if entity_text is not None:
            self.entity_text = entity_text

    @property
    def entity_type(self):
        """Gets the entity_type of this Entity.  # noqa: E501


        :return: The entity_type of this Entity.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this Entity.


        :param entity_type: The entity_type of this Entity.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

    @property
    def entity_text(self):
        """Gets the entity_text of this Entity.  # noqa: E501


        :return: The entity_text of this Entity.  # noqa: E501
        :rtype: str
        """
        return self._entity_text

    @entity_text.setter
    def entity_text(self, entity_text):
        """Sets the entity_text of this Entity.


        :param entity_text: The entity_text of this Entity.  # noqa: E501
        :type: str
        """

        self._entity_text = entity_text

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
        if issubclass(Entity, dict):
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
        if not isinstance(other, Entity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
