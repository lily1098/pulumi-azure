# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Workspace(pulumi.CustomResource):
    application_insights_id: pulumi.Output[str]
    """
    The ID of the Application Insights associated with this Machine Learning Workspace. Changing this forces a new resource to be created.
    """
    container_registry_id: pulumi.Output[str]
    """
    The ID of the container registry associated with this Machine Learning Workspace. Changing this forces a new resource to be created.
    """
    description: pulumi.Output[str]
    """
    The description of this Machine Learning Workspace.
    """
    friendly_name: pulumi.Output[str]
    """
    Friendly name for this Machine Learning Workspace.
    """
    identity: pulumi.Output[dict]
    """
    An `identity` block defined below.

      * `principal_id` (`str`) - The (Client) ID of the Service Principal.
      * `tenant_id` (`str`) - The ID of the Tenant the Service Principal is assigned in.
      * `type` (`str`) - The Type of Identity which should be used for this Disk Encryption Set. At this time the only possible value is `SystemAssigned`.
    """
    key_vault_id: pulumi.Output[str]
    """
    The ID of key vault associated with this Machine Learning Workspace. Changing this forces a new resource to be created.
    """
    location: pulumi.Output[str]
    """
    Specifies the supported Azure location where the Machine Learning Workspace should exist. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the Machine Learning Workspace. Changing this forces a new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    Specifies the name of the Resource Group in which the Machine Learning Workspace should exist. Changing this forces a new resource to be created.
    """
    sku_name: pulumi.Output[str]
    """
    SKU/edition of the Machine Learning Workspace, possible values are `Basic` for a basic workspace or `Enterprise` for a feature rich workspace. Defaults to `Basic`.
    """
    storage_account_id: pulumi.Output[str]
    """
    The ID of the Storage Account associated with this Machine Learning Workspace. Changing this forces a new resource to be created.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource. Changing this forces a new resource to be created.
    """
    def __init__(__self__, resource_name, opts=None, application_insights_id=None, container_registry_id=None, description=None, friendly_name=None, identity=None, key_vault_id=None, location=None, name=None, resource_group_name=None, sku_name=None, storage_account_id=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Azure Machine Learning Workspace

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/machine_learning_workspace.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_insights_id: The ID of the Application Insights associated with this Machine Learning Workspace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] container_registry_id: The ID of the container registry associated with this Machine Learning Workspace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: The description of this Machine Learning Workspace.
        :param pulumi.Input[str] friendly_name: Friendly name for this Machine Learning Workspace.
        :param pulumi.Input[dict] identity: An `identity` block defined below.
        :param pulumi.Input[str] key_vault_id: The ID of key vault associated with this Machine Learning Workspace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the Machine Learning Workspace should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Machine Learning Workspace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group in which the Machine Learning Workspace should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sku_name: SKU/edition of the Machine Learning Workspace, possible values are `Basic` for a basic workspace or `Enterprise` for a feature rich workspace. Defaults to `Basic`.
        :param pulumi.Input[str] storage_account_id: The ID of the Storage Account associated with this Machine Learning Workspace. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

        The **identity** object supports the following:

          * `principal_id` (`pulumi.Input[str]`) - The (Client) ID of the Service Principal.
          * `tenant_id` (`pulumi.Input[str]`) - The ID of the Tenant the Service Principal is assigned in.
          * `type` (`pulumi.Input[str]`) - The Type of Identity which should be used for this Disk Encryption Set. At this time the only possible value is `SystemAssigned`.
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
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if application_insights_id is None:
                raise TypeError("Missing required property 'application_insights_id'")
            __props__['application_insights_id'] = application_insights_id
            __props__['container_registry_id'] = container_registry_id
            __props__['description'] = description
            __props__['friendly_name'] = friendly_name
            if identity is None:
                raise TypeError("Missing required property 'identity'")
            __props__['identity'] = identity
            if key_vault_id is None:
                raise TypeError("Missing required property 'key_vault_id'")
            __props__['key_vault_id'] = key_vault_id
            __props__['location'] = location
            __props__['name'] = name
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['sku_name'] = sku_name
            if storage_account_id is None:
                raise TypeError("Missing required property 'storage_account_id'")
            __props__['storage_account_id'] = storage_account_id
            __props__['tags'] = tags
        super(Workspace, __self__).__init__(
            'azure:machinelearning/workspace:Workspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, application_insights_id=None, container_registry_id=None, description=None, friendly_name=None, identity=None, key_vault_id=None, location=None, name=None, resource_group_name=None, sku_name=None, storage_account_id=None, tags=None):
        """
        Get an existing Workspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_insights_id: The ID of the Application Insights associated with this Machine Learning Workspace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] container_registry_id: The ID of the container registry associated with this Machine Learning Workspace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: The description of this Machine Learning Workspace.
        :param pulumi.Input[str] friendly_name: Friendly name for this Machine Learning Workspace.
        :param pulumi.Input[dict] identity: An `identity` block defined below.
        :param pulumi.Input[str] key_vault_id: The ID of key vault associated with this Machine Learning Workspace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the Machine Learning Workspace should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Machine Learning Workspace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group in which the Machine Learning Workspace should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sku_name: SKU/edition of the Machine Learning Workspace, possible values are `Basic` for a basic workspace or `Enterprise` for a feature rich workspace. Defaults to `Basic`.
        :param pulumi.Input[str] storage_account_id: The ID of the Storage Account associated with this Machine Learning Workspace. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

        The **identity** object supports the following:

          * `principal_id` (`pulumi.Input[str]`) - The (Client) ID of the Service Principal.
          * `tenant_id` (`pulumi.Input[str]`) - The ID of the Tenant the Service Principal is assigned in.
          * `type` (`pulumi.Input[str]`) - The Type of Identity which should be used for this Disk Encryption Set. At this time the only possible value is `SystemAssigned`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["application_insights_id"] = application_insights_id
        __props__["container_registry_id"] = container_registry_id
        __props__["description"] = description
        __props__["friendly_name"] = friendly_name
        __props__["identity"] = identity
        __props__["key_vault_id"] = key_vault_id
        __props__["location"] = location
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["sku_name"] = sku_name
        __props__["storage_account_id"] = storage_account_id
        __props__["tags"] = tags
        return Workspace(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
