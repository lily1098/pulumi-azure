# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class VirtualNetworkRule(pulumi.CustomResource):
    ignore_missing_vnet_service_endpoint: pulumi.Output[bool]
    """
    Should the Virtual Network Rule be created before the Subnet has the Virtual Network Service Endpoint enabled? Defaults to `false`.
    """
    name: pulumi.Output[str]
    """
    The name of the PostgreSQL virtual network rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group where the PostgreSQL server resides. Changing this forces a new resource to be created.
    """
    server_name: pulumi.Output[str]
    """
    The name of the SQL Server to which this PostgreSQL virtual network rule will be applied to. Changing this forces a new resource to be created.
    """
    subnet_id: pulumi.Output[str]
    """
    The ID of the subnet that the PostgreSQL server will be connected to.
    """
    def __init__(__self__, __name__, __opts__=None, ignore_missing_vnet_service_endpoint=None, name=None, resource_group_name=None, server_name=None, subnet_id=None):
        """
        Manages a PostgreSQL Virtual Network Rule.
        
        -> **NOTE:** PostgreSQL Virtual Network Rules [can only be used with SKU Tiers of `GeneralPurpose` or `MemoryOptimized`](https://docs.microsoft.com/en-us/azure/postgresql/concepts-data-access-and-security-vnet)
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[bool] ignore_missing_vnet_service_endpoint: Should the Virtual Network Rule be created before the Subnet has the Virtual Network Service Endpoint enabled? Defaults to `false`.
        :param pulumi.Input[str] name: The name of the PostgreSQL virtual network rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the PostgreSQL server resides. Changing this forces a new resource to be created.
        :param pulumi.Input[str] server_name: The name of the SQL Server to which this PostgreSQL virtual network rule will be applied to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subnet_id: The ID of the subnet that the PostgreSQL server will be connected to.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['ignore_missing_vnet_service_endpoint'] = ignore_missing_vnet_service_endpoint

        __props__['name'] = name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        if not server_name:
            raise TypeError('Missing required property server_name')
        __props__['server_name'] = server_name

        if not subnet_id:
            raise TypeError('Missing required property subnet_id')
        __props__['subnet_id'] = subnet_id

        super(VirtualNetworkRule, __self__).__init__(
            'azure:postgresql/virtualNetworkRule:VirtualNetworkRule',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
