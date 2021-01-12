// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Compute
{
    /// <summary>
    /// Manages a SSH Public Key.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.IO;
    /// using Pulumi;
    /// using Azure = Pulumi.Azure;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var example = new Azure.Compute.SshPublicKey("example", new Azure.Compute.SshPublicKeyArgs
    ///         {
    ///             ResourceGroupName = "example",
    ///             Location = "West Europe",
    ///             PublicKey = File.ReadAllText("~/.ssh/id_rsa.pub"),
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// SSH Public Keys can be imported using the `resource id`, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import azure:compute/sshPublicKey:SshPublicKey example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Compute/SshPublicKeys/mySshPublicKeyName1
    /// ```
    /// </summary>
    public partial class SshPublicKey : Pulumi.CustomResource
    {
        /// <summary>
        /// The Azure Region where the SSH Public Key should exist. Changing this forces a new SSH Public Key to be created.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// The name which should be used for this SSH Public Key. Changing this forces a new SSH Public Key to be created.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// SSH public key used to authenticate to a virtual machine through ssh. the provided public key needs to be at least 2048-bit and in ssh-rsa format.
        /// </summary>
        [Output("publicKey")]
        public Output<string> PublicKey { get; private set; } = null!;

        /// <summary>
        /// The name of the Resource Group where the SSH Public Key should exist. Changing this forces a new SSH Public Key to be created.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags which should be assigned to the SSH Public Key.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a SshPublicKey resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SshPublicKey(string name, SshPublicKeyArgs args, CustomResourceOptions? options = null)
            : base("azure:compute/sshPublicKey:SshPublicKey", name, args ?? new SshPublicKeyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SshPublicKey(string name, Input<string> id, SshPublicKeyState? state = null, CustomResourceOptions? options = null)
            : base("azure:compute/sshPublicKey:SshPublicKey", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SshPublicKey resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SshPublicKey Get(string name, Input<string> id, SshPublicKeyState? state = null, CustomResourceOptions? options = null)
        {
            return new SshPublicKey(name, id, state, options);
        }
    }

    public sealed class SshPublicKeyArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Azure Region where the SSH Public Key should exist. Changing this forces a new SSH Public Key to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The name which should be used for this SSH Public Key. Changing this forces a new SSH Public Key to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// SSH public key used to authenticate to a virtual machine through ssh. the provided public key needs to be at least 2048-bit and in ssh-rsa format.
        /// </summary>
        [Input("publicKey", required: true)]
        public Input<string> PublicKey { get; set; } = null!;

        /// <summary>
        /// The name of the Resource Group where the SSH Public Key should exist. Changing this forces a new SSH Public Key to be created.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A mapping of tags which should be assigned to the SSH Public Key.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        public SshPublicKeyArgs()
        {
        }
    }

    public sealed class SshPublicKeyState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Azure Region where the SSH Public Key should exist. Changing this forces a new SSH Public Key to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The name which should be used for this SSH Public Key. Changing this forces a new SSH Public Key to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// SSH public key used to authenticate to a virtual machine through ssh. the provided public key needs to be at least 2048-bit and in ssh-rsa format.
        /// </summary>
        [Input("publicKey")]
        public Input<string>? PublicKey { get; set; }

        /// <summary>
        /// The name of the Resource Group where the SSH Public Key should exist. Changing this forces a new SSH Public Key to be created.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A mapping of tags which should be assigned to the SSH Public Key.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        public SshPublicKeyState()
        {
        }
    }
}