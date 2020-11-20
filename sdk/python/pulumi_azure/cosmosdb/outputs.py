# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'AccountCapability',
    'AccountConsistencyPolicy',
    'AccountGeoLocation',
    'AccountVirtualNetworkRule',
    'CassandraKeyspaceAutoscaleSettings',
    'GremlinDatabaseAutoscaleSettings',
    'GremlinGraphAutoscaleSettings',
    'GremlinGraphConflictResolutionPolicy',
    'GremlinGraphIndexPolicy',
    'GremlinGraphUniqueKey',
    'MongoCollectionAutoscaleSettings',
    'MongoCollectionIndex',
    'MongoCollectionSystemIndex',
    'MongoDatabaseAutoscaleSettings',
    'SqlContainerAutoscaleSettings',
    'SqlContainerIndexingPolicy',
    'SqlContainerIndexingPolicyCompositeIndex',
    'SqlContainerIndexingPolicyCompositeIndexIndex',
    'SqlContainerIndexingPolicyExcludedPath',
    'SqlContainerIndexingPolicyIncludedPath',
    'SqlContainerUniqueKey',
    'SqlDatabaseAutoscaleSettings',
    'TableAutoscaleSettings',
    'GetAccountCapabilityResult',
    'GetAccountConsistencyPolicyResult',
    'GetAccountGeoLocationResult',
    'GetAccountVirtualNetworkRuleResult',
]

