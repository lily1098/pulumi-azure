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

__all__ = ['Server']


class Server(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_login: Optional[pulumi.Input[str]] = None,
                 administrator_login_password: Optional[pulumi.Input[str]] = None,
                 azuread_administrator: Optional[pulumi.Input[pulumi.InputType['ServerAzureadAdministratorArgs']]] = None,
                 connection_policy: Optional[pulumi.Input[str]] = None,
                 extended_auditing_policy: Optional[pulumi.Input[pulumi.InputType['ServerExtendedAuditingPolicyArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ServerIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 minimum_tls_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_network_access_enabled: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Microsoft SQL Azure Database Server.

        > **Note:** All arguments including the administrator login and password will be stored in the raw state as plain-text.
        [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West US")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_server = azure.mssql.Server("exampleServer",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            version="12.0",
            administrator_login="missadministrator",
            administrator_login_password="thisIsKat11",
            minimum_tls_version="1.2",
            azuread_administrator=azure.mssql.ServerAzureadAdministratorArgs(
                login_username="AzureAD Admin",
                object_id="00000000-0000-0000-0000-000000000000",
            ),
            extended_auditing_policy=azure.mssql.ServerExtendedAuditingPolicyArgs(
                storage_endpoint=example_account.primary_blob_endpoint,
                storage_account_access_key=example_account.primary_access_key,
                storage_account_access_key_is_secondary=True,
                retention_in_days=6,
            ),
            tags={
                "environment": "production",
            })
        ```

        ## Import

        SQL Servers can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:mssql/server:Server example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myresourcegroup/providers/Microsoft.Sql/servers/myserver
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] administrator_login: The administrator login name for the new server. Changing this forces a new resource to be created.
        :param pulumi.Input[str] administrator_login_password: The password associated with the `administrator_login` user. Needs to comply with Azure's [Password Policy](https://msdn.microsoft.com/library/ms161959.aspx)
        :param pulumi.Input[pulumi.InputType['ServerAzureadAdministratorArgs']] azuread_administrator: An `azuread_administrator` block as defined below.
        :param pulumi.Input[str] connection_policy: The connection policy the server will use. Possible values are `Default`, `Proxy`, and `Redirect`. Defaults to `Default`.
        :param pulumi.Input[pulumi.InputType['ServerExtendedAuditingPolicyArgs']] extended_auditing_policy: A `extended_auditing_policy` block as defined below.
        :param pulumi.Input[pulumi.InputType['ServerIdentityArgs']] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] minimum_tls_version: The Minimum TLS Version for all SQL Database and SQL Data Warehouse databases associated with the server. Valid values are: `1.0`, `1.1` and `1.2`.
        :param pulumi.Input[str] name: The name of the Microsoft SQL Server. This needs to be globally unique within Azure.
        :param pulumi.Input[bool] public_network_access_enabled: Whether or not public network access is allowed for this server. Defaults to `true`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Microsoft SQL Server.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] version: The version for the new server. Valid values are: 2.0 (for v11 server) and 12.0 (for v12 server).
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

            if administrator_login is None and not opts.urn:
                raise TypeError("Missing required property 'administrator_login'")
            __props__['administrator_login'] = administrator_login
            if administrator_login_password is None and not opts.urn:
                raise TypeError("Missing required property 'administrator_login_password'")
            __props__['administrator_login_password'] = administrator_login_password
            __props__['azuread_administrator'] = azuread_administrator
            __props__['connection_policy'] = connection_policy
            if extended_auditing_policy is not None and not opts.urn:
                warnings.warn("""the `extended_auditing_policy` block has been moved to `azurerm_mssql_server_extended_auditing_policy` and `azurerm_mssql_database_extended_auditing_policy`. This block will be removed in version 3.0 of the provider.""", DeprecationWarning)
                pulumi.log.warn("extended_auditing_policy is deprecated: the `extended_auditing_policy` block has been moved to `azurerm_mssql_server_extended_auditing_policy` and `azurerm_mssql_database_extended_auditing_policy`. This block will be removed in version 3.0 of the provider.")
            __props__['extended_auditing_policy'] = extended_auditing_policy
            __props__['identity'] = identity
            __props__['location'] = location
            __props__['minimum_tls_version'] = minimum_tls_version
            __props__['name'] = name
            __props__['public_network_access_enabled'] = public_network_access_enabled
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['tags'] = tags
            if version is None and not opts.urn:
                raise TypeError("Missing required property 'version'")
            __props__['version'] = version
            __props__['fully_qualified_domain_name'] = None
            __props__['restorable_dropped_database_ids'] = None
        super(Server, __self__).__init__(
            'azure:mssql/server:Server',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            administrator_login: Optional[pulumi.Input[str]] = None,
            administrator_login_password: Optional[pulumi.Input[str]] = None,
            azuread_administrator: Optional[pulumi.Input[pulumi.InputType['ServerAzureadAdministratorArgs']]] = None,
            connection_policy: Optional[pulumi.Input[str]] = None,
            extended_auditing_policy: Optional[pulumi.Input[pulumi.InputType['ServerExtendedAuditingPolicyArgs']]] = None,
            fully_qualified_domain_name: Optional[pulumi.Input[str]] = None,
            identity: Optional[pulumi.Input[pulumi.InputType['ServerIdentityArgs']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            minimum_tls_version: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            public_network_access_enabled: Optional[pulumi.Input[bool]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            restorable_dropped_database_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'Server':
        """
        Get an existing Server resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] administrator_login: The administrator login name for the new server. Changing this forces a new resource to be created.
        :param pulumi.Input[str] administrator_login_password: The password associated with the `administrator_login` user. Needs to comply with Azure's [Password Policy](https://msdn.microsoft.com/library/ms161959.aspx)
        :param pulumi.Input[pulumi.InputType['ServerAzureadAdministratorArgs']] azuread_administrator: An `azuread_administrator` block as defined below.
        :param pulumi.Input[str] connection_policy: The connection policy the server will use. Possible values are `Default`, `Proxy`, and `Redirect`. Defaults to `Default`.
        :param pulumi.Input[pulumi.InputType['ServerExtendedAuditingPolicyArgs']] extended_auditing_policy: A `extended_auditing_policy` block as defined below.
        :param pulumi.Input[str] fully_qualified_domain_name: The fully qualified domain name of the Azure SQL Server (e.g. myServerName.database.windows.net)
        :param pulumi.Input[pulumi.InputType['ServerIdentityArgs']] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] minimum_tls_version: The Minimum TLS Version for all SQL Database and SQL Data Warehouse databases associated with the server. Valid values are: `1.0`, `1.1` and `1.2`.
        :param pulumi.Input[str] name: The name of the Microsoft SQL Server. This needs to be globally unique within Azure.
        :param pulumi.Input[bool] public_network_access_enabled: Whether or not public network access is allowed for this server. Defaults to `true`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Microsoft SQL Server.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] restorable_dropped_database_ids: A list of dropped restorable database IDs on the server.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] version: The version for the new server. Valid values are: 2.0 (for v11 server) and 12.0 (for v12 server).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["administrator_login"] = administrator_login
        __props__["administrator_login_password"] = administrator_login_password
        __props__["azuread_administrator"] = azuread_administrator
        __props__["connection_policy"] = connection_policy
        __props__["extended_auditing_policy"] = extended_auditing_policy
        __props__["fully_qualified_domain_name"] = fully_qualified_domain_name
        __props__["identity"] = identity
        __props__["location"] = location
        __props__["minimum_tls_version"] = minimum_tls_version
        __props__["name"] = name
        __props__["public_network_access_enabled"] = public_network_access_enabled
        __props__["resource_group_name"] = resource_group_name
        __props__["restorable_dropped_database_ids"] = restorable_dropped_database_ids
        __props__["tags"] = tags
        __props__["version"] = version
        return Server(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> pulumi.Output[str]:
        """
        The administrator login name for the new server. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter(name="administratorLoginPassword")
    def administrator_login_password(self) -> pulumi.Output[str]:
        """
        The password associated with the `administrator_login` user. Needs to comply with Azure's [Password Policy](https://msdn.microsoft.com/library/ms161959.aspx)
        """
        return pulumi.get(self, "administrator_login_password")

    @property
    @pulumi.getter(name="azureadAdministrator")
    def azuread_administrator(self) -> pulumi.Output[Optional['outputs.ServerAzureadAdministrator']]:
        """
        An `azuread_administrator` block as defined below.
        """
        return pulumi.get(self, "azuread_administrator")

    @property
    @pulumi.getter(name="connectionPolicy")
    def connection_policy(self) -> pulumi.Output[Optional[str]]:
        """
        The connection policy the server will use. Possible values are `Default`, `Proxy`, and `Redirect`. Defaults to `Default`.
        """
        return pulumi.get(self, "connection_policy")

    @property
    @pulumi.getter(name="extendedAuditingPolicy")
    def extended_auditing_policy(self) -> pulumi.Output['outputs.ServerExtendedAuditingPolicy']:
        """
        A `extended_auditing_policy` block as defined below.
        """
        return pulumi.get(self, "extended_auditing_policy")

    @property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> pulumi.Output[str]:
        """
        The fully qualified domain name of the Azure SQL Server (e.g. myServerName.database.windows.net)
        """
        return pulumi.get(self, "fully_qualified_domain_name")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ServerIdentity']]:
        """
        An `identity` block as defined below.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> pulumi.Output[Optional[str]]:
        """
        The Minimum TLS Version for all SQL Database and SQL Data Warehouse databases associated with the server. Valid values are: `1.0`, `1.1` and `1.2`.
        """
        return pulumi.get(self, "minimum_tls_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Microsoft SQL Server. This needs to be globally unique within Azure.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicNetworkAccessEnabled")
    def public_network_access_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether or not public network access is allowed for this server. Defaults to `true`.
        """
        return pulumi.get(self, "public_network_access_enabled")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the Microsoft SQL Server.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="restorableDroppedDatabaseIds")
    def restorable_dropped_database_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of dropped restorable database IDs on the server.
        """
        return pulumi.get(self, "restorable_dropped_database_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        The version for the new server. Valid values are: 2.0 (for v11 server) and 12.0 (for v12 server).
        """
        return pulumi.get(self, "version")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

