// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a Key Vault Secret.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 *
 * const current = azure.core.getClientConfig({});
 * const exampleResourceGroup = new azure.core.ResourceGroup("exampleResourceGroup", {location: "West Europe"});
 * const exampleKeyVault = new azure.keyvault.KeyVault("exampleKeyVault", {
 *     location: exampleResourceGroup.location,
 *     resourceGroupName: exampleResourceGroup.name,
 *     tenantId: current.then(current => current.tenantId),
 *     skuName: "premium",
 *     softDeleteEnabled: true,
 *     softDeleteRetentionDays: 7,
 *     accessPolicies: [{
 *         tenantId: current.then(current => current.tenantId),
 *         objectId: current.then(current => current.objectId),
 *         keyPermissions: [
 *             "create",
 *             "get",
 *         ],
 *         secretPermissions: [
 *             "set",
 *             "get",
 *             "delete",
 *             "purge",
 *             "recover",
 *         ],
 *     }],
 * });
 * const exampleSecret = new azure.keyvault.Secret("exampleSecret", {
 *     value: "szechuan",
 *     keyVaultId: exampleKeyVault.id,
 * });
 * ```
 *
 * ## Import
 *
 * Key Vault Secrets which are Enabled can be imported using the `resource id`, e.g.
 *
 * ```sh
 *  $ pulumi import azure:keyvault/secret:Secret example "https://example-keyvault.vault.azure.net/secrets/example/fdf067c93bbb4b22bff4d8b7a9a56217"
 * ```
 */
export class Secret extends pulumi.CustomResource {
    /**
     * Get an existing Secret resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecretState, opts?: pulumi.CustomResourceOptions): Secret {
        return new Secret(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure:keyvault/secret:Secret';

    /**
     * Returns true if the given object is an instance of Secret.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Secret {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Secret.__pulumiType;
    }

    /**
     * Specifies the content type for the Key Vault Secret.
     */
    public readonly contentType!: pulumi.Output<string | undefined>;
    /**
     * Expiration UTC datetime (Y-m-d'T'H:M:S'Z').
     */
    public readonly expirationDate!: pulumi.Output<string | undefined>;
    /**
     * The ID of the Key Vault where the Secret should be created.
     */
    public readonly keyVaultId!: pulumi.Output<string>;
    /**
     * Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Key not usable before the provided UTC datetime (Y-m-d'T'H:M:S'Z').
     */
    public readonly notBeforeDate!: pulumi.Output<string | undefined>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * Specifies the value of the Key Vault Secret.
     */
    public readonly value!: pulumi.Output<string>;
    /**
     * The current version of the Key Vault Secret.
     */
    public /*out*/ readonly version!: pulumi.Output<string>;

    /**
     * Create a Secret resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SecretArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SecretArgs | SecretState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as SecretState | undefined;
            inputs["contentType"] = state ? state.contentType : undefined;
            inputs["expirationDate"] = state ? state.expirationDate : undefined;
            inputs["keyVaultId"] = state ? state.keyVaultId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["notBeforeDate"] = state ? state.notBeforeDate : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["value"] = state ? state.value : undefined;
            inputs["version"] = state ? state.version : undefined;
        } else {
            const args = argsOrState as SecretArgs | undefined;
            if ((!args || args.keyVaultId === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'keyVaultId'");
            }
            if ((!args || args.value === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'value'");
            }
            inputs["contentType"] = args ? args.contentType : undefined;
            inputs["expirationDate"] = args ? args.expirationDate : undefined;
            inputs["keyVaultId"] = args ? args.keyVaultId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["notBeforeDate"] = args ? args.notBeforeDate : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["value"] = args ? args.value : undefined;
            inputs["version"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Secret.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Secret resources.
 */
export interface SecretState {
    /**
     * Specifies the content type for the Key Vault Secret.
     */
    readonly contentType?: pulumi.Input<string>;
    /**
     * Expiration UTC datetime (Y-m-d'T'H:M:S'Z').
     */
    readonly expirationDate?: pulumi.Input<string>;
    /**
     * The ID of the Key Vault where the Secret should be created.
     */
    readonly keyVaultId?: pulumi.Input<string>;
    /**
     * Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Key not usable before the provided UTC datetime (Y-m-d'T'H:M:S'Z').
     */
    readonly notBeforeDate?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Specifies the value of the Key Vault Secret.
     */
    readonly value?: pulumi.Input<string>;
    /**
     * The current version of the Key Vault Secret.
     */
    readonly version?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Secret resource.
 */
export interface SecretArgs {
    /**
     * Specifies the content type for the Key Vault Secret.
     */
    readonly contentType?: pulumi.Input<string>;
    /**
     * Expiration UTC datetime (Y-m-d'T'H:M:S'Z').
     */
    readonly expirationDate?: pulumi.Input<string>;
    /**
     * The ID of the Key Vault where the Secret should be created.
     */
    readonly keyVaultId: pulumi.Input<string>;
    /**
     * Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Key not usable before the provided UTC datetime (Y-m-d'T'H:M:S'Z').
     */
    readonly notBeforeDate?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Specifies the value of the Key Vault Secret.
     */
    readonly value: pulumi.Input<string>;
}
