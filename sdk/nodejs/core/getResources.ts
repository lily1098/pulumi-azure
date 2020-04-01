// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to access information about existing resources.
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/resources.html.markdown.
 */
export function getResources(args?: GetResourcesArgs, opts?: pulumi.InvokeOptions): Promise<GetResourcesResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("azure:core/getResources:getResources", {
        "name": args.name,
        "requiredTags": args.requiredTags,
        "resourceGroupName": args.resourceGroupName,
        "type": args.type,
    }, opts);
}

/**
 * A collection of arguments for invoking getResources.
 */
export interface GetResourcesArgs {
    /**
     * The name of the Resource.
     */
    readonly name?: string;
    /**
     * A mapping of tags which the resource has to have in order to be included in the result.
     */
    readonly requiredTags?: {[key: string]: string};
    /**
     * The name of the Resource group where the Resources are located.
     */
    readonly resourceGroupName?: string;
    /**
     * The Resource Type of the Resources you want to list (e.g. `Microsoft.Network/virtualNetworks`). A full list of available Resource Types can be found [here](https://docs.microsoft.com/en-us/azure/azure-resource-manager/azure-services-resource-providers).
     */
    readonly type?: string;
}

/**
 * A collection of values returned by getResources.
 */
export interface GetResourcesResult {
    /**
     * The name of this Resource.
     */
    readonly name: string;
    readonly requiredTags?: {[key: string]: string};
    readonly resourceGroupName: string;
    /**
     * One or more `resource` blocks as defined below.
     */
    readonly resources: outputs.core.GetResourcesResource[];
    /**
     * The type of this Resource. (e.g. `Microsoft.Network/virtualNetworks`).
     */
    readonly type: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
