# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .fabric import *
from .network_mapping import *
from .protection_container import *
from .protection_container_mapping import *
from .replicated_vm import *
from .replication_policy import *
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
            if typ == "azure:siterecovery/fabric:Fabric":
                return Fabric(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:siterecovery/networkMapping:NetworkMapping":
                return NetworkMapping(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:siterecovery/protectionContainer:ProtectionContainer":
                return ProtectionContainer(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:siterecovery/protectionContainerMapping:ProtectionContainerMapping":
                return ProtectionContainerMapping(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:siterecovery/replicatedVM:ReplicatedVM":
                return ReplicatedVM(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:siterecovery/replicationPolicy:ReplicationPolicy":
                return ReplicationPolicy(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure", "siterecovery/fabric", _module_instance)
    pulumi.runtime.register_resource_module("azure", "siterecovery/networkMapping", _module_instance)
    pulumi.runtime.register_resource_module("azure", "siterecovery/protectionContainer", _module_instance)
    pulumi.runtime.register_resource_module("azure", "siterecovery/protectionContainerMapping", _module_instance)
    pulumi.runtime.register_resource_module("azure", "siterecovery/replicatedVM", _module_instance)
    pulumi.runtime.register_resource_module("azure", "siterecovery/replicationPolicy", _module_instance)

_register_module()
