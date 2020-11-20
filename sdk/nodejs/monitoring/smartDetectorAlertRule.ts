// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages an Monitor Smart Detector Alert Rule.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 *
 * const exampleResourceGroup = new azure.core.ResourceGroup("exampleResourceGroup", {location: "West Europe"});
 * const exampleInsights = new azure.appinsights.Insights("exampleInsights", {
 *     location: exampleResourceGroup.location,
 *     resourceGroupName: exampleResourceGroup.name,
 *     applicationType: "web",
 * });
 * const exampleActionGroup = new azure.monitoring.ActionGroup("exampleActionGroup", {
 *     resourceGroupName: exampleResourceGroup.name,
 *     shortName: "exampleactiongroup",
 * });
 * const exampleSmartDetectorAlertRule = new azure.monitoring.SmartDetectorAlertRule("exampleSmartDetectorAlertRule", {
 *     resourceGroupName: exampleResourceGroup.name,
 *     severity: "Sev0",
 *     scopeResourceIds: [exampleInsights.id],
 *     frequency: "PT1M",
 *     detectorType: "FailureAnomaliesDetector",
 *     actionGroup: {
 *         ids: [azurerm_monitor_action_group.test.id],
 *     },
 * });
 * ```
 */
export class SmartDetectorAlertRule extends pulumi.CustomResource {
    /**
     * Get an existing SmartDetectorAlertRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SmartDetectorAlertRuleState, opts?: pulumi.CustomResourceOptions): SmartDetectorAlertRule {
        return new SmartDetectorAlertRule(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure:monitoring/smartDetectorAlertRule:SmartDetectorAlertRule';

    /**
     * Returns true if the given object is an instance of SmartDetectorAlertRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SmartDetectorAlertRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SmartDetectorAlertRule.__pulumiType;
    }

    /**
     * An `actionGroup` block as defined below.
     */
    public readonly actionGroup!: pulumi.Output<outputs.monitoring.SmartDetectorAlertRuleActionGroup>;
    /**
     * Specifies a description for the Smart Detector Alert Rule.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Specifies the Built-In Smart Detector type that this alert rule will use. Currently the only possible value is `FailureAnomaliesDetector`.
     */
    public readonly detectorType!: pulumi.Output<string>;
    /**
     * Is the Smart Detector Alert Rule enabled? Defaults to `true`.
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    /**
     * Specifies the frequency of this Smart Detector Alert Rule in ISO8601 format.
     */
    public readonly frequency!: pulumi.Output<string>;
    /**
     * Specifies the name of the Monitor Smart Detector Alert Rule. Changing this forces a new resource to be created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Specifies the name of the resource group in which the Monitor Smart Detector Alert Rule should exist. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName!: pulumi.Output<string>;
    /**
     * Specifies the scopes of this Smart Detector Alert Rule.
     */
    public readonly scopeResourceIds!: pulumi.Output<string[]>;
    /**
     * Specifies the severity of this Smart Detector Alert Rule. Possible values are `Sev0`, `Sev1`, `Sev2`, `Sev3` or `Sev4`.
     */
    public readonly severity!: pulumi.Output<string>;
    /**
     * Specifies the duration (in ISO8601 format) to wait before notifying on the alert rule again.
     */
    public readonly throttlingDuration!: pulumi.Output<string | undefined>;

    /**
     * Create a SmartDetectorAlertRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SmartDetectorAlertRuleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SmartDetectorAlertRuleArgs | SmartDetectorAlertRuleState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as SmartDetectorAlertRuleState | undefined;
            inputs["actionGroup"] = state ? state.actionGroup : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["detectorType"] = state ? state.detectorType : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["frequency"] = state ? state.frequency : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["scopeResourceIds"] = state ? state.scopeResourceIds : undefined;
            inputs["severity"] = state ? state.severity : undefined;
            inputs["throttlingDuration"] = state ? state.throttlingDuration : undefined;
        } else {
            const args = argsOrState as SmartDetectorAlertRuleArgs | undefined;
            if (!args || args.actionGroup === undefined) {
                throw new Error("Missing required property 'actionGroup'");
            }
            if (!args || args.detectorType === undefined) {
                throw new Error("Missing required property 'detectorType'");
            }
            if (!args || args.frequency === undefined) {
                throw new Error("Missing required property 'frequency'");
            }
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if (!args || args.scopeResourceIds === undefined) {
                throw new Error("Missing required property 'scopeResourceIds'");
            }
            if (!args || args.severity === undefined) {
                throw new Error("Missing required property 'severity'");
            }
            inputs["actionGroup"] = args ? args.actionGroup : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["detectorType"] = args ? args.detectorType : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["frequency"] = args ? args.frequency : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["scopeResourceIds"] = args ? args.scopeResourceIds : undefined;
            inputs["severity"] = args ? args.severity : undefined;
            inputs["throttlingDuration"] = args ? args.throttlingDuration : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(SmartDetectorAlertRule.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SmartDetectorAlertRule resources.
 */
export interface SmartDetectorAlertRuleState {
    /**
     * An `actionGroup` block as defined below.
     */
    readonly actionGroup?: pulumi.Input<inputs.monitoring.SmartDetectorAlertRuleActionGroup>;
    /**
     * Specifies a description for the Smart Detector Alert Rule.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Specifies the Built-In Smart Detector type that this alert rule will use. Currently the only possible value is `FailureAnomaliesDetector`.
     */
    readonly detectorType?: pulumi.Input<string>;
    /**
     * Is the Smart Detector Alert Rule enabled? Defaults to `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * Specifies the frequency of this Smart Detector Alert Rule in ISO8601 format.
     */
    readonly frequency?: pulumi.Input<string>;
    /**
     * Specifies the name of the Monitor Smart Detector Alert Rule. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specifies the name of the resource group in which the Monitor Smart Detector Alert Rule should exist. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * Specifies the scopes of this Smart Detector Alert Rule.
     */
    readonly scopeResourceIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Specifies the severity of this Smart Detector Alert Rule. Possible values are `Sev0`, `Sev1`, `Sev2`, `Sev3` or `Sev4`.
     */
    readonly severity?: pulumi.Input<string>;
    /**
     * Specifies the duration (in ISO8601 format) to wait before notifying on the alert rule again.
     */
    readonly throttlingDuration?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a SmartDetectorAlertRule resource.
 */
