// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./analyticsAccount";
export * from "./analyticsFirewallRule";
export * from "./getStore";
export * from "./store";
export * from "./storeFile";
export * from "./storeFirewallRule";

// Import resources to register:
import { AnalyticsAccount } from "./analyticsAccount";
import { AnalyticsFirewallRule } from "./analyticsFirewallRule";
import { Store } from "./store";
import { StoreFile } from "./storeFile";
import { StoreFirewallRule } from "./storeFirewallRule";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "azure:datalake/analyticsAccount:AnalyticsAccount":
                return new AnalyticsAccount(name, <any>undefined, { urn })
            case "azure:datalake/analyticsFirewallRule:AnalyticsFirewallRule":
                return new AnalyticsFirewallRule(name, <any>undefined, { urn })
            case "azure:datalake/store:Store":
                return new Store(name, <any>undefined, { urn })
            case "azure:datalake/storeFile:StoreFile":
                return new StoreFile(name, <any>undefined, { urn })
            case "azure:datalake/storeFirewallRule:StoreFirewallRule":
                return new StoreFirewallRule(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("azure", "datalake/analyticsAccount", _module)
pulumi.runtime.registerResourceModule("azure", "datalake/analyticsFirewallRule", _module)
pulumi.runtime.registerResourceModule("azure", "datalake/store", _module)
pulumi.runtime.registerResourceModule("azure", "datalake/storeFile", _module)
pulumi.runtime.registerResourceModule("azure", "datalake/storeFirewallRule", _module)
