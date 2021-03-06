// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Use this data source to access information about an existing certificate in a Batch Account.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as azure from "@pulumi/azure";
 *
 * const example = azure.batch.getCertificate({
 *     name: "SHA1-42C107874FD0E4A9583292A2F1098E8FE4B2EDDA",
 *     accountName: "examplebatchaccount",
 *     resourceGroupName: "example",
 * });
 * export const thumbprint = example.then(example => example.thumbprint);
 * ```
 */
export function getCertificate(args: GetCertificateArgs, opts?: pulumi.InvokeOptions): Promise<GetCertificateResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("azure:batch/getCertificate:getCertificate", {
        "accountName": args.accountName,
        "name": args.name,
        "resourceGroupName": args.resourceGroupName,
    }, opts);
}

/**
 * A collection of arguments for invoking getCertificate.
 */
export interface GetCertificateArgs {
    /**
     * The name of the Batch account.
     */
    readonly accountName: string;
    /**
     * The name of the Batch certificate.
     */
    readonly name: string;
    /**
     * The Name of the Resource Group where this Batch account exists.
     */
    readonly resourceGroupName: string;
}

/**
 * A collection of values returned by getCertificate.
 */
export interface GetCertificateResult {
    readonly accountName: string;
    /**
     * The format of the certificate, such as `Cer` or `Pfx`.
     */
    readonly format: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly name: string;
    /**
     * The public key of the certificate.
     */
    readonly publicData: string;
    readonly resourceGroupName: string;
    /**
     * The thumbprint of the certificate.
     */
    readonly thumbprint: string;
    /**
     * The algorithm of the certificate thumbprint.
     */
    readonly thumbprintAlgorithm: string;
}
