# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['CustomHostnameBinding']


class CustomHostnameBinding(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_service_name: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 ssl_state: Optional[pulumi.Input[str]] = None,
                 thumbprint: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Hostname Binding within an App Service (or Function App).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_random as random

        server = random.RandomId("server",
            keepers={
                "azi_id": 1,
            },
            byte_length=8)
        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
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
        example_custom_hostname_binding = azure.appservice.CustomHostnameBinding("exampleCustomHostnameBinding",
            hostname="www.mywebsite.com",
            app_service_name=example_app_service.name,
            resource_group_name=example_resource_group.name)
        ```

        ## Import

        App Service Custom Hostname Bindings can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appservice/customHostnameBinding:CustomHostnameBinding mywebsite /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Web/sites/instance1/hostNameBindings/mywebsite.com
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_service_name: The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.
        :param pulumi.Input[str] hostname: Specifies the Custom Hostname to use for the App Service, example `www.example.com`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] ssl_state: The SSL type. Possible values are `IpBasedEnabled` and `SniEnabled`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] thumbprint: The SSL certificate thumbprint. Changing this forces a new resource to be created.
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

            if app_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'app_service_name'")
            __props__['app_service_name'] = app_service_name
            if hostname is None and not opts.urn:
                raise TypeError("Missing required property 'hostname'")
            __props__['hostname'] = hostname
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['ssl_state'] = ssl_state
            __props__['thumbprint'] = thumbprint
            __props__['virtual_ip'] = None
        super(CustomHostnameBinding, __self__).__init__(
            'azure:appservice/customHostnameBinding:CustomHostnameBinding',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_service_name: Optional[pulumi.Input[str]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            ssl_state: Optional[pulumi.Input[str]] = None,
            thumbprint: Optional[pulumi.Input[str]] = None,
            virtual_ip: Optional[pulumi.Input[str]] = None) -> 'CustomHostnameBinding':
        """
        Get an existing CustomHostnameBinding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_service_name: The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.
        :param pulumi.Input[str] hostname: Specifies the Custom Hostname to use for the App Service, example `www.example.com`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] ssl_state: The SSL type. Possible values are `IpBasedEnabled` and `SniEnabled`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] thumbprint: The SSL certificate thumbprint. Changing this forces a new resource to be created.
        :param pulumi.Input[str] virtual_ip: The virtual IP address assigned to the hostname if IP based SSL is enabled.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["app_service_name"] = app_service_name
        __props__["hostname"] = hostname
        __props__["resource_group_name"] = resource_group_name
        __props__["ssl_state"] = ssl_state
        __props__["thumbprint"] = thumbprint
        __props__["virtual_ip"] = virtual_ip
        return CustomHostnameBinding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appServiceName")
    def app_service_name(self) -> pulumi.Output[str]:
        """
        The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "app_service_name")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[str]:
        """
        Specifies the Custom Hostname to use for the App Service, example `www.example.com`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="sslState")
    def ssl_state(self) -> pulumi.Output[str]:
        """
        The SSL type. Possible values are `IpBasedEnabled` and `SniEnabled`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "ssl_state")

    @property
    @pulumi.getter
    def thumbprint(self) -> pulumi.Output[str]:
        """
        The SSL certificate thumbprint. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "thumbprint")

    @property
    @pulumi.getter(name="virtualIp")
    def virtual_ip(self) -> pulumi.Output[str]:
        """
        The virtual IP address assigned to the hostname if IP based SSL is enabled.
        """
        return pulumi.get(self, "virtual_ip")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

