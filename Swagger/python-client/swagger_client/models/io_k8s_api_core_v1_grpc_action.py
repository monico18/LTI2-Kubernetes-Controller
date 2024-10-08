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


class IoK8sApiCoreV1GRPCAction(object):
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
        'port': 'int',
        'service': 'str'
    }

    attribute_map = {
        'port': 'port',
        'service': 'service'
    }

    def __init__(self, port=None, service=None, _configuration=None):  # noqa: E501
        """IoK8sApiCoreV1GRPCAction - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._port = None
        self._service = None
        self.discriminator = None

        self.port = port
        if service is not None:
            self.service = service

    @property
    def port(self):
        """Gets the port of this IoK8sApiCoreV1GRPCAction.  # noqa: E501

        Port number of the gRPC service. Number must be in the range 1 to 65535.  # noqa: E501

        :return: The port of this IoK8sApiCoreV1GRPCAction.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this IoK8sApiCoreV1GRPCAction.

        Port number of the gRPC service. Number must be in the range 1 to 65535.  # noqa: E501

        :param port: The port of this IoK8sApiCoreV1GRPCAction.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def service(self):
        """Gets the service of this IoK8sApiCoreV1GRPCAction.  # noqa: E501

        Service is the name of the service to place in the gRPC HealthCheckRequest (see https://github.com/grpc/grpc/blob/master/doc/health-checking.md).  If this is not specified, the default behavior is defined by gRPC.  # noqa: E501

        :return: The service of this IoK8sApiCoreV1GRPCAction.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this IoK8sApiCoreV1GRPCAction.

        Service is the name of the service to place in the gRPC HealthCheckRequest (see https://github.com/grpc/grpc/blob/master/doc/health-checking.md).  If this is not specified, the default behavior is defined by gRPC.  # noqa: E501

        :param service: The service of this IoK8sApiCoreV1GRPCAction.  # noqa: E501
        :type: str
        """

        self._service = service

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
        if issubclass(IoK8sApiCoreV1GRPCAction, dict):
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
        if not isinstance(other, IoK8sApiCoreV1GRPCAction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiCoreV1GRPCAction):
            return True

        return self.to_dict() != other.to_dict()
