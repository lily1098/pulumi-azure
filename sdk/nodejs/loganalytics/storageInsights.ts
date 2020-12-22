// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a Log Analytics Storage Insights resource.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 *
 * const exampleResourceGroup = new azure.core.ResourceGroup("exampleResourceGroup", {location: "West Europe"});
 * const exampleAnalyticsWorkspace = new azure.operationalinsights.AnalyticsWorkspace("exampleAnalyticsWorkspace", {
 *     location: exampleResourceGroup.location,
 *     resourceGroupName: exampleResourceGroup.name,
 *     sku: "PerGB2018",
 *     retentionInDays: 30,
 * });
 * const exampleAccount = new azure.storage.Account("exampleAccount", {
 *     resourceGroupName: exampleResourceGroup.name,
 *     location: exampleResourceGroup.location,
 *     accountTier: "Standard",
 *     accountReplicationType: "LRS",
 * });
 * const exampleStorageInsights = new azure.loganalytics.StorageInsights("exampleStorageInsights", {
 *     resourceGroupName: exampleResourceGroup.name,
 *     workspaceId: exampleAnalyticsWorkspace.id,
 *     storageAccountId: exampleAccount.id,
 *     storageAccountKey: exampleAccount.primaryAccessKey,
 * });
 * ```
 *
 * ## Import
 *
 * Log Analytics Storage Insight Configs can be imported using the `resource id`, e.g.
 *
 * ```sh
 *  $ pulumi import azure:loganalytics/storageInsights:StorageInsights example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.OperationalInsights/workspaces/workspace1/storageInsightConfigs/storageInsight1
 * ```
 */
export class StorageInsights extends pulumi.CustomResource {
    /**
     * Get an existing StorageInsights resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StorageInsightsState, opts?: pulumi.CustomResourceOptions): StorageInsights {
        return new StorageInsights(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure:loganalytics/storageInsights:StorageInsights';

    /**
     * Returns true if the given object is an instance of StorageInsights.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is StorageInsights {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === StorageInsights.__pulumiType;
    }

    /**
     * The names of the blob containers that the workspace should read.
     */
    public readonly blobContainerNames!: pulumi.Output<string[] | undefined>;
    /**
     * The name which should be used for this Log Analytics Storage Insights. Changing this forces a new Log Analytics Storage Insights to be created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The name of the Resource Group where the Log Analytics Storage Insights should exist. Changing this forces a new Log Analytics Storage Insights to be created.
     */
    public readonly resourceGroupName!: pulumi.Output<string>;
    /**
     * The ID of the Storage Account used by this Log Analytics Storage Insights.
     */
    public readonly storageAccountId!: pulumi.Output<string>;
    /**
     * The storage access key to be used to connect to the storage account.
     */
    public readonly storageAccountKey!: pulumi.Output<string>;
    /**
     * The names of the Azure tables that the workspace should read.
     */
    public readonly tableNames!: pulumi.Output<string[] | undefined>;
    /**
     * A mapping of tags which should be assigned to the Log Analytics Storage Insights.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * The ID of the Log Analytics Workspace within which the Storage Insights should exist. Changing this forces a new Log Analytics Storage Insights to be created.
     */
    public readonly workspaceId!: pulumi.Output<string>;

    /**
     * Create a StorageInsights resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: StorageInsightsArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: StorageInsightsArgs | StorageInsightsState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as StorageInsightsState | undefined;
            inputs["blobContainerNames"] = state ? state.blobContainerNames : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["storageAccountId"] = state ? state.storageAccountId : undefined;
            inputs["storageAccountKey"] = state ? state.storageAccountKey : undefined;
            inputs["tableNames"] = state ? state.tableNames : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["workspaceId"] = state ? state.workspaceId : undefined;
        } else {
            const args = argsOrState as StorageInsightsArgs | undefined;
            if ((!args || args.resourceGroupName === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if ((!args || args.storageAccountId === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'storageAccountId'");
            }
            if ((!args || args.storageAccountKey === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'storageAccountKey'");
            }
            if ((!args || args.workspaceId === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'workspaceId'");
            }
            inputs["blobContainerNames"] = args ? args.blobContainerNames : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["storageAccountId"] = args ? args.storageAccountId : undefined;
            inputs["storageAccountKey"] = args ? args.storageAccountKey : undefined;
            inputs["tableNames"] = args ? args.tableNames : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["workspaceId"] = args ? args.workspaceId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(StorageInsights.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering StorageInsights resources.
 */
export interface StorageInsightsState {
    /**
     * The names of the blob containers that the workspace should read.
     */
    readonly blobContainerNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name which should be used for this Log Analytics Storage Insights. Changing this forces a new Log Analytics Storage Insights to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the Resource Group where the Log Analytics Storage Insights should exist. Changing this forces a new Log Analytics Storage Insights to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * The ID of the Storage Account used by this Log Analytics Storage Insights.
     */
    readonly storageAccountId?: pulumi.Input<string>;
    /**
     * The storage access key to be used to connect to the storage account.
     */
    readonly storageAccountKey?: pulumi.Input<string>;
    /**
     * The names of the Azure tables that the workspace should read.
     */
    readonly tableNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A mapping of tags which should be assigned to the Log Analytics Storage Insights.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The ID of the Log Analytics Workspace within which the Storage Insights should exist. Changing this forces a new Log Analytics Storage Insights to be created.
     */
    readonly workspaceId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a StorageInsights resource.
 */
export interface StorageInsightsArgs {
    /**
     * The names of the blob containers that the workspace should read.
     */
    readonly blobContainerNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name which should be used for this Log Analytics Storage Insights. Changing this forces a new Log Analytics Storage Insights to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the Resource Group where the Log Analytics Storage Insights should exist. Changing this forces a new Log Analytics Storage Insights to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * The ID of the Storage Account used by this Log Analytics Storage Insights.
     */
    readonly storageAccountId: pulumi.Input<string>;
    /**
     * The storage access key to be used to connect to the storage account.
     */
    readonly storageAccountKey: pulumi.Input<string>;
    /**
     * The names of the Azure tables that the workspace should read.
     */
    readonly tableNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A mapping of tags which should be assigned to the Log Analytics Storage Insights.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The ID of the Log Analytics Workspace within which the Storage Insights should exist. Changing this forces a new Log Analytics Storage Insights to be created.
     */
    readonly workspaceId: pulumi.Input<string>;
}