@pulumi.output_type
class AccountCapability(dict):
    def __init__(__self__, *,
                 name: str):
        """
        :param str name: Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class AccountConsistencyPolicy(dict):
    def __init__(__self__, *,
                 consistency_level: str,
                 max_interval_in_seconds: Optional[int] = None,
                 max_staleness_prefix: Optional[int] = None):
        """
        :param str consistency_level: The Consistency Level to use for this CosmosDB Account - can be either `BoundedStaleness`, `Eventual`, `Session`, `Strong` or `ConsistentPrefix`.
        :param int max_interval_in_seconds: When used with the Bounded Staleness consistency level, this value represents the time amount of staleness (in seconds) tolerated. Accepted range for this value is `5` - `86400` (1 day). Defaults to `5`. Required when `consistency_level` is set to `BoundedStaleness`.
        :param int max_staleness_prefix: When used with the Bounded Staleness consistency level, this value represents the number of stale requests tolerated. Accepted range for this value is `10` – `2147483647`. Defaults to `100`. Required when `consistency_level` is set to `BoundedStaleness`.
        """
        pulumi.set(__self__, "consistency_level", consistency_level)
        if max_interval_in_seconds is not None:
            pulumi.set(__self__, "max_interval_in_seconds", max_interval_in_seconds)
        if max_staleness_prefix is not None:
            pulumi.set(__self__, "max_staleness_prefix", max_staleness_prefix)

    @property
    @pulumi.getter(name="consistencyLevel")
    def consistency_level(self) -> str:
        """
        The Consistency Level to use for this CosmosDB Account - can be either `BoundedStaleness`, `Eventual`, `Session`, `Strong` or `ConsistentPrefix`.
        """
        return pulumi.get(self, "consistency_level")

    @property
    @pulumi.getter(name="maxIntervalInSeconds")
    def max_interval_in_seconds(self) -> Optional[int]:
        """
        When used with the Bounded Staleness consistency level, this value represents the time amount of staleness (in seconds) tolerated. Accepted range for this value is `5` - `86400` (1 day). Defaults to `5`. Required when `consistency_level` is set to `BoundedStaleness`.
        """
        return pulumi.get(self, "max_interval_in_seconds")

    @property
    @pulumi.getter(name="maxStalenessPrefix")
    def max_staleness_prefix(self) -> Optional[int]:
        """
        When used with the Bounded Staleness consistency level, this value represents the number of stale requests tolerated. Accepted range for this value is `10` – `2147483647`. Defaults to `100`. Required when `consistency_level` is set to `BoundedStaleness`.
        """
        return pulumi.get(self, "max_staleness_prefix")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class AccountGeoLocation(dict):
    def __init__(__self__, *,
                 failover_priority: int,
                 location: str,
                 id: Optional[str] = None,
                 prefix: Optional[str] = None,
                 zone_redundant: Optional[bool] = None):
        """
        :param int failover_priority: The failover priority of the region. A failover priority of `0` indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. Changing this causes the location to be re-provisioned and cannot be changed for the location with failover priority `0`.
        :param str location: The name of the Azure region to host replicated data.
        :param str id: The ID of the virtual network subnet.
        :param str prefix: The string used to generate the document endpoints for this region. If not specified it defaults to `${cosmosdb_account.name}-${location}`. Changing this causes the location to be deleted and re-provisioned and cannot be changed for the location with failover priority `0`.
        :param bool zone_redundant: Should zone redundancy be enabled for this region? Defaults to `false`.
        """
        pulumi.set(__self__, "failover_priority", failover_priority)
        pulumi.set(__self__, "location", location)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)
        if zone_redundant is not None:
            pulumi.set(__self__, "zone_redundant", zone_redundant)

    @property
    @pulumi.getter(name="failoverPriority")
    def failover_priority(self) -> int:
        """
        The failover priority of the region. A failover priority of `0` indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. Changing this causes the location to be re-provisioned and cannot be changed for the location with failover priority `0`.
        """
        return pulumi.get(self, "failover_priority")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The name of the Azure region to host replicated data.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ID of the virtual network subnet.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        """
        The string used to generate the document endpoints for this region. If not specified it defaults to `${cosmosdb_account.name}-${location}`. Changing this causes the location to be deleted and re-provisioned and cannot be changed for the location with failover priority `0`.
        """
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[bool]:
        """
        Should zone redundancy be enabled for this region? Defaults to `false`.
        """
        return pulumi.get(self, "zone_redundant")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class AccountVirtualNetworkRule(dict):
    def __init__(__self__, *,
                 id: str,
                 ignore_missing_vnet_service_endpoint: Optional[bool] = None):
        """
        :param str id: The ID of the virtual network subnet.
        :param bool ignore_missing_vnet_service_endpoint: If set to true, the specified subnet will be added as a virtual network rule even if its CosmosDB service endpoint is not active. Defaults to `false`.
        """
        pulumi.set(__self__, "id", id)
        if ignore_missing_vnet_service_endpoint is not None:
            pulumi.set(__self__, "ignore_missing_vnet_service_endpoint", ignore_missing_vnet_service_endpoint)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the virtual network subnet.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ignoreMissingVnetServiceEndpoint")
    def ignore_missing_vnet_service_endpoint(self) -> Optional[bool]:
        """
        If set to true, the specified subnet will be added as a virtual network rule even if its CosmosDB service endpoint is not active. Defaults to `false`.
        """
        return pulumi.get(self, "ignore_missing_vnet_service_endpoint")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CassandraKeyspaceAutoscaleSettings(dict):
    def __init__(__self__, *,
                 max_throughput: Optional[int] = None):
        """
        :param int max_throughput: The maximum throughput of the Cassandra KeySpace (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.
        """
        if max_throughput is not None:
            pulumi.set(__self__, "max_throughput", max_throughput)

    @property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> Optional[int]:
        """
        The maximum throughput of the Cassandra KeySpace (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.
        """
        return pulumi.get(self, "max_throughput")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GremlinDatabaseAutoscaleSettings(dict):
    def __init__(__self__, *,
                 max_throughput: Optional[int] = None):
        """
        :param int max_throughput: The maximum throughput of the Gremlin database (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.
        """
        if max_throughput is not None:
            pulumi.set(__self__, "max_throughput", max_throughput)

    @property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> Optional[int]:
        """
        The maximum throughput of the Gremlin database (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.
        """
        return pulumi.get(self, "max_throughput")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GremlinGraphAutoscaleSettings(dict):
    def __init__(__self__, *,
                 max_throughput: Optional[int] = None):
        """
        :param int max_throughput: The maximum throughput of the Gremlin graph (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.
        """
        if max_throughput is not None:
            pulumi.set(__self__, "max_throughput", max_throughput)

    @property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> Optional[int]:
        """
        The maximum throughput of the Gremlin graph (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.
        """
        return pulumi.get(self, "max_throughput")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GremlinGraphConflictResolutionPolicy(dict):
    def __init__(__self__, *,
                 mode: str,
                 conflict_resolution_path: Optional[str] = None,
                 conflict_resolution_procedure: Optional[str] = None):
        """
        :param str mode: Indicates the conflict resolution mode. Possible values include: `LastWriterWins`, `Custom`.
        :param str conflict_resolution_path: The conflict resolution path in the case of LastWriterWins mode.
        :param str conflict_resolution_procedure: The procedure to resolve conflicts in the case of custom mode.
        """
        pulumi.set(__self__, "mode", mode)
        if conflict_resolution_path is not None:
            pulumi.set(__self__, "conflict_resolution_path", conflict_resolution_path)
        if conflict_resolution_procedure is not None:
            pulumi.set(__self__, "conflict_resolution_procedure", conflict_resolution_procedure)

    @property
    @pulumi.getter
    def mode(self) -> str:
        """
        Indicates the conflict resolution mode. Possible values include: `LastWriterWins`, `Custom`.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter(name="conflictResolutionPath")
    def conflict_resolution_path(self) -> Optional[str]:
        """
        The conflict resolution path in the case of LastWriterWins mode.
        """
        return pulumi.get(self, "conflict_resolution_path")

    @property
    @pulumi.getter(name="conflictResolutionProcedure")
    def conflict_resolution_procedure(self) -> Optional[str]:
        """
        The procedure to resolve conflicts in the case of custom mode.
        """
        return pulumi.get(self, "conflict_resolution_procedure")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GremlinGraphIndexPolicy(dict):
    def __init__(__self__, *,
                 indexing_mode: str,
                 automatic: Optional[bool] = None,
                 excluded_paths: Optional[Sequence[str]] = None,
                 included_paths: Optional[Sequence[str]] = None):
        """
        :param str indexing_mode: Indicates the indexing mode. Possible values include: `Consistent`, `Lazy`, `None`.
        :param bool automatic: Indicates if the indexing policy is automatic. Defaults to `true`.
        :param Sequence[str] excluded_paths: List of paths to exclude from indexing. Required if `indexing_mode` is `Consistent` or `Lazy`.
        :param Sequence[str] included_paths: List of paths to include in the indexing. Required if `indexing_mode` is `Consistent` or `Lazy`.
        """
        pulumi.set(__self__, "indexing_mode", indexing_mode)
        if automatic is not None:
            pulumi.set(__self__, "automatic", automatic)
        if excluded_paths is not None:
            pulumi.set(__self__, "excluded_paths", excluded_paths)
        if included_paths is not None:
            pulumi.set(__self__, "included_paths", included_paths)

    @property
    @pulumi.getter(name="indexingMode")
    def indexing_mode(self) -> str:
        """
        Indicates the indexing mode. Possible values include: `Consistent`, `Lazy`, `None`.
        """
        return pulumi.get(self, "indexing_mode")

    @property
    @pulumi.getter
    def automatic(self) -> Optional[bool]:
        """
        Indicates if the indexing policy is automatic. Defaults to `true`.
        """
        return pulumi.get(self, "automatic")

    @property
    @pulumi.getter(name="excludedPaths")
    def excluded_paths(self) -> Optional[Sequence[str]]:
        """
        List of paths to exclude from indexing. Required if `indexing_mode` is `Consistent` or `Lazy`.
        """
        return pulumi.get(self, "excluded_paths")

    @property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[str]]:
        """
        List of paths to include in the indexing. Required if `indexing_mode` is `Consistent` or `Lazy`.
        """
        return pulumi.get(self, "included_paths")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GremlinGraphUniqueKey(dict):
    def __init__(__self__, *,
                 paths: Sequence[str]):
        """
        :param Sequence[str] paths: A list of paths to use for this unique key.
        """
        pulumi.set(__self__, "paths", paths)

    @property
    @pulumi.getter
    def paths(self) -> Sequence[str]:
        """
        A list of paths to use for this unique key.
        """
        return pulumi.get(self, "paths")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MongoCollectionAutoscaleSettings(dict):
    def __init__(__self__, *,
                 max_throughput: Optional[int] = None):
        """
        :param int max_throughput: The maximum throughput of the MongoDB collection (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.
        """
        if max_throughput is not None:
            pulumi.set(__self__, "max_throughput", max_throughput)

    @property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> Optional[int]:
        """
        The maximum throughput of the MongoDB collection (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.
        """
        return pulumi.get(self, "max_throughput")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MongoCollectionIndex(dict):
    def __init__(__self__, *,
                 keys: Sequence[str],
                 unique: Optional[bool] = None):
        """
        :param Sequence[str] keys: Specifies the list of user settable keys for each Cosmos DB Mongo Collection.
        :param bool unique: Is the index unique or not? Defaults to `false`.
        """
        pulumi.set(__self__, "keys", keys)
        if unique is not None:
            pulumi.set(__self__, "unique", unique)

    @property
    @pulumi.getter
    def keys(self) -> Sequence[str]:
        """
        Specifies the list of user settable keys for each Cosmos DB Mongo Collection.
        """
        return pulumi.get(self, "keys")

    @property
    @pulumi.getter
    def unique(self) -> Optional[bool]:
        """
        Is the index unique or not? Defaults to `false`.
        """
        return pulumi.get(self, "unique")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MongoCollectionSystemIndex(dict):
    def __init__(__self__, *,
                 keys: Optional[Sequence[str]] = None,
                 unique: Optional[bool] = None):
        """
        :param Sequence[str] keys: Specifies the list of user settable keys for each Cosmos DB Mongo Collection.
        :param bool unique: Is the index unique or not? Defaults to `false`.
        """
        if keys is not None:
            pulumi.set(__self__, "keys", keys)
        if unique is not None:
            pulumi.set(__self__, "unique", unique)

    @property
    @pulumi.getter
    def keys(self) -> Optional[Sequence[str]]:
        """
        Specifies the list of user settable keys for each Cosmos DB Mongo Collection.
        """
        return pulumi.get(self, "keys")

    @property
    @pulumi.getter
    def unique(self) -> Optional[bool]:
        """
        Is the index unique or not? Defaults to `false`.
        """
        return pulumi.get(self, "unique")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MongoDatabaseAutoscaleSettings(dict):
    def __init__(__self__, *,
                 max_throughput: Optional[int] = None):
        """
        :param int max_throughput: The maximum throughput of the MongoDB database (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.
        """
        if max_throughput is not None:
            pulumi.set(__self__, "max_throughput", max_throughput)

    @property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> Optional[int]:
        """
        The maximum throughput of the MongoDB database (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.
        """
        return pulumi.get(self, "max_throughput")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SqlContainerAutoscaleSettings(dict):
    def __init__(__self__, *,
                 max_throughput: Optional[int] = None):
        """
        :param int max_throughput: The maximum throughput of the SQL container (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.
        """
        if max_throughput is not None:
            pulumi.set(__self__, "max_throughput", max_throughput)

    @property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> Optional[int]:
        """
        The maximum throughput of the SQL container (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.
        """
        return pulumi.get(self, "max_throughput")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SqlContainerIndexingPolicy(dict):
    def __init__(__self__, *,
                 composite_indices: Optional[Sequence['outputs.SqlContainerIndexingPolicyCompositeIndex']] = None,
                 excluded_paths: Optional[Sequence['outputs.SqlContainerIndexingPolicyExcludedPath']] = None,
                 included_paths: Optional[Sequence['outputs.SqlContainerIndexingPolicyIncludedPath']] = None,
                 indexing_mode: Optional[str] = None):
        """
        :param Sequence['SqlContainerIndexingPolicyCompositeIndexArgs'] composite_indices: One or more `composite_index` blocks as defined below.
        :param Sequence['SqlContainerIndexingPolicyExcludedPathArgs'] excluded_paths: One or more `excluded_path` blocks as defined below. Either `included_path` or `excluded_path` must contain the `path` `/*`
        :param Sequence['SqlContainerIndexingPolicyIncludedPathArgs'] included_paths: One or more `included_path` blocks as defined below. Either `included_path` or `excluded_path` must contain the `path` `/*`
        :param str indexing_mode: Indicates the indexing mode. Possible values include: `Consistent` and `None`. Defaults to `Consistent`.
        """
        if composite_indices is not None:
            pulumi.set(__self__, "composite_indices", composite_indices)
        if excluded_paths is not None:
            pulumi.set(__self__, "excluded_paths", excluded_paths)
        if included_paths is not None:
            pulumi.set(__self__, "included_paths", included_paths)
        if indexing_mode is not None:
            pulumi.set(__self__, "indexing_mode", indexing_mode)

    @property
    @pulumi.getter(name="compositeIndices")
    def composite_indices(self) -> Optional[Sequence['outputs.SqlContainerIndexingPolicyCompositeIndex']]:
        """
        One or more `composite_index` blocks as defined below.
        """
        return pulumi.get(self, "composite_indices")

    @property
    @pulumi.getter(name="excludedPaths")
    def excluded_paths(self) -> Optional[Sequence['outputs.SqlContainerIndexingPolicyExcludedPath']]:
        """
        One or more `excluded_path` blocks as defined below. Either `included_path` or `excluded_path` must contain the `path` `/*`
        """
        return pulumi.get(self, "excluded_paths")

    @property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence['outputs.SqlContainerIndexingPolicyIncludedPath']]:
        """
        One or more `included_path` blocks as defined below. Either `included_path` or `excluded_path` must contain the `path` `/*`
        """
        return pulumi.get(self, "included_paths")

    @property
    @pulumi.getter(name="indexingMode")
    def indexing_mode(self) -> Optional[str]:
        """
        Indicates the indexing mode. Possible values include: `Consistent` and `None`. Defaults to `Consistent`.
        """
        return pulumi.get(self, "indexing_mode")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SqlContainerIndexingPolicyCompositeIndex(dict):
    def __init__(__self__, *,
                 indices: Sequence['outputs.SqlContainerIndexingPolicyCompositeIndexIndex']):
        """
        :param Sequence['SqlContainerIndexingPolicyCompositeIndexIndexArgs'] indices: One or more `index` blocks as defined below.
        """
        pulumi.set(__self__, "indices", indices)

    @property
    @pulumi.getter
    def indices(self) -> Sequence['outputs.SqlContainerIndexingPolicyCompositeIndexIndex']:
        """
        One or more `index` blocks as defined below.
        """
        return pulumi.get(self, "indices")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SqlContainerIndexingPolicyCompositeIndexIndex(dict):
    def __init__(__self__, *,
                 order: str,
                 path: str):
        """
        :param str order: Order of the index. Possible values are `Ascending` or `Descending`.
        :param str path: Path for which the indexing behaviour applies to.
        """
        pulumi.set(__self__, "order", order)
        pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter
    def order(self) -> str:
        """
        Order of the index. Possible values are `Ascending` or `Descending`.
        """
        return pulumi.get(self, "order")

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        Path for which the indexing behaviour applies to.
        """
        return pulumi.get(self, "path")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SqlContainerIndexingPolicyExcludedPath(dict):
    def __init__(__self__, *,
                 path: str):
        """
        :param str path: Path that is excluded from indexing.
        """
        pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        Path that is excluded from indexing.
        """
        return pulumi.get(self, "path")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SqlContainerIndexingPolicyIncludedPath(dict):
    def __init__(__self__, *,
                 path: str):
        """
        :param str path: Path for which the indexing behaviour applies to.
        """
        pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        Path for which the indexing behaviour applies to.
        """
        return pulumi.get(self, "path")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SqlContainerUniqueKey(dict):
    def __init__(__self__, *,
                 paths: Sequence[str]):
        """
        :param Sequence[str] paths: A list of paths to use for this unique key.
        """
        pulumi.set(__self__, "paths", paths)

    @property
    @pulumi.getter
    def paths(self) -> Sequence[str]:
        """
        A list of paths to use for this unique key.
        """
        return pulumi.get(self, "paths")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SqlDatabaseAutoscaleSettings(dict):
    def __init__(__self__, *,
                 max_throughput: Optional[int] = None):
        """
        :param int max_throughput: The maximum throughput of the SQL database (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.
        """
        if max_throughput is not None:
            pulumi.set(__self__, "max_throughput", max_throughput)

    @property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> Optional[int]:
        """
        The maximum throughput of the SQL database (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.
        """
        return pulumi.get(self, "max_throughput")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class TableAutoscaleSettings(dict):
    def __init__(__self__, *,
                 max_throughput: Optional[int] = None):
        """
        :param int max_throughput: The maximum throughput of the Table (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.
        """
        if max_throughput is not None:
            pulumi.set(__self__, "max_throughput", max_throughput)

    @property
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> Optional[int]:
        """
        The maximum throughput of the Table (RU/s). Must be between `4,000` and `1,000,000`. Must be set in increments of `1,000`. Conflicts with `throughput`.
        """
        return pulumi.get(self, "max_throughput")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetAccountCapabilityResult(dict):
    def __init__(__self__, *,
                 name: str):
        """
        :param str name: Specifies the name of the CosmosDB Account.
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Specifies the name of the CosmosDB Account.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetAccountConsistencyPolicyResult(dict):
    def __init__(__self__, *,
                 consistency_level: str,
                 max_interval_in_seconds: int,
                 max_staleness_prefix: int):
        """
        :param str consistency_level: The Consistency Level used by this CosmosDB Account.
        :param int max_interval_in_seconds: The amount of staleness (in seconds) tolerated when the consistency level is Bounded Staleness.
        :param int max_staleness_prefix: The number of stale requests tolerated when the consistency level is Bounded Staleness.
        """
        pulumi.set(__self__, "consistency_level", consistency_level)
        pulumi.set(__self__, "max_interval_in_seconds", max_interval_in_seconds)
        pulumi.set(__self__, "max_staleness_prefix", max_staleness_prefix)

    @property
    @pulumi.getter(name="consistencyLevel")
    def consistency_level(self) -> str:
        """
        The Consistency Level used by this CosmosDB Account.
        """
        return pulumi.get(self, "consistency_level")

    @property
    @pulumi.getter(name="maxIntervalInSeconds")
    def max_interval_in_seconds(self) -> int:
        """
        The amount of staleness (in seconds) tolerated when the consistency level is Bounded Staleness.
        """
        return pulumi.get(self, "max_interval_in_seconds")

    @property
    @pulumi.getter(name="maxStalenessPrefix")
    def max_staleness_prefix(self) -> int:
        """
        The number of stale requests tolerated when the consistency level is Bounded Staleness.
        """
        return pulumi.get(self, "max_staleness_prefix")


@pulumi.output_type
class GetAccountGeoLocationResult(dict):
    def __init__(__self__, *,
                 failover_priority: int,
                 id: str,
                 location: str):
        """
        :param str id: The ID of the virtual network subnet.
        :param str location: The name of the Azure region hosting replicated data.
        """
        pulumi.set(__self__, "failover_priority", failover_priority)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "location", location)

    @property
    @pulumi.getter(name="failoverPriority")
    def failover_priority(self) -> int:
        return pulumi.get(self, "failover_priority")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the virtual network subnet.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The name of the Azure region hosting replicated data.
        """
        return pulumi.get(self, "location")


@pulumi.output_type
class GetAccountVirtualNetworkRuleResult(dict):
    def __init__(__self__, *,
                 id: str):
        """
        :param str id: The ID of the virtual network subnet.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the virtual network subnet.
        """
        return pulumi.get(self, "id")