export interface SmartDetectorAlertRuleArgs {
    /**
     * An `actionGroup` block as defined below.
     */
    readonly actionGroup: pulumi.Input<inputs.monitoring.SmartDetectorAlertRuleActionGroup>;
    /**
     * Specifies a description for the Smart Detector Alert Rule.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Specifies the Built-In Smart Detector type that this alert rule will use. Currently the only possible value is `FailureAnomaliesDetector`.
     */
    readonly detectorType: pulumi.Input<string>;
    /**
     * Is the Smart Detector Alert Rule enabled? Defaults to `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * Specifies the frequency of this Smart Detector Alert Rule in ISO8601 format.
     */
    readonly frequency: pulumi.Input<string>;
    /**
     * Specifies the name of the Monitor Smart Detector Alert Rule. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specifies the name of the resource group in which the Monitor Smart Detector Alert Rule should exist. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * Specifies the scopes of this Smart Detector Alert Rule.
     */
    readonly scopeResourceIds: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Specifies the severity of this Smart Detector Alert Rule. Possible values are `Sev0`, `Sev1`, `Sev2`, `Sev3` or `Sev4`.
     */
    readonly severity: pulumi.Input<string>;
    /**
     * Specifies the duration (in ISO8601 format) to wait before notifying on the alert rule again.
     */
    readonly throttlingDuration?: pulumi.Input<string>;
}
