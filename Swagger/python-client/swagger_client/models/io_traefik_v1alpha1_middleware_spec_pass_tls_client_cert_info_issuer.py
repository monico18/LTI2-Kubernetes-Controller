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


class IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer(object):
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
        'common_name': 'bool',
        'country': 'bool',
        'domain_component': 'bool',
        'locality': 'bool',
        'organization': 'bool',
        'province': 'bool',
        'serial_number': 'bool'
    }

    attribute_map = {
        'common_name': 'commonName',
        'country': 'country',
        'domain_component': 'domainComponent',
        'locality': 'locality',
        'organization': 'organization',
        'province': 'province',
        'serial_number': 'serialNumber'
    }

    def __init__(self, common_name=None, country=None, domain_component=None, locality=None, organization=None, province=None, serial_number=None, _configuration=None):  # noqa: E501
        """IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._common_name = None
        self._country = None
        self._domain_component = None
        self._locality = None
        self._organization = None
        self._province = None
        self._serial_number = None
        self.discriminator = None

        if common_name is not None:
            self.common_name = common_name
        if country is not None:
            self.country = country
        if domain_component is not None:
            self.domain_component = domain_component
        if locality is not None:
            self.locality = locality
        if organization is not None:
            self.organization = organization
        if province is not None:
            self.province = province
        if serial_number is not None:
            self.serial_number = serial_number

    @property
    def common_name(self):
        """Gets the common_name of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501

        CommonName defines whether to add the organizationalUnit information into the issuer.  # noqa: E501

        :return: The common_name of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501
        :rtype: bool
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.

        CommonName defines whether to add the organizationalUnit information into the issuer.  # noqa: E501

        :param common_name: The common_name of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501
        :type: bool
        """

        self._common_name = common_name

    @property
    def country(self):
        """Gets the country of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501

        Country defines whether to add the country information into the issuer.  # noqa: E501

        :return: The country of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501
        :rtype: bool
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.

        Country defines whether to add the country information into the issuer.  # noqa: E501

        :param country: The country of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501
        :type: bool
        """

        self._country = country

    @property
    def domain_component(self):
        """Gets the domain_component of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501

        DomainComponent defines whether to add the domainComponent information into the issuer.  # noqa: E501

        :return: The domain_component of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501
        :rtype: bool
        """
        return self._domain_component

    @domain_component.setter
    def domain_component(self, domain_component):
        """Sets the domain_component of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.

        DomainComponent defines whether to add the domainComponent information into the issuer.  # noqa: E501

        :param domain_component: The domain_component of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501
        :type: bool
        """

        self._domain_component = domain_component

    @property
    def locality(self):
        """Gets the locality of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501

        Locality defines whether to add the locality information into the issuer.  # noqa: E501

        :return: The locality of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501
        :rtype: bool
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.

        Locality defines whether to add the locality information into the issuer.  # noqa: E501

        :param locality: The locality of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501
        :type: bool
        """

        self._locality = locality

    @property
    def organization(self):
        """Gets the organization of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501

        Organization defines whether to add the organization information into the issuer.  # noqa: E501

        :return: The organization of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501
        :rtype: bool
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.

        Organization defines whether to add the organization information into the issuer.  # noqa: E501

        :param organization: The organization of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501
        :type: bool
        """

        self._organization = organization

    @property
    def province(self):
        """Gets the province of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501

        Province defines whether to add the province information into the issuer.  # noqa: E501

        :return: The province of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501
        :rtype: bool
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.

        Province defines whether to add the province information into the issuer.  # noqa: E501

        :param province: The province of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501
        :type: bool
        """

        self._province = province

    @property
    def serial_number(self):
        """Gets the serial_number of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501

        SerialNumber defines whether to add the serialNumber information into the issuer.  # noqa: E501

        :return: The serial_number of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501
        :rtype: bool
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.

        SerialNumber defines whether to add the serialNumber information into the issuer.  # noqa: E501

        :param serial_number: The serial_number of this IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer.  # noqa: E501
        :type: bool
        """

        self._serial_number = serial_number

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
        if issubclass(IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer, dict):
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
        if not isinstance(other, IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoTraefikV1alpha1MiddlewareSpecPassTLSClientCertInfoIssuer):
            return True

        return self.to_dict() != other.to_dict()
