# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Workspace(pulumi.CustomResource):
    scope: pulumi.Output[str]
    """
    The scope of VMs to send their security data to the desired workspace, unless overridden by a setting with more specific scope.
    """
    workspace_id: pulumi.Output[str]
    """
    The ID of the Log Analytics Workspace to save the data in.
    """
    def __init__(__self__, resource_name, opts=None, scope=None, workspace_id=None, __name__=None, __opts__=None):
        """
        Manages the subscription's Security Center Workspace.
        
        > **NOTE:** Owner access permission is required.
        
        > **NOTE:** The subscription's pricing model can not be `Free` for this to have any affect.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] scope: The scope of VMs to send their security data to the desired workspace, unless overridden by a setting with more specific scope.
        :param pulumi.Input[str] workspace_id: The ID of the Log Analytics Workspace to save the data in.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/security_center_workspace.html.markdown.
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

        if scope is None:
            raise TypeError("Missing required property 'scope'")
        __props__['scope'] = scope

        if workspace_id is None:
            raise TypeError("Missing required property 'workspace_id'")
        __props__['workspace_id'] = workspace_id

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = utilities.get_version()
        super(Workspace, __self__).__init__(
            'azure:securitycenter/workspace:Workspace',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

