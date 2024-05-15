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


class IoK8sApiNodeV1Overhead(object):
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
        'pod_fixed': 'dict(str, IoK8sApimachineryPkgApiResourceQuantity)'
    }

    attribute_map = {
        'pod_fixed': 'podFixed'
    }

    def __init__(self, pod_fixed=None, _configuration=None):  # noqa: E501
        """IoK8sApiNodeV1Overhead - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._pod_fixed = None
        self.discriminator = None

        if pod_fixed is not None:
            self.pod_fixed = pod_fixed

    @property
    def pod_fixed(self):
        """Gets the pod_fixed of this IoK8sApiNodeV1Overhead.  # noqa: E501

        podFixed represents the fixed resource overhead associated with running a pod.  # noqa: E501

        :return: The pod_fixed of this IoK8sApiNodeV1Overhead.  # noqa: E501
        :rtype: dict(str, IoK8sApimachineryPkgApiResourceQuantity)
        """
        return self._pod_fixed

    @pod_fixed.setter
    def pod_fixed(self, pod_fixed):
        """Sets the pod_fixed of this IoK8sApiNodeV1Overhead.

        podFixed represents the fixed resource overhead associated with running a pod.  # noqa: E501

        :param pod_fixed: The pod_fixed of this IoK8sApiNodeV1Overhead.  # noqa: E501
        :type: dict(str, IoK8sApimachineryPkgApiResourceQuantity)
        """

        self._pod_fixed = pod_fixed

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
        if issubclass(IoK8sApiNodeV1Overhead, dict):
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
        if not isinstance(other, IoK8sApiNodeV1Overhead):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiNodeV1Overhead):
            return True

        return self.to_dict() != other.to_dict()
