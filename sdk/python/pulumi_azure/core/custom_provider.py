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

__all__ = ['CustomProvider']


class CustomProvider(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomProviderActionArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomProviderResourceTypeArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 validations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomProviderValidationArgs']]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an Azure Custom Provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="northeurope")
        example_custom_provider = azure.core.CustomProvider("exampleCustomProvider",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            resource_types=[azure.core.CustomProviderResourceTypeArgs(
                name="dEf1",
                endpoint="https://testendpoint.com/",
            )])
        ```

        ## Import

        Custom Provider can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:core/customProvider:CustomProvider example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example/providers/Microsoft.CustomProviders/resourceProviders/example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomProviderActionArgs']]]] actions: Any number of `action` block as defined below. One of `resource_type` or `action` must be specified.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Custom Provider. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Custom Provider.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomProviderResourceTypeArgs']]]] resource_types: Any number of `resource_type` block as defined below. One of `resource_type` or `action` must be specified.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomProviderValidationArgs']]]] validations: Any number of `validation` block as defined below.
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

            __props__['actions'] = actions
            __props__['location'] = location
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['resource_types'] = resource_types
            __props__['tags'] = tags
            __props__['validations'] = validations
        super(CustomProvider, __self__).__init__(
            'azure:core/customProvider:CustomProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomProviderActionArgs']]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomProviderResourceTypeArgs']]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            validations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomProviderValidationArgs']]]]] = None) -> 'CustomProvider':
        """
        Get an existing CustomProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomProviderActionArgs']]]] actions: Any number of `action` block as defined below. One of `resource_type` or `action` must be specified.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Custom Provider. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Custom Provider.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomProviderResourceTypeArgs']]]] resource_types: Any number of `resource_type` block as defined below. One of `resource_type` or `action` must be specified.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomProviderValidationArgs']]]] validations: Any number of `validation` block as defined below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["actions"] = actions
        __props__["location"] = location
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["resource_types"] = resource_types
        __props__["tags"] = tags
        __props__["validations"] = validations
        return CustomProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Optional[Sequence['outputs.CustomProviderAction']]]:
        """
        Any number of `action` block as defined below. One of `resource_type` or `action` must be specified.
        """
        return pulumi.get(self, "actions")

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
        Specifies the name of the Custom Provider. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the Custom Provider.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> pulumi.Output[Optional[Sequence['outputs.CustomProviderResourceType']]]:
        """
        Any number of `resource_type` block as defined below. One of `resource_type` or `action` must be specified.
        """
        return pulumi.get(self, "resource_types")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def validations(self) -> pulumi.Output[Optional[Sequence['outputs.CustomProviderValidation']]]:
        """
        Any number of `validation` block as defined below.
        """
        return pulumi.get(self, "validations")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

