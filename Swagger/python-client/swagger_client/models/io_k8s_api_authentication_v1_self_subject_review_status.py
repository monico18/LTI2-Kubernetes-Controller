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


class IoK8sApiAuthenticationV1SelfSubjectReviewStatus(object):
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
        'user_info': 'IoK8sApiAuthenticationV1UserInfo'
    }

    attribute_map = {
        'user_info': 'userInfo'
    }

    def __init__(self, user_info=None, _configuration=None):  # noqa: E501
        """IoK8sApiAuthenticationV1SelfSubjectReviewStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_info = None
        self.discriminator = None

        if user_info is not None:
            self.user_info = user_info

    @property
    def user_info(self):
        """Gets the user_info of this IoK8sApiAuthenticationV1SelfSubjectReviewStatus.  # noqa: E501

        User attributes of the user making this request.  # noqa: E501

        :return: The user_info of this IoK8sApiAuthenticationV1SelfSubjectReviewStatus.  # noqa: E501
        :rtype: IoK8sApiAuthenticationV1UserInfo
        """
        return self._user_info

    @user_info.setter
    def user_info(self, user_info):
        """Sets the user_info of this IoK8sApiAuthenticationV1SelfSubjectReviewStatus.

        User attributes of the user making this request.  # noqa: E501

        :param user_info: The user_info of this IoK8sApiAuthenticationV1SelfSubjectReviewStatus.  # noqa: E501
        :type: IoK8sApiAuthenticationV1UserInfo
        """

        self._user_info = user_info

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
        if issubclass(IoK8sApiAuthenticationV1SelfSubjectReviewStatus, dict):
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
        if not isinstance(other, IoK8sApiAuthenticationV1SelfSubjectReviewStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiAuthenticationV1SelfSubjectReviewStatus):
            return True

        return self.to_dict() != other.to_dict()
