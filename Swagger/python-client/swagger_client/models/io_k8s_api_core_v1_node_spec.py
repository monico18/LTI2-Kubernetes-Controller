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


class IoK8sApiCoreV1NodeSpec(object):
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
        'config_source': 'IoK8sApiCoreV1NodeConfigSource',
        'external_id': 'str',
        'pod_cidr': 'str',
        'pod_cidrs': 'list[str]',
        'provider_id': 'str',
        'taints': 'list[IoK8sApiCoreV1Taint]',
        'unschedulable': 'bool'
    }

    attribute_map = {
        'config_source': 'configSource',
        'external_id': 'externalID',
        'pod_cidr': 'podCIDR',
        'pod_cidrs': 'podCIDRs',
        'provider_id': 'providerID',
        'taints': 'taints',
        'unschedulable': 'unschedulable'
    }

    def __init__(self, config_source=None, external_id=None, pod_cidr=None, pod_cidrs=None, provider_id=None, taints=None, unschedulable=None, _configuration=None):  # noqa: E501
        """IoK8sApiCoreV1NodeSpec - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._config_source = None
        self._external_id = None
        self._pod_cidr = None
        self._pod_cidrs = None
        self._provider_id = None
        self._taints = None
        self._unschedulable = None
        self.discriminator = None

        if config_source is not None:
            self.config_source = config_source
        if external_id is not None:
            self.external_id = external_id
        if pod_cidr is not None:
            self.pod_cidr = pod_cidr
        if pod_cidrs is not None:
            self.pod_cidrs = pod_cidrs
        if provider_id is not None:
            self.provider_id = provider_id
        if taints is not None:
            self.taints = taints
        if unschedulable is not None:
            self.unschedulable = unschedulable

    @property
    def config_source(self):
        """Gets the config_source of this IoK8sApiCoreV1NodeSpec.  # noqa: E501

        Deprecated: Previously used to specify the source of the node's configuration for the DynamicKubeletConfig feature. This feature is removed.  # noqa: E501

        :return: The config_source of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :rtype: IoK8sApiCoreV1NodeConfigSource
        """
        return self._config_source

    @config_source.setter
    def config_source(self, config_source):
        """Sets the config_source of this IoK8sApiCoreV1NodeSpec.

        Deprecated: Previously used to specify the source of the node's configuration for the DynamicKubeletConfig feature. This feature is removed.  # noqa: E501

        :param config_source: The config_source of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :type: IoK8sApiCoreV1NodeConfigSource
        """

        self._config_source = config_source

    @property
    def external_id(self):
        """Gets the external_id of this IoK8sApiCoreV1NodeSpec.  # noqa: E501

        Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966  # noqa: E501

        :return: The external_id of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this IoK8sApiCoreV1NodeSpec.

        Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966  # noqa: E501

        :param external_id: The external_id of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def pod_cidr(self):
        """Gets the pod_cidr of this IoK8sApiCoreV1NodeSpec.  # noqa: E501

        PodCIDR represents the pod IP range assigned to the node.  # noqa: E501

        :return: The pod_cidr of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :rtype: str
        """
        return self._pod_cidr

    @pod_cidr.setter
    def pod_cidr(self, pod_cidr):
        """Sets the pod_cidr of this IoK8sApiCoreV1NodeSpec.

        PodCIDR represents the pod IP range assigned to the node.  # noqa: E501

        :param pod_cidr: The pod_cidr of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :type: str
        """

        self._pod_cidr = pod_cidr

    @property
    def pod_cidrs(self):
        """Gets the pod_cidrs of this IoK8sApiCoreV1NodeSpec.  # noqa: E501

        podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6.  # noqa: E501

        :return: The pod_cidrs of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._pod_cidrs

    @pod_cidrs.setter
    def pod_cidrs(self, pod_cidrs):
        """Sets the pod_cidrs of this IoK8sApiCoreV1NodeSpec.

        podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6.  # noqa: E501

        :param pod_cidrs: The pod_cidrs of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :type: list[str]
        """

        self._pod_cidrs = pod_cidrs

    @property
    def provider_id(self):
        """Gets the provider_id of this IoK8sApiCoreV1NodeSpec.  # noqa: E501

        ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>  # noqa: E501

        :return: The provider_id of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this IoK8sApiCoreV1NodeSpec.

        ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>  # noqa: E501

        :param provider_id: The provider_id of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :type: str
        """

        self._provider_id = provider_id

    @property
    def taints(self):
        """Gets the taints of this IoK8sApiCoreV1NodeSpec.  # noqa: E501

        If specified, the node's taints.  # noqa: E501

        :return: The taints of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :rtype: list[IoK8sApiCoreV1Taint]
        """
        return self._taints

    @taints.setter
    def taints(self, taints):
        """Sets the taints of this IoK8sApiCoreV1NodeSpec.

        If specified, the node's taints.  # noqa: E501

        :param taints: The taints of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :type: list[IoK8sApiCoreV1Taint]
        """

        self._taints = taints

    @property
    def unschedulable(self):
        """Gets the unschedulable of this IoK8sApiCoreV1NodeSpec.  # noqa: E501

        Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration  # noqa: E501

        :return: The unschedulable of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :rtype: bool
        """
        return self._unschedulable

    @unschedulable.setter
    def unschedulable(self, unschedulable):
        """Sets the unschedulable of this IoK8sApiCoreV1NodeSpec.

        Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration  # noqa: E501

        :param unschedulable: The unschedulable of this IoK8sApiCoreV1NodeSpec.  # noqa: E501
        :type: bool
        """

        self._unschedulable = unschedulable

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
        if issubclass(IoK8sApiCoreV1NodeSpec, dict):
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
        if not isinstance(other, IoK8sApiCoreV1NodeSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiCoreV1NodeSpec):
            return True

        return self.to_dict() != other.to_dict()
