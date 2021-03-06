// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./getGroup";
export * from "./group";
export * from "./lock";

// Import resources to register:
import { Group } from "./group";
import { Lock } from "./lock";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "azure:management/group:Group":
                return new Group(name, <any>undefined, { urn })
            case "azure:management/lock:Lock":
                return new Lock(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("azure", "management/group", _module)
pulumi.runtime.registerResourceModule("azure", "management/lock", _module)
