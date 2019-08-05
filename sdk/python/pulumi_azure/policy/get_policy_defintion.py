# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetPolicyDefintionResult:
    """
    A collection of values returned by getPolicyDefintion.
    """
    def __init__(__self__, description=None, display_name=None, management_group_id=None, metadata=None, name=None, parameters=None, policy_rule=None, policy_type=None, type=None, id=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        The Description of the Policy.
        """
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        __self__.display_name = display_name
        if management_group_id and not isinstance(management_group_id, str):
            raise TypeError("Expected argument 'management_group_id' to be a str")
        __self__.management_group_id = management_group_id
        if metadata and not isinstance(metadata, str):
            raise TypeError("Expected argument 'metadata' to be a str")
        __self__.metadata = metadata
        """
        Any Metadata defined in the Policy.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The Name of the Policy Definition.
        """
        if parameters and not isinstance(parameters, str):
            raise TypeError("Expected argument 'parameters' to be a str")
        __self__.parameters = parameters
        """
        Any Parameters defined in the Policy.
        """
        if policy_rule and not isinstance(policy_rule, str):
            raise TypeError("Expected argument 'policy_rule' to be a str")
        __self__.policy_rule = policy_rule
        """
        The Rule as defined (in JSON) in the Policy.
        """
        if policy_type and not isinstance(policy_type, str):
            raise TypeError("Expected argument 'policy_type' to be a str")
        __self__.policy_type = policy_type
        """
        The Type of the Policy, such as `Microsoft.Authorization/policyDefinitions`.
        """
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        __self__.type = type
        """
        The Type of Policy.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return self

    __iter__ = __await__

def get_policy_defintion(display_name=None,management_group_id=None,opts=None):
    """
    Use this data source to access information about a Policy Definition, both custom and built in. Retrieves Policy Definitions from your current subscription by default.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/policy_definition.html.markdown.
    """
    __args__ = dict()

    __args__['displayName'] = display_name
    __args__['managementGroupId'] = management_group_id
    if opts is None:
        opts = pulumi.ResourceOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:policy/getPolicyDefintion:getPolicyDefintion', __args__, opts=opts).value

    return GetPolicyDefintionResult(
        description=__ret__.get('description'),
        display_name=__ret__.get('displayName'),
        management_group_id=__ret__.get('managementGroupId'),
        metadata=__ret__.get('metadata'),
        name=__ret__.get('name'),
        parameters=__ret__.get('parameters'),
        policy_rule=__ret__.get('policyRule'),
        policy_type=__ret__.get('policyType'),
        type=__ret__.get('type'),
        id=__ret__.get('id'))
