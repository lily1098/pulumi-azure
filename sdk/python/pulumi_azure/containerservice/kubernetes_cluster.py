# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class KubernetesCluster(pulumi.CustomResource):
    addon_profile: pulumi.Output[dict]
    """
    A `addon_profile` block.
    """
    agent_pool_profile: pulumi.Output[dict]
    """
    One or more `agent_pool_profile` blocks as documented below.
    """
    dns_prefix: pulumi.Output[str]
    """
    DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.
    """
    fqdn: pulumi.Output[str]
    """
    The FQDN of the Azure Kubernetes Managed Cluster.
    """
    kube_admin_config: pulumi.Output[dict]
    """
    A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.
    """
    kube_admin_config_raw: pulumi.Output[str]
    """
    Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.
    """
    kube_config: pulumi.Output[dict]
    """
    A `kube_config` block as defined below.
    """
    kube_config_raw: pulumi.Output[str]
    """
    Raw Kubernetes config to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools
    """
    kubernetes_version: pulumi.Output[str]
    """
    Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).
    """
    linux_profile: pulumi.Output[dict]
    """
    A `linux_profile` block.
    """
    location: pulumi.Output[str]
    """
    The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.
    """
    network_profile: pulumi.Output[dict]
    """
    A `network_profile` block.
    """
    node_resource_group: pulumi.Output[str]
    """
    The auto-generated Resource Group which contains the resources for this Managed Kubernetes Cluster.
    """
    resource_group_name: pulumi.Output[str]
    """
    Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.
    """
    role_based_access_control: pulumi.Output[dict]
    """
    A `role_based_access_control` block. Changing this forces a new resource to be created.
    """
    service_principal: pulumi.Output[dict]
    """
    A `service_principal` block as documented below.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, resource_name, opts=None, addon_profile=None, agent_pool_profile=None, dns_prefix=None, kubernetes_version=None, linux_profile=None, location=None, name=None, network_profile=None, resource_group_name=None, role_based_access_control=None, service_principal=None, tags=None, __name__=None, __opts__=None):
        """
        Manages a Managed Kubernetes Cluster (also known as AKS / Azure Kubernetes Service)
        
        > **Note:** All arguments including the client secret will be stored in the raw state as plain-text. [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] addon_profile: A `addon_profile` block.
        :param pulumi.Input[dict] agent_pool_profile: One or more `agent_pool_profile` blocks as documented below.
        :param pulumi.Input[str] dns_prefix: DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] kubernetes_version: Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).
        :param pulumi.Input[dict] linux_profile: A `linux_profile` block.
        :param pulumi.Input[str] location: The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] network_profile: A `network_profile` block.
        :param pulumi.Input[str] resource_group_name: Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] role_based_access_control: A `role_based_access_control` block. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] service_principal: A `service_principal` block as documented below.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['addon_profile'] = addon_profile

        if agent_pool_profile is None:
            raise TypeError('Missing required property agent_pool_profile')
        __props__['agent_pool_profile'] = agent_pool_profile

        if dns_prefix is None:
            raise TypeError('Missing required property dns_prefix')
        __props__['dns_prefix'] = dns_prefix

        __props__['kubernetes_version'] = kubernetes_version

        __props__['linux_profile'] = linux_profile

        if location is None:
            raise TypeError('Missing required property location')
        __props__['location'] = location

        __props__['name'] = name

        __props__['network_profile'] = network_profile

        if resource_group_name is None:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        __props__['role_based_access_control'] = role_based_access_control

        if service_principal is None:
            raise TypeError('Missing required property service_principal')
        __props__['service_principal'] = service_principal

        __props__['tags'] = tags

        __props__['fqdn'] = None
        __props__['kube_admin_config'] = None
        __props__['kube_admin_config_raw'] = None
        __props__['kube_config'] = None
        __props__['kube_config_raw'] = None
        __props__['node_resource_group'] = None

        super(KubernetesCluster, __self__).__init__(
            'azure:containerservice/kubernetesCluster:KubernetesCluster',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

