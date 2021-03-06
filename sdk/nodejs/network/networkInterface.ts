// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Manages a Network Interface.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 *
 * const exampleResourceGroup = new azure.core.ResourceGroup("exampleResourceGroup", {location: "West Europe"});
 * const exampleVirtualNetwork = new azure.network.VirtualNetwork("exampleVirtualNetwork", {
 *     addressSpaces: ["10.0.0.0/16"],
 *     location: exampleResourceGroup.location,
 *     resourceGroupName: exampleResourceGroup.name,
 * });
 * const exampleSubnet = new azure.network.Subnet("exampleSubnet", {
 *     resourceGroupName: exampleResourceGroup.name,
 *     virtualNetworkName: exampleVirtualNetwork.name,
 *     addressPrefixes: ["10.0.2.0/24"],
 * });
 * const exampleNetworkInterface = new azure.network.NetworkInterface("exampleNetworkInterface", {
 *     location: exampleResourceGroup.location,
 *     resourceGroupName: exampleResourceGroup.name,
 *     ipConfigurations: [{
 *         name: "internal",
 *         subnetId: exampleSubnet.id,
 *         privateIpAddressAllocation: "Dynamic",
 *     }],
 * });
 * ```
 *
 * ## Import
 *
 * Network Interfaces can be imported using the `resource id`, e.g.
 *
 * ```sh
 *  $ pulumi import azure:network/networkInterface:NetworkInterface example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/networkInterfaces/nic1
 * ```
 */
export class NetworkInterface extends pulumi.CustomResource {
    /**
     * Get an existing NetworkInterface resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkInterfaceState, opts?: pulumi.CustomResourceOptions): NetworkInterface {
        return new NetworkInterface(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure:network/networkInterface:NetworkInterface';

    /**
     * Returns true if the given object is an instance of NetworkInterface.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is NetworkInterface {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === NetworkInterface.__pulumiType;
    }

    /**
     * If the Virtual Machine using this Network Interface is part of an Availability Set, then this list will have the union of all DNS servers from all Network Interfaces that are part of the Availability Set.
     */
    public /*out*/ readonly appliedDnsServers!: pulumi.Output<string[]>;
    /**
     * A list of IP Addresses defining the DNS Servers which should be used for this Network Interface.
     */
    public readonly dnsServers!: pulumi.Output<string[]>;
    /**
     * Should Accelerated Networking be enabled? Defaults to `false`.
     */
    public readonly enableAcceleratedNetworking!: pulumi.Output<boolean | undefined>;
    /**
     * Should IP Forwarding be enabled? Defaults to `false`.
     */
    public readonly enableIpForwarding!: pulumi.Output<boolean | undefined>;
    /**
     * The (relative) DNS Name used for internal communications between Virtual Machines in the same Virtual Network.
     */
    public readonly internalDnsNameLabel!: pulumi.Output<string>;
    /**
     * Even if `internalDnsNameLabel` is not specified, a DNS entry is created for the primary NIC of the VM. This DNS name can be constructed by concatenating the VM name with the value of `internalDomainNameSuffix`.
     */
    public /*out*/ readonly internalDomainNameSuffix!: pulumi.Output<string>;
    /**
     * One or more `ipConfiguration` blocks as defined below.
     */
    public readonly ipConfigurations!: pulumi.Output<outputs.network.NetworkInterfaceIpConfiguration[]>;
    /**
     * The location where the Network Interface should exist. Changing this forces a new resource to be created.
     */
    public readonly location!: pulumi.Output<string>;
    /**
     * The Media Access Control (MAC) Address of the Network Interface.
     */
    public /*out*/ readonly macAddress!: pulumi.Output<string>;
    /**
     * The name of the Network Interface. Changing this forces a new resource to be created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The Static IP Address which should be used.
     */
    public /*out*/ readonly privateIpAddress!: pulumi.Output<string>;
    /**
     * The private IP addresses of the network interface.
     */
    public /*out*/ readonly privateIpAddresses!: pulumi.Output<string[]>;
    /**
     * The name of the Resource Group in which to create the Network Interface. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName!: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * The ID of the Virtual Machine which this Network Interface is connected to.
     */
    public /*out*/ readonly virtualMachineId!: pulumi.Output<string>;

    /**
     * Create a NetworkInterface resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NetworkInterfaceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NetworkInterfaceArgs | NetworkInterfaceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as NetworkInterfaceState | undefined;
            inputs["appliedDnsServers"] = state ? state.appliedDnsServers : undefined;
            inputs["dnsServers"] = state ? state.dnsServers : undefined;
            inputs["enableAcceleratedNetworking"] = state ? state.enableAcceleratedNetworking : undefined;
            inputs["enableIpForwarding"] = state ? state.enableIpForwarding : undefined;
            inputs["internalDnsNameLabel"] = state ? state.internalDnsNameLabel : undefined;
            inputs["internalDomainNameSuffix"] = state ? state.internalDomainNameSuffix : undefined;
            inputs["ipConfigurations"] = state ? state.ipConfigurations : undefined;
            inputs["location"] = state ? state.location : undefined;
            inputs["macAddress"] = state ? state.macAddress : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["privateIpAddress"] = state ? state.privateIpAddress : undefined;
            inputs["privateIpAddresses"] = state ? state.privateIpAddresses : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["virtualMachineId"] = state ? state.virtualMachineId : undefined;
        } else {
            const args = argsOrState as NetworkInterfaceArgs | undefined;
            if ((!args || args.ipConfigurations === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ipConfigurations'");
            }
            if ((!args || args.resourceGroupName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            inputs["dnsServers"] = args ? args.dnsServers : undefined;
            inputs["enableAcceleratedNetworking"] = args ? args.enableAcceleratedNetworking : undefined;
            inputs["enableIpForwarding"] = args ? args.enableIpForwarding : undefined;
            inputs["internalDnsNameLabel"] = args ? args.internalDnsNameLabel : undefined;
            inputs["ipConfigurations"] = args ? args.ipConfigurations : undefined;
            inputs["location"] = args ? args.location : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["appliedDnsServers"] = undefined /*out*/;
            inputs["internalDomainNameSuffix"] = undefined /*out*/;
            inputs["macAddress"] = undefined /*out*/;
            inputs["privateIpAddress"] = undefined /*out*/;
            inputs["privateIpAddresses"] = undefined /*out*/;
            inputs["virtualMachineId"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(NetworkInterface.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering NetworkInterface resources.
 */
export interface NetworkInterfaceState {
    /**
     * If the Virtual Machine using this Network Interface is part of an Availability Set, then this list will have the union of all DNS servers from all Network Interfaces that are part of the Availability Set.
     */
    readonly appliedDnsServers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of IP Addresses defining the DNS Servers which should be used for this Network Interface.
     */
    readonly dnsServers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Should Accelerated Networking be enabled? Defaults to `false`.
     */
    readonly enableAcceleratedNetworking?: pulumi.Input<boolean>;
    /**
     * Should IP Forwarding be enabled? Defaults to `false`.
     */
    readonly enableIpForwarding?: pulumi.Input<boolean>;
    /**
     * The (relative) DNS Name used for internal communications between Virtual Machines in the same Virtual Network.
     */
    readonly internalDnsNameLabel?: pulumi.Input<string>;
    /**
     * Even if `internalDnsNameLabel` is not specified, a DNS entry is created for the primary NIC of the VM. This DNS name can be constructed by concatenating the VM name with the value of `internalDomainNameSuffix`.
     */
    readonly internalDomainNameSuffix?: pulumi.Input<string>;
    /**
     * One or more `ipConfiguration` blocks as defined below.
     */
    readonly ipConfigurations?: pulumi.Input<pulumi.Input<inputs.network.NetworkInterfaceIpConfiguration>[]>;
    /**
     * The location where the Network Interface should exist. Changing this forces a new resource to be created.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * The Media Access Control (MAC) Address of the Network Interface.
     */
    readonly macAddress?: pulumi.Input<string>;
    /**
     * The name of the Network Interface. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The Static IP Address which should be used.
     */
    readonly privateIpAddress?: pulumi.Input<string>;
    /**
     * The private IP addresses of the network interface.
     */
    readonly privateIpAddresses?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the Resource Group in which to create the Network Interface. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The ID of the Virtual Machine which this Network Interface is connected to.
     */
    readonly virtualMachineId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a NetworkInterface resource.
 */
export interface NetworkInterfaceArgs {
    /**
     * A list of IP Addresses defining the DNS Servers which should be used for this Network Interface.
     */
    readonly dnsServers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Should Accelerated Networking be enabled? Defaults to `false`.
     */
    readonly enableAcceleratedNetworking?: pulumi.Input<boolean>;
    /**
     * Should IP Forwarding be enabled? Defaults to `false`.
     */
    readonly enableIpForwarding?: pulumi.Input<boolean>;
    /**
     * The (relative) DNS Name used for internal communications between Virtual Machines in the same Virtual Network.
     */
    readonly internalDnsNameLabel?: pulumi.Input<string>;
    /**
     * One or more `ipConfiguration` blocks as defined below.
     */
    readonly ipConfigurations: pulumi.Input<pulumi.Input<inputs.network.NetworkInterfaceIpConfiguration>[]>;
    /**
     * The location where the Network Interface should exist. Changing this forces a new resource to be created.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * The name of the Network Interface. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The name of the Resource Group in which to create the Network Interface. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
