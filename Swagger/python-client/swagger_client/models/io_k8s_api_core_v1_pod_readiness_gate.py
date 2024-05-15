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


class IoK8sApiCoreV1PodReadinessGate(object):
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
        'condition_type': 'str'
    }

    attribute_map = {
        'condition_type': 'conditionType'
    }

    def __init__(self, condition_type=None, _configuration=None):  # noqa: E501
        """IoK8sApiCoreV1PodReadinessGate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._condition_type = None
        self.discriminator = None

        self.condition_type = condition_type

    @property
    def condition_type(self):
        """Gets the condition_type of this IoK8sApiCoreV1PodReadinessGate.  # noqa: E501

        ConditionType refers to a condition in the pod's condition list with matching type.  # noqa: E501

        :return: The condition_type of this IoK8sApiCoreV1PodReadinessGate.  # noqa: E501
        :rtype: str
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type):
        """Sets the condition_type of this IoK8sApiCoreV1PodReadinessGate.

        ConditionType refers to a condition in the pod's condition list with matching type.  # noqa: E501

        :param condition_type: The condition_type of this IoK8sApiCoreV1PodReadinessGate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and condition_type is None:
            raise ValueError("Invalid value for `condition_type`, must not be `None`")  # noqa: E501

        self._condition_type = condition_type

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
        if issubclass(IoK8sApiCoreV1PodReadinessGate, dict):
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
        if not isinstance(other, IoK8sApiCoreV1PodReadinessGate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiCoreV1PodReadinessGate):
            return True

        return self.to_dict() != other.to_dict()
