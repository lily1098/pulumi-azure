# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .database import *
from .database_extended_auditing_policy import *
from .database_vulnerability_assessment_rule_baseline import *
from .elastic_pool import *
from .get_database import *
from .get_elastic_pool import *
from .get_server import *
from .server import *
from .server_extended_auditing_policy import *
from .server_security_alert_policy import *
from .server_vulnerability_assessment import *
from .virtual_machine import *
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
            if typ == "azure:mssql/database:Database":
                return Database(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:mssql/databaseExtendedAuditingPolicy:DatabaseExtendedAuditingPolicy":
                return DatabaseExtendedAuditingPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:mssql/databaseVulnerabilityAssessmentRuleBaseline:DatabaseVulnerabilityAssessmentRuleBaseline":
                return DatabaseVulnerabilityAssessmentRuleBaseline(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:mssql/elasticPool:ElasticPool":
                return ElasticPool(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:mssql/server:Server":
                return Server(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:mssql/serverExtendedAuditingPolicy:ServerExtendedAuditingPolicy":
                return ServerExtendedAuditingPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:mssql/serverSecurityAlertPolicy:ServerSecurityAlertPolicy":
                return ServerSecurityAlertPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:mssql/serverVulnerabilityAssessment:ServerVulnerabilityAssessment":
                return ServerVulnerabilityAssessment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure:mssql/virtualMachine:VirtualMachine":
                return VirtualMachine(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure", "mssql/database", _module_instance)
    pulumi.runtime.register_resource_module("azure", "mssql/databaseExtendedAuditingPolicy", _module_instance)
    pulumi.runtime.register_resource_module("azure", "mssql/databaseVulnerabilityAssessmentRuleBaseline", _module_instance)
    pulumi.runtime.register_resource_module("azure", "mssql/elasticPool", _module_instance)
    pulumi.runtime.register_resource_module("azure", "mssql/server", _module_instance)
    pulumi.runtime.register_resource_module("azure", "mssql/serverExtendedAuditingPolicy", _module_instance)
    pulumi.runtime.register_resource_module("azure", "mssql/serverSecurityAlertPolicy", _module_instance)
    pulumi.runtime.register_resource_module("azure", "mssql/serverVulnerabilityAssessment", _module_instance)
    pulumi.runtime.register_resource_module("azure", "mssql/virtualMachine", _module_instance)

_register_module()
