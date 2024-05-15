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


class IoK8sApiAutoscalingV2ExternalMetricStatus(object):
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
        'current': 'IoK8sApiAutoscalingV2MetricValueStatus',
        'metric': 'IoK8sApiAutoscalingV2MetricIdentifier'
    }

    attribute_map = {
        'current': 'current',
        'metric': 'metric'
    }

    def __init__(self, current=None, metric=None, _configuration=None):  # noqa: E501
        """IoK8sApiAutoscalingV2ExternalMetricStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._current = None
        self._metric = None
        self.discriminator = None

        self.current = current
        self.metric = metric

    @property
    def current(self):
        """Gets the current of this IoK8sApiAutoscalingV2ExternalMetricStatus.  # noqa: E501

        current contains the current value for the given metric  # noqa: E501

        :return: The current of this IoK8sApiAutoscalingV2ExternalMetricStatus.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2MetricValueStatus
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this IoK8sApiAutoscalingV2ExternalMetricStatus.

        current contains the current value for the given metric  # noqa: E501

        :param current: The current of this IoK8sApiAutoscalingV2ExternalMetricStatus.  # noqa: E501
        :type: IoK8sApiAutoscalingV2MetricValueStatus
        """
        if self._configuration.client_side_validation and current is None:
            raise ValueError("Invalid value for `current`, must not be `None`")  # noqa: E501

        self._current = current

    @property
    def metric(self):
        """Gets the metric of this IoK8sApiAutoscalingV2ExternalMetricStatus.  # noqa: E501

        metric identifies the target metric by name and selector  # noqa: E501

        :return: The metric of this IoK8sApiAutoscalingV2ExternalMetricStatus.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2MetricIdentifier
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this IoK8sApiAutoscalingV2ExternalMetricStatus.

        metric identifies the target metric by name and selector  # noqa: E501

        :param metric: The metric of this IoK8sApiAutoscalingV2ExternalMetricStatus.  # noqa: E501
        :type: IoK8sApiAutoscalingV2MetricIdentifier
        """
        if self._configuration.client_side_validation and metric is None:
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

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
        if issubclass(IoK8sApiAutoscalingV2ExternalMetricStatus, dict):
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
        if not isinstance(other, IoK8sApiAutoscalingV2ExternalMetricStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiAutoscalingV2ExternalMetricStatus):
            return True

        return self.to_dict() != other.to_dict()
