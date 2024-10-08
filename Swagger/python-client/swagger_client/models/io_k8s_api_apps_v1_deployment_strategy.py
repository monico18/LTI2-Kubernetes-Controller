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


class IoK8sApiAppsV1DeploymentStrategy(object):
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
        'rolling_update': 'IoK8sApiAppsV1RollingUpdateDeployment',
        'type': 'str'
    }

    attribute_map = {
        'rolling_update': 'rollingUpdate',
        'type': 'type'
    }

    def __init__(self, rolling_update=None, type=None, _configuration=None):  # noqa: E501
        """IoK8sApiAppsV1DeploymentStrategy - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._rolling_update = None
        self._type = None
        self.discriminator = None

        if rolling_update is not None:
            self.rolling_update = rolling_update
        if type is not None:
            self.type = type

    @property
    def rolling_update(self):
        """Gets the rolling_update of this IoK8sApiAppsV1DeploymentStrategy.  # noqa: E501

        Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.  # noqa: E501

        :return: The rolling_update of this IoK8sApiAppsV1DeploymentStrategy.  # noqa: E501
        :rtype: IoK8sApiAppsV1RollingUpdateDeployment
        """
        return self._rolling_update

    @rolling_update.setter
    def rolling_update(self, rolling_update):
        """Sets the rolling_update of this IoK8sApiAppsV1DeploymentStrategy.

        Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.  # noqa: E501

        :param rolling_update: The rolling_update of this IoK8sApiAppsV1DeploymentStrategy.  # noqa: E501
        :type: IoK8sApiAppsV1RollingUpdateDeployment
        """

        self._rolling_update = rolling_update

    @property
    def type(self):
        """Gets the type of this IoK8sApiAppsV1DeploymentStrategy.  # noqa: E501

        Type of deployment. Can be \"Recreate\" or \"RollingUpdate\". Default is RollingUpdate.  Possible enum values:  - `\"Recreate\"` Kill all existing pods before creating new ones.  - `\"RollingUpdate\"` Replace the old ReplicaSets by new one using rolling update i.e gradually scale down the old ReplicaSets and scale up the new one.  # noqa: E501

        :return: The type of this IoK8sApiAppsV1DeploymentStrategy.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoK8sApiAppsV1DeploymentStrategy.

        Type of deployment. Can be \"Recreate\" or \"RollingUpdate\". Default is RollingUpdate.  Possible enum values:  - `\"Recreate\"` Kill all existing pods before creating new ones.  - `\"RollingUpdate\"` Replace the old ReplicaSets by new one using rolling update i.e gradually scale down the old ReplicaSets and scale up the new one.  # noqa: E501

        :param type: The type of this IoK8sApiAppsV1DeploymentStrategy.  # noqa: E501
        :type: str
        """
        allowed_values = ["Recreate", "RollingUpdate"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

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
        if issubclass(IoK8sApiAppsV1DeploymentStrategy, dict):
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
        if not isinstance(other, IoK8sApiAppsV1DeploymentStrategy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiAppsV1DeploymentStrategy):
            return True

        return self.to_dict() != other.to_dict()
