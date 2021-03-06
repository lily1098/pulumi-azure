# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['ResourceGroupTemplateDeployment']


class ResourceGroupTemplateDeployment(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 debug_level: Optional[pulumi.Input[str]] = None,
                 deployment_mode: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters_content: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 template_content: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Resource Group Template Deployment.

        > **Note:** This resource will automatically attempt to delete resources deployed by the ARM Template when it is deleted. You can opt-out of this by setting the `delete_nested_items_during_deletion` field within the `template_deployment` block of the `features` block to `false`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroupTemplateDeployment("example",
            deployment_mode="Complete",
            resource_group_name="example-group",
            template_content=\"\"\"{
          "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
          "contentVersion": "1.0.0.0",
          "parameters": {},
          "variables": {},
          "resources": [
            {
              "type": "Microsoft.Network/virtualNetworks",
              "apiVersion": "2020-05-01",
              "name": "acctest-network",
              "location": "[resourceGroup().location]",
              "properties": {
                "addressSpace": {
                  "addressPrefixes": [
                    "10.0.0.0/16"
                  ]
                }
              }
            }
          ]
        }

        \"\"\")
        ```

        ## Import

        Resource Group Template Deployments can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:core/resourceGroupTemplateDeployment:ResourceGroupTemplateDeployment example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Resources/deployments/template1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] debug_level: The Debug Level which should be used for this Resource Group Template Deployment. Possible values are `none`, `requestContent`, `responseContent` and `requestContent, responseContent`.
        :param pulumi.Input[str] deployment_mode: The Deployment Mode for this Resource Group Template Deployment. Possible values are `Complete` (where resources in the Resource Group not specified in the ARM Template will be destroyed) and `Incremental` (where resources are additive only).
        :param pulumi.Input[str] name: The name which should be used for this Resource Group Template Deployment. Changing this forces a new Resource Group Template Deployment to be created.
        :param pulumi.Input[str] parameters_content: The contents of the ARM Template parameters file - containing a JSON list of parameters.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Resource Group Template Deployment should exist. Changing this forces a new Resource Group Template Deployment to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Resource Group Template Deployment.
        :param pulumi.Input[str] template_content: The contents of the ARM Template which should be deployed into this Resource Group.
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

            __props__['debug_level'] = debug_level
            if deployment_mode is None and not opts.urn:
                raise TypeError("Missing required property 'deployment_mode'")
            __props__['deployment_mode'] = deployment_mode
            __props__['name'] = name
            __props__['parameters_content'] = parameters_content
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['tags'] = tags
            if template_content is None and not opts.urn:
                raise TypeError("Missing required property 'template_content'")
            __props__['template_content'] = template_content
            __props__['output_content'] = None
        super(ResourceGroupTemplateDeployment, __self__).__init__(
            'azure:core/resourceGroupTemplateDeployment:ResourceGroupTemplateDeployment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            debug_level: Optional[pulumi.Input[str]] = None,
            deployment_mode: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            output_content: Optional[pulumi.Input[str]] = None,
            parameters_content: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            template_content: Optional[pulumi.Input[str]] = None) -> 'ResourceGroupTemplateDeployment':
        """
        Get an existing ResourceGroupTemplateDeployment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] debug_level: The Debug Level which should be used for this Resource Group Template Deployment. Possible values are `none`, `requestContent`, `responseContent` and `requestContent, responseContent`.
        :param pulumi.Input[str] deployment_mode: The Deployment Mode for this Resource Group Template Deployment. Possible values are `Complete` (where resources in the Resource Group not specified in the ARM Template will be destroyed) and `Incremental` (where resources are additive only).
        :param pulumi.Input[str] name: The name which should be used for this Resource Group Template Deployment. Changing this forces a new Resource Group Template Deployment to be created.
        :param pulumi.Input[str] output_content: The JSON Content of the Outputs of the ARM Template Deployment.
        :param pulumi.Input[str] parameters_content: The contents of the ARM Template parameters file - containing a JSON list of parameters.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Resource Group Template Deployment should exist. Changing this forces a new Resource Group Template Deployment to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Resource Group Template Deployment.
        :param pulumi.Input[str] template_content: The contents of the ARM Template which should be deployed into this Resource Group.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["debug_level"] = debug_level
        __props__["deployment_mode"] = deployment_mode
        __props__["name"] = name
        __props__["output_content"] = output_content
        __props__["parameters_content"] = parameters_content
        __props__["resource_group_name"] = resource_group_name
        __props__["tags"] = tags
        __props__["template_content"] = template_content
        return ResourceGroupTemplateDeployment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="debugLevel")
    def debug_level(self) -> pulumi.Output[Optional[str]]:
        """
        The Debug Level which should be used for this Resource Group Template Deployment. Possible values are `none`, `requestContent`, `responseContent` and `requestContent, responseContent`.
        """
        return pulumi.get(self, "debug_level")

    @property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> pulumi.Output[str]:
        """
        The Deployment Mode for this Resource Group Template Deployment. Possible values are `Complete` (where resources in the Resource Group not specified in the ARM Template will be destroyed) and `Incremental` (where resources are additive only).
        """
        return pulumi.get(self, "deployment_mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Resource Group Template Deployment. Changing this forces a new Resource Group Template Deployment to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outputContent")
    def output_content(self) -> pulumi.Output[str]:
        """
        The JSON Content of the Outputs of the ARM Template Deployment.
        """
        return pulumi.get(self, "output_content")

    @property
    @pulumi.getter(name="parametersContent")
    def parameters_content(self) -> pulumi.Output[str]:
        """
        The contents of the ARM Template parameters file - containing a JSON list of parameters.
        """
        return pulumi.get(self, "parameters_content")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Resource Group Template Deployment should exist. Changing this forces a new Resource Group Template Deployment to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags which should be assigned to the Resource Group Template Deployment.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateContent")
    def template_content(self) -> pulumi.Output[str]:
        """
        The contents of the ARM Template which should be deployed into this Resource Group.
        """
        return pulumi.get(self, "template_content")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

