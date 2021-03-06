// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Manages a Azure Web Application Firewall Policy instance.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 *
 * const exampleResourceGroup = new azure.core.ResourceGroup("exampleResourceGroup", {location: "West US 2"});
 * const examplePolicy = new azure.waf.Policy("examplePolicy", {
 *     resourceGroupName: exampleResourceGroup.name,
 *     location: exampleResourceGroup.location,
 *     customRules: [
 *         {
 *             name: "Rule1",
 *             priority: 1,
 *             ruleType: "MatchRule",
 *             matchConditions: [{
 *                 matchVariables: [{
 *                     variableName: "RemoteAddr",
 *                 }],
 *                 operator: "IPMatch",
 *                 negationCondition: false,
 *                 matchValues: [
 *                     "192.168.1.0/24",
 *                     "10.0.0.0/24",
 *                 ],
 *             }],
 *             action: "Block",
 *         },
 *         {
 *             name: "Rule2",
 *             priority: 2,
 *             ruleType: "MatchRule",
 *             matchConditions: [
 *                 {
 *                     matchVariables: [{
 *                         variableName: "RemoteAddr",
 *                     }],
 *                     operator: "IPMatch",
 *                     negationCondition: false,
 *                     matchValues: ["192.168.1.0/24"],
 *                 },
 *                 {
 *                     matchVariables: [{
 *                         variableName: "RequestHeaders",
 *                         selector: "UserAgent",
 *                     }],
 *                     operator: "Contains",
 *                     negationCondition: false,
 *                     matchValues: ["Windows"],
 *                 },
 *             ],
 *             action: "Block",
 *         },
 *     ],
 *     policySettings: {
 *         enabled: true,
 *         mode: "Prevention",
 *         requestBodyCheck: true,
 *         fileUploadLimitInMb: 100,
 *         maxRequestBodySizeInKb: 128,
 *     },
 *     managedRules: {
 *         exclusions: [
 *             {
 *                 matchVariable: "RequestHeaderNames",
 *                 selector: "x-company-secret-header",
 *                 selectorMatchOperator: "Equals",
 *             },
 *             {
 *                 matchVariable: "RequestCookieNames",
 *                 selector: "too-tasty",
 *                 selectorMatchOperator: "EndsWith",
 *             },
 *         ],
 *         managedRuleSets: [{
 *             type: "OWASP",
 *             version: "3.1",
 *             ruleGroupOverrides: [{
 *                 ruleGroupName: "REQUEST-920-PROTOCOL-ENFORCEMENT",
 *                 disabledRules: [
 *                     "920300",
 *                     "920440",
 *                 ],
 *             }],
 *         }],
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * Web Application Firewall Policy can be imported using the `resource id`, e.g.
 *
 * ```sh
 *  $ pulumi import azure:waf/policy:Policy example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example-rg/providers/Microsoft.Network/ApplicationGatewayWebApplicationFirewallPolicies/example-wafpolicy
 * ```
 */
export class Policy extends pulumi.CustomResource {
    /**
     * Get an existing Policy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyState, opts?: pulumi.CustomResourceOptions): Policy {
        return new Policy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure:waf/policy:Policy';

    /**
     * Returns true if the given object is an instance of Policy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Policy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Policy.__pulumiType;
    }

    /**
     * One or more `customRules` blocks as defined below.
     */
    public readonly customRules!: pulumi.Output<outputs.waf.PolicyCustomRule[] | undefined>;
    /**
     * Resource location. Changing this forces a new resource to be created.
     */
    public readonly location!: pulumi.Output<string>;
    /**
     * A `managedRules` blocks as defined below.
     */
    public readonly managedRules!: pulumi.Output<outputs.waf.PolicyManagedRules>;
    /**
     * The name of the policy. Changing this forces a new resource to be created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * A `policySettings` block as defined below.
     */
    public readonly policySettings!: pulumi.Output<outputs.waf.PolicyPolicySettings | undefined>;
    /**
     * The name of the resource group. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName!: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the Web Application Firewall Policy.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;

    /**
     * Create a Policy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PolicyArgs | PolicyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PolicyState | undefined;
            inputs["customRules"] = state ? state.customRules : undefined;
            inputs["location"] = state ? state.location : undefined;
            inputs["managedRules"] = state ? state.managedRules : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["policySettings"] = state ? state.policySettings : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as PolicyArgs | undefined;
            if ((!args || args.managedRules === undefined) && !opts.urn) {
                throw new Error("Missing required property 'managedRules'");
            }
            if ((!args || args.resourceGroupName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            inputs["customRules"] = args ? args.customRules : undefined;
            inputs["location"] = args ? args.location : undefined;
            inputs["managedRules"] = args ? args.managedRules : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["policySettings"] = args ? args.policySettings : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["tags"] = args ? args.tags : undefined;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Policy.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Policy resources.
 */
export interface PolicyState {
    /**
     * One or more `customRules` blocks as defined below.
     */
    readonly customRules?: pulumi.Input<pulumi.Input<inputs.waf.PolicyCustomRule>[]>;
    /**
     * Resource location. Changing this forces a new resource to be created.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * A `managedRules` blocks as defined below.
     */
    readonly managedRules?: pulumi.Input<inputs.waf.PolicyManagedRules>;
    /**
     * The name of the policy. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A `policySettings` block as defined below.
     */
    readonly policySettings?: pulumi.Input<inputs.waf.PolicyPolicySettings>;
    /**
     * The name of the resource group. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the Web Application Firewall Policy.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The set of arguments for constructing a Policy resource.
 */
export interface PolicyArgs {
    /**
     * One or more `customRules` blocks as defined below.
     */
    readonly customRules?: pulumi.Input<pulumi.Input<inputs.waf.PolicyCustomRule>[]>;
    /**
     * Resource location. Changing this forces a new resource to be created.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * A `managedRules` blocks as defined below.
     */
    readonly managedRules: pulumi.Input<inputs.waf.PolicyManagedRules>;
    /**
     * The name of the policy. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A `policySettings` block as defined below.
     */
    readonly policySettings?: pulumi.Input<inputs.waf.PolicyPolicySettings>;
    /**
     * The name of the resource group. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the Web Application Firewall Policy.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
