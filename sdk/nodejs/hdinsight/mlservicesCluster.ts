// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Manages a HDInsight ML Services Cluster.
 *
 * !> **Note:** [HDInsight 3.6 is deprecated and will be retired on 2020-12-31 - HDInsight 4.0 no longer supports ML Services Clusters](https://docs.microsoft.com/en-us/azure/hdinsight/hdinsight-component-versioning#available-versions) - as such this resource is deprecated and will be removed in the next major version of the Provider.
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
 * });
 * const exampleContainer = new azure.storage.Container("exampleContainer", {
 *     storageAccountName: exampleAccount.name,
 *     containerAccessType: "private",
 * });
 * const exampleMLServicesCluster = new azure.hdinsight.MLServicesCluster("exampleMLServicesCluster", {
 *     resourceGroupName: exampleResourceGroup.name,
 *     location: exampleResourceGroup.location,
 *     clusterVersion: "3.6",
 *     tier: "Standard",
 *     rstudio: true,
 *     gateway: {
 *         enabled: true,
 *         username: "acctestusrgw",
 *         password: "Password123!",
 *     },
 *     storageAccounts: [{
 *         storageContainerId: exampleContainer.id,
 *         storageAccountKey: exampleAccount.primaryAccessKey,
 *         isDefault: true,
 *     }],
 *     roles: {
 *         headNode: {
 *             vmSize: "Standard_D3_v2",
 *             username: "acctestusrvm",
 *             password: "AccTestvdSC4daf986!",
 *         },
 *         workerNode: {
 *             vmSize: "Standard_D4_V2",
 *             username: "acctestusrvm",
 *             password: "AccTestvdSC4daf986!",
 *             targetInstanceCount: 3,
 *         },
 *         zookeeperNode: {
 *             vmSize: "Standard_D3_v2",
 *             username: "acctestusrvm",
 *             password: "AccTestvdSC4daf986!",
 *         },
 *         edgeNode: {
 *             vmSize: "Standard_D3_v2",
 *             username: "acctestusrvm",
 *             password: "AccTestvdSC4daf986!",
 *         },
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * HDInsight ML Services Clusters can be imported using the `resource id`, e.g.
 *
 * ```sh
 *  $ pulumi import azure:hdinsight/mLServicesCluster:MLServicesCluster example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.HDInsight/clusters/cluster1
 * ```
 */
export class MLServicesCluster extends pulumi.CustomResource {
    /**
     * Get an existing MLServicesCluster resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MLServicesClusterState, opts?: pulumi.CustomResourceOptions): MLServicesCluster {
        return new MLServicesCluster(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure:hdinsight/mLServicesCluster:MLServicesCluster';

    /**
     * Returns true if the given object is an instance of MLServicesCluster.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MLServicesCluster {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MLServicesCluster.__pulumiType;
    }

    /**
     * Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
     */
    public readonly clusterVersion!: pulumi.Output<string>;
    /**
     * The SSH Connectivity Endpoint for the Edge Node of the HDInsight ML Cluster.
     */
    public /*out*/ readonly edgeSshEndpoint!: pulumi.Output<string>;
    /**
     * A `gateway` block as defined below.
     */
    public readonly gateway!: pulumi.Output<outputs.hdinsight.MLServicesClusterGateway>;
    /**
     * The HTTPS Connectivity Endpoint for this HDInsight ML Services Cluster.
     */
    public /*out*/ readonly httpsEndpoint!: pulumi.Output<string>;
    /**
     * Specifies the Azure Region which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.
     */
    public readonly location!: pulumi.Output<string>;
    /**
     * Specifies the name for this HDInsight ML Services Cluster. Changing this forces a new resource to be created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Specifies the name of the Resource Group in which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName!: pulumi.Output<string>;
    /**
     * A `roles` block as defined below.
     */
    public readonly roles!: pulumi.Output<outputs.hdinsight.MLServicesClusterRoles>;
    /**
     * Should R Studio community edition for ML Services be installed? Changing this forces a new resource to be created.
     */
    public readonly rstudio!: pulumi.Output<boolean>;
    /**
     * The SSH Connectivity Endpoint for this HDInsight ML Services Cluster.
     */
    public /*out*/ readonly sshEndpoint!: pulumi.Output<string>;
    /**
     * One or more `storageAccount` block as defined below.
     */
    public readonly storageAccounts!: pulumi.Output<outputs.hdinsight.MLServicesClusterStorageAccount[] | undefined>;
    /**
     * A map of Tags which should be assigned to this HDInsight ML Services Cluster.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * Specifies the Tier which should be used for this HDInsight ML Services Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
     */
    public readonly tier!: pulumi.Output<string>;
    public readonly tlsMinVersion!: pulumi.Output<string | undefined>;

    /**
     * Create a MLServicesCluster resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MLServicesClusterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MLServicesClusterArgs | MLServicesClusterState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as MLServicesClusterState | undefined;
            inputs["clusterVersion"] = state ? state.clusterVersion : undefined;
            inputs["edgeSshEndpoint"] = state ? state.edgeSshEndpoint : undefined;
            inputs["gateway"] = state ? state.gateway : undefined;
            inputs["httpsEndpoint"] = state ? state.httpsEndpoint : undefined;
            inputs["location"] = state ? state.location : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["roles"] = state ? state.roles : undefined;
            inputs["rstudio"] = state ? state.rstudio : undefined;
            inputs["sshEndpoint"] = state ? state.sshEndpoint : undefined;
            inputs["storageAccounts"] = state ? state.storageAccounts : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["tier"] = state ? state.tier : undefined;
            inputs["tlsMinVersion"] = state ? state.tlsMinVersion : undefined;
        } else {
            const args = argsOrState as MLServicesClusterArgs | undefined;
            if ((!args || args.clusterVersion === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'clusterVersion'");
            }
            if ((!args || args.gateway === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'gateway'");
            }
            if ((!args || args.resourceGroupName === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if ((!args || args.roles === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'roles'");
            }
            if ((!args || args.rstudio === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'rstudio'");
            }
            if ((!args || args.tier === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'tier'");
            }
            inputs["clusterVersion"] = args ? args.clusterVersion : undefined;
            inputs["gateway"] = args ? args.gateway : undefined;
            inputs["location"] = args ? args.location : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["roles"] = args ? args.roles : undefined;
            inputs["rstudio"] = args ? args.rstudio : undefined;
            inputs["storageAccounts"] = args ? args.storageAccounts : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["tier"] = args ? args.tier : undefined;
            inputs["tlsMinVersion"] = args ? args.tlsMinVersion : undefined;
            inputs["edgeSshEndpoint"] = undefined /*out*/;
            inputs["httpsEndpoint"] = undefined /*out*/;
            inputs["sshEndpoint"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(MLServicesCluster.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MLServicesCluster resources.
 */
export interface MLServicesClusterState {
    /**
     * Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
     */
    readonly clusterVersion?: pulumi.Input<string>;
    /**
     * The SSH Connectivity Endpoint for the Edge Node of the HDInsight ML Cluster.
     */
    readonly edgeSshEndpoint?: pulumi.Input<string>;
    /**
     * A `gateway` block as defined below.
     */
    readonly gateway?: pulumi.Input<inputs.hdinsight.MLServicesClusterGateway>;
    /**
     * The HTTPS Connectivity Endpoint for this HDInsight ML Services Cluster.
     */
    readonly httpsEndpoint?: pulumi.Input<string>;
    /**
     * Specifies the Azure Region which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * Specifies the name for this HDInsight ML Services Cluster. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specifies the name of the Resource Group in which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * A `roles` block as defined below.
     */
    readonly roles?: pulumi.Input<inputs.hdinsight.MLServicesClusterRoles>;
    /**
     * Should R Studio community edition for ML Services be installed? Changing this forces a new resource to be created.
     */
    readonly rstudio?: pulumi.Input<boolean>;
    /**
     * The SSH Connectivity Endpoint for this HDInsight ML Services Cluster.
     */
    readonly sshEndpoint?: pulumi.Input<string>;
    /**
     * One or more `storageAccount` block as defined below.
     */
    readonly storageAccounts?: pulumi.Input<pulumi.Input<inputs.hdinsight.MLServicesClusterStorageAccount>[]>;
    /**
     * A map of Tags which should be assigned to this HDInsight ML Services Cluster.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Specifies the Tier which should be used for this HDInsight ML Services Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
     */
    readonly tier?: pulumi.Input<string>;
    readonly tlsMinVersion?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a MLServicesCluster resource.
 */
export interface MLServicesClusterArgs {
    /**
     * Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
     */
    readonly clusterVersion: pulumi.Input<string>;
    /**
     * A `gateway` block as defined below.
     */
    readonly gateway: pulumi.Input<inputs.hdinsight.MLServicesClusterGateway>;
    /**
     * Specifies the Azure Region which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * Specifies the name for this HDInsight ML Services Cluster. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specifies the name of the Resource Group in which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * A `roles` block as defined below.
     */
    readonly roles: pulumi.Input<inputs.hdinsight.MLServicesClusterRoles>;
    /**
     * Should R Studio community edition for ML Services be installed? Changing this forces a new resource to be created.
     */
    readonly rstudio: pulumi.Input<boolean>;
    /**
     * One or more `storageAccount` block as defined below.
     */
    readonly storageAccounts?: pulumi.Input<pulumi.Input<inputs.hdinsight.MLServicesClusterStorageAccount>[]>;
    /**
     * A map of Tags which should be assigned to this HDInsight ML Services Cluster.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Specifies the Tier which should be used for this HDInsight ML Services Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
     */
    readonly tier: pulumi.Input<string>;
    readonly tlsMinVersion?: pulumi.Input<string>;
}
