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


class IoTraefikV1alpha1MiddlewareTCPSpec(object):
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
        'in_flight_conn': 'IoTraefikV1alpha1MiddlewareTCPSpecInFlightConn',
        'ip_white_list': 'IoTraefikV1alpha1MiddlewareTCPSpecIpWhiteList'
    }

    attribute_map = {
        'in_flight_conn': 'inFlightConn',
        'ip_white_list': 'ipWhiteList'
    }

    def __init__(self, in_flight_conn=None, ip_white_list=None, _configuration=None):  # noqa: E501
        """IoTraefikV1alpha1MiddlewareTCPSpec - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._in_flight_conn = None
        self._ip_white_list = None
        self.discriminator = None

        if in_flight_conn is not None:
            self.in_flight_conn = in_flight_conn
        if ip_white_list is not None:
            self.ip_white_list = ip_white_list

    @property
    def in_flight_conn(self):
        """Gets the in_flight_conn of this IoTraefikV1alpha1MiddlewareTCPSpec.  # noqa: E501


        :return: The in_flight_conn of this IoTraefikV1alpha1MiddlewareTCPSpec.  # noqa: E501
        :rtype: IoTraefikV1alpha1MiddlewareTCPSpecInFlightConn
        """
        return self._in_flight_conn

    @in_flight_conn.setter
    def in_flight_conn(self, in_flight_conn):
        """Sets the in_flight_conn of this IoTraefikV1alpha1MiddlewareTCPSpec.


        :param in_flight_conn: The in_flight_conn of this IoTraefikV1alpha1MiddlewareTCPSpec.  # noqa: E501
        :type: IoTraefikV1alpha1MiddlewareTCPSpecInFlightConn
        """

        self._in_flight_conn = in_flight_conn

    @property
    def ip_white_list(self):
        """Gets the ip_white_list of this IoTraefikV1alpha1MiddlewareTCPSpec.  # noqa: E501


        :return: The ip_white_list of this IoTraefikV1alpha1MiddlewareTCPSpec.  # noqa: E501
        :rtype: IoTraefikV1alpha1MiddlewareTCPSpecIpWhiteList
        """
        return self._ip_white_list

    @ip_white_list.setter
    def ip_white_list(self, ip_white_list):
        """Sets the ip_white_list of this IoTraefikV1alpha1MiddlewareTCPSpec.


        :param ip_white_list: The ip_white_list of this IoTraefikV1alpha1MiddlewareTCPSpec.  # noqa: E501
        :type: IoTraefikV1alpha1MiddlewareTCPSpecIpWhiteList
        """

        self._ip_white_list = ip_white_list

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
        if issubclass(IoTraefikV1alpha1MiddlewareTCPSpec, dict):
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
        if not isinstance(other, IoTraefikV1alpha1MiddlewareTCPSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoTraefikV1alpha1MiddlewareTCPSpec):
            return True

        return self.to_dict() != other.to_dict()
