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


class IoK8sApiAutoscalingV1ScaleStatus(object):
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
        'replicas': 'int',
        'selector': 'str'
    }

    attribute_map = {
        'replicas': 'replicas',
        'selector': 'selector'
    }

    def __init__(self, replicas=None, selector=None, _configuration=None):  # noqa: E501
        """IoK8sApiAutoscalingV1ScaleStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._replicas = None
        self._selector = None
        self.discriminator = None

        self.replicas = replicas
        if selector is not None:
            self.selector = selector

    @property
    def replicas(self):
        """Gets the replicas of this IoK8sApiAutoscalingV1ScaleStatus.  # noqa: E501

        replicas is the actual number of observed instances of the scaled object.  # noqa: E501

        :return: The replicas of this IoK8sApiAutoscalingV1ScaleStatus.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this IoK8sApiAutoscalingV1ScaleStatus.

        replicas is the actual number of observed instances of the scaled object.  # noqa: E501

        :param replicas: The replicas of this IoK8sApiAutoscalingV1ScaleStatus.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and replicas is None:
            raise ValueError("Invalid value for `replicas`, must not be `None`")  # noqa: E501

        self._replicas = replicas

    @property
    def selector(self):
        """Gets the selector of this IoK8sApiAutoscalingV1ScaleStatus.  # noqa: E501

        selector is the label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by clients. The string will be in the same format as the query-param syntax. More info about label selectors: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/  # noqa: E501

        :return: The selector of this IoK8sApiAutoscalingV1ScaleStatus.  # noqa: E501
        :rtype: str
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this IoK8sApiAutoscalingV1ScaleStatus.

        selector is the label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by clients. The string will be in the same format as the query-param syntax. More info about label selectors: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/  # noqa: E501

        :param selector: The selector of this IoK8sApiAutoscalingV1ScaleStatus.  # noqa: E501
        :type: str
        """

        self._selector = selector

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
        if issubclass(IoK8sApiAutoscalingV1ScaleStatus, dict):
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
        if not isinstance(other, IoK8sApiAutoscalingV1ScaleStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiAutoscalingV1ScaleStatus):
            return True

        return self.to_dict() != other.to_dict()
