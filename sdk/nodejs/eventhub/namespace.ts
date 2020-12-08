// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a ServiceBus Namespace.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 *
 * const exampleResourceGroup = new azure.core.ResourceGroup("exampleResourceGroup", {location: "West Europe"});
 * const exampleNamespace = new azure.servicebus.Namespace("exampleNamespace", {
 *     location: exampleResourceGroup.location,
 *     resourceGroupName: exampleResourceGroup.name,
 *     sku: "Standard",
 *     tags: {
 *         source: "example",
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * Service Bus Namespace can be imported using the `resource id`, e.g.
 *
 * ```sh
 *  $ pulumi import azure:eventhub/namespace:Namespace example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/microsoft.servicebus/namespaces/sbns1
 * ```
 *
 * @deprecated azure.eventhub.Namespace has been deprecated in favor of azure.servicebus.Namespace
 */
export class Namespace extends pulumi.CustomResource {
    /**
     * Get an existing Namespace resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NamespaceState, opts?: pulumi.CustomResourceOptions): Namespace {
        pulumi.log.warn("Namespace is deprecated: azure.eventhub.Namespace has been deprecated in favor of azure.servicebus.Namespace")
        return new Namespace(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure:eventhub/namespace:Namespace';

    /**
     * Returns true if the given object is an instance of Namespace.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Namespace {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Namespace.__pulumiType;
    }

    /**
     * Specifies the capacity. When `sku` is `Premium`, capacity can be `1`, `2`, `4` or `8`. When `sku` is `Basic` or `Standard`, capacity can be `0` only.
     */
    public readonly capacity!: pulumi.Output<number | undefined>;
    /**
     * The primary connection string for the authorization
     * rule `RootManageSharedAccessKey`.
     */
    public /*out*/ readonly defaultPrimaryConnectionString!: pulumi.Output<string>;
    /**
     * The primary access key for the authorization rule `RootManageSharedAccessKey`.
     */
    public /*out*/ readonly defaultPrimaryKey!: pulumi.Output<string>;
    /**
     * The secondary connection string for the
     * authorization rule `RootManageSharedAccessKey`.
     */
    public /*out*/ readonly defaultSecondaryConnectionString!: pulumi.Output<string>;
    /**
     * The secondary access key for the authorization rule `RootManageSharedAccessKey`.
     */
    public /*out*/ readonly defaultSecondaryKey!: pulumi.Output<string>;
    /**
     * Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
     */
    public readonly location!: pulumi.Output<string>;
    /**
     * Specifies the name of the ServiceBus Namespace resource . Changing this forces a
     * new resource to be created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The name of the resource group in which to
     * create the namespace.
     */
    public readonly resourceGroupName!: pulumi.Output<string>;
    /**
     * Defines which tier to use. Options are basic, standard or premium. Changing this forces a new resource to be created.
     */
    public readonly sku!: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * Whether or not this resource is zone redundant. `sku` needs to be `Premium`. Defaults to `false`.
     */
    public readonly zoneRedundant!: pulumi.Output<boolean | undefined>;

    /**
     * Create a Namespace resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated azure.eventhub.Namespace has been deprecated in favor of azure.servicebus.Namespace */
    constructor(name: string, args: NamespaceArgs, opts?: pulumi.CustomResourceOptions)
    /** @deprecated azure.eventhub.Namespace has been deprecated in favor of azure.servicebus.Namespace */
    constructor(name: string, argsOrState?: NamespaceArgs | NamespaceState, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Namespace is deprecated: azure.eventhub.Namespace has been deprecated in favor of azure.servicebus.Namespace")
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as NamespaceState | undefined;
            inputs["capacity"] = state ? state.capacity : undefined;
            inputs["defaultPrimaryConnectionString"] = state ? state.defaultPrimaryConnectionString : undefined;
            inputs["defaultPrimaryKey"] = state ? state.defaultPrimaryKey : undefined;
            inputs["defaultSecondaryConnectionString"] = state ? state.defaultSecondaryConnectionString : undefined;
            inputs["defaultSecondaryKey"] = state ? state.defaultSecondaryKey : undefined;
            inputs["location"] = state ? state.location : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["sku"] = state ? state.sku : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["zoneRedundant"] = state ? state.zoneRedundant : undefined;
        } else {
            const args = argsOrState as NamespaceArgs | undefined;
            if ((!args || args.resourceGroupName === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if ((!args || args.sku === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'sku'");
            }
            inputs["capacity"] = args ? args.capacity : undefined;
            inputs["location"] = args ? args.location : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["sku"] = args ? args.sku : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["zoneRedundant"] = args ? args.zoneRedundant : undefined;
            inputs["defaultPrimaryConnectionString"] = undefined /*out*/;
            inputs["defaultPrimaryKey"] = undefined /*out*/;
            inputs["defaultSecondaryConnectionString"] = undefined /*out*/;
            inputs["defaultSecondaryKey"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Namespace.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Namespace resources.
 */
export interface NamespaceState {
    /**
     * Specifies the capacity. When `sku` is `Premium`, capacity can be `1`, `2`, `4` or `8`. When `sku` is `Basic` or `Standard`, capacity can be `0` only.
     */
    readonly capacity?: pulumi.Input<number>;
    /**
     * The primary connection string for the authorization
     * rule `RootManageSharedAccessKey`.
     */
    readonly defaultPrimaryConnectionString?: pulumi.Input<string>;
    /**
     * The primary access key for the authorization rule `RootManageSharedAccessKey`.
     */
    readonly defaultPrimaryKey?: pulumi.Input<string>;
    /**
     * The secondary connection string for the
     * authorization rule `RootManageSharedAccessKey`.
     */
    readonly defaultSecondaryConnectionString?: pulumi.Input<string>;
    /**
     * The secondary access key for the authorization rule `RootManageSharedAccessKey`.
     */
    readonly defaultSecondaryKey?: pulumi.Input<string>;
    /**
     * Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * Specifies the name of the ServiceBus Namespace resource . Changing this forces a
     * new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the resource group in which to
     * create the namespace.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * Defines which tier to use. Options are basic, standard or premium. Changing this forces a new resource to be created.
     */
    readonly sku?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Whether or not this resource is zone redundant. `sku` needs to be `Premium`. Defaults to `false`.
     */
    readonly zoneRedundant?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a Namespace resource.
 */
export interface NamespaceArgs {
    /**
     * Specifies the capacity. When `sku` is `Premium`, capacity can be `1`, `2`, `4` or `8`. When `sku` is `Basic` or `Standard`, capacity can be `0` only.
     */
    readonly capacity?: pulumi.Input<number>;
    /**
     * Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * Specifies the name of the ServiceBus Namespace resource . Changing this forces a
     * new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the resource group in which to
     * create the namespace.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * Defines which tier to use. Options are basic, standard or premium. Changing this forces a new resource to be created.
     */
    readonly sku: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Whether or not this resource is zone redundant. `sku` needs to be `Premium`. Defaults to `false`.
     */
    readonly zoneRedundant?: pulumi.Input<boolean>;
}
