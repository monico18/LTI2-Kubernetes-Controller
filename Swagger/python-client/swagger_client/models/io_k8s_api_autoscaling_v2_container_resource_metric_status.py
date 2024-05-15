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


class IoK8sApiAutoscalingV2ContainerResourceMetricStatus(object):
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
        'container': 'str',
        'current': 'IoK8sApiAutoscalingV2MetricValueStatus',
        'name': 'str'
    }

    attribute_map = {
        'container': 'container',
        'current': 'current',
        'name': 'name'
    }

    def __init__(self, container=None, current=None, name=None, _configuration=None):  # noqa: E501
        """IoK8sApiAutoscalingV2ContainerResourceMetricStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._container = None
        self._current = None
        self._name = None
        self.discriminator = None

        self.container = container
        self.current = current
        self.name = name

    @property
    def container(self):
        """Gets the container of this IoK8sApiAutoscalingV2ContainerResourceMetricStatus.  # noqa: E501

        container is the name of the container in the pods of the scaling target  # noqa: E501

        :return: The container of this IoK8sApiAutoscalingV2ContainerResourceMetricStatus.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this IoK8sApiAutoscalingV2ContainerResourceMetricStatus.

        container is the name of the container in the pods of the scaling target  # noqa: E501

        :param container: The container of this IoK8sApiAutoscalingV2ContainerResourceMetricStatus.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and container is None:
            raise ValueError("Invalid value for `container`, must not be `None`")  # noqa: E501

        self._container = container

    @property
    def current(self):
        """Gets the current of this IoK8sApiAutoscalingV2ContainerResourceMetricStatus.  # noqa: E501

        current contains the current value for the given metric  # noqa: E501

        :return: The current of this IoK8sApiAutoscalingV2ContainerResourceMetricStatus.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2MetricValueStatus
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this IoK8sApiAutoscalingV2ContainerResourceMetricStatus.

        current contains the current value for the given metric  # noqa: E501

        :param current: The current of this IoK8sApiAutoscalingV2ContainerResourceMetricStatus.  # noqa: E501
        :type: IoK8sApiAutoscalingV2MetricValueStatus
        """
        if self._configuration.client_side_validation and current is None:
            raise ValueError("Invalid value for `current`, must not be `None`")  # noqa: E501

        self._current = current

    @property
    def name(self):
        """Gets the name of this IoK8sApiAutoscalingV2ContainerResourceMetricStatus.  # noqa: E501

        name is the name of the resource in question.  # noqa: E501

        :return: The name of this IoK8sApiAutoscalingV2ContainerResourceMetricStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IoK8sApiAutoscalingV2ContainerResourceMetricStatus.

        name is the name of the resource in question.  # noqa: E501

        :param name: The name of this IoK8sApiAutoscalingV2ContainerResourceMetricStatus.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(IoK8sApiAutoscalingV2ContainerResourceMetricStatus, dict):
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
        if not isinstance(other, IoK8sApiAutoscalingV2ContainerResourceMetricStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiAutoscalingV2ContainerResourceMetricStatus):
            return True

        return self.to_dict() != other.to_dict()
