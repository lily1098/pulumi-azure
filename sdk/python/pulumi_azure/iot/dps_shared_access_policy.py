# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['DpsSharedAccessPolicy']


class DpsSharedAccessPolicy(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enrollment_read: Optional[pulumi.Input[bool]] = None,
                 enrollment_write: Optional[pulumi.Input[bool]] = None,
                 iothub_dps_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 registration_read: Optional[pulumi.Input[bool]] = None,
                 registration_write: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_config: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an IotHub Device Provisioning Service Shared Access Policy

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_iot_hub_dps = azure.iot.IotHubDps("exampleIotHubDps",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            sku=azure.iot.IotHubDpsSkuArgs(
                name="S1",
                capacity=1,
            ))
        example_dps_shared_access_policy = azure.iot.DpsSharedAccessPolicy("exampleDpsSharedAccessPolicy",
            resource_group_name=example_resource_group.name,
            iothub_dps_name=example_iot_hub_dps.name,
            enrollment_write=True,
            enrollment_read=True)
        ```

        ## Import

        IoTHub Device Provisioning Service Shared Access Policies can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:iot/dpsSharedAccessPolicy:DpsSharedAccessPolicy shared_access_policy1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Devices/provisioningServices/dps1/keys/shared_access_policy1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enrollment_read: Adds `EnrollmentRead` permission to this Shared Access Account. It allows read access to enrollment data.
        :param pulumi.Input[bool] enrollment_write: Adds `EnrollmentWrite` permission to this Shared Access Account. It allows write access to enrollment data.
        :param pulumi.Input[str] iothub_dps_name: The name of the IoT Hub Device Provisioning service to which this Shared Access Policy belongs. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the IotHub Shared Access Policy resource. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] registration_read: Adds `RegistrationStatusRead` permission to this Shared Access Account. It allows read access to device registrations.
        :param pulumi.Input[bool] registration_write: Adds `RegistrationStatusWrite` permission to this Shared Access Account. It allows write access to device registrations.
        :param pulumi.Input[str] resource_group_name: The name of the resource group under which the IotHub Shared Access Policy resource has to be created. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] service_config: Adds `ServiceConfig` permission to this Shared Access Account. It allows configuration of the Device Provisioning Service.
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

            __props__['enrollment_read'] = enrollment_read
            __props__['enrollment_write'] = enrollment_write
            if iothub_dps_name is None and not opts.urn:
                raise TypeError("Missing required property 'iothub_dps_name'")
            __props__['iothub_dps_name'] = iothub_dps_name
            __props__['name'] = name
            __props__['registration_read'] = registration_read
            __props__['registration_write'] = registration_write
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['service_config'] = service_config
            __props__['primary_connection_string'] = None
            __props__['primary_key'] = None
            __props__['secondary_connection_string'] = None
            __props__['secondary_key'] = None
        super(DpsSharedAccessPolicy, __self__).__init__(
            'azure:iot/dpsSharedAccessPolicy:DpsSharedAccessPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enrollment_read: Optional[pulumi.Input[bool]] = None,
            enrollment_write: Optional[pulumi.Input[bool]] = None,
            iothub_dps_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            primary_connection_string: Optional[pulumi.Input[str]] = None,
            primary_key: Optional[pulumi.Input[str]] = None,
            registration_read: Optional[pulumi.Input[bool]] = None,
            registration_write: Optional[pulumi.Input[bool]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            secondary_connection_string: Optional[pulumi.Input[str]] = None,
            secondary_key: Optional[pulumi.Input[str]] = None,
            service_config: Optional[pulumi.Input[bool]] = None) -> 'DpsSharedAccessPolicy':
        """
        Get an existing DpsSharedAccessPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enrollment_read: Adds `EnrollmentRead` permission to this Shared Access Account. It allows read access to enrollment data.
        :param pulumi.Input[bool] enrollment_write: Adds `EnrollmentWrite` permission to this Shared Access Account. It allows write access to enrollment data.
        :param pulumi.Input[str] iothub_dps_name: The name of the IoT Hub Device Provisioning service to which this Shared Access Policy belongs. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the IotHub Shared Access Policy resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] primary_connection_string: The primary connection string of the Shared Access Policy.
        :param pulumi.Input[str] primary_key: The primary key used to create the authentication token.
        :param pulumi.Input[bool] registration_read: Adds `RegistrationStatusRead` permission to this Shared Access Account. It allows read access to device registrations.
        :param pulumi.Input[bool] registration_write: Adds `RegistrationStatusWrite` permission to this Shared Access Account. It allows write access to device registrations.
        :param pulumi.Input[str] resource_group_name: The name of the resource group under which the IotHub Shared Access Policy resource has to be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] secondary_connection_string: The secondary connection string of the Shared Access Policy.
        :param pulumi.Input[str] secondary_key: The secondary key used to create the authentication token.
        :param pulumi.Input[bool] service_config: Adds `ServiceConfig` permission to this Shared Access Account. It allows configuration of the Device Provisioning Service.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["enrollment_read"] = enrollment_read
        __props__["enrollment_write"] = enrollment_write
        __props__["iothub_dps_name"] = iothub_dps_name
        __props__["name"] = name
        __props__["primary_connection_string"] = primary_connection_string
        __props__["primary_key"] = primary_key
        __props__["registration_read"] = registration_read
        __props__["registration_write"] = registration_write
        __props__["resource_group_name"] = resource_group_name
        __props__["secondary_connection_string"] = secondary_connection_string
        __props__["secondary_key"] = secondary_key
        __props__["service_config"] = service_config
        return DpsSharedAccessPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="enrollmentRead")
    def enrollment_read(self) -> pulumi.Output[Optional[bool]]:
        """
        Adds `EnrollmentRead` permission to this Shared Access Account. It allows read access to enrollment data.
        """
        return pulumi.get(self, "enrollment_read")

    @property
    @pulumi.getter(name="enrollmentWrite")
    def enrollment_write(self) -> pulumi.Output[Optional[bool]]:
        """
        Adds `EnrollmentWrite` permission to this Shared Access Account. It allows write access to enrollment data.
        """
        return pulumi.get(self, "enrollment_write")

    @property
    @pulumi.getter(name="iothubDpsName")
    def iothub_dps_name(self) -> pulumi.Output[str]:
        """
        The name of the IoT Hub Device Provisioning service to which this Shared Access Policy belongs. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "iothub_dps_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the IotHub Shared Access Policy resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="primaryConnectionString")
    def primary_connection_string(self) -> pulumi.Output[str]:
        """
        The primary connection string of the Shared Access Policy.
        """
        return pulumi.get(self, "primary_connection_string")

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> pulumi.Output[str]:
        """
        The primary key used to create the authentication token.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="registrationRead")
    def registration_read(self) -> pulumi.Output[Optional[bool]]:
        """
        Adds `RegistrationStatusRead` permission to this Shared Access Account. It allows read access to device registrations.
        """
        return pulumi.get(self, "registration_read")

    @property
    @pulumi.getter(name="registrationWrite")
    def registration_write(self) -> pulumi.Output[Optional[bool]]:
        """
        Adds `RegistrationStatusWrite` permission to this Shared Access Account. It allows write access to device registrations.
        """
        return pulumi.get(self, "registration_write")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group under which the IotHub Shared Access Policy resource has to be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="secondaryConnectionString")
    def secondary_connection_string(self) -> pulumi.Output[str]:
        """
        The secondary connection string of the Shared Access Policy.
        """
        return pulumi.get(self, "secondary_connection_string")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> pulumi.Output[str]:
        """
        The secondary key used to create the authentication token.
        """
        return pulumi.get(self, "secondary_key")

    @property
    @pulumi.getter(name="serviceConfig")
    def service_config(self) -> pulumi.Output[Optional[bool]]:
        """
        Adds `ServiceConfig` permission to this Shared Access Account. It allows configuration of the Device Provisioning Service.
        """
        return pulumi.get(self, "service_config")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

