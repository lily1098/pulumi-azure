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

__all__ = ['DataLakeGen2Path']


class DataLakeGen2Path(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLakeGen2PathAceArgs']]]]] = None,
                 filesystem_name: Optional[pulumi.Input[str]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 resource: Optional[pulumi.Input[str]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Data Lake Gen2 Path in a File System within an Azure Storage Account.

        > **NOTE:** This Resource requires using Azure Active Directory to connect to Azure Storage, which in turn requires the `Storage` specific roles - which are not granted by default.

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
        example_data_lake_gen2_path = azure.storage.DataLakeGen2Path("exampleDataLakeGen2Path",
            path="example",
            filesystem_name=example_data_lake_gen2_filesystem.name,
            storage_account_id=example_account.id,
            resource="directory")
        ```

        ## Import

        Data Lake Gen2 Paths can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:storage/dataLakeGen2Path:DataLakeGen2Path example https://account1.dfs.core.windows.net/fileSystem1/path
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLakeGen2PathAceArgs']]]] aces: One or more `ace` blocks as defined below to specify the entries for the ACL for the path.
        :param pulumi.Input[str] filesystem_name: The name of the Data Lake Gen2 File System which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        :param pulumi.Input[str] group: Specifies the Object ID of the Azure Active Directory Group to make the owning group.
        :param pulumi.Input[str] owner: Specifies the Object ID of the Azure Active Directory User to make the owning user.
        :param pulumi.Input[str] path: The path which should be created within the Data Lake Gen2 File System in the Storage Account. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource: Specifies the type for path to create. Currently only `directory` is supported.
        :param pulumi.Input[str] storage_account_id: Specifies the ID of the Storage Account in which the Data Lake Gen2 File System should exist. Changing this forces a new resource to be created.
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

            __props__['aces'] = aces
            if filesystem_name is None and not opts.urn:
                raise TypeError("Missing required property 'filesystem_name'")
            __props__['filesystem_name'] = filesystem_name
            __props__['group'] = group
            __props__['owner'] = owner
            if path is None and not opts.urn:
                raise TypeError("Missing required property 'path'")
            __props__['path'] = path
            if resource is None and not opts.urn:
                raise TypeError("Missing required property 'resource'")
            __props__['resource'] = resource
            if storage_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_id'")
            __props__['storage_account_id'] = storage_account_id
        super(DataLakeGen2Path, __self__).__init__(
            'azure:storage/dataLakeGen2Path:DataLakeGen2Path',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            aces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLakeGen2PathAceArgs']]]]] = None,
            filesystem_name: Optional[pulumi.Input[str]] = None,
            group: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[str]] = None,
            path: Optional[pulumi.Input[str]] = None,
            resource: Optional[pulumi.Input[str]] = None,
            storage_account_id: Optional[pulumi.Input[str]] = None) -> 'DataLakeGen2Path':
        """
        Get an existing DataLakeGen2Path resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLakeGen2PathAceArgs']]]] aces: One or more `ace` blocks as defined below to specify the entries for the ACL for the path.
        :param pulumi.Input[str] filesystem_name: The name of the Data Lake Gen2 File System which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        :param pulumi.Input[str] group: Specifies the Object ID of the Azure Active Directory Group to make the owning group.
        :param pulumi.Input[str] owner: Specifies the Object ID of the Azure Active Directory User to make the owning user.
        :param pulumi.Input[str] path: The path which should be created within the Data Lake Gen2 File System in the Storage Account. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource: Specifies the type for path to create. Currently only `directory` is supported.
        :param pulumi.Input[str] storage_account_id: Specifies the ID of the Storage Account in which the Data Lake Gen2 File System should exist. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["aces"] = aces
        __props__["filesystem_name"] = filesystem_name
        __props__["group"] = group
        __props__["owner"] = owner
        __props__["path"] = path
        __props__["resource"] = resource
        __props__["storage_account_id"] = storage_account_id
        return DataLakeGen2Path(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def aces(self) -> pulumi.Output[Sequence['outputs.DataLakeGen2PathAce']]:
        """
        One or more `ace` blocks as defined below to specify the entries for the ACL for the path.
        """
        return pulumi.get(self, "aces")

    @property
    @pulumi.getter(name="filesystemName")
    def filesystem_name(self) -> pulumi.Output[str]:
        """
        The name of the Data Lake Gen2 File System which should be created within the Storage Account. Must be unique within the storage account the queue is located. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "filesystem_name")

    @property
    @pulumi.getter
    def group(self) -> pulumi.Output[str]:
        """
        Specifies the Object ID of the Azure Active Directory Group to make the owning group.
        """
        return pulumi.get(self, "group")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        Specifies the Object ID of the Azure Active Directory User to make the owning user.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        """
        The path which should be created within the Data Lake Gen2 File System in the Storage Account. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def resource(self) -> pulumi.Output[str]:
        """
        Specifies the type for path to create. Currently only `directory` is supported.
        """
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Output[str]:
        """
        Specifies the ID of the Storage Account in which the Data Lake Gen2 File System should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "storage_account_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

