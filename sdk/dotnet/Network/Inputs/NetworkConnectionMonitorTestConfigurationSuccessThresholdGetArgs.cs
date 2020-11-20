// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Network.Inputs
{

    public sealed class NetworkConnectionMonitorTestConfigurationSuccessThresholdGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The maximum percentage of failed checks permitted for a test to be successful.
        /// </summary>
        [Input("checksFailedPercent")]
        public Input<int>? ChecksFailedPercent { get; set; }

        /// <summary>
        /// The maximum round-trip time in milliseconds permitted for a test to be successful.
        /// </summary>
        [Input("roundTripTimeMs")]
        public Input<double>? RoundTripTimeMs { get; set; }

        public NetworkConnectionMonitorTestConfigurationSuccessThresholdGetArgs()
        {
        }
    }
}
