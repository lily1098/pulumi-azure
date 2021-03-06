# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['StreamingEndpoint']


class StreamingEndpoint(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_control: Optional[pulumi.Input[pulumi.InputType['StreamingEndpointAccessControlArgs']]] = None,
                 auto_start_enabled: Optional[pulumi.Input[bool]] = None,
                 cdn_enabled: Optional[pulumi.Input[bool]] = None,
                 cdn_profile: Optional[pulumi.Input[str]] = None,
                 cdn_provider: Optional[pulumi.Input[str]] = None,
                 cross_site_access_policy: Optional[pulumi.Input[pulumi.InputType['StreamingEndpointCrossSiteAccessPolicyArgs']]] = None,
                 custom_host_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_cache_age_seconds: Optional[pulumi.Input[int]] = None,
                 media_services_account_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scale_units: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Streaming Endpoint.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="GRS")
        example_service_account = azure.media.ServiceAccount("exampleServiceAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            storage_accounts=[azure.media.ServiceAccountStorageAccountArgs(
                id=example_account.id,
                is_primary=True,
            )])
        example_streaming_endpoint = azure.media.StreamingEndpoint("exampleStreamingEndpoint",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            media_services_account_name=example_service_account.name,
            scale_units=2)
        ```
        ### With Access Control

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="GRS")
        example_service_account = azure.media.ServiceAccount("exampleServiceAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            storage_accounts=[azure.media.ServiceAccountStorageAccountArgs(
                id=example_account.id,
                is_primary=True,
            )])
        example_streaming_endpoint = azure.media.StreamingEndpoint("exampleStreamingEndpoint",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            media_services_account_name=example_service_account.name,
            scale_units=2,
            access_control=azure.media.StreamingEndpointAccessControlArgs(
                ip_allows=[
                    azure.media.StreamingEndpointAccessControlIpAllowArgs(
                        name="AllowedIP",
                        address="192.168.1.1",
                    ),
                    azure.media.StreamingEndpointAccessControlIpAllowArgs(
                        name="AnotherIp",
                        address="192.168.1.2",
                    ),
                ],
                akamai_signature_header_authentication_keys=[
                    azure.media.StreamingEndpointAccessControlAkamaiSignatureHeaderAuthenticationKeyArgs(
                        identifier="id1",
                        expiration="2030-12-31T16:00:00Z",
                        base64_key="dGVzdGlkMQ==",
                    ),
                    azure.media.StreamingEndpointAccessControlAkamaiSignatureHeaderAuthenticationKeyArgs(
                        identifier="id2",
                        expiration="2032-01-28T16:00:00Z",
                        base64_key="dGVzdGlkMQ==",
                    ),
                ],
            ))
        ```

        ## Import

        Streaming Endpoints can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:media/streamingEndpoint:StreamingEndpoint example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/mediaservices/service1/streamingendpoints/endpoint1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['StreamingEndpointAccessControlArgs']] access_control: A `access_control` block as defined below.
        :param pulumi.Input[bool] auto_start_enabled: The flag indicates if the resource should be automatically started on creation.
        :param pulumi.Input[bool] cdn_enabled: The CDN enabled flag.
        :param pulumi.Input[str] cdn_profile: The CDN profile name.
        :param pulumi.Input[str] cdn_provider: The CDN provider name. Supported value are `StandardVerizon`,`PremiumVerizon` and `StandardAkamai`
        :param pulumi.Input[pulumi.InputType['StreamingEndpointCrossSiteAccessPolicyArgs']] cross_site_access_policy: A `cross_site_access_policy` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] custom_host_names: The custom host names of the streaming endpoint.
        :param pulumi.Input[str] description: The streaming endpoint description.
        :param pulumi.Input[str] location: The Azure Region where the Streaming Endpoint should exist. Changing this forces a new Streaming Endpoint to be created.
        :param pulumi.Input[int] max_cache_age_seconds: Max cache age in seconds.
        :param pulumi.Input[str] media_services_account_name: The Media Services account name. Changing this forces a new Streaming Endpoint to be created.
        :param pulumi.Input[str] name: The name which should be used for this Streaming Endpoint maximum length is 24. Changing this forces a new Streaming Endpoint to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Streaming Endpoint should exist. Changing this forces a new Streaming Endpoint to be created.
        :param pulumi.Input[int] scale_units: The number of scale units.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Streaming Endpoint.
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

            __props__['access_control'] = access_control
            __props__['auto_start_enabled'] = auto_start_enabled
            __props__['cdn_enabled'] = cdn_enabled
            __props__['cdn_profile'] = cdn_profile
            __props__['cdn_provider'] = cdn_provider
            __props__['cross_site_access_policy'] = cross_site_access_policy
            __props__['custom_host_names'] = custom_host_names
            __props__['description'] = description
            __props__['location'] = location
            __props__['max_cache_age_seconds'] = max_cache_age_seconds
            if media_services_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'media_services_account_name'")
            __props__['media_services_account_name'] = media_services_account_name
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if scale_units is None and not opts.urn:
                raise TypeError("Missing required property 'scale_units'")
            __props__['scale_units'] = scale_units
            __props__['tags'] = tags
            __props__['host_name'] = None
        super(StreamingEndpoint, __self__).__init__(
            'azure:media/streamingEndpoint:StreamingEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_control: Optional[pulumi.Input[pulumi.InputType['StreamingEndpointAccessControlArgs']]] = None,
            auto_start_enabled: Optional[pulumi.Input[bool]] = None,
            cdn_enabled: Optional[pulumi.Input[bool]] = None,
            cdn_profile: Optional[pulumi.Input[str]] = None,
            cdn_provider: Optional[pulumi.Input[str]] = None,
            cross_site_access_policy: Optional[pulumi.Input[pulumi.InputType['StreamingEndpointCrossSiteAccessPolicyArgs']]] = None,
            custom_host_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            host_name: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            max_cache_age_seconds: Optional[pulumi.Input[int]] = None,
            media_services_account_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            scale_units: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'StreamingEndpoint':
        """
        Get an existing StreamingEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['StreamingEndpointAccessControlArgs']] access_control: A `access_control` block as defined below.
        :param pulumi.Input[bool] auto_start_enabled: The flag indicates if the resource should be automatically started on creation.
        :param pulumi.Input[bool] cdn_enabled: The CDN enabled flag.
        :param pulumi.Input[str] cdn_profile: The CDN profile name.
        :param pulumi.Input[str] cdn_provider: The CDN provider name. Supported value are `StandardVerizon`,`PremiumVerizon` and `StandardAkamai`
        :param pulumi.Input[pulumi.InputType['StreamingEndpointCrossSiteAccessPolicyArgs']] cross_site_access_policy: A `cross_site_access_policy` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] custom_host_names: The custom host names of the streaming endpoint.
        :param pulumi.Input[str] description: The streaming endpoint description.
        :param pulumi.Input[str] host_name: The host name of the Streaming Endpoint.
        :param pulumi.Input[str] location: The Azure Region where the Streaming Endpoint should exist. Changing this forces a new Streaming Endpoint to be created.
        :param pulumi.Input[int] max_cache_age_seconds: Max cache age in seconds.
        :param pulumi.Input[str] media_services_account_name: The Media Services account name. Changing this forces a new Streaming Endpoint to be created.
        :param pulumi.Input[str] name: The name which should be used for this Streaming Endpoint maximum length is 24. Changing this forces a new Streaming Endpoint to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Streaming Endpoint should exist. Changing this forces a new Streaming Endpoint to be created.
        :param pulumi.Input[int] scale_units: The number of scale units.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Streaming Endpoint.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_control"] = access_control
        __props__["auto_start_enabled"] = auto_start_enabled
        __props__["cdn_enabled"] = cdn_enabled
        __props__["cdn_profile"] = cdn_profile
        __props__["cdn_provider"] = cdn_provider
        __props__["cross_site_access_policy"] = cross_site_access_policy
        __props__["custom_host_names"] = custom_host_names
        __props__["description"] = description
        __props__["host_name"] = host_name
        __props__["location"] = location
        __props__["max_cache_age_seconds"] = max_cache_age_seconds
        __props__["media_services_account_name"] = media_services_account_name
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["scale_units"] = scale_units
        __props__["tags"] = tags
        return StreamingEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessControl")
    def access_control(self) -> pulumi.Output[Optional['outputs.StreamingEndpointAccessControl']]:
        """
        A `access_control` block as defined below.
        """
        return pulumi.get(self, "access_control")

    @property
    @pulumi.getter(name="autoStartEnabled")
    def auto_start_enabled(self) -> pulumi.Output[bool]:
        """
        The flag indicates if the resource should be automatically started on creation.
        """
        return pulumi.get(self, "auto_start_enabled")

    @property
    @pulumi.getter(name="cdnEnabled")
    def cdn_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        The CDN enabled flag.
        """
        return pulumi.get(self, "cdn_enabled")

    @property
    @pulumi.getter(name="cdnProfile")
    def cdn_profile(self) -> pulumi.Output[str]:
        """
        The CDN profile name.
        """
        return pulumi.get(self, "cdn_profile")

    @property
    @pulumi.getter(name="cdnProvider")
    def cdn_provider(self) -> pulumi.Output[str]:
        """
        The CDN provider name. Supported value are `StandardVerizon`,`PremiumVerizon` and `StandardAkamai`
        """
        return pulumi.get(self, "cdn_provider")

    @property
    @pulumi.getter(name="crossSiteAccessPolicy")
    def cross_site_access_policy(self) -> pulumi.Output[Optional['outputs.StreamingEndpointCrossSiteAccessPolicy']]:
        """
        A `cross_site_access_policy` block as defined below.
        """
        return pulumi.get(self, "cross_site_access_policy")

    @property
    @pulumi.getter(name="customHostNames")
    def custom_host_names(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The custom host names of the streaming endpoint.
        """
        return pulumi.get(self, "custom_host_names")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The streaming endpoint description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[str]:
        """
        The host name of the Streaming Endpoint.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure Region where the Streaming Endpoint should exist. Changing this forces a new Streaming Endpoint to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxCacheAgeSeconds")
    def max_cache_age_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        Max cache age in seconds.
        """
        return pulumi.get(self, "max_cache_age_seconds")

    @property
    @pulumi.getter(name="mediaServicesAccountName")
    def media_services_account_name(self) -> pulumi.Output[str]:
        """
        The Media Services account name. Changing this forces a new Streaming Endpoint to be created.
        """
        return pulumi.get(self, "media_services_account_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Streaming Endpoint maximum length is 24. Changing this forces a new Streaming Endpoint to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Streaming Endpoint should exist. Changing this forces a new Streaming Endpoint to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="scaleUnits")
    def scale_units(self) -> pulumi.Output[int]:
        """
        The number of scale units.
        """
        return pulumi.get(self, "scale_units")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags which should be assigned to the Streaming Endpoint.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

