# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['VirtualNetworkSwiftConnection']


class VirtualNetworkSwiftConnection(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_service_id: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an App Service Virtual Network Association (this is for the [Regional VNet Integration](https://docs.microsoft.com/en-us/azure/app-service/web-sites-integrate-with-vnet#regional-vnet-integration)).

        > **Note:** This resource can be used for both `appservice.AppService` and `appservice.FunctionApp`.

        > **Note:** There is a hard limit of [one VNet integration per App Service Plan](https://docs.microsoft.com/en-us/azure/app-service/web-sites-integrate-with-vnet#regional-vnet-integration).
        Multiple apps in the same App Service plan can use the same VNet.

        ## Example Usage
        ### With App Service)

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="uksouth")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            address_spaces=["10.0.0.0/16"],
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=example_resource_group.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.0.1.0/24"],
            delegations=[azure.network.SubnetDelegationArgs(
                name="example-delegation",
                service_delegation=azure.network.SubnetDelegationServiceDelegationArgs(
                    name="Microsoft.Web/serverFarms",
                    actions=["Microsoft.Network/virtualNetworks/subnets/action"],
                ),
            )])
        example_plan = azure.appservice.Plan("examplePlan",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku=azure.appservice.PlanSkuArgs(
                tier="Standard",
                size="S1",
            ))
        example_app_service = azure.appservice.AppService("exampleAppService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            app_service_plan_id=example_plan.id)
        example_virtual_network_swift_connection = azure.appservice.VirtualNetworkSwiftConnection("exampleVirtualNetworkSwiftConnection",
            app_service_id=example_app_service.id,
            subnet_id=example_subnet.id)
        ```
        ### With Function App)
        ```python
        import pulumi
        import pulumi_azure as azure

        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            address_spaces=["10.0.0.0/16"],
            location=azurerm_resource_group["example"]["location"],
            resource_group_name=azurerm_resource_group["example"]["name"])
        example_subnet = azure.network.Subnet("exampleSubnet",
            resource_group_name=azurerm_resource_group["example"]["name"],
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.0.1.0/24"],
            delegations=[azure.network.SubnetDelegationArgs(
                name="example-delegation",
                service_delegation=azure.network.SubnetDelegationServiceDelegationArgs(
                    name="Microsoft.Web/serverFarms",
                    actions=["Microsoft.Network/virtualNetworks/subnets/action"],
                ),
            )])
        example_plan = azure.appservice.Plan("examplePlan",
            location=azurerm_resource_group["example"]["location"],
            resource_group_name=azurerm_resource_group["example"]["name"],
            sku=azure.appservice.PlanSkuArgs(
                tier="Standard",
                size="S1",
            ))
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=azurerm_resource_group["example"]["name"],
            location=azurerm_resource_group["example"]["location"],
            account_tier="Standard",
            account_replication_type="LRS")
        example_function_app = azure.appservice.FunctionApp("exampleFunctionApp",
            location=azurerm_resource_group["example"]["location"],
            resource_group_name=azurerm_resource_group["example"]["name"],
            app_service_plan_id=example_plan.id,
            storage_account_name=example_account.name,
            storage_account_access_key=example_account.primary_access_key)
        example_virtual_network_swift_connection = azure.appservice.VirtualNetworkSwiftConnection("exampleVirtualNetworkSwiftConnection",
            app_service_id=example_function_app.id,
            subnet_id=example_subnet.id)
        ```

        ## Import

        App Service Virtual Network Associations can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appservice/virtualNetworkSwiftConnection:VirtualNetworkSwiftConnection myassociation /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Web/sites/instance1/config/virtualNetwork
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_service_id: The ID of the App Service or Function App to associate to the VNet. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subnet_id: The ID of the subnet the app service will be associated to (the subnet must have a `service_delegation` configured for `Microsoft.Web/serverFarms`).
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

            if app_service_id is None and not opts.urn:
                raise TypeError("Missing required property 'app_service_id'")
            __props__['app_service_id'] = app_service_id
            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__['subnet_id'] = subnet_id
        super(VirtualNetworkSwiftConnection, __self__).__init__(
            'azure:appservice/virtualNetworkSwiftConnection:VirtualNetworkSwiftConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_service_id: Optional[pulumi.Input[str]] = None,
            subnet_id: Optional[pulumi.Input[str]] = None) -> 'VirtualNetworkSwiftConnection':
        """
        Get an existing VirtualNetworkSwiftConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_service_id: The ID of the App Service or Function App to associate to the VNet. Changing this forces a new resource to be created.
        :param pulumi.Input[str] subnet_id: The ID of the subnet the app service will be associated to (the subnet must have a `service_delegation` configured for `Microsoft.Web/serverFarms`).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["app_service_id"] = app_service_id
        __props__["subnet_id"] = subnet_id
        return VirtualNetworkSwiftConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appServiceId")
    def app_service_id(self) -> pulumi.Output[str]:
        """
        The ID of the App Service or Function App to associate to the VNet. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "app_service_id")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        The ID of the subnet the app service will be associated to (the subnet must have a `service_delegation` configured for `Microsoft.Web/serverFarms`).
        """
        return pulumi.get(self, "subnet_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

