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


class IoK8sApiAuthenticationV1TokenRequestStatus(object):
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
        'expiration_timestamp': 'IoK8sApimachineryPkgApisMetaV1Time',
        'token': 'str'
    }

    attribute_map = {
        'expiration_timestamp': 'expirationTimestamp',
        'token': 'token'
    }

    def __init__(self, expiration_timestamp=None, token=None, _configuration=None):  # noqa: E501
        """IoK8sApiAuthenticationV1TokenRequestStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._expiration_timestamp = None
        self._token = None
        self.discriminator = None

        self.expiration_timestamp = expiration_timestamp
        self.token = token

    @property
    def expiration_timestamp(self):
        """Gets the expiration_timestamp of this IoK8sApiAuthenticationV1TokenRequestStatus.  # noqa: E501

        ExpirationTimestamp is the time of expiration of the returned token.  # noqa: E501

        :return: The expiration_timestamp of this IoK8sApiAuthenticationV1TokenRequestStatus.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1Time
        """
        return self._expiration_timestamp

    @expiration_timestamp.setter
    def expiration_timestamp(self, expiration_timestamp):
        """Sets the expiration_timestamp of this IoK8sApiAuthenticationV1TokenRequestStatus.

        ExpirationTimestamp is the time of expiration of the returned token.  # noqa: E501

        :param expiration_timestamp: The expiration_timestamp of this IoK8sApiAuthenticationV1TokenRequestStatus.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1Time
        """
        if self._configuration.client_side_validation and expiration_timestamp is None:
            raise ValueError("Invalid value for `expiration_timestamp`, must not be `None`")  # noqa: E501

        self._expiration_timestamp = expiration_timestamp

    @property
    def token(self):
        """Gets the token of this IoK8sApiAuthenticationV1TokenRequestStatus.  # noqa: E501

        Token is the opaque bearer token.  # noqa: E501

        :return: The token of this IoK8sApiAuthenticationV1TokenRequestStatus.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this IoK8sApiAuthenticationV1TokenRequestStatus.

        Token is the opaque bearer token.  # noqa: E501

        :param token: The token of this IoK8sApiAuthenticationV1TokenRequestStatus.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

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
        if issubclass(IoK8sApiAuthenticationV1TokenRequestStatus, dict):
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
        if not isinstance(other, IoK8sApiAuthenticationV1TokenRequestStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiAuthenticationV1TokenRequestStatus):
            return True

        return self.to_dict() != other.to_dict()
