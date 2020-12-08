# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Namespace']


class Namespace(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_type: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Notification Hub Namespace.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="Australia East")
        example_namespace = azure.notificationhub.Namespace("exampleNamespace",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            namespace_type="NotificationHub",
            sku_name="Free")
        ```

        ## Import

        Notification Hub Namespaces can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:notificationhub/namespace:Namespace namespace1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: Is this Notification Hub Namespace enabled? Defaults to `true`.
        :param pulumi.Input[str] location: The Azure Region in which this Notification Hub Namespace should be created.
        :param pulumi.Input[str] name: The name to use for this Notification Hub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] namespace_type: The Type of Namespace - possible values are `Messaging` or `NotificationHub`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group in which the Notification Hub Namespace should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sku_name: The name of the SKU to use for this Notification Hub Namespace. Possible values are `Free`, `Basic` or `Standard`. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['enabled'] = enabled
            __props__['location'] = location
            __props__['name'] = name
            if namespace_type is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_type'")
            __props__['namespace_type'] = namespace_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if sku_name is None and not opts.urn:
                raise TypeError("Missing required property 'sku_name'")
            __props__['sku_name'] = sku_name
            __props__['tags'] = tags
            __props__['servicebus_endpoint'] = None
        super(Namespace, __self__).__init__(
            'azure:notificationhub/namespace:Namespace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace_type: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            servicebus_endpoint: Optional[pulumi.Input[str]] = None,
            sku_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Namespace':
        """
        Get an existing Namespace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: Is this Notification Hub Namespace enabled? Defaults to `true`.
        :param pulumi.Input[str] location: The Azure Region in which this Notification Hub Namespace should be created.
        :param pulumi.Input[str] name: The name to use for this Notification Hub Namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] namespace_type: The Type of Namespace - possible values are `Messaging` or `NotificationHub`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group in which the Notification Hub Namespace should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] servicebus_endpoint: The ServiceBus Endpoint for this Notification Hub Namespace.
        :param pulumi.Input[str] sku_name: The name of the SKU to use for this Notification Hub Namespace. Possible values are `Free`, `Basic` or `Standard`. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["enabled"] = enabled
        __props__["location"] = location
        __props__["name"] = name
        __props__["namespace_type"] = namespace_type
        __props__["resource_group_name"] = resource_group_name
        __props__["servicebus_endpoint"] = servicebus_endpoint
        __props__["sku_name"] = sku_name
        __props__["tags"] = tags
        return Namespace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Is this Notification Hub Namespace enabled? Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure Region in which this Notification Hub Namespace should be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name to use for this Notification Hub Namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namespaceType")
    def namespace_type(self) -> pulumi.Output[str]:
        """
        The Type of Namespace - possible values are `Messaging` or `NotificationHub`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "namespace_type")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group in which the Notification Hub Namespace should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="servicebusEndpoint")
    def servicebus_endpoint(self) -> pulumi.Output[str]:
        """
        The ServiceBus Endpoint for this Notification Hub Namespace.
        """
        return pulumi.get(self, "servicebus_endpoint")

    @property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> pulumi.Output[str]:
        """
        The name of the SKU to use for this Notification Hub Namespace. Possible values are `Free`, `Basic` or `Standard`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "sku_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

