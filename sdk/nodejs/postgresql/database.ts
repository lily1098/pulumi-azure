// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a PostgreSQL Database within a PostgreSQL Server
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 * 
 * const testResourceGroup = new azure.core.ResourceGroup("test", {
 *     location: "West Europe",
 * });
 * const testServer = new azure.postgresql.Server("test", {
 *     administratorLogin: "psqladminun",
 *     administratorLoginPassword: "H@Sh1CoR3!",
 *     location: testResourceGroup.location,
 *     resourceGroupName: testResourceGroup.name,
 *     sku: {
 *         capacity: 2,
 *         family: "Gen4",
 *         name: "B_Gen4_2",
 *         tier: "Basic",
 *     },
 *     sslEnforcement: "Enabled",
 *     storageProfile: {
 *         backupRetentionDays: 7,
 *         geoRedundantBackup: "Disabled",
 *         storageMb: 5120,
 *     },
 *     version: "9.5",
 * });
 * const testDatabase = new azure.postgresql.Database("test", {
 *     charset: "UTF8",
 *     collation: "English_United States.1252",
 *     resourceGroupName: testResourceGroup.name,
 *     serverName: testServer.name,
 * });
 * ```
 */
export class Database extends pulumi.CustomResource {
    /**
     * Get an existing Database resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseState, opts?: pulumi.CustomResourceOptions): Database {
        return new Database(name, <any>state, { ...opts, id: id });
    }

    /**
     * Specifies the Charset for the PostgreSQL Database, which needs [to be a valid PostgreSQL Charset](https://www.postgresql.org/docs/current/static/multibyte.html). Changing this forces a new resource to be created.
     */
    public readonly charset: pulumi.Output<string>;
    /**
     * Specifies the Collation for the PostgreSQL Database, which needs [to be a valid PostgreSQL Collation](https://www.postgresql.org/docs/current/static/collation.html). Note that Microsoft uses different [notation](https://msdn.microsoft.com/library/windows/desktop/dd373814.aspx) - en-US instead of en_US. Changing this forces a new resource to be created.
     */
    public readonly collation: pulumi.Output<string>;
    /**
     * Specifies the name of the PostgreSQL Database, which needs [to be a valid PostgreSQL identifier](https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS). Changing this forces a
     * new resource to be created.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName: pulumi.Output<string>;
    /**
     * Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.
     */
    public readonly serverName: pulumi.Output<string>;

    /**
     * Create a Database resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DatabaseArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DatabaseArgs | DatabaseState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: DatabaseState = argsOrState as DatabaseState | undefined;
            inputs["charset"] = state ? state.charset : undefined;
            inputs["collation"] = state ? state.collation : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["serverName"] = state ? state.serverName : undefined;
        } else {
            const args = argsOrState as DatabaseArgs | undefined;
            if (!args || args.charset === undefined) {
                throw new Error("Missing required property 'charset'");
            }
            if (!args || args.collation === undefined) {
                throw new Error("Missing required property 'collation'");
            }
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if (!args || args.serverName === undefined) {
                throw new Error("Missing required property 'serverName'");
            }
            inputs["charset"] = args ? args.charset : undefined;
            inputs["collation"] = args ? args.collation : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["serverName"] = args ? args.serverName : undefined;
        }
        super("azure:postgresql/database:Database", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Database resources.
 */
export interface DatabaseState {
    /**
     * Specifies the Charset for the PostgreSQL Database, which needs [to be a valid PostgreSQL Charset](https://www.postgresql.org/docs/current/static/multibyte.html). Changing this forces a new resource to be created.
     */
    readonly charset?: pulumi.Input<string>;
    /**
     * Specifies the Collation for the PostgreSQL Database, which needs [to be a valid PostgreSQL Collation](https://www.postgresql.org/docs/current/static/collation.html). Note that Microsoft uses different [notation](https://msdn.microsoft.com/library/windows/desktop/dd373814.aspx) - en-US instead of en_US. Changing this forces a new resource to be created.
     */
    readonly collation?: pulumi.Input<string>;
    /**
     * Specifies the name of the PostgreSQL Database, which needs [to be a valid PostgreSQL identifier](https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS). Changing this forces a
     * new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.
     */
    readonly serverName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Database resource.
 */
export interface DatabaseArgs {
    /**
     * Specifies the Charset for the PostgreSQL Database, which needs [to be a valid PostgreSQL Charset](https://www.postgresql.org/docs/current/static/multibyte.html). Changing this forces a new resource to be created.
     */
    readonly charset: pulumi.Input<string>;
    /**
     * Specifies the Collation for the PostgreSQL Database, which needs [to be a valid PostgreSQL Collation](https://www.postgresql.org/docs/current/static/collation.html). Note that Microsoft uses different [notation](https://msdn.microsoft.com/library/windows/desktop/dd373814.aspx) - en-US instead of en_US. Changing this forces a new resource to be created.
     */
    readonly collation: pulumi.Input<string>;
    /**
     * Specifies the name of the PostgreSQL Database, which needs [to be a valid PostgreSQL identifier](https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS). Changing this forces a
     * new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.
     */
    readonly serverName: pulumi.Input<string>;
}
