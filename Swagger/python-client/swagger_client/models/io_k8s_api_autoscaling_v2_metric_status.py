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


class IoK8sApiAutoscalingV2MetricStatus(object):
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
        'container_resource': 'IoK8sApiAutoscalingV2ContainerResourceMetricStatus',
        'external': 'IoK8sApiAutoscalingV2ExternalMetricStatus',
        'object': 'IoK8sApiAutoscalingV2ObjectMetricStatus',
        'pods': 'IoK8sApiAutoscalingV2PodsMetricStatus',
        'resource': 'IoK8sApiAutoscalingV2ResourceMetricStatus',
        'type': 'str'
    }

    attribute_map = {
        'container_resource': 'containerResource',
        'external': 'external',
        'object': 'object',
        'pods': 'pods',
        'resource': 'resource',
        'type': 'type'
    }

    def __init__(self, container_resource=None, external=None, object=None, pods=None, resource=None, type=None, _configuration=None):  # noqa: E501
        """IoK8sApiAutoscalingV2MetricStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._container_resource = None
        self._external = None
        self._object = None
        self._pods = None
        self._resource = None
        self._type = None
        self.discriminator = None

        if container_resource is not None:
            self.container_resource = container_resource
        if external is not None:
            self.external = external
        if object is not None:
            self.object = object
        if pods is not None:
            self.pods = pods
        if resource is not None:
            self.resource = resource
        self.type = type

    @property
    def container_resource(self):
        """Gets the container_resource of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501

        container resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \"pods\" source.  # noqa: E501

        :return: The container_resource of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2ContainerResourceMetricStatus
        """
        return self._container_resource

    @container_resource.setter
    def container_resource(self, container_resource):
        """Sets the container_resource of this IoK8sApiAutoscalingV2MetricStatus.

        container resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \"pods\" source.  # noqa: E501

        :param container_resource: The container_resource of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501
        :type: IoK8sApiAutoscalingV2ContainerResourceMetricStatus
        """

        self._container_resource = container_resource

    @property
    def external(self):
        """Gets the external of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501

        external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).  # noqa: E501

        :return: The external of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2ExternalMetricStatus
        """
        return self._external

    @external.setter
    def external(self, external):
        """Sets the external of this IoK8sApiAutoscalingV2MetricStatus.

        external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).  # noqa: E501

        :param external: The external of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501
        :type: IoK8sApiAutoscalingV2ExternalMetricStatus
        """

        self._external = external

    @property
    def object(self):
        """Gets the object of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501

        object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).  # noqa: E501

        :return: The object of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2ObjectMetricStatus
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this IoK8sApiAutoscalingV2MetricStatus.

        object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).  # noqa: E501

        :param object: The object of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501
        :type: IoK8sApiAutoscalingV2ObjectMetricStatus
        """

        self._object = object

    @property
    def pods(self):
        """Gets the pods of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501

        pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.  # noqa: E501

        :return: The pods of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2PodsMetricStatus
        """
        return self._pods

    @pods.setter
    def pods(self, pods):
        """Sets the pods of this IoK8sApiAutoscalingV2MetricStatus.

        pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.  # noqa: E501

        :param pods: The pods of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501
        :type: IoK8sApiAutoscalingV2PodsMetricStatus
        """

        self._pods = pods

    @property
    def resource(self):
        """Gets the resource of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501

        resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \"pods\" source.  # noqa: E501

        :return: The resource of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501
        :rtype: IoK8sApiAutoscalingV2ResourceMetricStatus
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this IoK8sApiAutoscalingV2MetricStatus.

        resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \"pods\" source.  # noqa: E501

        :param resource: The resource of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501
        :type: IoK8sApiAutoscalingV2ResourceMetricStatus
        """

        self._resource = resource

    @property
    def type(self):
        """Gets the type of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501

        type is the type of metric source.  It will be one of \"ContainerResource\", \"External\", \"Object\", \"Pods\" or \"Resource\", each corresponds to a matching field in the object. Note: \"ContainerResource\" type is available on when the feature-gate HPAContainerMetrics is enabled  # noqa: E501

        :return: The type of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IoK8sApiAutoscalingV2MetricStatus.

        type is the type of metric source.  It will be one of \"ContainerResource\", \"External\", \"Object\", \"Pods\" or \"Resource\", each corresponds to a matching field in the object. Note: \"ContainerResource\" type is available on when the feature-gate HPAContainerMetrics is enabled  # noqa: E501

        :param type: The type of this IoK8sApiAutoscalingV2MetricStatus.  # noqa: E501
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
        if issubclass(IoK8sApiAutoscalingV2MetricStatus, dict):
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
        if not isinstance(other, IoK8sApiAutoscalingV2MetricStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IoK8sApiAutoscalingV2MetricStatus):
            return True

        return self.to_dict() != other.to_dict()
