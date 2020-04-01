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
    /// Manages the association between a Network Interface and a Network Security Group.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_interface_security_group_association.html.markdown.
    /// </summary>
    public partial class NetworkInterfaceSecurityGroupAssociation : Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the Network Interface. Changing this forces a new resource to be created.
        /// </summary>
        [Output("networkInterfaceId")]
        public Output<string> NetworkInterfaceId { get; private set; } = null!;

        /// <summary>
        /// The ID of the Network Security Group which should be attached to the Network Interface. Changing this forces a new resource to be created.
        /// </summary>
        [Output("networkSecurityGroupId")]
        public Output<string> NetworkSecurityGroupId { get; private set; } = null!;


        /// <summary>
        /// Create a NetworkInterfaceSecurityGroupAssociation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NetworkInterfaceSecurityGroupAssociation(string name, NetworkInterfaceSecurityGroupAssociationArgs args, CustomResourceOptions? options = null)
            : base("azure:network/networkInterfaceSecurityGroupAssociation:NetworkInterfaceSecurityGroupAssociation", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private NetworkInterfaceSecurityGroupAssociation(string name, Input<string> id, NetworkInterfaceSecurityGroupAssociationState? state = null, CustomResourceOptions? options = null)
            : base("azure:network/networkInterfaceSecurityGroupAssociation:NetworkInterfaceSecurityGroupAssociation", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing NetworkInterfaceSecurityGroupAssociation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NetworkInterfaceSecurityGroupAssociation Get(string name, Input<string> id, NetworkInterfaceSecurityGroupAssociationState? state = null, CustomResourceOptions? options = null)
        {
            return new NetworkInterfaceSecurityGroupAssociation(name, id, state, options);
        }
    }

    public sealed class NetworkInterfaceSecurityGroupAssociationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the Network Interface. Changing this forces a new resource to be created.
        /// </summary>
        [Input("networkInterfaceId", required: true)]
        public Input<string> NetworkInterfaceId { get; set; } = null!;

        /// <summary>
        /// The ID of the Network Security Group which should be attached to the Network Interface. Changing this forces a new resource to be created.
        /// </summary>
        [Input("networkSecurityGroupId", required: true)]
        public Input<string> NetworkSecurityGroupId { get; set; } = null!;

        public NetworkInterfaceSecurityGroupAssociationArgs()
        {
        }
    }

    public sealed class NetworkInterfaceSecurityGroupAssociationState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the Network Interface. Changing this forces a new resource to be created.
        /// </summary>
        [Input("networkInterfaceId")]
        public Input<string>? NetworkInterfaceId { get; set; }

        /// <summary>
        /// The ID of the Network Security Group which should be attached to the Network Interface. Changing this forces a new resource to be created.
        /// </summary>
        [Input("networkSecurityGroupId")]
        public Input<string>? NetworkSecurityGroupId { get; set; }

        public NetworkInterfaceSecurityGroupAssociationState()
        {
        }
    }
}