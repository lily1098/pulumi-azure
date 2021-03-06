# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .firewall_rule import *
from .get_workspace import *
from .managed_private_endpoint import *
from .role_assignment import *
from .spark_pool import *
from .sql_pool import *
from .workspace import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "azure:synapse/firewallRule:FirewallRule":
                return FirewallRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:synapse/managedPrivateEndpoint:ManagedPrivateEndpoint":
                return ManagedPrivateEndpoint(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:synapse/roleAssignment:RoleAssignment":
                return RoleAssignment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:synapse/sparkPool:SparkPool":
                return SparkPool(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:synapse/sqlPool:SqlPool":
                return SqlPool(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:synapse/workspace:Workspace":
                return Workspace(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure", "synapse/firewallRule", _module_instance)
    pulumi.runtime.register_resource_module("azure", "synapse/managedPrivateEndpoint", _module_instance)
    pulumi.runtime.register_resource_module("azure", "synapse/roleAssignment", _module_instance)
    pulumi.runtime.register_resource_module("azure", "synapse/sparkPool", _module_instance)
    pulumi.runtime.register_resource_module("azure", "synapse/sqlPool", _module_instance)
    pulumi.runtime.register_resource_module("azure", "synapse/workspace", _module_instance)

_register_module()
