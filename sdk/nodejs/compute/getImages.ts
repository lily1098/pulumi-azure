// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Use this data source to access information about existing Images within a Resource Group.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 *
 * const example = pulumi.output(azure.compute.getImages({
 *     resourceGroupName: "example-resources",
 * }, { async: true }));
 * ```
 */
export function getImages(args: GetImagesArgs, opts?: pulumi.InvokeOptions): Promise<GetImagesResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("azure:compute/getImages:getImages", {
        "resourceGroupName": args.resourceGroupName,
        "tagsFilter": args.tagsFilter,
    }, opts);
}

/**
 * A collection of arguments for invoking getImages.
 */
export interface GetImagesArgs {
    /**
     * The name of the Resource Group in which the Image exists.
     */
    readonly resourceGroupName: string;
    /**
     * A mapping of tags to filter the list of images against.
     */
    readonly tagsFilter?: {[key: string]: string};
}

/**
 * A collection of values returned by getImages.
 */
export interface GetImagesResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * One or more `images` blocks as defined below:
     */
    readonly images: outputs.compute.GetImagesImage[];
    readonly resourceGroupName: string;
    readonly tagsFilter?: {[key: string]: string};
}
