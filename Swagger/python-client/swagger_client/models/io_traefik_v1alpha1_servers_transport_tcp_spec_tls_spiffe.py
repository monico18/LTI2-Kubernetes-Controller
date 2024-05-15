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


class IoTraefikV1alpha1ServersTransportTCPSpecTlsSpiffe(object):
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
        'ids': 'list[str]',
        'trust_domain': 'str'
    }

    attribute_map = {
        'ids': 'ids',
        'trust_domain': 'trustDomain'
    }

    def __init__(self, ids=None, trust_domain=None, _configuration=None):  # noqa: E501
        """IoTraefikV1alpha1ServersTransportTCPSpecTlsSpiffe - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ids = None
        self._trust_domain = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if trust_domain is not None:
            self.trust_domain = trust_domain

    @property
    def ids(self):
        """Gets the ids of this IoTraefikV1alpha1ServersTransportTCPSpecTlsSpiffe.  # noqa: E501

        IDs defines the allowed SPIFFE IDs (takes precedence over the SPIFFE TrustDomain).  # noqa: E501

        :return: The ids of this IoTraefikV1alpha1ServersTransportTCPSpecTlsSpiffe.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this IoTraefikV1alpha1ServersTransportTCPSpecTlsSpiffe.

        IDs defines the allowed SPIFFE IDs (takes precedence over the SPIFFE TrustDomain).  # noqa: E501

        :param ids: The ids of this IoTraefikV1alpha1ServersTransportTCPSpecTlsSpiffe.  # noqa: E501
        :type: list[str]
        """

        self._ids = ids

    @property
    def trust_domain(self):
        """Gets the trust_domain of this IoTraefikV1alpha1ServersTransportTCPSpecTlsSpiffe.  # noqa: E501

        TrustDomain defines the allowed SPIFFE trust domain.  # noqa: E501

        :return: The trust_domain of this IoTraefikV1alpha1ServersTransportTCPSpecTlsSpiffe.  # noqa: E501
        :rtype: str
        """
        return self._trust_domain

    @trust_domain.setter
    def trust_domain(self, trust_domain):
        """Sets the trust_domain of this IoTraefikV1alpha1ServersTransportTCPSpecTlsSpiffe.

        TrustDomain defines the allowed SPIFFE trust domain.  # noqa: E501

        :param trust_domain: The trust_domain of this IoTraefikV1alpha1ServersTransportTCPSpecTlsSpiffe.  # noqa: E501
        :type: str
        """

        self._trust_domain = trust_domain

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
        if issubclass(IoTraefikV1alpha1ServersTransportTCPSpecTlsSpiffe, dict):
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
        if not isinstance(other, IoTraefikV1alpha1ServersTransportTCPSpecTlsSpiffe):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoTraefikV1alpha1ServersTransportTCPSpecTlsSpiffe):
            return True

        return self.to_dict() != other.to_dict()
