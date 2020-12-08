# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .a_record import *
from .aaaa_record import *
from .c_name_record import *
from .caa_record import *
from .get_zone import *
from .mx_record import *
from .ns_record import *
from .ptr_record import *
from .srv_record import *
from .txt_record import *
from .zone import *
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
            if typ == "azure:dns/aRecord:ARecord":
                return ARecord(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:dns/aaaaRecord:AaaaRecord":
                return AaaaRecord(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:dns/cNameRecord:CNameRecord":
                return CNameRecord(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:dns/caaRecord:CaaRecord":
                return CaaRecord(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:dns/mxRecord:MxRecord":
                return MxRecord(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:dns/nsRecord:NsRecord":
                return NsRecord(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:dns/ptrRecord:PtrRecord":
                return PtrRecord(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:dns/srvRecord:SrvRecord":
                return SrvRecord(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:dns/txtRecord:TxtRecord":
                return TxtRecord(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:dns/zone:Zone":
                return Zone(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure", "dns/aRecord", _module_instance)
    pulumi.runtime.register_resource_module("azure", "dns/aaaaRecord", _module_instance)
    pulumi.runtime.register_resource_module("azure", "dns/cNameRecord", _module_instance)
    pulumi.runtime.register_resource_module("azure", "dns/caaRecord", _module_instance)
    pulumi.runtime.register_resource_module("azure", "dns/mxRecord", _module_instance)
    pulumi.runtime.register_resource_module("azure", "dns/nsRecord", _module_instance)
    pulumi.runtime.register_resource_module("azure", "dns/ptrRecord", _module_instance)
    pulumi.runtime.register_resource_module("azure", "dns/srvRecord", _module_instance)
    pulumi.runtime.register_resource_module("azure", "dns/txtRecord", _module_instance)
    pulumi.runtime.register_resource_module("azure", "dns/zone", _module_instance)

_register_module()
