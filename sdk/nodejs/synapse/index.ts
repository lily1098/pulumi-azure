// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./firewallRule";
export * from "./getWorkspace";
export * from "./managedPrivateEndpoint";
export * from "./roleAssignment";
export * from "./sparkPool";
export * from "./sqlPool";
export * from "./workspace";

// Import resources to register:
import { FirewallRule } from "./firewallRule";
import { ManagedPrivateEndpoint } from "./managedPrivateEndpoint";
import { RoleAssignment } from "./roleAssignment";
import { SparkPool } from "./sparkPool";
import { SqlPool } from "./sqlPool";
import { Workspace } from "./workspace";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "azure:synapse/firewallRule:FirewallRule":
                return new FirewallRule(name, <any>undefined, { urn })
            case "azure:synapse/managedPrivateEndpoint:ManagedPrivateEndpoint":
                return new ManagedPrivateEndpoint(name, <any>undefined, { urn })
            case "azure:synapse/roleAssignment:RoleAssignment":
                return new RoleAssignment(name, <any>undefined, { urn })
            case "azure:synapse/sparkPool:SparkPool":
                return new SparkPool(name, <any>undefined, { urn })
            case "azure:synapse/sqlPool:SqlPool":
                return new SqlPool(name, <any>undefined, { urn })
            case "azure:synapse/workspace:Workspace":
                return new Workspace(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("azure", "synapse/firewallRule", _module)
pulumi.runtime.registerResourceModule("azure", "synapse/managedPrivateEndpoint", _module)
pulumi.runtime.registerResourceModule("azure", "synapse/roleAssignment", _module)
pulumi.runtime.registerResourceModule("azure", "synapse/sparkPool", _module)
pulumi.runtime.registerResourceModule("azure", "synapse/sqlPool", _module)
pulumi.runtime.registerResourceModule("azure", "synapse/workspace", _module)
