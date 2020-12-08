// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Manage an Azure Spring Cloud Application.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 *
 * const exampleResourceGroup = new azure.core.ResourceGroup("exampleResourceGroup", {location: "Southeast Asia"});
 * const exampleSpringCloudService = new azure.appplatform.SpringCloudService("exampleSpringCloudService", {
 *     resourceGroupName: exampleResourceGroup.name,
 *     location: exampleResourceGroup.location,
 * });
 * const exampleSpringCloudApp = new azure.appplatform.SpringCloudApp("exampleSpringCloudApp", {
 *     resourceGroupName: exampleResourceGroup.name,
 *     serviceName: exampleSpringCloudService.name,
 *     identity: {
 *         type: "SystemAssigned",
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * Spring Cloud Application can be imported using the `resource id`, e.g.
 *
 * ```sh
 *  $ pulumi import azure:appplatform/springCloudApp:SpringCloudApp example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myresourcegroup/providers/Microsoft.AppPlatform/Spring/myservice/apps/myapp
 * ```
 */
export class SpringCloudApp extends pulumi.CustomResource {
    /**
     * Get an existing SpringCloudApp resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SpringCloudAppState, opts?: pulumi.CustomResourceOptions): SpringCloudApp {
        return new SpringCloudApp(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure:appplatform/springCloudApp:SpringCloudApp';

    /**
     * Returns true if the given object is an instance of SpringCloudApp.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SpringCloudApp {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SpringCloudApp.__pulumiType;
    }

    /**
     * An `identity` block as defined below.
     */
    public readonly identity!: pulumi.Output<outputs.appplatform.SpringCloudAppIdentity | undefined>;
    /**
     * Specifies the name of the Spring Cloud Application. Changing this forces a new resource to be created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Specifies the name of the resource group in which to create the Spring Cloud Application. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName!: pulumi.Output<string>;
    /**
     * Specifies the name of the Spring Cloud Service resource. Changing this forces a new resource to be created.
     */
    public readonly serviceName!: pulumi.Output<string>;

    /**
     * Create a SpringCloudApp resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SpringCloudAppArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SpringCloudAppArgs | SpringCloudAppState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as SpringCloudAppState | undefined;
            inputs["identity"] = state ? state.identity : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["serviceName"] = state ? state.serviceName : undefined;
        } else {
            const args = argsOrState as SpringCloudAppArgs | undefined;
            if ((!args || args.resourceGroupName === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if ((!args || args.serviceName === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'serviceName'");
            }
            inputs["identity"] = args ? args.identity : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["serviceName"] = args ? args.serviceName : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(SpringCloudApp.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SpringCloudApp resources.
 */
export interface SpringCloudAppState {
    /**
     * An `identity` block as defined below.
     */
    readonly identity?: pulumi.Input<inputs.appplatform.SpringCloudAppIdentity>;
    /**
     * Specifies the name of the Spring Cloud Application. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specifies the name of the resource group in which to create the Spring Cloud Application. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * Specifies the name of the Spring Cloud Service resource. Changing this forces a new resource to be created.
     */
    readonly serviceName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a SpringCloudApp resource.
 */
export interface SpringCloudAppArgs {
    /**
     * An `identity` block as defined below.
     */
    readonly identity?: pulumi.Input<inputs.appplatform.SpringCloudAppIdentity>;
    /**
     * Specifies the name of the Spring Cloud Application. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specifies the name of the resource group in which to create the Spring Cloud Application. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * Specifies the name of the Spring Cloud Service resource. Changing this forces a new resource to be created.
     */
    readonly serviceName: pulumi.Input<string>;
}
