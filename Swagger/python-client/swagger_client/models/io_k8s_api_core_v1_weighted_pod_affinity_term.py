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


class IoK8sApiCoreV1WeightedPodAffinityTerm(object):
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
        'pod_affinity_term': 'IoK8sApiCoreV1PodAffinityTerm',
        'weight': 'int'
    }

    attribute_map = {
        'pod_affinity_term': 'podAffinityTerm',
        'weight': 'weight'
    }

    def __init__(self, pod_affinity_term=None, weight=None, _configuration=None):  # noqa: E501
        """IoK8sApiCoreV1WeightedPodAffinityTerm - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._pod_affinity_term = None
        self._weight = None
        self.discriminator = None

        self.pod_affinity_term = pod_affinity_term
        self.weight = weight

    @property
    def pod_affinity_term(self):
        """Gets the pod_affinity_term of this IoK8sApiCoreV1WeightedPodAffinityTerm.  # noqa: E501

        Required. A pod affinity term, associated with the corresponding weight.  # noqa: E501

        :return: The pod_affinity_term of this IoK8sApiCoreV1WeightedPodAffinityTerm.  # noqa: E501
        :rtype: IoK8sApiCoreV1PodAffinityTerm
        """
        return self._pod_affinity_term

    @pod_affinity_term.setter
    def pod_affinity_term(self, pod_affinity_term):
        """Sets the pod_affinity_term of this IoK8sApiCoreV1WeightedPodAffinityTerm.

        Required. A pod affinity term, associated with the corresponding weight.  # noqa: E501

        :param pod_affinity_term: The pod_affinity_term of this IoK8sApiCoreV1WeightedPodAffinityTerm.  # noqa: E501
        :type: IoK8sApiCoreV1PodAffinityTerm
        """
        if self._configuration.client_side_validation and pod_affinity_term is None:
            raise ValueError("Invalid value for `pod_affinity_term`, must not be `None`")  # noqa: E501

        self._pod_affinity_term = pod_affinity_term

    @property
    def weight(self):
        """Gets the weight of this IoK8sApiCoreV1WeightedPodAffinityTerm.  # noqa: E501

        weight associated with matching the corresponding podAffinityTerm, in the range 1-100.  # noqa: E501

        :return: The weight of this IoK8sApiCoreV1WeightedPodAffinityTerm.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this IoK8sApiCoreV1WeightedPodAffinityTerm.

        weight associated with matching the corresponding podAffinityTerm, in the range 1-100.  # noqa: E501

        :param weight: The weight of this IoK8sApiCoreV1WeightedPodAffinityTerm.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and weight is None:
            raise ValueError("Invalid value for `weight`, must not be `None`")  # noqa: E501

        self._weight = weight

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
        if issubclass(IoK8sApiCoreV1WeightedPodAffinityTerm, dict):
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
        if not isinstance(other, IoK8sApiCoreV1WeightedPodAffinityTerm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiCoreV1WeightedPodAffinityTerm):
            return True

        return self.to_dict() != other.to_dict()
