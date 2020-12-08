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

__all__ = ['IntegrationRuntimeManaged']


class IntegrationRuntimeManaged(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_info: Optional[pulumi.Input[pulumi.InputType['IntegrationRuntimeManagedCatalogInfoArgs']]] = None,
                 custom_setup_script: Optional[pulumi.Input[pulumi.InputType['IntegrationRuntimeManagedCustomSetupScriptArgs']]] = None,
                 data_factory_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 edition: Optional[pulumi.Input[str]] = None,
                 license_type: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_parallel_executions_per_node: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_size: Optional[pulumi.Input[str]] = None,
                 number_of_nodes: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 vnet_integration: Optional[pulumi.Input[pulumi.InputType['IntegrationRuntimeManagedVnetIntegrationArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an Azure Data Factory Managed Integration Runtime.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="northeurope")
        example_factory = azure.datafactory.Factory("exampleFactory",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_integration_runtime_managed = azure.datafactory.IntegrationRuntimeManaged("exampleIntegrationRuntimeManaged",
            data_factory_name=example_factory.name,
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            node_size="Standard_D8_v3")
        ```

        ## Import

        Data Factory Integration Managed Runtimes can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:datafactory/integrationRuntimeManaged:IntegrationRuntimeManaged example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example/providers/Microsoft.DataFactory/factories/example/integrationruntimes/example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['IntegrationRuntimeManagedCatalogInfoArgs']] catalog_info: A `catalog_info` block as defined below.
        :param pulumi.Input[pulumi.InputType['IntegrationRuntimeManagedCustomSetupScriptArgs']] custom_setup_script: A `custom_setup_script` block as defined below.
        :param pulumi.Input[str] data_factory_name: Specifies the name of the Data Factory the Managed Integration Runtime belongs to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] edition: The Managed Integration Runtime edition. Valid values are `Standard` and `Enterprise`. Defaults to `Standard`.
        :param pulumi.Input[str] license_type: The type of the license that is used. Valid values are `LicenseIncluded` and `BasePrize`. Defaults to `LicenseIncluded`.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[int] max_parallel_executions_per_node: Defines the maximum parallel executions per node. Defaults to `1`. Max is `16`.
        :param pulumi.Input[str] name: Specifies the name of the Managed Integration Runtime. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
        :param pulumi.Input[str] node_size: The size of the nodes on which the Managed Integration Runtime runs. Valid values are: `Standard_D2_v3`, `Standard_D4_v3`, `Standard_D8_v3`, `Standard_D16_v3`, `Standard_D32_v3`, `Standard_D64_v3`, `Standard_E2_v3`, `Standard_E4_v3`, `Standard_E8_v3`, `Standard_E16_v3`, `Standard_E32_v3`, `Standard_E64_v3`, `Standard_D1_v2`, `Standard_D2_v2`, `Standard_D3_v2`, `Standard_D4_v2`, `Standard_A4_v2` and `Standard_A8_v2`
        :param pulumi.Input[int] number_of_nodes: Number of nodes for the Managed Integration Runtime. Max is `10`. Defaults to `1`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Managed Integration Runtime. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['IntegrationRuntimeManagedVnetIntegrationArgs']] vnet_integration: A `vnet_integration` block as defined below.
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

            __props__['catalog_info'] = catalog_info
            __props__['custom_setup_script'] = custom_setup_script
            if data_factory_name is None and not opts.urn:
                raise TypeError("Missing required property 'data_factory_name'")
            __props__['data_factory_name'] = data_factory_name
            __props__['description'] = description
            __props__['edition'] = edition
            __props__['license_type'] = license_type
            __props__['location'] = location
            __props__['max_parallel_executions_per_node'] = max_parallel_executions_per_node
            __props__['name'] = name
            if node_size is None and not opts.urn:
                raise TypeError("Missing required property 'node_size'")
            __props__['node_size'] = node_size
            __props__['number_of_nodes'] = number_of_nodes
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['vnet_integration'] = vnet_integration
        super(IntegrationRuntimeManaged, __self__).__init__(
            'azure:datafactory/integrationRuntimeManaged:IntegrationRuntimeManaged',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            catalog_info: Optional[pulumi.Input[pulumi.InputType['IntegrationRuntimeManagedCatalogInfoArgs']]] = None,
            custom_setup_script: Optional[pulumi.Input[pulumi.InputType['IntegrationRuntimeManagedCustomSetupScriptArgs']]] = None,
            data_factory_name: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            edition: Optional[pulumi.Input[str]] = None,
            license_type: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            max_parallel_executions_per_node: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            node_size: Optional[pulumi.Input[str]] = None,
            number_of_nodes: Optional[pulumi.Input[int]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            vnet_integration: Optional[pulumi.Input[pulumi.InputType['IntegrationRuntimeManagedVnetIntegrationArgs']]] = None) -> 'IntegrationRuntimeManaged':
        """
        Get an existing IntegrationRuntimeManaged resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['IntegrationRuntimeManagedCatalogInfoArgs']] catalog_info: A `catalog_info` block as defined below.
        :param pulumi.Input[pulumi.InputType['IntegrationRuntimeManagedCustomSetupScriptArgs']] custom_setup_script: A `custom_setup_script` block as defined below.
        :param pulumi.Input[str] data_factory_name: Specifies the name of the Data Factory the Managed Integration Runtime belongs to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] edition: The Managed Integration Runtime edition. Valid values are `Standard` and `Enterprise`. Defaults to `Standard`.
        :param pulumi.Input[str] license_type: The type of the license that is used. Valid values are `LicenseIncluded` and `BasePrize`. Defaults to `LicenseIncluded`.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[int] max_parallel_executions_per_node: Defines the maximum parallel executions per node. Defaults to `1`. Max is `16`.
        :param pulumi.Input[str] name: Specifies the name of the Managed Integration Runtime. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
        :param pulumi.Input[str] node_size: The size of the nodes on which the Managed Integration Runtime runs. Valid values are: `Standard_D2_v3`, `Standard_D4_v3`, `Standard_D8_v3`, `Standard_D16_v3`, `Standard_D32_v3`, `Standard_D64_v3`, `Standard_E2_v3`, `Standard_E4_v3`, `Standard_E8_v3`, `Standard_E16_v3`, `Standard_E32_v3`, `Standard_E64_v3`, `Standard_D1_v2`, `Standard_D2_v2`, `Standard_D3_v2`, `Standard_D4_v2`, `Standard_A4_v2` and `Standard_A8_v2`
        :param pulumi.Input[int] number_of_nodes: Number of nodes for the Managed Integration Runtime. Max is `10`. Defaults to `1`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Managed Integration Runtime. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['IntegrationRuntimeManagedVnetIntegrationArgs']] vnet_integration: A `vnet_integration` block as defined below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["catalog_info"] = catalog_info
        __props__["custom_setup_script"] = custom_setup_script
        __props__["data_factory_name"] = data_factory_name
        __props__["description"] = description
        __props__["edition"] = edition
        __props__["license_type"] = license_type
        __props__["location"] = location
        __props__["max_parallel_executions_per_node"] = max_parallel_executions_per_node
        __props__["name"] = name
        __props__["node_size"] = node_size
        __props__["number_of_nodes"] = number_of_nodes
        __props__["resource_group_name"] = resource_group_name
        __props__["vnet_integration"] = vnet_integration
        return IntegrationRuntimeManaged(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="catalogInfo")
    def catalog_info(self) -> pulumi.Output[Optional['outputs.IntegrationRuntimeManagedCatalogInfo']]:
        """
        A `catalog_info` block as defined below.
        """
        return pulumi.get(self, "catalog_info")

    @property
    @pulumi.getter(name="customSetupScript")
    def custom_setup_script(self) -> pulumi.Output[Optional['outputs.IntegrationRuntimeManagedCustomSetupScript']]:
        """
        A `custom_setup_script` block as defined below.
        """
        return pulumi.get(self, "custom_setup_script")

    @property
    @pulumi.getter(name="dataFactoryName")
    def data_factory_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Data Factory the Managed Integration Runtime belongs to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "data_factory_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def edition(self) -> pulumi.Output[Optional[str]]:
        """
        The Managed Integration Runtime edition. Valid values are `Standard` and `Enterprise`. Defaults to `Standard`.
        """
        return pulumi.get(self, "edition")

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the license that is used. Valid values are `LicenseIncluded` and `BasePrize`. Defaults to `LicenseIncluded`.
        """
        return pulumi.get(self, "license_type")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxParallelExecutionsPerNode")
    def max_parallel_executions_per_node(self) -> pulumi.Output[Optional[int]]:
        """
        Defines the maximum parallel executions per node. Defaults to `1`. Max is `16`.
        """
        return pulumi.get(self, "max_parallel_executions_per_node")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Managed Integration Runtime. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeSize")
    def node_size(self) -> pulumi.Output[str]:
        """
        The size of the nodes on which the Managed Integration Runtime runs. Valid values are: `Standard_D2_v3`, `Standard_D4_v3`, `Standard_D8_v3`, `Standard_D16_v3`, `Standard_D32_v3`, `Standard_D64_v3`, `Standard_E2_v3`, `Standard_E4_v3`, `Standard_E8_v3`, `Standard_E16_v3`, `Standard_E32_v3`, `Standard_E64_v3`, `Standard_D1_v2`, `Standard_D2_v2`, `Standard_D3_v2`, `Standard_D4_v2`, `Standard_A4_v2` and `Standard_A8_v2`
        """
        return pulumi.get(self, "node_size")

    @property
    @pulumi.getter(name="numberOfNodes")
    def number_of_nodes(self) -> pulumi.Output[Optional[int]]:
        """
        Number of nodes for the Managed Integration Runtime. Max is `10`. Defaults to `1`.
        """
        return pulumi.get(self, "number_of_nodes")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the Managed Integration Runtime. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="vnetIntegration")
    def vnet_integration(self) -> pulumi.Output[Optional['outputs.IntegrationRuntimeManagedVnetIntegration']]:
        """
        A `vnet_integration` block as defined below.
        """
        return pulumi.get(self, "vnet_integration")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

