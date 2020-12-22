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

__all__ = ['SparkCluster']


class SparkCluster(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_version: Optional[pulumi.Input[str]] = None,
                 component_version: Optional[pulumi.Input[pulumi.InputType['SparkClusterComponentVersionArgs']]] = None,
                 gateway: Optional[pulumi.Input[pulumi.InputType['SparkClusterGatewayArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metastores: Optional[pulumi.Input[pulumi.InputType['SparkClusterMetastoresArgs']]] = None,
                 monitor: Optional[pulumi.Input[pulumi.InputType['SparkClusterMonitorArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[pulumi.InputType['SparkClusterRolesArgs']]] = None,
                 storage_account_gen2: Optional[pulumi.Input[pulumi.InputType['SparkClusterStorageAccountGen2Args']]] = None,
                 storage_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SparkClusterStorageAccountArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tier: Optional[pulumi.Input[str]] = None,
                 tls_min_version: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a HDInsight Spark Cluster.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.storage.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_container = azure.storage.Container("exampleContainer",
            storage_account_name=example_account.name,
            container_access_type="private")
        example_spark_cluster = azure.hdinsight.SparkCluster("exampleSparkCluster",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            cluster_version="3.6",
            tier="Standard",
            component_version=azure.hdinsight.SparkClusterComponentVersionArgs(
                spark="2.3",
            ),
            gateway=azure.hdinsight.SparkClusterGatewayArgs(
                enabled=True,
                username="acctestusrgw",
                password="Password123!",
            ),
            storage_accounts=[azure.hdinsight.SparkClusterStorageAccountArgs(
                storage_container_id=example_container.id,
                storage_account_key=example_account.primary_access_key,
                is_default=True,
            )],
            roles=azure.hdinsight.SparkClusterRolesArgs(
                head_node=azure.hdinsight.SparkClusterRolesHeadNodeArgs(
                    vm_size="Standard_A3",
                    username="acctestusrvm",
                    password="AccTestvdSC4daf986!",
                ),
                worker_node=azure.hdinsight.SparkClusterRolesWorkerNodeArgs(
                    vm_size="Standard_A3",
                    username="acctestusrvm",
                    password="AccTestvdSC4daf986!",
                    target_instance_count=3,
                ),
                zookeeper_node=azure.hdinsight.SparkClusterRolesZookeeperNodeArgs(
                    vm_size="Medium",
                    username="acctestusrvm",
                    password="AccTestvdSC4daf986!",
                ),
            ))
        ```

        ## Import

        HDInsight Spark Clusters can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:hdinsight/sparkCluster:SparkCluster example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.HDInsight/clusters/cluster1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_version: Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['SparkClusterComponentVersionArgs']] component_version: A `component_version` block as defined below.
        :param pulumi.Input[pulumi.InputType['SparkClusterGatewayArgs']] gateway: A `gateway` block as defined below.
        :param pulumi.Input[str] location: Specifies the Azure Region which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['SparkClusterMetastoresArgs']] metastores: A `metastores` block as defined below.
        :param pulumi.Input[pulumi.InputType['SparkClusterMonitorArgs']] monitor: A `monitor` block as defined below.
        :param pulumi.Input[str] name: Specifies the name for this HDInsight Spark Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group in which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['SparkClusterRolesArgs']] roles: A `roles` block as defined below.
        :param pulumi.Input[pulumi.InputType['SparkClusterStorageAccountGen2Args']] storage_account_gen2: A `storage_account_gen2` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SparkClusterStorageAccountArgs']]]] storage_accounts: One or more `storage_account` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of Tags which should be assigned to this HDInsight Spark Cluster.
        :param pulumi.Input[str] tier: Specifies the Tier which should be used for this HDInsight Spark Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
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

            if cluster_version is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_version'")
            __props__['cluster_version'] = cluster_version
            if component_version is None and not opts.urn:
                raise TypeError("Missing required property 'component_version'")
            __props__['component_version'] = component_version
            if gateway is None and not opts.urn:
                raise TypeError("Missing required property 'gateway'")
            __props__['gateway'] = gateway
            __props__['location'] = location
            __props__['metastores'] = metastores
            __props__['monitor'] = monitor
            __props__['name'] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if roles is None and not opts.urn:
                raise TypeError("Missing required property 'roles'")
            __props__['roles'] = roles
            __props__['storage_account_gen2'] = storage_account_gen2
            __props__['storage_accounts'] = storage_accounts
            __props__['tags'] = tags
            if tier is None and not opts.urn:
                raise TypeError("Missing required property 'tier'")
            __props__['tier'] = tier
            __props__['tls_min_version'] = tls_min_version
            __props__['https_endpoint'] = None
            __props__['ssh_endpoint'] = None
        super(SparkCluster, __self__).__init__(
            'azure:hdinsight/sparkCluster:SparkCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_version: Optional[pulumi.Input[str]] = None,
            component_version: Optional[pulumi.Input[pulumi.InputType['SparkClusterComponentVersionArgs']]] = None,
            gateway: Optional[pulumi.Input[pulumi.InputType['SparkClusterGatewayArgs']]] = None,
            https_endpoint: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            metastores: Optional[pulumi.Input[pulumi.InputType['SparkClusterMetastoresArgs']]] = None,
            monitor: Optional[pulumi.Input[pulumi.InputType['SparkClusterMonitorArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            roles: Optional[pulumi.Input[pulumi.InputType['SparkClusterRolesArgs']]] = None,
            ssh_endpoint: Optional[pulumi.Input[str]] = None,
            storage_account_gen2: Optional[pulumi.Input[pulumi.InputType['SparkClusterStorageAccountGen2Args']]] = None,
            storage_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SparkClusterStorageAccountArgs']]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tier: Optional[pulumi.Input[str]] = None,
            tls_min_version: Optional[pulumi.Input[str]] = None) -> 'SparkCluster':
        """
        Get an existing SparkCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_version: Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['SparkClusterComponentVersionArgs']] component_version: A `component_version` block as defined below.
        :param pulumi.Input[pulumi.InputType['SparkClusterGatewayArgs']] gateway: A `gateway` block as defined below.
        :param pulumi.Input[str] https_endpoint: The HTTPS Connectivity Endpoint for this HDInsight Spark Cluster.
        :param pulumi.Input[str] location: Specifies the Azure Region which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['SparkClusterMetastoresArgs']] metastores: A `metastores` block as defined below.
        :param pulumi.Input[pulumi.InputType['SparkClusterMonitorArgs']] monitor: A `monitor` block as defined below.
        :param pulumi.Input[str] name: Specifies the name for this HDInsight Spark Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group in which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['SparkClusterRolesArgs']] roles: A `roles` block as defined below.
        :param pulumi.Input[str] ssh_endpoint: The SSH Connectivity Endpoint for this HDInsight Spark Cluster.
        :param pulumi.Input[pulumi.InputType['SparkClusterStorageAccountGen2Args']] storage_account_gen2: A `storage_account_gen2` block as defined below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SparkClusterStorageAccountArgs']]]] storage_accounts: One or more `storage_account` block as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of Tags which should be assigned to this HDInsight Spark Cluster.
        :param pulumi.Input[str] tier: Specifies the Tier which should be used for this HDInsight Spark Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cluster_version"] = cluster_version
        __props__["component_version"] = component_version
        __props__["gateway"] = gateway
        __props__["https_endpoint"] = https_endpoint
        __props__["location"] = location
        __props__["metastores"] = metastores
        __props__["monitor"] = monitor
        __props__["name"] = name
        __props__["resource_group_name"] = resource_group_name
        __props__["roles"] = roles
        __props__["ssh_endpoint"] = ssh_endpoint
        __props__["storage_account_gen2"] = storage_account_gen2
        __props__["storage_accounts"] = storage_accounts
        __props__["tags"] = tags
        __props__["tier"] = tier
        __props__["tls_min_version"] = tls_min_version
        return SparkCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> pulumi.Output[str]:
        """
        Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cluster_version")

    @property
    @pulumi.getter(name="componentVersion")
    def component_version(self) -> pulumi.Output['outputs.SparkClusterComponentVersion']:
        """
        A `component_version` block as defined below.
        """
        return pulumi.get(self, "component_version")

    @property
    @pulumi.getter
    def gateway(self) -> pulumi.Output['outputs.SparkClusterGateway']:
        """
        A `gateway` block as defined below.
        """
        return pulumi.get(self, "gateway")

    @property
    @pulumi.getter(name="httpsEndpoint")
    def https_endpoint(self) -> pulumi.Output[str]:
        """
        The HTTPS Connectivity Endpoint for this HDInsight Spark Cluster.
        """
        return pulumi.get(self, "https_endpoint")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the Azure Region which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metastores(self) -> pulumi.Output[Optional['outputs.SparkClusterMetastores']]:
        """
        A `metastores` block as defined below.
        """
        return pulumi.get(self, "metastores")

    @property
    @pulumi.getter
    def monitor(self) -> pulumi.Output[Optional['outputs.SparkClusterMonitor']]:
        """
        A `monitor` block as defined below.
        """
        return pulumi.get(self, "monitor")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name for this HDInsight Spark Cluster. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Resource Group in which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Output['outputs.SparkClusterRoles']:
        """
        A `roles` block as defined below.
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter(name="sshEndpoint")
    def ssh_endpoint(self) -> pulumi.Output[str]:
        """
        The SSH Connectivity Endpoint for this HDInsight Spark Cluster.
        """
        return pulumi.get(self, "ssh_endpoint")

    @property
    @pulumi.getter(name="storageAccountGen2")
    def storage_account_gen2(self) -> pulumi.Output[Optional['outputs.SparkClusterStorageAccountGen2']]:
        """
        A `storage_account_gen2` block as defined below.
        """
        return pulumi.get(self, "storage_account_gen2")

    @property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(self) -> pulumi.Output[Optional[Sequence['outputs.SparkClusterStorageAccount']]]:
        """
        One or more `storage_account` block as defined below.
        """
        return pulumi.get(self, "storage_accounts")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of Tags which should be assigned to this HDInsight Spark Cluster.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Output[str]:
        """
        Specifies the Tier which should be used for this HDInsight Spark Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "tier")

    @property
    @pulumi.getter(name="tlsMinVersion")
    def tls_min_version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "tls_min_version")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

