// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to access information about an existing App Service Plan (formerly known as a `Server Farm`).
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const test = pulumi.output(azure.appservice.getAppServicePlan({
 *     name: "search-app-service-plan",
 *     resourceGroupName: "search-service",
 * }));
 * 
 * export const appServicePlanId = test.apply(test => test.id);
 * ```
 */
export function getAppServicePlan(args: GetAppServicePlanArgs, opts?: pulumi.InvokeOptions): Promise<GetAppServicePlanResult> {
    return pulumi.runtime.invoke("azure:appservice/getAppServicePlan:getAppServicePlan", {
        "name": args.name,
        "resourceGroupName": args.resourceGroupName,
    }, opts);
}

/**
 * A collection of arguments for invoking getAppServicePlan.
 */
export interface GetAppServicePlanArgs {
    /**
     * The name of the App Service Plan.
     */
    readonly name: string;
    /**
     * The Name of the Resource Group where the App Service Plan exists.
     */
    readonly resourceGroupName: string;
}

/**
 * A collection of values returned by getAppServicePlan.
 */
export interface GetAppServicePlanResult {
    /**
     * The Operating System type of the App Service Plan
     */
    readonly kind: string;
    /**
     * The Azure location where the App Service Plan exists
     */
    readonly location: string;
    /**
     * Maximum number of instances that can be assigned to this App Service plan.
     */
    readonly maximumNumberOfWorkers: number;
    /**
     * A `properties` block as documented below.
     */
    readonly properties: { appServiceEnvironmentId: string, perSiteScaling: boolean, reserved: boolean }[];
    /**
     * A `sku` block as documented below.
     */
    readonly sku: { capacity: number, size: string, tier: string };
    /**
     * A mapping of tags assigned to the resource.
     */
    readonly tags: {[key: string]: any};
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
