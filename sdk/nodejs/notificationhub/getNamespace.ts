// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to access information about an existing Notification Hub Namespace.
 * 
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/notification_hub_namespace.html.markdown.
 */
export function getNamespace(args: GetNamespaceArgs, opts?: pulumi.InvokeOptions): Promise<GetNamespaceResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("azure:notificationhub/getNamespace:getNamespace", {
        "name": args.name,
        "resourceGroupName": args.resourceGroupName,
    }, opts);
}

/**
 * A collection of arguments for invoking getNamespace.
 */
export interface GetNamespaceArgs {
    /**
     * Specifies the Name of the Notification Hub Namespace.
     */
    readonly name: string;
    /**
     * Specifies the Name of the Resource Group within which the Notification Hub exists.
     */
    readonly resourceGroupName: string;
}

/**
 * A collection of values returned by getNamespace.
 */
export interface GetNamespaceResult {
    /**
     * Is this Notification Hub Namespace enabled?
     */
    readonly enabled: boolean;
    /**
     * The Azure Region in which this Notification Hub Namespace exists.
     */
    readonly location: string;
    /**
     * The name of the SKU to use for this Notification Hub Namespace. Possible values are `Free`, `Basic` or `Standard.`
     */
    readonly name: string;
    /**
     * The Type of Namespace, such as `Messaging` or `NotificationHub`.
     */
    readonly namespaceType: string;
    readonly resourceGroupName: string;
    readonly servicebusEndpoint: string;
    /**
     * A `sku` block as defined below.
     */
    readonly sku: outputs.notificationhub.GetNamespaceSku;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags: {[key: string]: string};
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
