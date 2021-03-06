// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Network.Outputs
{

    [OutputType]
    public sealed class NetworkConnectionMonitorEndpoint
    {
        /// <summary>
        /// The IP address or domain name of the Network Connection Monitor endpoint.
        /// </summary>
        public readonly string? Address;
        /// <summary>
        /// A `filter` block as defined below.
        /// </summary>
        public readonly Outputs.NetworkConnectionMonitorEndpointFilter? Filter;
        /// <summary>
        /// The name of the endpoint for the Network Connection Monitor .
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The ID of the Virtual Machine which is used as the endpoint by the Network Connection Monitor.
        /// </summary>
        public readonly string? VirtualMachineId;

        [OutputConstructor]
        private NetworkConnectionMonitorEndpoint(
            string? address,

            Outputs.NetworkConnectionMonitorEndpointFilter? filter,

            string name,

            string? virtualMachineId)
        {
            Address = address;
            Filter = filter;
            Name = name;
            VirtualMachineId = virtualMachineId;
        }
    }
}
