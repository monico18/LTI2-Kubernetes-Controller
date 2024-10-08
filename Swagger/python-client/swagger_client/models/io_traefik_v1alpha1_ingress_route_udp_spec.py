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


class IoTraefikV1alpha1IngressRouteUDPSpec(object):
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
        'entry_points': 'list[str]',
        'routes': 'list[IoTraefikV1alpha1IngressRouteUDPSpecRoutes]'
    }

    attribute_map = {
        'entry_points': 'entryPoints',
        'routes': 'routes'
    }

    def __init__(self, entry_points=None, routes=None, _configuration=None):  # noqa: E501
        """IoTraefikV1alpha1IngressRouteUDPSpec - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._entry_points = None
        self._routes = None
        self.discriminator = None

        if entry_points is not None:
            self.entry_points = entry_points
        self.routes = routes

    @property
    def entry_points(self):
        """Gets the entry_points of this IoTraefikV1alpha1IngressRouteUDPSpec.  # noqa: E501

        EntryPoints defines the list of entry point names to bind to. Entry points have to be configured in the static configuration. More info: https://doc.traefik.io/traefik/v2.10/routing/entrypoints/ Default: all.  # noqa: E501

        :return: The entry_points of this IoTraefikV1alpha1IngressRouteUDPSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._entry_points

    @entry_points.setter
    def entry_points(self, entry_points):
        """Sets the entry_points of this IoTraefikV1alpha1IngressRouteUDPSpec.

        EntryPoints defines the list of entry point names to bind to. Entry points have to be configured in the static configuration. More info: https://doc.traefik.io/traefik/v2.10/routing/entrypoints/ Default: all.  # noqa: E501

        :param entry_points: The entry_points of this IoTraefikV1alpha1IngressRouteUDPSpec.  # noqa: E501
        :type: list[str]
        """

        self._entry_points = entry_points

    @property
    def routes(self):
        """Gets the routes of this IoTraefikV1alpha1IngressRouteUDPSpec.  # noqa: E501

        Routes defines the list of routes.  # noqa: E501

        :return: The routes of this IoTraefikV1alpha1IngressRouteUDPSpec.  # noqa: E501
        :rtype: list[IoTraefikV1alpha1IngressRouteUDPSpecRoutes]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this IoTraefikV1alpha1IngressRouteUDPSpec.

        Routes defines the list of routes.  # noqa: E501

        :param routes: The routes of this IoTraefikV1alpha1IngressRouteUDPSpec.  # noqa: E501
        :type: list[IoTraefikV1alpha1IngressRouteUDPSpecRoutes]
        """
        if self._configuration.client_side_validation and routes is None:
            raise ValueError("Invalid value for `routes`, must not be `None`")  # noqa: E501

        self._routes = routes

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
        if issubclass(IoTraefikV1alpha1IngressRouteUDPSpec, dict):
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
        if not isinstance(other, IoTraefikV1alpha1IngressRouteUDPSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoTraefikV1alpha1IngressRouteUDPSpec):
            return True

        return self.to_dict() != other.to_dict()
