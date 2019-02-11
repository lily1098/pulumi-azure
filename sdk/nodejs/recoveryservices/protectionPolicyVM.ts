// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages an Recovery Services VM Protection Policy.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const exampleResourceGroup = new azure.core.ResourceGroup("example", {
 *     location: "West US",
 * });
 * const exampleVault = new azure.recoveryservices.Vault("example", {
 *     location: exampleResourceGroup.location,
 *     resourceGroupName: exampleResourceGroup.name,
 *     sku: "Standard",
 * });
 * const test = new azure.recoveryservices.ProtectionPolicyVM("test", {
 *     backup: {
 *         frequency: "Daily",
 *         time: "23:00",
 *     },
 *     recoveryVaultName: exampleVault.name,
 *     resourceGroupName: exampleResourceGroup.name,
 *     retentionDaily: {
 *         count: 10,
 *     },
 *     retentionMonthly: {
 *         count: 7,
 *         weekdays: [
 *             "Sunday",
 *             "Wednesday",
 *         ],
 *         weeks: [
 *             "First",
 *             "Last",
 *         ],
 *     },
 *     retentionWeekly: {
 *         count: 42,
 *         weekdays: [
 *             "Sunday",
 *             "Wednesday",
 *             "Friday",
 *             "Saturday",
 *         ],
 *     },
 *     retentionYearly: {
 *         count: 77,
 *         months: ["January"],
 *         weekdays: ["Sunday"],
 *         weeks: ["Last"],
 *     },
 *     timezone: "UTC",
 * });
 * ```
 */
export class ProtectionPolicyVM extends pulumi.CustomResource {
    /**
     * Get an existing ProtectionPolicyVM resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProtectionPolicyVMState, opts?: pulumi.CustomResourceOptions): ProtectionPolicyVM {
        return new ProtectionPolicyVM(name, <any>state, { ...opts, id: id });
    }

    /**
     * Configures the Policy backup frequecent, times & days as documented in the `backup` block below. 
     */
    public readonly backup: pulumi.Output<{ frequency: string, time: string, weekdays?: string[] }>;
    /**
     * Specifies the name of the Recovery Services Vault Policy. Changing this forces a new resource to be created.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
     */
    public readonly recoveryVaultName: pulumi.Output<string>;
    /**
     * The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName: pulumi.Output<string>;
    /**
     * Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.
     */
    public readonly retentionDaily: pulumi.Output<{ count: number } | undefined>;
    /**
     * Configures the policy monthly retention as documented in the `retention_monthly` block below.
     */
    public readonly retentionMonthly: pulumi.Output<{ count: number, weekdays: string[], weeks: string[] } | undefined>;
    /**
     * Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.
     */
    public readonly retentionWeekly: pulumi.Output<{ count: number, weekdays: string[] } | undefined>;
    /**
     * Configures the policy yearly retention as documented in the `retention_yearly` block below.
     */
    public readonly retentionYearly: pulumi.Output<{ count: number, months: string[], weekdays: string[], weeks: string[] } | undefined>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags: pulumi.Output<{[key: string]: any}>;
    /**
     * Specifies the timezone. Defaults to `UTC`
     */
    public readonly timezone: pulumi.Output<string | undefined>;

    /**
     * Create a ProtectionPolicyVM resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProtectionPolicyVMArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ProtectionPolicyVMArgs | ProtectionPolicyVMState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ProtectionPolicyVMState = argsOrState as ProtectionPolicyVMState | undefined;
            inputs["backup"] = state ? state.backup : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["recoveryVaultName"] = state ? state.recoveryVaultName : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["retentionDaily"] = state ? state.retentionDaily : undefined;
            inputs["retentionMonthly"] = state ? state.retentionMonthly : undefined;
            inputs["retentionWeekly"] = state ? state.retentionWeekly : undefined;
            inputs["retentionYearly"] = state ? state.retentionYearly : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["timezone"] = state ? state.timezone : undefined;
        } else {
            const args = argsOrState as ProtectionPolicyVMArgs | undefined;
            if (!args || args.backup === undefined) {
                throw new Error("Missing required property 'backup'");
            }
            if (!args || args.recoveryVaultName === undefined) {
                throw new Error("Missing required property 'recoveryVaultName'");
            }
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            inputs["backup"] = args ? args.backup : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["recoveryVaultName"] = args ? args.recoveryVaultName : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["retentionDaily"] = args ? args.retentionDaily : undefined;
            inputs["retentionMonthly"] = args ? args.retentionMonthly : undefined;
            inputs["retentionWeekly"] = args ? args.retentionWeekly : undefined;
            inputs["retentionYearly"] = args ? args.retentionYearly : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["timezone"] = args ? args.timezone : undefined;
        }
        super("azure:recoveryservices/protectionPolicyVM:ProtectionPolicyVM", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ProtectionPolicyVM resources.
 */
export interface ProtectionPolicyVMState {
    /**
     * Configures the Policy backup frequecent, times & days as documented in the `backup` block below. 
     */
    readonly backup?: pulumi.Input<{ frequency: pulumi.Input<string>, time: pulumi.Input<string>, weekdays?: pulumi.Input<pulumi.Input<string>[]> }>;
    /**
     * Specifies the name of the Recovery Services Vault Policy. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
     */
    readonly recoveryVaultName?: pulumi.Input<string>;
    /**
     * The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.
     */
    readonly retentionDaily?: pulumi.Input<{ count: pulumi.Input<number> }>;
    /**
     * Configures the policy monthly retention as documented in the `retention_monthly` block below.
     */
    readonly retentionMonthly?: pulumi.Input<{ count: pulumi.Input<number>, weekdays: pulumi.Input<pulumi.Input<string>[]>, weeks: pulumi.Input<pulumi.Input<string>[]> }>;
    /**
     * Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.
     */
    readonly retentionWeekly?: pulumi.Input<{ count: pulumi.Input<number>, weekdays: pulumi.Input<pulumi.Input<string>[]> }>;
    /**
     * Configures the policy yearly retention as documented in the `retention_yearly` block below.
     */
    readonly retentionYearly?: pulumi.Input<{ count: pulumi.Input<number>, months: pulumi.Input<pulumi.Input<string>[]>, weekdays: pulumi.Input<pulumi.Input<string>[]>, weeks: pulumi.Input<pulumi.Input<string>[]> }>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * Specifies the timezone. Defaults to `UTC`
     */
    readonly timezone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ProtectionPolicyVM resource.
 */
export interface ProtectionPolicyVMArgs {
    /**
     * Configures the Policy backup frequecent, times & days as documented in the `backup` block below. 
     */
    readonly backup: pulumi.Input<{ frequency: pulumi.Input<string>, time: pulumi.Input<string>, weekdays?: pulumi.Input<pulumi.Input<string>[]> }>;
    /**
     * Specifies the name of the Recovery Services Vault Policy. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
     */
    readonly recoveryVaultName: pulumi.Input<string>;
    /**
     * The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.
     */
    readonly retentionDaily?: pulumi.Input<{ count: pulumi.Input<number> }>;
    /**
     * Configures the policy monthly retention as documented in the `retention_monthly` block below.
     */
    readonly retentionMonthly?: pulumi.Input<{ count: pulumi.Input<number>, weekdays: pulumi.Input<pulumi.Input<string>[]>, weeks: pulumi.Input<pulumi.Input<string>[]> }>;
    /**
     * Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.
     */
    readonly retentionWeekly?: pulumi.Input<{ count: pulumi.Input<number>, weekdays: pulumi.Input<pulumi.Input<string>[]> }>;
    /**
     * Configures the policy yearly retention as documented in the `retention_yearly` block below.
     */
    readonly retentionYearly?: pulumi.Input<{ count: pulumi.Input<number>, months: pulumi.Input<pulumi.Input<string>[]>, weekdays: pulumi.Input<pulumi.Input<string>[]>, weeks: pulumi.Input<pulumi.Input<string>[]> }>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * Specifies the timezone. Defaults to `UTC`
     */
    readonly timezone?: pulumi.Input<string>;
}
