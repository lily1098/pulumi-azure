// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Network.Inputs
{

    public sealed class NetworkConnectionMonitorEndpointGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IP address or domain name of the Network Connection Monitor endpoint.
        /// </summary>
        [Input("address")]
        public Input<string>? Address { get; set; }

        /// <summary>
        /// A `filter` block as defined below.
        /// </summary>
        [Input("filter")]
        public Input<Inputs.NetworkConnectionMonitorEndpointFilterGetArgs>? Filter { get; set; }

        /// <summary>
        /// The name of the endpoint for the Network Connection Monitor .
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The ID of the Virtual Machine which is used as the endpoint by the Network Connection Monitor.
        /// </summary>
        [Input("virtualMachineId")]
        public Input<string>? VirtualMachineId { get; set; }

        public NetworkConnectionMonitorEndpointGetArgs()
        {
        }
    }
}
