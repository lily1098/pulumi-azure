// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages an API Management Service.
 * 
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management.html.markdown.
 */
export class Service extends pulumi.CustomResource {
    /**
     * Get an existing Service resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServiceState, opts?: pulumi.CustomResourceOptions): Service {
        return new Service(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure:apimanagement/service:Service';

    /**
     * Returns true if the given object is an instance of Service.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Service {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Service.__pulumiType;
    }

    /**
     * One or more `additionalLocation` blocks as defined below.
     */
    public readonly additionalLocations!: pulumi.Output<outputs.apimanagement.ServiceAdditionalLocation[] | undefined>;
    /**
     * One or more (up to 10) `certificate` blocks as defined below.
     */
    public readonly certificates!: pulumi.Output<outputs.apimanagement.ServiceCertificate[] | undefined>;
    /**
     * The URL of the Regional Gateway for the API Management Service in the specified region.
     */
    public /*out*/ readonly gatewayRegionalUrl!: pulumi.Output<string>;
    /**
     * The URL of the Gateway for the API Management Service.
     */
    public /*out*/ readonly gatewayUrl!: pulumi.Output<string>;
    /**
     * A `hostnameConfiguration` block as defined below.
     */
    public readonly hostnameConfiguration!: pulumi.Output<outputs.apimanagement.ServiceHostnameConfiguration>;
    /**
     * An `identity` block is documented below.
     */
    public readonly identity!: pulumi.Output<outputs.apimanagement.ServiceIdentity | undefined>;
    /**
     * The Azure location where the API Management Service exists. Changing this forces a new resource to be created.
     */
    public readonly location!: pulumi.Output<string>;
    /**
     * The URL for the Management API associated with this API Management service.
     */
    public /*out*/ readonly managementApiUrl!: pulumi.Output<string>;
    /**
     * The name of the API Management Service. Changing this forces a new resource to be created.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Email address from which the notification will be sent.
     */
    public readonly notificationSenderEmail!: pulumi.Output<string>;
    /**
     * A `policy` block as defined below.
     */
    public readonly policy!: pulumi.Output<outputs.apimanagement.ServicePolicy>;
    /**
     * The URL for the Publisher Portal associated with this API Management service.
     */
    public /*out*/ readonly portalUrl!: pulumi.Output<string>;
    public /*out*/ readonly privateIpAddresses!: pulumi.Output<string[]>;
    /**
     * A `protocols` block as defined below.
     */
    public readonly protocols!: pulumi.Output<outputs.apimanagement.ServiceProtocols>;
    /**
     * Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.
     */
    public /*out*/ readonly publicIpAddresses!: pulumi.Output<string[]>;
    /**
     * The email of publisher/company.
     */
    public readonly publisherEmail!: pulumi.Output<string>;
    /**
     * The name of publisher/company.
     */
    public readonly publisherName!: pulumi.Output<string>;
    /**
     * The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.
     */
    public readonly resourceGroupName!: pulumi.Output<string>;
    /**
     * The URL for the SCM (Source Code Management) Endpoint associated with this API Management service.
     */
    public /*out*/ readonly scmUrl!: pulumi.Output<string>;
    /**
     * A `security` block as defined below.
     */
    public readonly security!: pulumi.Output<outputs.apimanagement.ServiceSecurity>;
    /**
     * A `signIn` block as defined below.
     */
    public readonly signIn!: pulumi.Output<outputs.apimanagement.ServiceSignIn>;
    /**
     * A `signUp` block as defined below.
     */
    public readonly signUp!: pulumi.Output<outputs.apimanagement.ServiceSignUp>;
    /**
     * `skuName` is a string consisting of two parts separated by an underscore(\_). The fist part is the `name`, valid values include: `Consumption`, `Developer`, `Basic`, `Standard` and `Premium`. The second part is the `capacity` (e.g. the number of deployed units of the `sku`), which must be a positive `integer` (e.g. `Developer_1`).
     */
    public readonly skuName!: pulumi.Output<string>;
    /**
     * A mapping of tags assigned to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * A `virtualNetworkConfiguration` block as defined below. Required when `virtualNetworkType` is `External` or `Internal`.
     */
    public readonly virtualNetworkConfiguration!: pulumi.Output<outputs.apimanagement.ServiceVirtualNetworkConfiguration | undefined>;
    /**
     * The type of virtual network you want to use, valid values include: `None`, `External`, `Internal`.
     */
    public readonly virtualNetworkType!: pulumi.Output<string | undefined>;

