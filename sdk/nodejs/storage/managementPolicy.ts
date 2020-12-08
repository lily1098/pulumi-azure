// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Manages an Azure Storage Account Management Policy.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 *
 * const exampleResourceGroup = new azure.core.ResourceGroup("exampleResourceGroup", {location: "westus"});
 * const exampleAccount = new azure.storage.Account("exampleAccount", {
 *     resourceGroupName: exampleResourceGroup.name,
 *     location: exampleResourceGroup.location,
 *     accountTier: "Standard",
 *     accountReplicationType: "LRS",
 *     accountKind: "BlobStorage",
 * });
 * const exampleManagementPolicy = new azure.storage.ManagementPolicy("exampleManagementPolicy", {
 *     storageAccountId: exampleAccount.id,
 *     rules: [
 *         {
 *             name: "rule1",
 *             enabled: true,
 *             filters: {
 *                 prefixMatches: ["container1/prefix1"],
 *                 blobTypes: ["blockBlob"],
 *             },
 *             actions: {
 *                 baseBlob: {
 *                     tierToCoolAfterDaysSinceModificationGreaterThan: 10,
 *                     tierToArchiveAfterDaysSinceModificationGreaterThan: 50,
 *                     deleteAfterDaysSinceModificationGreaterThan: 100,
 *                 },
 *                 snapshot: {
 *                     deleteAfterDaysSinceCreationGreaterThan: 30,
 *                 },
 *             },
 *         },
 *         {
 *             name: "rule2",
 *             enabled: false,
 *             filters: {
 *                 prefixMatches: [
 *                     "container2/prefix1",
 *                     "container2/prefix2",
 *                 ],
 *                 blobTypes: ["blockBlob"],
 *             },
 *             actions: {
 *                 baseBlob: {
 *                     tierToCoolAfterDaysSinceModificationGreaterThan: 11,
 *                     tierToArchiveAfterDaysSinceModificationGreaterThan: 51,
 *                     deleteAfterDaysSinceModificationGreaterThan: 101,
 *                 },
 *                 snapshot: {
 *                     deleteAfterDaysSinceCreationGreaterThan: 31,
 *                 },
 *             },
 *         },
 *     ],
 * });
 * ```
 *
 * ## Import
 *
 * Storage Account Management Policies can be imported using the `resource id`, e.g.
 *
 * ```sh
 *  $ pulumi import azure:storage/managementPolicy:ManagementPolicy example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Storage/storageAccounts/myaccountname/managementPolicies/default
 * ```
 */
export class ManagementPolicy extends pulumi.CustomResource {
    /**
     * Get an existing ManagementPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ManagementPolicyState, opts?: pulumi.CustomResourceOptions): ManagementPolicy {
        return new ManagementPolicy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure:storage/managementPolicy:ManagementPolicy';

    /**
     * Returns true if the given object is an instance of ManagementPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ManagementPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ManagementPolicy.__pulumiType;
    }

    /**
     * A `rule` block as documented below.
     */
    public readonly rules!: pulumi.Output<outputs.storage.ManagementPolicyRule[] | undefined>;
    /**
     * Specifies the id of the storage account to apply the management policy to.
     */
    public readonly storageAccountId!: pulumi.Output<string>;

    /**
     * Create a ManagementPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ManagementPolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ManagementPolicyArgs | ManagementPolicyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ManagementPolicyState | undefined;
            inputs["rules"] = state ? state.rules : undefined;
            inputs["storageAccountId"] = state ? state.storageAccountId : undefined;
        } else {
            const args = argsOrState as ManagementPolicyArgs | undefined;
            if ((!args || args.storageAccountId === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'storageAccountId'");
            }
            inputs["rules"] = args ? args.rules : undefined;
            inputs["storageAccountId"] = args ? args.storageAccountId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ManagementPolicy.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ManagementPolicy resources.
 */
export interface ManagementPolicyState {
    /**
     * A `rule` block as documented below.
     */
    readonly rules?: pulumi.Input<pulumi.Input<inputs.storage.ManagementPolicyRule>[]>;
    /**
     * Specifies the id of the storage account to apply the management policy to.
     */
    readonly storageAccountId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ManagementPolicy resource.
 */
export interface ManagementPolicyArgs {
    /**
     * A `rule` block as documented below.
     */
    readonly rules?: pulumi.Input<pulumi.Input<inputs.storage.ManagementPolicyRule>[]>;
    /**
     * Specifies the id of the storage account to apply the management policy to.
     */
    readonly storageAccountId: pulumi.Input<string>;
}
