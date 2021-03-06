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

__all__ = ['Api']


class Api(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_management_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 import_: Optional[pulumi.Input[pulumi.InputType['ApiImportArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 oauth2_authorization: Optional[pulumi.Input[pulumi.InputType['ApiOauth2AuthorizationArgs']]] = None,
                 openid_authentication: Optional[pulumi.Input[pulumi.InputType['ApiOpenidAuthenticationArgs']]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 protocols: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 revision: Optional[pulumi.Input[str]] = None,
                 service_url: Optional[pulumi.Input[str]] = None,
                 soap_pass_through: Optional[pulumi.Input[bool]] = None,
                 subscription_key_parameter_names: Optional[pulumi.Input[pulumi.InputType['ApiSubscriptionKeyParameterNamesArgs']]] = None,
                 subscription_required: Optional[pulumi.Input[bool]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 version_set_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an API within an API Management Service.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_service = azure.apimanagement.Service("exampleService",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            publisher_name="My Company",
            publisher_email="company@exmaple.com",
            sku_name="Developer_1")
        example_api = azure.apimanagement.Api("exampleApi",
            resource_group_name=example_resource_group.name,
            api_management_name=example_service.name,
            revision="1",
            display_name="Example API",
            path="example",
            protocols=["https"],
            import_=azure.apimanagement.ApiImportArgs(
                content_format="swagger-link-json",
                content_value="http://conferenceapi.azurewebsites.net/?format=json",
            ))
        ```

        ## Import

        API Management API's can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:apimanagement/api:Api example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.ApiManagement/service/instance1/apis/api1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_management_name: The Name of the API Management Service where this API should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: A description of the API Management API, which may include HTML formatting tags.
        :param pulumi.Input[str] display_name: The display name of the API.
        :param pulumi.Input[pulumi.InputType['ApiImportArgs']] import_: A `import` block as documented below.
        :param pulumi.Input[str] name: The name of the API Management API. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['ApiOauth2AuthorizationArgs']] oauth2_authorization: An `oauth2_authorization` block as documented below.
        :param pulumi.Input[pulumi.InputType['ApiOpenidAuthenticationArgs']] openid_authentication: An `openid_authentication` block as documented below.
        :param pulumi.Input[str] path: The Path for this API Management API, which is a relative URL which uniquely identifies this API and all of its resource paths within the API Management Service.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] protocols: A list of protocols the operations in this API can be invoked. Possible values are `http` and `https`.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group where the API Management API exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] revision: The Revision which used for this API.
        :param pulumi.Input[str] service_url: Absolute URL of the backend service implementing this API.
        :param pulumi.Input[bool] soap_pass_through: Should this API expose a SOAP frontend, rather than a HTTP frontend? Defaults to `false`.
        :param pulumi.Input[pulumi.InputType['ApiSubscriptionKeyParameterNamesArgs']] subscription_key_parameter_names: A `subscription_key_parameter_names` block as documented below.
        :param pulumi.Input[bool] subscription_required: Should this API require a subscription key?
        :param pulumi.Input[str] version: The Version number of this API, if this API is versioned.
        :param pulumi.Input[str] version_set_id: The ID of the Version Set which this API is associated with.
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

            if api_management_name is None and not opts.urn:
                raise TypeError("Missing required property 'api_management_name'")
            __props__['api_management_name'] = api_management_name
            __props__['description'] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__['display_name'] = display_name
            __props__['import_'] = import_
            __props__['name'] = name
            __props__['oauth2_authorization'] = oauth2_authorization
            __props__['openid_authentication'] = openid_authentication
            if path is None and not opts.urn:
                raise TypeError("Missing required property 'path'")
            __props__['path'] = path
            if protocols is None and not opts.urn:
                raise TypeError("Missing required property 'protocols'")
            __props__['protocols'] = protocols
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if revision is None and not opts.urn:
                raise TypeError("Missing required property 'revision'")
            __props__['revision'] = revision
            __props__['service_url'] = service_url
            __props__['soap_pass_through'] = soap_pass_through
            __props__['subscription_key_parameter_names'] = subscription_key_parameter_names
            __props__['subscription_required'] = subscription_required
            __props__['version'] = version
            __props__['version_set_id'] = version_set_id
            __props__['is_current'] = None
            __props__['is_online'] = None
        super(Api, __self__).__init__(
            'azure:apimanagement/api:Api',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_management_name: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            import_: Optional[pulumi.Input[pulumi.InputType['ApiImportArgs']]] = None,
            is_current: Optional[pulumi.Input[bool]] = None,
            is_online: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            oauth2_authorization: Optional[pulumi.Input[pulumi.InputType['ApiOauth2AuthorizationArgs']]] = None,
            openid_authentication: Optional[pulumi.Input[pulumi.InputType['ApiOpenidAuthenticationArgs']]] = None,
            path: Optional[pulumi.Input[str]] = None,
            protocols: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            revision: Optional[pulumi.Input[str]] = None,
            service_url: Optional[pulumi.Input[str]] = None,
            soap_pass_through: Optional[pulumi.Input[bool]] = None,
            subscription_key_parameter_names: Optional[pulumi.Input[pulumi.InputType['ApiSubscriptionKeyParameterNamesArgs']]] = None,
            subscription_required: Optional[pulumi.Input[bool]] = None,
            version: Optional[pulumi.Input[str]] = None,
            version_set_id: Optional[pulumi.Input[str]] = None) -> 'Api':
        """
        Get an existing Api resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_management_name: The Name of the API Management Service where this API should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] description: A description of the API Management API, which may include HTML formatting tags.
        :param pulumi.Input[str] display_name: The display name of the API.
        :param pulumi.Input[pulumi.InputType['ApiImportArgs']] import_: A `import` block as documented below.
        :param pulumi.Input[bool] is_current: Is this the current API Revision?
        :param pulumi.Input[bool] is_online: Is this API Revision online/accessible via the Gateway?
        :param pulumi.Input[str] name: The name of the API Management API. Changing this forces a new resource to be created.
        :param pulumi.Input[pulumi.InputType['ApiOauth2AuthorizationArgs']] oauth2_authorization: An `oauth2_authorization` block as documented below.
        :param pulumi.Input[pulumi.InputType['ApiOpenidAuthenticationArgs']] openid_authentication: An `openid_authentication` block as documented below.
        :param pulumi.Input[str] path: The Path for this API Management API, which is a relative URL which uniquely identifies this API and all of its resource paths within the API Management Service.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] protocols: A list of protocols the operations in this API can be invoked. Possible values are `http` and `https`.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group where the API Management API exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] revision: The Revision which used for this API.
        :param pulumi.Input[str] service_url: Absolute URL of the backend service implementing this API.
        :param pulumi.Input[bool] soap_pass_through: Should this API expose a SOAP frontend, rather than a HTTP frontend? Defaults to `false`.
        :param pulumi.Input[pulumi.InputType['ApiSubscriptionKeyParameterNamesArgs']] subscription_key_parameter_names: A `subscription_key_parameter_names` block as documented below.
        :param pulumi.Input[bool] subscription_required: Should this API require a subscription key?
        :param pulumi.Input[str] version: The Version number of this API, if this API is versioned.
        :param pulumi.Input[str] version_set_id: The ID of the Version Set which this API is associated with.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["api_management_name"] = api_management_name
        __props__["description"] = description
        __props__["display_name"] = display_name
        __props__["import_"] = import_
        __props__["is_current"] = is_current
        __props__["is_online"] = is_online
        __props__["name"] = name
        __props__["oauth2_authorization"] = oauth2_authorization
        __props__["openid_authentication"] = openid_authentication
        __props__["path"] = path
        __props__["protocols"] = protocols
        __props__["resource_group_name"] = resource_group_name
        __props__["revision"] = revision
        __props__["service_url"] = service_url
        __props__["soap_pass_through"] = soap_pass_through
        __props__["subscription_key_parameter_names"] = subscription_key_parameter_names
        __props__["subscription_required"] = subscription_required
        __props__["version"] = version
        __props__["version_set_id"] = version_set_id
        return Api(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiManagementName")
    def api_management_name(self) -> pulumi.Output[str]:
        """
        The Name of the API Management Service where this API should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "api_management_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the API Management API, which may include HTML formatting tags.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of the API.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="import")
    def import_(self) -> pulumi.Output[Optional['outputs.ApiImport']]:
        """
        A `import` block as documented below.
        """
        return pulumi.get(self, "import_")

    @property
    @pulumi.getter(name="isCurrent")
    def is_current(self) -> pulumi.Output[bool]:
        """
        Is this the current API Revision?
        """
        return pulumi.get(self, "is_current")

    @property
    @pulumi.getter(name="isOnline")
    def is_online(self) -> pulumi.Output[bool]:
        """
        Is this API Revision online/accessible via the Gateway?
        """
        return pulumi.get(self, "is_online")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the API Management API. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oauth2Authorization")
    def oauth2_authorization(self) -> pulumi.Output[Optional['outputs.ApiOauth2Authorization']]:
        """
        An `oauth2_authorization` block as documented below.
        """
        return pulumi.get(self, "oauth2_authorization")

    @property
    @pulumi.getter(name="openidAuthentication")
    def openid_authentication(self) -> pulumi.Output[Optional['outputs.ApiOpenidAuthentication']]:
        """
        An `openid_authentication` block as documented below.
        """
        return pulumi.get(self, "openid_authentication")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        """
        The Path for this API Management API, which is a relative URL which uniquely identifies this API and all of its resource paths within the API Management Service.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def protocols(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of protocols the operations in this API can be invoked. Possible values are `http` and `https`.
        """
        return pulumi.get(self, "protocols")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The Name of the Resource Group where the API Management API exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def revision(self) -> pulumi.Output[str]:
        """
        The Revision which used for this API.
        """
        return pulumi.get(self, "revision")

    @property
    @pulumi.getter(name="serviceUrl")
    def service_url(self) -> pulumi.Output[str]:
        """
        Absolute URL of the backend service implementing this API.
        """
        return pulumi.get(self, "service_url")

    @property
    @pulumi.getter(name="soapPassThrough")
    def soap_pass_through(self) -> pulumi.Output[Optional[bool]]:
        """
        Should this API expose a SOAP frontend, rather than a HTTP frontend? Defaults to `false`.
        """
        return pulumi.get(self, "soap_pass_through")

    @property
    @pulumi.getter(name="subscriptionKeyParameterNames")
    def subscription_key_parameter_names(self) -> pulumi.Output['outputs.ApiSubscriptionKeyParameterNames']:
        """
        A `subscription_key_parameter_names` block as documented below.
        """
        return pulumi.get(self, "subscription_key_parameter_names")

    @property
    @pulumi.getter(name="subscriptionRequired")
    def subscription_required(self) -> pulumi.Output[Optional[bool]]:
        """
        Should this API require a subscription key?
        """
        return pulumi.get(self, "subscription_required")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        The Version number of this API, if this API is versioned.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="versionSetId")
    def version_set_id(self) -> pulumi.Output[str]:
        """
        The ID of the Version Set which this API is associated with.
        """
        return pulumi.get(self, "version_set_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

