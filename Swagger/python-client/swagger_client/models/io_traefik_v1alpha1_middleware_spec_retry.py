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


class IoTraefikV1alpha1MiddlewareSpecRetry(object):
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
        'attempts': 'int',
        'initial_interval': 'object'
    }

    attribute_map = {
        'attempts': 'attempts',
        'initial_interval': 'initialInterval'
    }

    def __init__(self, attempts=None, initial_interval=None, _configuration=None):  # noqa: E501
        """IoTraefikV1alpha1MiddlewareSpecRetry - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attempts = None
        self._initial_interval = None
        self.discriminator = None

        if attempts is not None:
            self.attempts = attempts
        if initial_interval is not None:
            self.initial_interval = initial_interval

    @property
    def attempts(self):
        """Gets the attempts of this IoTraefikV1alpha1MiddlewareSpecRetry.  # noqa: E501

        Attempts defines how many times the request should be retried.  # noqa: E501

        :return: The attempts of this IoTraefikV1alpha1MiddlewareSpecRetry.  # noqa: E501
        :rtype: int
        """
        return self._attempts

    @attempts.setter
    def attempts(self, attempts):
        """Sets the attempts of this IoTraefikV1alpha1MiddlewareSpecRetry.

        Attempts defines how many times the request should be retried.  # noqa: E501

        :param attempts: The attempts of this IoTraefikV1alpha1MiddlewareSpecRetry.  # noqa: E501
        :type: int
        """

        self._attempts = attempts

    @property
    def initial_interval(self):
        """Gets the initial_interval of this IoTraefikV1alpha1MiddlewareSpecRetry.  # noqa: E501

        InitialInterval defines the first wait time in the exponential backoff series. The maximum interval is calculated as twice the initialInterval. If unspecified, requests will be retried immediately. The value of initialInterval should be provided in seconds or as a valid duration format, see https://pkg.go.dev/time#ParseDuration.  # noqa: E501

        :return: The initial_interval of this IoTraefikV1alpha1MiddlewareSpecRetry.  # noqa: E501
        :rtype: object
        """
        return self._initial_interval

    @initial_interval.setter
    def initial_interval(self, initial_interval):
        """Sets the initial_interval of this IoTraefikV1alpha1MiddlewareSpecRetry.

        InitialInterval defines the first wait time in the exponential backoff series. The maximum interval is calculated as twice the initialInterval. If unspecified, requests will be retried immediately. The value of initialInterval should be provided in seconds or as a valid duration format, see https://pkg.go.dev/time#ParseDuration.  # noqa: E501

        :param initial_interval: The initial_interval of this IoTraefikV1alpha1MiddlewareSpecRetry.  # noqa: E501
        :type: object
        """

        self._initial_interval = initial_interval

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
        if issubclass(IoTraefikV1alpha1MiddlewareSpecRetry, dict):
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
        if not isinstance(other, IoTraefikV1alpha1MiddlewareSpecRetry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoTraefikV1alpha1MiddlewareSpecRetry):
            return True

        return self.to_dict() != other.to_dict()
