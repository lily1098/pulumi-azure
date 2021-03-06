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

__all__ = ['BackendAddressPool']


class BackendAddressPool(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BackendAddressPoolBackendAddressArgs']]]]] = None,
                 loadbalancer_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Load Balancer Backend Address Pool.

        > **NOTE:** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West US")
        example_public_ip = azure.network.PublicIp("examplePublicIp",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            allocation_method="Static")
        example_load_balancer = azure.lb.LoadBalancer("exampleLoadBalancer",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            frontend_ip_configurations=[azure.lb.LoadBalancerFrontendIpConfigurationArgs(
                name="PublicIPAddress",
                public_ip_address_id=example_public_ip.id,
            )])
        example_backend_address_pool = azure.lb.BackendAddressPool("exampleBackendAddressPool", loadbalancer_id=example_load_balancer.id)
        ```

        ## Import

        Load Balancer Backend Address Pools can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:lb/backendAddressPool:BackendAddressPool example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/loadBalancers/lb1/backendAddressPools/pool1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] loadbalancer_id: The ID of the Load Balancer in which to create the Backend Address Pool.
        :param pulumi.Input[str] name: Specifies the name of the Backend Address Pool.
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

            if backend_addresses is not None and not opts.urn:
                warnings.warn("""This field is non-functional and will be removed in version 3.0 of the Azure Provider - use the separate `azurerm_lb_backend_address_pool_address` resource instead.""", DeprecationWarning)
                pulumi.log.warn("backend_addresses is deprecated: This field is non-functional and will be removed in version 3.0 of the Azure Provider - use the separate `azurerm_lb_backend_address_pool_address` resource instead.")
            __props__['backend_addresses'] = backend_addresses
            if loadbalancer_id is None and not opts.urn:
                raise TypeError("Missing required property 'loadbalancer_id'")
            __props__['loadbalancer_id'] = loadbalancer_id
            __props__['name'] = name
            if resource_group_name is not None and not opts.urn:
                warnings.warn("""This field is no longer used and will be removed in the next major version of the Azure Provider""", DeprecationWarning)
                pulumi.log.warn("resource_group_name is deprecated: This field is no longer used and will be removed in the next major version of the Azure Provider")
            __props__['resource_group_name'] = resource_group_name
            __props__['backend_ip_configurations'] = None
            __props__['load_balancing_rules'] = None
            __props__['outbound_rules'] = None
        super(BackendAddressPool, __self__).__init__(
            'azure:lb/backendAddressPool:BackendAddressPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            backend_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BackendAddressPoolBackendAddressArgs']]]]] = None,
            backend_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            load_balancing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            loadbalancer_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            outbound_rules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None) -> 'BackendAddressPool':
        """
        Get an existing BackendAddressPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] backend_ip_configurations: The Backend IP Configurations associated with this Backend Address Pool.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] load_balancing_rules: The Load Balancing Rules associated with this Backend Address Pool.
        :param pulumi.Input[str] loadbalancer_id: The ID of the Load Balancer in which to create the Backend Address Pool.
        :param pulumi.Input[str] name: Specifies the name of the Backend Address Pool.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] outbound_rules: An array of the Load Balancing Outbound Rules associated with this Backend Address Pool.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["backend_addresses"] = backend_addresses
        __props__["backend_ip_configurations"] = backend_ip_configurations
        __props__["load_balancing_rules"] = load_balancing_rules
        __props__["loadbalancer_id"] = loadbalancer_id
        __props__["name"] = name
        __props__["outbound_rules"] = outbound_rules
        __props__["resource_group_name"] = resource_group_name
        return BackendAddressPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backendAddresses")
    def backend_addresses(self) -> pulumi.Output[Optional[Sequence['outputs.BackendAddressPoolBackendAddress']]]:
        return pulumi.get(self, "backend_addresses")

    @property
    @pulumi.getter(name="backendIpConfigurations")
    def backend_ip_configurations(self) -> pulumi.Output[Sequence[str]]:
        """
        The Backend IP Configurations associated with this Backend Address Pool.
        """
        return pulumi.get(self, "backend_ip_configurations")

    @property
    @pulumi.getter(name="loadBalancingRules")
    def load_balancing_rules(self) -> pulumi.Output[Sequence[str]]:
        """
        The Load Balancing Rules associated with this Backend Address Pool.
        """
        return pulumi.get(self, "load_balancing_rules")

    @property
    @pulumi.getter(name="loadbalancerId")
    def loadbalancer_id(self) -> pulumi.Output[str]:
        """
        The ID of the Load Balancer in which to create the Backend Address Pool.
        """
        return pulumi.get(self, "loadbalancer_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Backend Address Pool.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outboundRules")
    def outbound_rules(self) -> pulumi.Output[Sequence[str]]:
        """
        An array of the Load Balancing Outbound Rules associated with this Backend Address Pool.
        """
        return pulumi.get(self, "outbound_rules")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "resource_group_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

