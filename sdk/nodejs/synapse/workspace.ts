// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Manages a Synapse Workspace.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 *
 * const exampleResourceGroup = new azure.core.ResourceGroup("exampleResourceGroup", {location: "West Europe"});
 * const exampleAccount = new azure.storage.Account("exampleAccount", {
 *     resourceGroupName: exampleResourceGroup.name,
 *     location: exampleResourceGroup.location,
 *     accountTier: "Standard",
 *     accountReplicationType: "LRS",
 *     accountKind: "StorageV2",
 *     isHnsEnabled: "true",
 * });
 * const exampleDataLakeGen2Filesystem = new azure.storage.DataLakeGen2Filesystem("exampleDataLakeGen2Filesystem", {storageAccountId: exampleAccount.id});
 * const exampleWorkspace = new azure.synapse.Workspace("exampleWorkspace", {
 *     resourceGroupName: exampleResourceGroup.name,
 *     location: exampleResourceGroup.location,
 *     storageDataLakeGen2FilesystemId: exampleDataLakeGen2Filesystem.id,
 *     sqlAdministratorLogin: "sqladminuser",
 *     sqlAdministratorLoginPassword: "H@Sh1CoR3!",
 *     aadAdmin: {
 *         login: "AzureAD Admin",
 *         objectId: "00000000-0000-0000-0000-000000000000",
 *         tenantId: "00000000-0000-0000-0000-000000000000",
 *     },
 *     tags: {
 *         Env: "production",
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * Synapse Workspace can be imported using the `resource id`, e.g.
 *
 * ```sh
 *  $ pulumi import azure:synapse/workspace:Workspace example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Synapse/workspaces/workspace1
 * ```
 */
export class Workspace extends pulumi.CustomResource {
    /**
     * Get an existing Workspace resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WorkspaceState, opts?: pulumi.CustomResourceOptions): Workspace {
        return new Workspace(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure:synapse/workspace:Workspace';

    /**
     * Returns true if the given object is an instance of Workspace.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Workspace {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Workspace.__pulumiType;
    }

    /**
     * An `aadAdmin` block as defined below.
     */
    public readonly aadAdmin!: pulumi.Output<outputs.synapse.WorkspaceAadAdmin>;
    /**
     * A list of Connectivity endpoints for this Synapse Workspace.
     */
    public /*out*/ readonly connectivityEndpoints!: pulumi.Output<{[key: string]: string}>;
    /**
     * An `identity` block as defined below, which contains the Managed Service Identity information for this Synapse Workspace.
     */
    public /*out*/ readonly identities!: pulumi.Output<outputs.synapse.WorkspaceIdentity[]>;
    /**
     * Specifies the Azure Region where the synapse Workspace should exist. Changing this forces a new resource to be created.
     */
    public readonly location!: pulumi.Output<string>;
    /**
     * Workspace managed resource group.
     */
    public /*out*/ readonly managedResourceGroupName!: pulumi.Output<string>;
    /**
     * Is Virtual Network enabled for all computes in this workspace. Changing this forces a new resource to be created.
     */
    public readonly managedVirtualNetworkEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * Specifies the name which should be used for this synapse Workspace. Changing this forces a new resource to be created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Specifies the name of the Resource Group where the synapse Workspace should exist. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName!: pulumi.Output<string>;
    /**
     * Specifies The Login Name of the SQL administrator. Changing this forces a new resource to be created.
     */
    public readonly sqlAdministratorLogin!: pulumi.Output<string>;
    /**
     * The Password associated with the `sqlAdministratorLogin` for the SQL administrator.
     */
    public readonly sqlAdministratorLoginPassword!: pulumi.Output<string>;
    /**
     * Specifies the ID of storage data lake gen2 filesystem resource. Changing this forces a new resource to be created.
     */
    public readonly storageDataLakeGen2FilesystemId!: pulumi.Output<string>;
    /**
     * A mapping of tags which should be assigned to the Synapse Workspace.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;

    /**
     * Create a Workspace resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: WorkspaceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: WorkspaceArgs | WorkspaceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as WorkspaceState | undefined;
            inputs["aadAdmin"] = state ? state.aadAdmin : undefined;
            inputs["connectivityEndpoints"] = state ? state.connectivityEndpoints : undefined;
            inputs["identities"] = state ? state.identities : undefined;
            inputs["location"] = state ? state.location : undefined;
            inputs["managedResourceGroupName"] = state ? state.managedResourceGroupName : undefined;
            inputs["managedVirtualNetworkEnabled"] = state ? state.managedVirtualNetworkEnabled : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["sqlAdministratorLogin"] = state ? state.sqlAdministratorLogin : undefined;
            inputs["sqlAdministratorLoginPassword"] = state ? state.sqlAdministratorLoginPassword : undefined;
            inputs["storageDataLakeGen2FilesystemId"] = state ? state.storageDataLakeGen2FilesystemId : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as WorkspaceArgs | undefined;
            if ((!args || args.resourceGroupName === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if ((!args || args.sqlAdministratorLogin === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'sqlAdministratorLogin'");
            }
            if ((!args || args.sqlAdministratorLoginPassword === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'sqlAdministratorLoginPassword'");
            }
            if ((!args || args.storageDataLakeGen2FilesystemId === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'storageDataLakeGen2FilesystemId'");
            }
            inputs["aadAdmin"] = args ? args.aadAdmin : undefined;
            inputs["location"] = args ? args.location : undefined;
            inputs["managedVirtualNetworkEnabled"] = args ? args.managedVirtualNetworkEnabled : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["sqlAdministratorLogin"] = args ? args.sqlAdministratorLogin : undefined;
            inputs["sqlAdministratorLoginPassword"] = args ? args.sqlAdministratorLoginPassword : undefined;
            inputs["storageDataLakeGen2FilesystemId"] = args ? args.storageDataLakeGen2FilesystemId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["connectivityEndpoints"] = undefined /*out*/;
            inputs["identities"] = undefined /*out*/;
            inputs["managedResourceGroupName"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Workspace.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Workspace resources.
 */
export interface WorkspaceState {
    /**
     * An `aadAdmin` block as defined below.
     */
    readonly aadAdmin?: pulumi.Input<inputs.synapse.WorkspaceAadAdmin>;
    /**
     * A list of Connectivity endpoints for this Synapse Workspace.
     */
    readonly connectivityEndpoints?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * An `identity` block as defined below, which contains the Managed Service Identity information for this Synapse Workspace.
     */
    readonly identities?: pulumi.Input<pulumi.Input<inputs.synapse.WorkspaceIdentity>[]>;
    /**
     * Specifies the Azure Region where the synapse Workspace should exist. Changing this forces a new resource to be created.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * Workspace managed resource group.
     */
    readonly managedResourceGroupName?: pulumi.Input<string>;
    /**
     * Is Virtual Network enabled for all computes in this workspace. Changing this forces a new resource to be created.
     */
    readonly managedVirtualNetworkEnabled?: pulumi.Input<boolean>;
    /**
     * Specifies the name which should be used for this synapse Workspace. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specifies the name of the Resource Group where the synapse Workspace should exist. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * Specifies The Login Name of the SQL administrator. Changing this forces a new resource to be created.
     */
    readonly sqlAdministratorLogin?: pulumi.Input<string>;
    /**
     * The Password associated with the `sqlAdministratorLogin` for the SQL administrator.
     */
    readonly sqlAdministratorLoginPassword?: pulumi.Input<string>;
    /**
     * Specifies the ID of storage data lake gen2 filesystem resource. Changing this forces a new resource to be created.
     */
    readonly storageDataLakeGen2FilesystemId?: pulumi.Input<string>;
    /**
     * A mapping of tags which should be assigned to the Synapse Workspace.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The set of arguments for constructing a Workspace resource.
 */
export interface WorkspaceArgs {
    /**
     * An `aadAdmin` block as defined below.
     */
    readonly aadAdmin?: pulumi.Input<inputs.synapse.WorkspaceAadAdmin>;
    /**
     * Specifies the Azure Region where the synapse Workspace should exist. Changing this forces a new resource to be created.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * Is Virtual Network enabled for all computes in this workspace. Changing this forces a new resource to be created.
     */
    readonly managedVirtualNetworkEnabled?: pulumi.Input<boolean>;
    /**
     * Specifies the name which should be used for this synapse Workspace. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specifies the name of the Resource Group where the synapse Workspace should exist. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * Specifies The Login Name of the SQL administrator. Changing this forces a new resource to be created.
     */
    readonly sqlAdministratorLogin: pulumi.Input<string>;
    /**
     * The Password associated with the `sqlAdministratorLogin` for the SQL administrator.
     */
    readonly sqlAdministratorLoginPassword: pulumi.Input<string>;
    /**
     * Specifies the ID of storage data lake gen2 filesystem resource. Changing this forces a new resource to be created.
     */
    readonly storageDataLakeGen2FilesystemId: pulumi.Input<string>;
    /**
     * A mapping of tags which should be assigned to the Synapse Workspace.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
