# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class ActivityLogAlert(pulumi.CustomResource):
    actions: pulumi.Output[list]
    """
    One or more `action` blocks as defined below.
    """
    criteria: pulumi.Output[dict]
    """
    A `criteria` block as defined below.
    """
    description: pulumi.Output[str]
    """
    The description of this activity log alert.
    """
    enabled: pulumi.Output[bool]
    """
    Should this Activity Log Alert be enabled? Defaults to `true`.
    """
    name: pulumi.Output[str]
    """
    The name of the activity log alert. Changing this forces a new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which to create the activity log alert instance.
    """
    scopes: pulumi.Output[list]
    """
    The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, resource_name, opts=None, actions=None, criteria=None, description=None, enabled=None, name=None, resource_group_name=None, scopes=None, tags=None, __name__=None, __opts__=None):
        """
        Manages an Activity Log Alert within Azure Monitor.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] actions: One or more `action` blocks as defined below.
        :param pulumi.Input[dict] criteria: A `criteria` block as defined below.
        :param pulumi.Input[str] description: The description of this activity log alert.
        :param pulumi.Input[bool] enabled: Should this Activity Log Alert be enabled? Defaults to `true`.
        :param pulumi.Input[str] name: The name of the activity log alert. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the activity log alert instance.
        :param pulumi.Input[list] scopes: The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_activity_log_alert.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['actions'] = actions

        if criteria is None:
            raise TypeError("Missing required property 'criteria'")
        __props__['criteria'] = criteria

        __props__['description'] = description

        __props__['enabled'] = enabled

        __props__['name'] = name

        if resource_group_name is None:
            raise TypeError("Missing required property 'resource_group_name'")
        __props__['resource_group_name'] = resource_group_name

        if scopes is None:
            raise TypeError("Missing required property 'scopes'")
        __props__['scopes'] = scopes

        __props__['tags'] = tags

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = utilities.get_version()
        super(ActivityLogAlert, __self__).__init__(
            'azure:monitoring/activityLogAlert:ActivityLogAlert',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

