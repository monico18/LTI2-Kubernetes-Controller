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


class IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookConversion(object):
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
        'client_config': 'IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookClientConfig',
        'conversion_review_versions': 'list[str]'
    }

    attribute_map = {
        'client_config': 'clientConfig',
        'conversion_review_versions': 'conversionReviewVersions'
    }

    def __init__(self, client_config=None, conversion_review_versions=None, _configuration=None):  # noqa: E501
        """IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookConversion - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_config = None
        self._conversion_review_versions = None
        self.discriminator = None

        if client_config is not None:
            self.client_config = client_config
        self.conversion_review_versions = conversion_review_versions

    @property
    def client_config(self):
        """Gets the client_config of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookConversion.  # noqa: E501

        clientConfig is the instructions for how to call the webhook if strategy is `Webhook`.  # noqa: E501

        :return: The client_config of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookConversion.  # noqa: E501
        :rtype: IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookClientConfig
        """
        return self._client_config

    @client_config.setter
    def client_config(self, client_config):
        """Sets the client_config of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookConversion.

        clientConfig is the instructions for how to call the webhook if strategy is `Webhook`.  # noqa: E501

        :param client_config: The client_config of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookConversion.  # noqa: E501
        :type: IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookClientConfig
        """

        self._client_config = client_config

    @property
    def conversion_review_versions(self):
        """Gets the conversion_review_versions of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookConversion.  # noqa: E501

        conversionReviewVersions is an ordered list of preferred `ConversionReview` versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail.  # noqa: E501

        :return: The conversion_review_versions of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookConversion.  # noqa: E501
        :rtype: list[str]
        """
        return self._conversion_review_versions

    @conversion_review_versions.setter
    def conversion_review_versions(self, conversion_review_versions):
        """Sets the conversion_review_versions of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookConversion.

        conversionReviewVersions is an ordered list of preferred `ConversionReview` versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail.  # noqa: E501

        :param conversion_review_versions: The conversion_review_versions of this IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookConversion.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and conversion_review_versions is None:
            raise ValueError("Invalid value for `conversion_review_versions`, must not be `None`")  # noqa: E501

        self._conversion_review_versions = conversion_review_versions

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
        if issubclass(IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookConversion, dict):
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
        if not isinstance(other, IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookConversion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiextensionsApiserverPkgApisApiextensionsV1WebhookConversion):
            return True

        return self.to_dict() != other.to_dict()
