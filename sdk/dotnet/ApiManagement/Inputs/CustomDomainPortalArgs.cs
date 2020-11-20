// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.ApiManagement.Inputs
{

    public sealed class CustomDomainPortalArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Base64 Encoded Certificate. (Mutually exlusive with `key_vault_id`.)
        /// </summary>
        [Input("certificate")]
        public Input<string>? Certificate { get; set; }

        /// <summary>
        /// The password associated with the certificate provided above.
        /// </summary>
        [Input("certificatePassword")]
        public Input<string>? CertificatePassword { get; set; }

        /// <summary>
        /// The Hostname to use for the corresponding endpoint.
        /// </summary>
        [Input("hostName", required: true)]
        public Input<string> HostName { get; set; } = null!;

        /// <summary>
        /// The ID of the Key Vault Secret containing the SSL Certificate, which must be should be of the type application/x-pkcs12.
        /// </summary>
        [Input("keyVaultId")]
        public Input<string>? KeyVaultId { get; set; }

        /// <summary>
        /// Should Client Certificate Negotiation be enabled for this Hostname? Defaults to false.
        /// </summary>
        [Input("negotiateClientCertificate")]
        public Input<bool>? NegotiateClientCertificate { get; set; }

        public CustomDomainPortalArgs()
        {
        }
    }
}
