// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Manages a JavaScript UDF Function within Stream Analytics Streaming Job.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 *
 * const exampleResourceGroup = azure.core.getResourceGroup({
 *     name: "example-resources",
 * });
 * const exampleJob = azure.streamanalytics.getJob({
 *     name: "example-job",
 *     resourceGroupName: azurerm_resource_group.example.name,
 * });
 * const exampleFunctionJavaScriptUDF = new azure.streamanalytics.FunctionJavaScriptUDF("exampleFunctionJavaScriptUDF", {
 *     streamAnalyticsJobName: exampleJob.then(exampleJob => exampleJob.name),
 *     resourceGroupName: exampleJob.then(exampleJob => exampleJob.resourceGroupName),
 *     script: `function getRandomNumber(in) {
 *   return in;
 * }
 * `,
 *     inputs: [{
 *         type: "bigint",
 *     }],
 *     output: {
 *         type: "bigint",
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * Stream Analytics JavaScript UDF Functions can be imported using the `resource id`, e.g.
 *
 * ```sh
 *  $ pulumi import azure:streamanalytics/functionJavaScriptUDF:FunctionJavaScriptUDF example /subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/group1/providers/Microsoft.StreamAnalytics/streamingjobs/job1/outputs/output1
 * ```
 */
export class FunctionJavaScriptUDF extends pulumi.CustomResource {
    /**
     * Get an existing FunctionJavaScriptUDF resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FunctionJavaScriptUDFState, opts?: pulumi.CustomResourceOptions): FunctionJavaScriptUDF {
        return new FunctionJavaScriptUDF(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure:streamanalytics/functionJavaScriptUDF:FunctionJavaScriptUDF';

    /**
     * Returns true if the given object is an instance of FunctionJavaScriptUDF.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is FunctionJavaScriptUDF {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === FunctionJavaScriptUDF.__pulumiType;
    }

    /**
     * One or more `input` blocks as defined below.
     */
    public readonly inputs!: pulumi.Output<outputs.streamanalytics.FunctionJavaScriptUDFInput[]>;
    /**
     * The name of the JavaScript UDF Function. Changing this forces a new resource to be created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * An `output` blocks as defined below.
     */
    public readonly output!: pulumi.Output<outputs.streamanalytics.FunctionJavaScriptUDFOutput>;
    /**
     * The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName!: pulumi.Output<string>;
    /**
     * The JavaScript of this UDF Function.
     */
    public readonly script!: pulumi.Output<string>;
    /**
     * The name of the Stream Analytics Job where this Function should be created. Changing this forces a new resource to be created.
     */
    public readonly streamAnalyticsJobName!: pulumi.Output<string>;

    /**
     * Create a FunctionJavaScriptUDF resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FunctionJavaScriptUDFArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FunctionJavaScriptUDFArgs | FunctionJavaScriptUDFState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as FunctionJavaScriptUDFState | undefined;
            inputs["inputs"] = state ? state.inputs : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["output"] = state ? state.output : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["script"] = state ? state.script : undefined;
            inputs["streamAnalyticsJobName"] = state ? state.streamAnalyticsJobName : undefined;
        } else {
            const args = argsOrState as FunctionJavaScriptUDFArgs | undefined;
            if ((!args || args.inputs === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'inputs'");
            }
            if ((!args || args.output === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'output'");
            }
            if ((!args || args.resourceGroupName === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if ((!args || args.script === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'script'");
            }
            if ((!args || args.streamAnalyticsJobName === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'streamAnalyticsJobName'");
            }
            inputs["inputs"] = args ? args.inputs : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["output"] = args ? args.output : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["script"] = args ? args.script : undefined;
            inputs["streamAnalyticsJobName"] = args ? args.streamAnalyticsJobName : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(FunctionJavaScriptUDF.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering FunctionJavaScriptUDF resources.
 */
export interface FunctionJavaScriptUDFState {
    /**
     * One or more `input` blocks as defined below.
     */
    readonly inputs?: pulumi.Input<pulumi.Input<inputs.streamanalytics.FunctionJavaScriptUDFInput>[]>;
    /**
     * The name of the JavaScript UDF Function. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * An `output` blocks as defined below.
     */
    readonly output?: pulumi.Input<inputs.streamanalytics.FunctionJavaScriptUDFOutput>;
    /**
     * The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * The JavaScript of this UDF Function.
     */
    readonly script?: pulumi.Input<string>;
    /**
     * The name of the Stream Analytics Job where this Function should be created. Changing this forces a new resource to be created.
     */
    readonly streamAnalyticsJobName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a FunctionJavaScriptUDF resource.
 */
export interface FunctionJavaScriptUDFArgs {
    /**
     * One or more `input` blocks as defined below.
     */
    readonly inputs: pulumi.Input<pulumi.Input<inputs.streamanalytics.FunctionJavaScriptUDFInput>[]>;
    /**
     * The name of the JavaScript UDF Function. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * An `output` blocks as defined below.
     */
    readonly output: pulumi.Input<inputs.streamanalytics.FunctionJavaScriptUDFOutput>;
    /**
     * The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * The JavaScript of this UDF Function.
     */
    readonly script: pulumi.Input<string>;
    /**
     * The name of the Stream Analytics Job where this Function should be created. Changing this forces a new resource to be created.
     */
    readonly streamAnalyticsJobName: pulumi.Input<string>;
}
