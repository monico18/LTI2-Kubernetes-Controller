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


class IoK8sApiDiscoveryV1EndpointConditions(object):
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
        'ready': 'bool',
        'serving': 'bool',
        'terminating': 'bool'
    }

    attribute_map = {
        'ready': 'ready',
        'serving': 'serving',
        'terminating': 'terminating'
    }

    def __init__(self, ready=None, serving=None, terminating=None, _configuration=None):  # noqa: E501
        """IoK8sApiDiscoveryV1EndpointConditions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ready = None
        self._serving = None
        self._terminating = None
        self.discriminator = None

        if ready is not None:
            self.ready = ready
        if serving is not None:
            self.serving = serving
        if terminating is not None:
            self.terminating = terminating

    @property
    def ready(self):
        """Gets the ready of this IoK8sApiDiscoveryV1EndpointConditions.  # noqa: E501

        ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be \"true\" for terminating endpoints, except when the normal readiness behavior is being explicitly overridden, for example when the associated Service has set the publishNotReadyAddresses flag.  # noqa: E501

        :return: The ready of this IoK8sApiDiscoveryV1EndpointConditions.  # noqa: E501
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this IoK8sApiDiscoveryV1EndpointConditions.

        ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be \"true\" for terminating endpoints, except when the normal readiness behavior is being explicitly overridden, for example when the associated Service has set the publishNotReadyAddresses flag.  # noqa: E501

        :param ready: The ready of this IoK8sApiDiscoveryV1EndpointConditions.  # noqa: E501
        :type: bool
        """

        self._ready = ready

    @property
    def serving(self):
        """Gets the serving of this IoK8sApiDiscoveryV1EndpointConditions.  # noqa: E501

        serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition.  # noqa: E501

        :return: The serving of this IoK8sApiDiscoveryV1EndpointConditions.  # noqa: E501
        :rtype: bool
        """
        return self._serving

    @serving.setter
    def serving(self, serving):
        """Sets the serving of this IoK8sApiDiscoveryV1EndpointConditions.

        serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition.  # noqa: E501

        :param serving: The serving of this IoK8sApiDiscoveryV1EndpointConditions.  # noqa: E501
        :type: bool
        """

        self._serving = serving

    @property
    def terminating(self):
        """Gets the terminating of this IoK8sApiDiscoveryV1EndpointConditions.  # noqa: E501

        terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating.  # noqa: E501

        :return: The terminating of this IoK8sApiDiscoveryV1EndpointConditions.  # noqa: E501
        :rtype: bool
        """
        return self._terminating

    @terminating.setter
    def terminating(self, terminating):
        """Sets the terminating of this IoK8sApiDiscoveryV1EndpointConditions.

        terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating.  # noqa: E501

        :param terminating: The terminating of this IoK8sApiDiscoveryV1EndpointConditions.  # noqa: E501
        :type: bool
        """

        self._terminating = terminating

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
        if issubclass(IoK8sApiDiscoveryV1EndpointConditions, dict):
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
        if not isinstance(other, IoK8sApiDiscoveryV1EndpointConditions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiDiscoveryV1EndpointConditions):
            return True

        return self.to_dict() != other.to_dict()
