// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./activeDirectoryAdministrator";
export * from "./configuration";
export * from "./database";
export * from "./firewallRule";
export * from "./getServer";
export * from "./server";
export * from "./serverKey";
export * from "./virtualNetworkRule";

// Import resources to register:
import { ActiveDirectoryAdministrator } from "./activeDirectoryAdministrator";
import { Configuration } from "./configuration";
import { Database } from "./database";
import { FirewallRule } from "./firewallRule";
import { Server } from "./server";
import { ServerKey } from "./serverKey";
import { VirtualNetworkRule } from "./virtualNetworkRule";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "azure:mysql/activeDirectoryAdministrator:ActiveDirectoryAdministrator":
                return new ActiveDirectoryAdministrator(name, <any>undefined, { urn })
            case "azure:mysql/configuration:Configuration":
                return new Configuration(name, <any>undefined, { urn })
            case "azure:mysql/database:Database":
                return new Database(name, <any>undefined, { urn })
            case "azure:mysql/firewallRule:FirewallRule":
                return new FirewallRule(name, <any>undefined, { urn })
            case "azure:mysql/server:Server":
                return new Server(name, <any>undefined, { urn })
            case "azure:mysql/serverKey:ServerKey":
                return new ServerKey(name, <any>undefined, { urn })
            case "azure:mysql/virtualNetworkRule:VirtualNetworkRule":
                return new VirtualNetworkRule(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("azure", "mysql/activeDirectoryAdministrator", _module)
pulumi.runtime.registerResourceModule("azure", "mysql/configuration", _module)
pulumi.runtime.registerResourceModule("azure", "mysql/database", _module)
pulumi.runtime.registerResourceModule("azure", "mysql/firewallRule", _module)
pulumi.runtime.registerResourceModule("azure", "mysql/server", _module)
pulumi.runtime.registerResourceModule("azure", "mysql/serverKey", _module)
pulumi.runtime.registerResourceModule("azure", "mysql/virtualNetworkRule", _module)
