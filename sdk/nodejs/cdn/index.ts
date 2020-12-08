// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./endpoint";
export * from "./getProfile";
export * from "./profile";

// Import resources to register:
import { Endpoint } from "./endpoint";
import { Profile } from "./profile";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "azure:cdn/endpoint:Endpoint":
                return new Endpoint(name, <any>undefined, { urn })
            case "azure:cdn/profile:Profile":
                return new Profile(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("azure", "cdn/endpoint", _module)
pulumi.runtime.registerResourceModule("azure", "cdn/profile", _module)
