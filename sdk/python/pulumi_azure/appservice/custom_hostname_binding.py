# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class CustomHostnameBinding(pulumi.CustomResource):
    """
    Manages a Hostname Binding within an App Service.
    """
    def __init__(__self__, __name__, __opts__=None, app_service_name=None, hostname=None, resource_group_name=None):
        """Create a CustomHostnameBinding resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not app_service_name:
            raise TypeError('Missing required property app_service_name')
        elif not isinstance(app_service_name, basestring):
            raise TypeError('Expected property app_service_name to be a basestring')
        __self__.app_service_name = app_service_name
        """
        The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.
        """
        __props__['appServiceName'] = app_service_name

        if not hostname:
            raise TypeError('Missing required property hostname')
        elif not isinstance(hostname, basestring):
            raise TypeError('Expected property hostname to be a basestring')
        __self__.hostname = hostname
        """
        Specifies the Custom Hostname to use for the App Service, example `www.example.com`. Changing this forces a new resource to be created.
        """
        __props__['hostname'] = hostname

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        super(CustomHostnameBinding, __self__).__init__(
            'azure:appservice/customHostnameBinding:CustomHostnameBinding',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'appServiceName' in outs:
            self.app_service_name = outs['appServiceName']
        if 'hostname' in outs:
            self.hostname = outs['hostname']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']