// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Network.Inputs
{

    public sealed class ExpressRouteCircuitPeeringIpv6MicrosoftPeeringArgs : Pulumi.ResourceArgs
    {
        [Input("advertisedPublicPrefixes")]
        private InputList<string>? _advertisedPublicPrefixes;

        /// <summary>
        /// A list of Advertised Public Prefixes.
        /// </summary>
        public InputList<string> AdvertisedPublicPrefixes
        {
            get => _advertisedPublicPrefixes ?? (_advertisedPublicPrefixes = new InputList<string>());
            set => _advertisedPublicPrefixes = value;
        }

        /// <summary>
        /// The CustomerASN of the peering.
        /// </summary>
        [Input("customerAsn")]
        public Input<int>? CustomerAsn { get; set; }

        /// <summary>
        /// The Routing Registry against which the AS number and prefixes are registered. For example:  `ARIN`, `RIPE`, `AFRINIC` etc.
        /// </summary>
        [Input("routingRegistryName")]
        public Input<string>? RoutingRegistryName { get; set; }

        public ExpressRouteCircuitPeeringIpv6MicrosoftPeeringArgs()
        {
        }
    }
}