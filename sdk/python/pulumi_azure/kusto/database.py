# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Database']


class Database(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 hot_cache_period: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 soft_delete_period: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Kusto (also known as Azure Data Explorer) Database

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        rg = azure.core.ResourceGroup("rg", location="East US")
        cluster = azure.kusto.Cluster("cluster",
            location=rg.location,
            resource_group_name=rg.name,
            sku=azure.kusto.ClusterSkuArgs(
                name="Standard_D13_v2",
                capacity=2,
            ))
        database = azure.kusto.Database("database",
            resource_group_name=rg.name,
            location=rg.location,
            cluster_name=cluster.name,
            hot_cache_period="P7D",
            soft_delete_period="P31D")
        ```

        ## Import

        Kusto Clusters can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:kusto/database:Database example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Kusto/Clusters/cluster1/Databases/database1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: Specifies the name of the Kusto Cluster this database will be added to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] hot_cache_period: The time the data that should be kept in cache for fast queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        :param pulumi.Input[str] location: The location where the Kusto Database should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Kusto Database to create. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] soft_delete_period: The time the data should be kept before it stops being accessible to queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
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

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__['cluster_name'] = cluster_name
            __props__['hot_cache_period'] = hot_cache_period
            __props__['location'] = location
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['soft_delete_period'] = soft_delete_period
            __props__['size'] = None
        super(Database, __self__).__init__(
            'azure:kusto/database:Database',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_name: Optional[pulumi.Input[str]] = None,
            hot_cache_period: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[float]] = None,
            soft_delete_period: Optional[pulumi.Input[str]] = None) -> 'Database':
        """
        Get an existing Database resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: Specifies the name of the Kusto Cluster this database will be added to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] hot_cache_period: The time the data that should be kept in cache for fast queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        :param pulumi.Input[str] location: The location where the Kusto Database should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Kusto Database to create. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[float] size: The size of the database in bytes.
        :param pulumi.Input[str] soft_delete_period: The time the data should be kept before it stops being accessible to queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cluster_name"] = cluster_name
        __props__["hot_cache_period"] = hot_cache_period
        __props__["location"] = location
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["size"] = size
        __props__["soft_delete_period"] = soft_delete_period
        return Database(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Kusto Cluster this database will be added to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="hotCachePeriod")
    def hot_cache_period(self) -> pulumi.Output[Optional[str]]:
        """
        The time the data that should be kept in cache for fast queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        """
        return pulumi.get(self, "hot_cache_period")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location where the Kusto Database should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Kusto Database to create. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[float]:
        """
        The size of the database in bytes.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="softDeletePeriod")
    def soft_delete_period(self) -> pulumi.Output[Optional[str]]:
        """
        The time the data should be kept before it stops being accessible to queries as ISO 8601 timespan. Default is unlimited. For more information see: [ISO 8601 Timespan](https://en.wikipedia.org/wiki/ISO_8601#Durations)
        """
        return pulumi.get(self, "soft_delete_period")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

