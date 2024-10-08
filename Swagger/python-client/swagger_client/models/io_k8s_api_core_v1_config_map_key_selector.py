# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.29.4+k3s1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class IoK8sApiCoreV1ConfigMapKeySelector(object):
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
        'key': 'str',
        'name': 'str',
        'optional': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'optional': 'optional'
    }

    def __init__(self, key=None, name=None, optional=None, _configuration=None):  # noqa: E501
        """IoK8sApiCoreV1ConfigMapKeySelector - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key = None
        self._name = None
        self._optional = None
        self.discriminator = None

        self.key = key
        if name is not None:
            self.name = name
        if optional is not None:
            self.optional = optional

    @property
    def key(self):
        """Gets the key of this IoK8sApiCoreV1ConfigMapKeySelector.  # noqa: E501

        The key to select.  # noqa: E501

        :return: The key of this IoK8sApiCoreV1ConfigMapKeySelector.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this IoK8sApiCoreV1ConfigMapKeySelector.

        The key to select.  # noqa: E501

        :param key: The key of this IoK8sApiCoreV1ConfigMapKeySelector.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def name(self):
        """Gets the name of this IoK8sApiCoreV1ConfigMapKeySelector.  # noqa: E501

        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  # noqa: E501

        :return: The name of this IoK8sApiCoreV1ConfigMapKeySelector.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoK8sApiCoreV1ConfigMapKeySelector.

        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  # noqa: E501

        :param name: The name of this IoK8sApiCoreV1ConfigMapKeySelector.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def optional(self):
        """Gets the optional of this IoK8sApiCoreV1ConfigMapKeySelector.  # noqa: E501

        Specify whether the ConfigMap or its key must be defined  # noqa: E501

        :return: The optional of this IoK8sApiCoreV1ConfigMapKeySelector.  # noqa: E501
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this IoK8sApiCoreV1ConfigMapKeySelector.

        Specify whether the ConfigMap or its key must be defined  # noqa: E501

        :param optional: The optional of this IoK8sApiCoreV1ConfigMapKeySelector.  # noqa: E501
        :type: bool
        """

        self._optional = optional

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
        if issubclass(IoK8sApiCoreV1ConfigMapKeySelector, dict):
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
        if not isinstance(other, IoK8sApiCoreV1ConfigMapKeySelector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiCoreV1ConfigMapKeySelector):
            return True

        return self.to_dict() != other.to_dict()
