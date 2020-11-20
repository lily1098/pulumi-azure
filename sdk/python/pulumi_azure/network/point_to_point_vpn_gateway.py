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

__all__ = ['PointToPointVpnGateway']


class PointToPointVpnGateway(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_configuration: Optional[pulumi.Input[pulumi.InputType['PointToPointVpnGatewayConnectionConfigurationArgs']]] = None,
                 dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scale_unit: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub_id: Optional[pulumi.Input[str]] = None,
                 vpn_server_configuration_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Point-to-Site VPN Gateway.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.network.PointToPointVpnGateway("example",
            location=azurerm_resource_group["example"]["location"],
            resource_group_name=azurerm_resource_group["example"]["resource_group_name"],
            virtual_hub_id=azurerm_virtual_hub["example"]["id"],
            vpn_server_configuration_id=azurerm_vpn_server_configuration["example"]["id"],
            scale_unit=1)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['PointToPointVpnGatewayConnectionConfigurationArgs']] connection_configuration: A `connection_configuration` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_servers: A list of IP Addresses of DNS Servers for the Point-to-Site VPN Gateway.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Point-to-Site VPN Gateway. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Point-to-Site VPN Gateway. Changing this forces a new resource to be created.
        :param pulumi.Input[int] scale_unit: The Scale Unit for this Point-to-Site VPN Gateway.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the Point-to-Site VPN Gateway.
        :param pulumi.Input[str] virtual_hub_id: The ID of the Virtual Hub where this Point-to-Site VPN Gateway should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] vpn_server_configuration_id: The ID of the VPN Server Configuration which this Point-to-Site VPN Gateway should use. Changing this forces a new resource to be created.
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

            if connection_configuration is None:
                raise TypeError("Missing required property 'connection_configuration'")
            __props__['connection_configuration'] = connection_configuration
            __props__['dns_servers'] = dns_servers
            __props__['location'] = location
            __props__['name'] = name
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if scale_unit is None:
                raise TypeError("Missing required property 'scale_unit'")
            __props__['scale_unit'] = scale_unit
            __props__['tags'] = tags
            if virtual_hub_id is None:
                raise TypeError("Missing required property 'virtual_hub_id'")
            __props__['virtual_hub_id'] = virtual_hub_id
            if vpn_server_configuration_id is None:
                raise TypeError("Missing required property 'vpn_server_configuration_id'")
            __props__['vpn_server_configuration_id'] = vpn_server_configuration_id
        super(PointToPointVpnGateway, __self__).__init__(
            'azure:network/pointToPointVpnGateway:PointToPointVpnGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            connection_configuration: Optional[pulumi.Input[pulumi.InputType['PointToPointVpnGatewayConnectionConfigurationArgs']]] = None,
            dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            scale_unit: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            virtual_hub_id: Optional[pulumi.Input[str]] = None,
            vpn_server_configuration_id: Optional[pulumi.Input[str]] = None) -> 'PointToPointVpnGateway':
        """
        Get an existing PointToPointVpnGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['PointToPointVpnGatewayConnectionConfigurationArgs']] connection_configuration: A `connection_configuration` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_servers: A list of IP Addresses of DNS Servers for the Point-to-Site VPN Gateway.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Point-to-Site VPN Gateway. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Point-to-Site VPN Gateway. Changing this forces a new resource to be created.
        :param pulumi.Input[int] scale_unit: The Scale Unit for this Point-to-Site VPN Gateway.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the Point-to-Site VPN Gateway.
        :param pulumi.Input[str] virtual_hub_id: The ID of the Virtual Hub where this Point-to-Site VPN Gateway should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] vpn_server_configuration_id: The ID of the VPN Server Configuration which this Point-to-Site VPN Gateway should use. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["connection_configuration"] = connection_configuration
        __props__["dns_servers"] = dns_servers
        __props__["location"] = location
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["scale_unit"] = scale_unit
        __props__["tags"] = tags
        __props__["virtual_hub_id"] = virtual_hub_id
        __props__["vpn_server_configuration_id"] = vpn_server_configuration_id
        return PointToPointVpnGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectionConfiguration")
    def connection_configuration(self) -> pulumi.Output['outputs.PointToPointVpnGatewayConnectionConfiguration']:
        """
        A `connection_configuration` block as defined below.
        """
        return pulumi.get(self, "connection_configuration")

    @property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of IP Addresses of DNS Servers for the Point-to-Site VPN Gateway.
        """
        return pulumi.get(self, "dns_servers")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Point-to-Site VPN Gateway. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the Point-to-Site VPN Gateway. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="scaleUnit")
    def scale_unit(self) -> pulumi.Output[int]:
        """
        The Scale Unit for this Point-to-Site VPN Gateway.
        """
        return pulumi.get(self, "scale_unit")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the Point-to-Site VPN Gateway.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="virtualHubId")
    def virtual_hub_id(self) -> pulumi.Output[str]:
        """
        The ID of the Virtual Hub where this Point-to-Site VPN Gateway should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "virtual_hub_id")

    @property
    @pulumi.getter(name="vpnServerConfigurationId")
    def vpn_server_configuration_id(self) -> pulumi.Output[str]:
        """
        The ID of the VPN Server Configuration which this Point-to-Site VPN Gateway should use. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "vpn_server_configuration_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

