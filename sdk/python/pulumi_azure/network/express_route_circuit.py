# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class ExpressRouteCircuit(pulumi.CustomResource):
    allow_classic_operations: pulumi.Output[bool]
    """
    Allow the circuit to interact with classic (RDFE) resources. The default value is `false`.
    """
    bandwidth_in_mbps: pulumi.Output[float]
    """
    The bandwidth in Mbps of the circuit being created.
    """
    location: pulumi.Output[str]
    """
    Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    The name of the ExpressRoute circuit. Changing this forces a new resource to be created.
    """
    peering_location: pulumi.Output[str]
    """
    The name of the peering location and **not** the Azure resource location.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which to create the ExpressRoute circuit. Changing this forces a new resource to be created.
    """
    service_key: pulumi.Output[str]
    """
    The string needed by the service provider to provision the ExpressRoute circuit.
    """
    service_provider_name: pulumi.Output[str]
    """
    The name of the ExpressRoute Service Provider.
    """
    service_provider_provisioning_state: pulumi.Output[str]
    """
    The ExpressRoute circuit provisioning state from your chosen service provider. Possible values are "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning".
    """
    sku: pulumi.Output[dict]
    """
    A `sku` block for the ExpressRoute circuit as documented below.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, resource_name, opts=None, allow_classic_operations=None, bandwidth_in_mbps=None, location=None, name=None, peering_location=None, resource_group_name=None, service_provider_name=None, sku=None, tags=None, __name__=None, __opts__=None):
        """
        Manages an ExpressRoute circuit.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_classic_operations: Allow the circuit to interact with classic (RDFE) resources. The default value is `false`.
        :param pulumi.Input[float] bandwidth_in_mbps: The bandwidth in Mbps of the circuit being created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the ExpressRoute circuit. Changing this forces a new resource to be created.
        :param pulumi.Input[str] peering_location: The name of the peering location and **not** the Azure resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the ExpressRoute circuit. Changing this forces a new resource to be created.
        :param pulumi.Input[str] service_provider_name: The name of the ExpressRoute Service Provider.
        :param pulumi.Input[dict] sku: A `sku` block for the ExpressRoute circuit as documented below.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/express_route_circuit.html.markdown.
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

        __props__['allow_classic_operations'] = allow_classic_operations

        if bandwidth_in_mbps is None:
            raise TypeError("Missing required property 'bandwidth_in_mbps'")
        __props__['bandwidth_in_mbps'] = bandwidth_in_mbps

        __props__['location'] = location

        __props__['name'] = name

        if peering_location is None:
            raise TypeError("Missing required property 'peering_location'")
        __props__['peering_location'] = peering_location

        if resource_group_name is None:
            raise TypeError("Missing required property 'resource_group_name'")
        __props__['resource_group_name'] = resource_group_name

        if service_provider_name is None:
            raise TypeError("Missing required property 'service_provider_name'")
        __props__['service_provider_name'] = service_provider_name

        if sku is None:
            raise TypeError("Missing required property 'sku'")
        __props__['sku'] = sku

        __props__['tags'] = tags

        __props__['service_key'] = None
        __props__['service_provider_provisioning_state'] = None

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = utilities.get_version()
        super(ExpressRouteCircuit, __self__).__init__(
            'azure:network/expressRouteCircuit:ExpressRouteCircuit',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

