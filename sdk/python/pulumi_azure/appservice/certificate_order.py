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

__all__ = ['CertificateOrder']


class CertificateOrder(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_renew: Optional[pulumi.Input[bool]] = None,
                 csr: Optional[pulumi.Input[str]] = None,
                 distinguished_name: Optional[pulumi.Input[str]] = None,
                 key_size: Optional[pulumi.Input[int]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 product_type: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 validity_in_years: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an App Service Certificate Order.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_certificate_order = azure.appservice.CertificateOrder("exampleCertificateOrder",
            resource_group_name=example_resource_group.name,
            location="global",
            distinguished_name="CN=example.com",
            product_type="Standard")
        ```

        ## Import

        App Service Certificate Orders can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appservice/certificateOrder:CertificateOrder example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.CertificateRegistration/certificateOrders/certificateorder1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_renew: true if the certificate should be automatically renewed when it expires; otherwise, false. Defaults to true.
        :param pulumi.Input[str] csr: Last CSR that was created for this order.
        :param pulumi.Input[str] distinguished_name: The Distinguished Name for the App Service Certificate Order.
        :param pulumi.Input[int] key_size: Certificate key size.  Defaults to 2048.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created. Currently the only valid value is `global`.
        :param pulumi.Input[str] name: Specifies the name of the certificate. Changing this forces a new resource to be created.
        :param pulumi.Input[str] product_type: Certificate product type, such as `Standard` or `WildCard`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the certificate. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[int] validity_in_years: Duration in years (must be between `1` and `3`).  Defaults to `1`.
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

            __props__['auto_renew'] = auto_renew
            __props__['csr'] = csr
            __props__['distinguished_name'] = distinguished_name
            __props__['key_size'] = key_size
            __props__['location'] = location
            __props__['name'] = name
            __props__['product_type'] = product_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['tags'] = tags
            __props__['validity_in_years'] = validity_in_years
            __props__['app_service_certificate_not_renewable_reasons'] = None
            __props__['certificates'] = None
            __props__['domain_verification_token'] = None
            __props__['expiration_time'] = None
            __props__['intermediate_thumbprint'] = None
            __props__['is_private_key_external'] = None
            __props__['root_thumbprint'] = None
            __props__['signed_certificate_thumbprint'] = None
            __props__['status'] = None
        super(CertificateOrder, __self__).__init__(
            'azure:appservice/certificateOrder:CertificateOrder',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_service_certificate_not_renewable_reasons: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            auto_renew: Optional[pulumi.Input[bool]] = None,
            certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CertificateOrderCertificateArgs']]]]] = None,
            csr: Optional[pulumi.Input[str]] = None,
            distinguished_name: Optional[pulumi.Input[str]] = None,
            domain_verification_token: Optional[pulumi.Input[str]] = None,
            expiration_time: Optional[pulumi.Input[str]] = None,
            intermediate_thumbprint: Optional[pulumi.Input[str]] = None,
            is_private_key_external: Optional[pulumi.Input[bool]] = None,
            key_size: Optional[pulumi.Input[int]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            product_type: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            root_thumbprint: Optional[pulumi.Input[str]] = None,
            signed_certificate_thumbprint: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            validity_in_years: Optional[pulumi.Input[int]] = None) -> 'CertificateOrder':
        """
        Get an existing CertificateOrder resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] app_service_certificate_not_renewable_reasons: Reasons why App Service Certificate is not renewable at the current moment.
        :param pulumi.Input[bool] auto_renew: true if the certificate should be automatically renewed when it expires; otherwise, false. Defaults to true.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CertificateOrderCertificateArgs']]]] certificates: State of the Key Vault secret. A `certificates` block as defined below.
        :param pulumi.Input[str] csr: Last CSR that was created for this order.
        :param pulumi.Input[str] distinguished_name: The Distinguished Name for the App Service Certificate Order.
        :param pulumi.Input[str] domain_verification_token: Domain verification token.
        :param pulumi.Input[str] expiration_time: Certificate expiration time.
        :param pulumi.Input[str] intermediate_thumbprint: Certificate thumbprint intermediate certificate.
        :param pulumi.Input[bool] is_private_key_external: Whether the private key is external or not.
        :param pulumi.Input[int] key_size: Certificate key size.  Defaults to 2048.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created. Currently the only valid value is `global`.
        :param pulumi.Input[str] name: Specifies the name of the certificate. Changing this forces a new resource to be created.
        :param pulumi.Input[str] product_type: Certificate product type, such as `Standard` or `WildCard`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the certificate. Changing this forces a new resource to be created.
        :param pulumi.Input[str] root_thumbprint: Certificate thumbprint for root certificate.
        :param pulumi.Input[str] signed_certificate_thumbprint: Certificate thumbprint for signed certificate.
        :param pulumi.Input[str] status: Current order status.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[int] validity_in_years: Duration in years (must be between `1` and `3`).  Defaults to `1`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["app_service_certificate_not_renewable_reasons"] = app_service_certificate_not_renewable_reasons
        __props__["auto_renew"] = auto_renew
        __props__["certificates"] = certificates
        __props__["csr"] = csr
        __props__["distinguished_name"] = distinguished_name
        __props__["domain_verification_token"] = domain_verification_token
        __props__["expiration_time"] = expiration_time
        __props__["intermediate_thumbprint"] = intermediate_thumbprint
        __props__["is_private_key_external"] = is_private_key_external
        __props__["key_size"] = key_size
        __props__["location"] = location
        __props__["name"] = name
        __props__["product_type"] = product_type
        __props__["resource_group_name"] = resource_group_name
        __props__["root_thumbprint"] = root_thumbprint
        __props__["signed_certificate_thumbprint"] = signed_certificate_thumbprint
        __props__["status"] = status
        __props__["tags"] = tags
        __props__["validity_in_years"] = validity_in_years
        return CertificateOrder(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appServiceCertificateNotRenewableReasons")
    def app_service_certificate_not_renewable_reasons(self) -> pulumi.Output[Sequence[str]]:
        """
        Reasons why App Service Certificate is not renewable at the current moment.
        """
        return pulumi.get(self, "app_service_certificate_not_renewable_reasons")

    @property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> pulumi.Output[Optional[bool]]:
        """
        true if the certificate should be automatically renewed when it expires; otherwise, false. Defaults to true.
        """
        return pulumi.get(self, "auto_renew")

    @property
    @pulumi.getter
    def certificates(self) -> pulumi.Output[Sequence['outputs.CertificateOrderCertificate']]:
        """
        State of the Key Vault secret. A `certificates` block as defined below.
        """
        return pulumi.get(self, "certificates")

    @property
    @pulumi.getter
    def csr(self) -> pulumi.Output[str]:
        """
        Last CSR that was created for this order.
        """
        return pulumi.get(self, "csr")

    @property
    @pulumi.getter(name="distinguishedName")
    def distinguished_name(self) -> pulumi.Output[str]:
        """
        The Distinguished Name for the App Service Certificate Order.
        """
        return pulumi.get(self, "distinguished_name")

    @property
    @pulumi.getter(name="domainVerificationToken")
    def domain_verification_token(self) -> pulumi.Output[str]:
        """
        Domain verification token.
        """
        return pulumi.get(self, "domain_verification_token")

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> pulumi.Output[str]:
        """
        Certificate expiration time.
        """
        return pulumi.get(self, "expiration_time")

    @property
    @pulumi.getter(name="intermediateThumbprint")
    def intermediate_thumbprint(self) -> pulumi.Output[str]:
        """
        Certificate thumbprint intermediate certificate.
        """
        return pulumi.get(self, "intermediate_thumbprint")

    @property
    @pulumi.getter(name="isPrivateKeyExternal")
    def is_private_key_external(self) -> pulumi.Output[bool]:
        """
        Whether the private key is external or not.
        """
        return pulumi.get(self, "is_private_key_external")

    @property
    @pulumi.getter(name="keySize")
    def key_size(self) -> pulumi.Output[Optional[int]]:
        """
        Certificate key size.  Defaults to 2048.
        """
        return pulumi.get(self, "key_size")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created. Currently the only valid value is `global`.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the certificate. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="productType")
    def product_type(self) -> pulumi.Output[Optional[str]]:
        """
        Certificate product type, such as `Standard` or `WildCard`.
        """
        return pulumi.get(self, "product_type")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the certificate. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="rootThumbprint")
    def root_thumbprint(self) -> pulumi.Output[str]:
        """
        Certificate thumbprint for root certificate.
        """
        return pulumi.get(self, "root_thumbprint")

    @property
    @pulumi.getter(name="signedCertificateThumbprint")
    def signed_certificate_thumbprint(self) -> pulumi.Output[str]:
        """
        Certificate thumbprint for signed certificate.
        """
        return pulumi.get(self, "signed_certificate_thumbprint")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Current order status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="validityInYears")
    def validity_in_years(self) -> pulumi.Output[Optional[int]]:
        """
        Duration in years (must be between `1` and `3`).  Defaults to `1`.
        """
        return pulumi.get(self, "validity_in_years")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

