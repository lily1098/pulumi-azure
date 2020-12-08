# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .active_directory_administrator import *
from .configuration import *
from .database import *
from .firewall_rule import *
from .get_server import *
from .server import *
from .server_key import *
from .virtual_network_rule import *
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
            if typ == "azure:postgresql/activeDirectoryAdministrator:ActiveDirectoryAdministrator":
                return ActiveDirectoryAdministrator(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:postgresql/configuration:Configuration":
                return Configuration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:postgresql/database:Database":
                return Database(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:postgresql/firewallRule:FirewallRule":
                return FirewallRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:postgresql/server:Server":
                return Server(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:postgresql/serverKey:ServerKey":
                return ServerKey(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:postgresql/virtualNetworkRule:VirtualNetworkRule":
                return VirtualNetworkRule(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure", "postgresql/activeDirectoryAdministrator", _module_instance)
    pulumi.runtime.register_resource_module("azure", "postgresql/configuration", _module_instance)
    pulumi.runtime.register_resource_module("azure", "postgresql/database", _module_instance)
    pulumi.runtime.register_resource_module("azure", "postgresql/firewallRule", _module_instance)
    pulumi.runtime.register_resource_module("azure", "postgresql/server", _module_instance)
    pulumi.runtime.register_resource_module("azure", "postgresql/serverKey", _module_instance)
    pulumi.runtime.register_resource_module("azure", "postgresql/virtualNetworkRule", _module_instance)

_register_module()
