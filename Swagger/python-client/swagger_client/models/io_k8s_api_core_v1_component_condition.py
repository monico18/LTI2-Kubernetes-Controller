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


class IoK8sApiCoreV1ComponentCondition(object):
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
        'error': 'str',
        'message': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'error': 'error',
        'message': 'message',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, error=None, message=None, status=None, type=None, _configuration=None):  # noqa: E501
        """IoK8sApiCoreV1ComponentCondition - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._error = None
        self._message = None
        self._status = None
        self._type = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if message is not None:
            self.message = message
        self.status = status
        self.type = type

    @property
    def error(self):
        """Gets the error of this IoK8sApiCoreV1ComponentCondition.  # noqa: E501

        Condition error code for a component. For example, a health check error code.  # noqa: E501

        :return: The error of this IoK8sApiCoreV1ComponentCondition.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this IoK8sApiCoreV1ComponentCondition.

        Condition error code for a component. For example, a health check error code.  # noqa: E501

        :param error: The error of this IoK8sApiCoreV1ComponentCondition.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def message(self):
        """Gets the message of this IoK8sApiCoreV1ComponentCondition.  # noqa: E501

        Message about the condition for a component. For example, information about a health check.  # noqa: E501

        :return: The message of this IoK8sApiCoreV1ComponentCondition.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this IoK8sApiCoreV1ComponentCondition.

        Message about the condition for a component. For example, information about a health check.  # noqa: E501

        :param message: The message of this IoK8sApiCoreV1ComponentCondition.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def status(self):
        """Gets the status of this IoK8sApiCoreV1ComponentCondition.  # noqa: E501

        Status of the condition for a component. Valid values for \"Healthy\": \"True\", \"False\", or \"Unknown\".  # noqa: E501

        :return: The status of this IoK8sApiCoreV1ComponentCondition.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IoK8sApiCoreV1ComponentCondition.

        Status of the condition for a component. Valid values for \"Healthy\": \"True\", \"False\", or \"Unknown\".  # noqa: E501

        :param status: The status of this IoK8sApiCoreV1ComponentCondition.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def type(self):
        """Gets the type of this IoK8sApiCoreV1ComponentCondition.  # noqa: E501

        Type of condition for a component. Valid value: \"Healthy\"  # noqa: E501

        :return: The type of this IoK8sApiCoreV1ComponentCondition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoK8sApiCoreV1ComponentCondition.

        Type of condition for a component. Valid value: \"Healthy\"  # noqa: E501

        :param type: The type of this IoK8sApiCoreV1ComponentCondition.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(IoK8sApiCoreV1ComponentCondition, dict):
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
        if not isinstance(other, IoK8sApiCoreV1ComponentCondition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiCoreV1ComponentCondition):
            return True

        return self.to_dict() != other.to_dict()