    /**
     * Create a Service resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ServiceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ServiceArgs | ServiceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ServiceState | undefined;
            inputs["additionalLocations"] = state ? state.additionalLocations : undefined;
            inputs["certificates"] = state ? state.certificates : undefined;
            inputs["gatewayRegionalUrl"] = state ? state.gatewayRegionalUrl : undefined;
            inputs["gatewayUrl"] = state ? state.gatewayUrl : undefined;
            inputs["hostnameConfiguration"] = state ? state.hostnameConfiguration : undefined;
            inputs["identity"] = state ? state.identity : undefined;
            inputs["location"] = state ? state.location : undefined;
            inputs["managementApiUrl"] = state ? state.managementApiUrl : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["notificationSenderEmail"] = state ? state.notificationSenderEmail : undefined;
            inputs["policy"] = state ? state.policy : undefined;
            inputs["portalUrl"] = state ? state.portalUrl : undefined;
            inputs["privateIpAddresses"] = state ? state.privateIpAddresses : undefined;
            inputs["protocols"] = state ? state.protocols : undefined;
            inputs["publicIpAddresses"] = state ? state.publicIpAddresses : undefined;
            inputs["publisherEmail"] = state ? state.publisherEmail : undefined;
            inputs["publisherName"] = state ? state.publisherName : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["scmUrl"] = state ? state.scmUrl : undefined;
            inputs["security"] = state ? state.security : undefined;
            inputs["signIn"] = state ? state.signIn : undefined;
            inputs["signUp"] = state ? state.signUp : undefined;
            inputs["skuName"] = state ? state.skuName : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["virtualNetworkConfiguration"] = state ? state.virtualNetworkConfiguration : undefined;
            inputs["virtualNetworkType"] = state ? state.virtualNetworkType : undefined;
        } else {
            const args = argsOrState as ServiceArgs | undefined;
            if (!args || args.publisherEmail === undefined) {
                throw new Error("Missing required property 'publisherEmail'");
            }
            if (!args || args.publisherName === undefined) {
                throw new Error("Missing required property 'publisherName'");
            }
            if (!args || args.resourceGroupName === undefined) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if (!args || args.skuName === undefined) {
                throw new Error("Missing required property 'skuName'");
            }
            inputs["additionalLocations"] = args ? args.additionalLocations : undefined;
            inputs["certificates"] = args ? args.certificates : undefined;
            inputs["hostnameConfiguration"] = args ? args.hostnameConfiguration : undefined;
            inputs["identity"] = args ? args.identity : undefined;
            inputs["location"] = args ? args.location : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["notificationSenderEmail"] = args ? args.notificationSenderEmail : undefined;
            inputs["policy"] = args ? args.policy : undefined;
            inputs["protocols"] = args ? args.protocols : undefined;
            inputs["publisherEmail"] = args ? args.publisherEmail : undefined;
            inputs["publisherName"] = args ? args.publisherName : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["security"] = args ? args.security : undefined;
            inputs["signIn"] = args ? args.signIn : undefined;
            inputs["signUp"] = args ? args.signUp : undefined;
            inputs["skuName"] = args ? args.skuName : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["virtualNetworkConfiguration"] = args ? args.virtualNetworkConfiguration : undefined;
            inputs["virtualNetworkType"] = args ? args.virtualNetworkType : undefined;
            inputs["gatewayRegionalUrl"] = undefined /*out*/;
            inputs["gatewayUrl"] = undefined /*out*/;
            inputs["managementApiUrl"] = undefined /*out*/;
            inputs["portalUrl"] = undefined /*out*/;
            inputs["privateIpAddresses"] = undefined /*out*/;
            inputs["publicIpAddresses"] = undefined /*out*/;
            inputs["scmUrl"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Service.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Service resources.
 */
export interface ServiceState {
    /**
     * One or more `additionalLocation` blocks as defined below.
     */
    readonly additionalLocations?: pulumi.Input<pulumi.Input<inputs.apimanagement.ServiceAdditionalLocation>[]>;
    /**
     * One or more (up to 10) `certificate` blocks as defined below.
     */
    readonly certificates?: pulumi.Input<pulumi.Input<inputs.apimanagement.ServiceCertificate>[]>;
    /**
     * The URL of the Regional Gateway for the API Management Service in the specified region.
     */
    readonly gatewayRegionalUrl?: pulumi.Input<string>;
    /**
     * The URL of the Gateway for the API Management Service.
     */
    readonly gatewayUrl?: pulumi.Input<string>;
    /**
     * A `hostnameConfiguration` block as defined below.
     */
    readonly hostnameConfiguration?: pulumi.Input<inputs.apimanagement.ServiceHostnameConfiguration>;
    /**
     * An `identity` block is documented below.
     */
    readonly identity?: pulumi.Input<inputs.apimanagement.ServiceIdentity>;
    /**
     * The Azure location where the API Management Service exists. Changing this forces a new resource to be created.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * The URL for the Management API associated with this API Management service.
     */
    readonly managementApiUrl?: pulumi.Input<string>;
    /**
     * The name of the API Management Service. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Email address from which the notification will be sent.
     */
    readonly notificationSenderEmail?: pulumi.Input<string>;
    /**
     * A `policy` block as defined below.
     */
    readonly policy?: pulumi.Input<inputs.apimanagement.ServicePolicy>;
    /**
     * The URL for the Publisher Portal associated with this API Management service.
     */
    readonly portalUrl?: pulumi.Input<string>;
    readonly privateIpAddresses?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A `protocols` block as defined below.
     */
    readonly protocols?: pulumi.Input<inputs.apimanagement.ServiceProtocols>;
    /**
     * Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.
     */
    readonly publicIpAddresses?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The email of publisher/company.
     */
    readonly publisherEmail?: pulumi.Input<string>;
    /**
     * The name of publisher/company.
     */
    readonly publisherName?: pulumi.Input<string>;
    /**
     * The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * The URL for the SCM (Source Code Management) Endpoint associated with this API Management service.
     */
    readonly scmUrl?: pulumi.Input<string>;
    /**
     * A `security` block as defined below.
     */
    readonly security?: pulumi.Input<inputs.apimanagement.ServiceSecurity>;
    /**
     * A `signIn` block as defined below.
     */
    readonly signIn?: pulumi.Input<inputs.apimanagement.ServiceSignIn>;
    /**
     * A `signUp` block as defined below.
     */
    readonly signUp?: pulumi.Input<inputs.apimanagement.ServiceSignUp>;
    /**
     * `skuName` is a string consisting of two parts separated by an underscore(\_). The fist part is the `name`, valid values include: `Consumption`, `Developer`, `Basic`, `Standard` and `Premium`. The second part is the `capacity` (e.g. the number of deployed units of the `sku`), which must be a positive `integer` (e.g. `Developer_1`).
     */
    readonly skuName?: pulumi.Input<string>;
    /**
     * A mapping of tags assigned to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * A `virtualNetworkConfiguration` block as defined below. Required when `virtualNetworkType` is `External` or `Internal`.
     */
    readonly virtualNetworkConfiguration?: pulumi.Input<inputs.apimanagement.ServiceVirtualNetworkConfiguration>;
    /**
     * The type of virtual network you want to use, valid values include: `None`, `External`, `Internal`.
     */
    readonly virtualNetworkType?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Service resource.
 */
export interface ServiceArgs {
    /**
     * One or more `additionalLocation` blocks as defined below.
     */
    readonly additionalLocations?: pulumi.Input<pulumi.Input<inputs.apimanagement.ServiceAdditionalLocation>[]>;
    /**
     * One or more (up to 10) `certificate` blocks as defined below.
     */
    readonly certificates?: pulumi.Input<pulumi.Input<inputs.apimanagement.ServiceCertificate>[]>;
    /**
     * A `hostnameConfiguration` block as defined below.
     */
    readonly hostnameConfiguration?: pulumi.Input<inputs.apimanagement.ServiceHostnameConfiguration>;
    /**
     * An `identity` block is documented below.
     */
    readonly identity?: pulumi.Input<inputs.apimanagement.ServiceIdentity>;
    /**
     * The Azure location where the API Management Service exists. Changing this forces a new resource to be created.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * The name of the API Management Service. Changing this forces a new resource to be created.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Email address from which the notification will be sent.
     */
    readonly notificationSenderEmail?: pulumi.Input<string>;
    /**
     * A `policy` block as defined below.
     */
    readonly policy?: pulumi.Input<inputs.apimanagement.ServicePolicy>;
    /**
     * A `protocols` block as defined below.
     */
    readonly protocols?: pulumi.Input<inputs.apimanagement.ServiceProtocols>;
    /**
     * The email of publisher/company.
     */
    readonly publisherEmail: pulumi.Input<string>;
    /**
     * The name of publisher/company.
     */
    readonly publisherName: pulumi.Input<string>;
    /**
     * The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.
     */
    readonly resourceGroupName: pulumi.Input<string>;
    /**
     * A `security` block as defined below.
     */
    readonly security?: pulumi.Input<inputs.apimanagement.ServiceSecurity>;
    /**
     * A `signIn` block as defined below.
     */
    readonly signIn?: pulumi.Input<inputs.apimanagement.ServiceSignIn>;
    /**
     * A `signUp` block as defined below.
     */
    readonly signUp?: pulumi.Input<inputs.apimanagement.ServiceSignUp>;
    /**
     * `skuName` is a string consisting of two parts separated by an underscore(\_). The fist part is the `name`, valid values include: `Consumption`, `Developer`, `Basic`, `Standard` and `Premium`. The second part is the `capacity` (e.g. the number of deployed units of the `sku`), which must be a positive `integer` (e.g. `Developer_1`).
     */
    readonly skuName: pulumi.Input<string>;
    /**
     * A mapping of tags assigned to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * A `virtualNetworkConfiguration` block as defined below. Required when `virtualNetworkType` is `External` or `Internal`.
     */
    readonly virtualNetworkConfiguration?: pulumi.Input<inputs.apimanagement.ServiceVirtualNetworkConfiguration>;
    /**
     * The type of virtual network you want to use, valid values include: `None`, `External`, `Internal`.
     */
    readonly virtualNetworkType?: pulumi.Input<string>;
}
