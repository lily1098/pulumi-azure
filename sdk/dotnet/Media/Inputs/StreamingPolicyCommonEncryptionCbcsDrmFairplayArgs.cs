// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Media.Inputs
{

    public sealed class StreamingPolicyCommonEncryptionCbcsDrmFairplayArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// All license to be persistent or not. Changing this forces a new Streaming Policy to be created.
        /// </summary>
        [Input("allowPersistentLicense")]
        public Input<bool>? AllowPersistentLicense { get; set; }

        /// <summary>
        /// Template for the URL of the custom service delivering licenses to end user players. Not required when using Azure Media Services for issuing licenses. The template supports replaceable tokens that the service will update at runtime with the value specific to the request. The currently supported token values are `{AlternativeMediaId}`, which is replaced with the value of `StreamingLocatorId.AlternativeMediaId`, and `{ContentKeyId}`, which is replaced with the value of identifier of the key being requested. Changing this forces a new Streaming Policy to be created.
        /// </summary>
        [Input("customLicenseAcquisitionUrlTemplate")]
        public Input<string>? CustomLicenseAcquisitionUrlTemplate { get; set; }

        public StreamingPolicyCommonEncryptionCbcsDrmFairplayArgs()
        {
        }
    }
}