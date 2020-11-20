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
    public sealed class PointToPointVpnGatewayConnectionConfigurationRoutePropagatedRouteTable
    {
        /// <summary>
        /// The list of Virtual Hub Route Table resource id which the routes will be propagated to.
        /// </summary>
        public readonly ImmutableArray<string> Ids;
        /// <summary>
        /// The list of labels to logically group Virtual Hub Route Tables which the routes will be propagated to.
        /// </summary>
        public readonly ImmutableArray<string> Labels;

        [OutputConstructor]
        private PointToPointVpnGatewayConnectionConfigurationRoutePropagatedRouteTable(
            ImmutableArray<string> ids,

            ImmutableArray<string> labels)
        {
            Ids = ids;
            Labels = labels;
        }
    }
}
