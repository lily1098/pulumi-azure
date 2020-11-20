// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Network
{
    /// <summary>
    /// Manages a Bgp Connection for a Virtual Hub.
    /// </summary>
    public partial class BgpConnection : Pulumi.CustomResource
    {
        /// <summary>
        /// The name which should be used for this Virtual Hub Bgp Connection. Changing this forces a new resource to be created.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The peer autonomous system number for the Virtual Hub Bgp Connection. Changing this forces a new resource to be created.
        /// </summary>
        [Output("peerAsn")]
        public Output<int> PeerAsn { get; private set; } = null!;

        /// <summary>
        /// The peer ip address for the Virtual Hub Bgp Connection. Changing this forces a new resource to be created.
        /// </summary>
        [Output("peerIp")]
        public Output<string> PeerIp { get; private set; } = null!;

        /// <summary>
        /// The ID of the Virtual Hub within which this Bgp connection should be created. Changing this forces a new resource to be created.
        /// </summary>
        [Output("virtualHubId")]
        public Output<string> VirtualHubId { get; private set; } = null!;


        /// <summary>
        /// Create a BgpConnection resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BgpConnection(string name, BgpConnectionArgs args, CustomResourceOptions? options = null)
            : base("azure:network/bgpConnection:BgpConnection", name, args ?? new BgpConnectionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private BgpConnection(string name, Input<string> id, BgpConnectionState? state = null, CustomResourceOptions? options = null)
            : base("azure:network/bgpConnection:BgpConnection", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing BgpConnection resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BgpConnection Get(string name, Input<string> id, BgpConnectionState? state = null, CustomResourceOptions? options = null)
        {
            return new BgpConnection(name, id, state, options);
        }
    }

    public sealed class BgpConnectionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name which should be used for this Virtual Hub Bgp Connection. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The peer autonomous system number for the Virtual Hub Bgp Connection. Changing this forces a new resource to be created.
        /// </summary>
        [Input("peerAsn", required: true)]
        public Input<int> PeerAsn { get; set; } = null!;

        /// <summary>
        /// The peer ip address for the Virtual Hub Bgp Connection. Changing this forces a new resource to be created.
        /// </summary>
        [Input("peerIp", required: true)]
        public Input<string> PeerIp { get; set; } = null!;

        /// <summary>
        /// The ID of the Virtual Hub within which this Bgp connection should be created. Changing this forces a new resource to be created.
        /// </summary>
        [Input("virtualHubId", required: true)]
        public Input<string> VirtualHubId { get; set; } = null!;

        public BgpConnectionArgs()
        {
        }
    }

    public sealed class BgpConnectionState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name which should be used for this Virtual Hub Bgp Connection. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The peer autonomous system number for the Virtual Hub Bgp Connection. Changing this forces a new resource to be created.
        /// </summary>
        [Input("peerAsn")]
        public Input<int>? PeerAsn { get; set; }

        /// <summary>
        /// The peer ip address for the Virtual Hub Bgp Connection. Changing this forces a new resource to be created.
        /// </summary>
        [Input("peerIp")]
        public Input<string>? PeerIp { get; set; }

        /// <summary>
        /// The ID of the Virtual Hub within which this Bgp connection should be created. Changing this forces a new resource to be created.
        /// </summary>
        [Input("virtualHubId")]
        public Input<string>? VirtualHubId { get; set; }

        public BgpConnectionState()
        {
        }
    }
}
