# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Workspace(pulumi.CustomResource):
    location: pulumi.Output[str]
    """
    Specifies the supported Azure location where the resource has to be created. Changing this forces a new resource to be created.
    """
    managed_resource_group_id: pulumi.Output[str]
    """
    The ID of the Managed Resource Group created by the Databricks Workspace.
    """
    managed_resource_group_name: pulumi.Output[str]
    """
    The name of the resource group where Azure should place the managed Databricks resources. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the Databricks Workspace resource. Changing this forces a new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the Resource Group in which the Databricks Workspace should exist. Changing this forces a new resource to be created.
    """
    sku: pulumi.Output[str]
    """
    The `sku` to use for the Databricks Workspace. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, __name__, __opts__=None, location=None, managed_resource_group_name=None, name=None, resource_group_name=None, sku=None, tags=None):
        """
        Manages a Databricks Workspace
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource has to be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] managed_resource_group_name: The name of the resource group where Azure should place the managed Databricks resources. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Databricks Workspace resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group in which the Databricks Workspace should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sku: The `sku` to use for the Databricks Workspace. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not location:
            raise TypeError('Missing required property location')
        __props__['location'] = location

        __props__['managed_resource_group_name'] = managed_resource_group_name

        __props__['name'] = name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        if not sku:
            raise TypeError('Missing required property sku')
        __props__['sku'] = sku

        __props__['tags'] = tags

        __props__['managed_resource_group_id'] = None

        super(Workspace, __self__).__init__(
            'azure:databricks/workspace:Workspace',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
