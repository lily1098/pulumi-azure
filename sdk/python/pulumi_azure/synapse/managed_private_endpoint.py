# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['ManagedPrivateEndpoint']


class ManagedPrivateEndpoint(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 subresource_name: Optional[pulumi.Input[str]] = None,
                 synapse_workspace_id: Optional[pulumi.Input[str]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Allows you to Manages a Synapse Managed Private Endpoint.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS",
            account_kind="StorageV2",
            is_hns_enabled=True)
        example_data_lake_gen2_filesystem = azure.storage.DataLakeGen2Filesystem("exampleDataLakeGen2Filesystem", storage_account_id=example_account.id)
        example_workspace = azure.synapse.Workspace("exampleWorkspace",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            storage_data_lake_gen2_filesystem_id=example_data_lake_gen2_filesystem.id,
            sql_administrator_login="sqladminuser",
            sql_administrator_login_password="H@Sh1CoR3!",
            managed_virtual_network_enabled=True)
        example_firewall_rule = azure.synapse.FirewallRule("exampleFirewallRule",
            synapse_workspace_id=azurerm_synapse_workspace["test"]["id"],
            start_ip_address="0.0.0.0",
            end_ip_address="255.255.255.255")
        example_connect = azure.storage.Account("exampleConnect",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS",
            account_kind="BlobStorage")
        example_managed_private_endpoint = azure.synapse.ManagedPrivateEndpoint("exampleManagedPrivateEndpoint",
            synapse_workspace_id=example_workspace.id,
            target_resource_id=example_connect.id,
            subresource_name="blob",
            opts=pulumi.ResourceOptions(depends_on=[example_firewall_rule]))
        ```

        ## Import

        Synapse Managed Private Endpoint can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:synapse/managedPrivateEndpoint:ManagedPrivateEndpoint example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Synapse/workspaces/workspace1/managedVirtualNetworks/default/managedPrivateEndpoints/endpoint1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Managed Private Endpoint. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subresource_name: Specifies the sub resource name which the Synapse Private Endpoint is able to connect to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] synapse_workspace_id: The ID of the Synapse Workspace on which to create the Managed Private Endpoint. Changing this forces a new resource to be created.
        :param pulumi.Input[str] target_resource_id: The ID of the Private Link Enabled Remote Resource which this Synapse Private Endpoint should be connected to. Changing this forces a new resource to be created.
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

            __props__['name'] = name
            if subresource_name is None and not opts.urn:
                raise TypeError("Missing required property 'subresource_name'")
            __props__['subresource_name'] = subresource_name
            if synapse_workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'synapse_workspace_id'")
            __props__['synapse_workspace_id'] = synapse_workspace_id
            if target_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'target_resource_id'")
            __props__['target_resource_id'] = target_resource_id
        super(ManagedPrivateEndpoint, __self__).__init__(
            'azure:synapse/managedPrivateEndpoint:ManagedPrivateEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            subresource_name: Optional[pulumi.Input[str]] = None,
            synapse_workspace_id: Optional[pulumi.Input[str]] = None,
            target_resource_id: Optional[pulumi.Input[str]] = None) -> 'ManagedPrivateEndpoint':
        """
        Get an existing ManagedPrivateEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Managed Private Endpoint. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subresource_name: Specifies the sub resource name which the Synapse Private Endpoint is able to connect to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] synapse_workspace_id: The ID of the Synapse Workspace on which to create the Managed Private Endpoint. Changing this forces a new resource to be created.
        :param pulumi.Input[str] target_resource_id: The ID of the Private Link Enabled Remote Resource which this Synapse Private Endpoint should be connected to. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["name"] = name
        __props__["subresource_name"] = subresource_name
        __props__["synapse_workspace_id"] = synapse_workspace_id
        __props__["target_resource_id"] = target_resource_id
        return ManagedPrivateEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name which should be used for this Managed Private Endpoint. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="subresourceName")
    def subresource_name(self) -> pulumi.Output[str]:
        """
        Specifies the sub resource name which the Synapse Private Endpoint is able to connect to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "subresource_name")

    @property
    @pulumi.getter(name="synapseWorkspaceId")
    def synapse_workspace_id(self) -> pulumi.Output[str]:
        """
        The ID of the Synapse Workspace on which to create the Managed Private Endpoint. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "synapse_workspace_id")

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> pulumi.Output[str]:
        """
        The ID of the Private Link Enabled Remote Resource which this Synapse Private Endpoint should be connected to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "target_resource_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

