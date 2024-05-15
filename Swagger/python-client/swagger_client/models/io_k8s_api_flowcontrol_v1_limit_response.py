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


class IoK8sApiFlowcontrolV1LimitResponse(object):
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
        'queuing': 'IoK8sApiFlowcontrolV1QueuingConfiguration',
        'type': 'str'
    }

    attribute_map = {
        'queuing': 'queuing',
        'type': 'type'
    }

    def __init__(self, queuing=None, type=None, _configuration=None):  # noqa: E501
        """IoK8sApiFlowcontrolV1LimitResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._queuing = None
        self._type = None
        self.discriminator = None

        if queuing is not None:
            self.queuing = queuing
        self.type = type

    @property
    def queuing(self):
        """Gets the queuing of this IoK8sApiFlowcontrolV1LimitResponse.  # noqa: E501

        `queuing` holds the configuration parameters for queuing. This field may be non-empty only if `type` is `\"Queue\"`.  # noqa: E501

        :return: The queuing of this IoK8sApiFlowcontrolV1LimitResponse.  # noqa: E501
        :rtype: IoK8sApiFlowcontrolV1QueuingConfiguration
        """
        return self._queuing

    @queuing.setter
    def queuing(self, queuing):
        """Sets the queuing of this IoK8sApiFlowcontrolV1LimitResponse.

        `queuing` holds the configuration parameters for queuing. This field may be non-empty only if `type` is `\"Queue\"`.  # noqa: E501

        :param queuing: The queuing of this IoK8sApiFlowcontrolV1LimitResponse.  # noqa: E501
        :type: IoK8sApiFlowcontrolV1QueuingConfiguration
        """

        self._queuing = queuing

    @property
    def type(self):
        """Gets the type of this IoK8sApiFlowcontrolV1LimitResponse.  # noqa: E501

        `type` is \"Queue\" or \"Reject\". \"Queue\" means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. \"Reject\" means that requests that can not be executed upon arrival are rejected. Required.  # noqa: E501

        :return: The type of this IoK8sApiFlowcontrolV1LimitResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoK8sApiFlowcontrolV1LimitResponse.

        `type` is \"Queue\" or \"Reject\". \"Queue\" means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. \"Reject\" means that requests that can not be executed upon arrival are rejected. Required.  # noqa: E501

        :param type: The type of this IoK8sApiFlowcontrolV1LimitResponse.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

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
        if issubclass(IoK8sApiFlowcontrolV1LimitResponse, dict):
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
        if not isinstance(other, IoK8sApiFlowcontrolV1LimitResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiFlowcontrolV1LimitResponse):
            return True

        return self.to_dict() != other.to_dict()
