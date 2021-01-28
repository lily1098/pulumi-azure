// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.SiteRecovery
{
    /// <summary>
    /// Manages a Azure Site Recovery protection container. Protection containers serve as containers for replicated VMs and belong to a single region / recovery fabric. Protection containers can contain more than one replicated VM. To replicate a VM, a container must exist in both the source and target Azure regions.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Azure = Pulumi.Azure;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var primary = new Azure.Core.ResourceGroup("primary", new Azure.Core.ResourceGroupArgs
    ///         {
    ///             Location = "West US",
    ///         });
    ///         var secondary = new Azure.Core.ResourceGroup("secondary", new Azure.Core.ResourceGroupArgs
    ///         {
    ///             Location = "East US",
    ///         });
    ///         var vault = new Azure.RecoveryServices.Vault("vault", new Azure.RecoveryServices.VaultArgs
    ///         {
    ///             Location = secondary.Location,
    ///             ResourceGroupName = secondary.Name,
    ///             Sku = "Standard",
    ///         });
    ///         var fabric = new Azure.SiteRecovery.Fabric("fabric", new Azure.SiteRecovery.FabricArgs
    ///         {
    ///             ResourceGroupName = secondary.Name,
    ///             RecoveryVaultName = vault.Name,
    ///             Location = primary.Location,
    ///         });
    ///         var protection_container = new Azure.SiteRecovery.ProtectionContainer("protection-container", new Azure.SiteRecovery.ProtectionContainerArgs
    ///         {
    ///             ResourceGroupName = secondary.Name,
    ///             RecoveryVaultName = vault.Name,
    ///             RecoveryFabricName = fabric.Name,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Site Recovery Protection Containers can be imported using the `resource id`, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import azure:siterecovery/protectionContainer:ProtectionContainer mycontainer /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resource-group-name/providers/Microsoft.RecoveryServices/vaults/recovery-vault-name/replicationFabrics/fabric-name/replicationProtectionContainers/protection-container-name
    /// ```
    /// </summary>
    [AzureResourceType("azure:siterecovery/protectionContainer:ProtectionContainer")]
    public partial class ProtectionContainer : Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the network mapping.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Name of fabric that should contain this protection container.
        /// </summary>
        [Output("recoveryFabricName")]
        public Output<string> RecoveryFabricName { get; private set; } = null!;

        /// <summary>
        /// The name of the vault that should be updated.
        /// </summary>
        [Output("recoveryVaultName")]
        public Output<string> RecoveryVaultName { get; private set; } = null!;

        /// <summary>
        /// Name of the resource group where the vault that should be updated is located.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;


        /// <summary>
        /// Create a ProtectionContainer resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ProtectionContainer(string name, ProtectionContainerArgs args, CustomResourceOptions? options = null)
            : base("azure:siterecovery/protectionContainer:ProtectionContainer", name, args ?? new ProtectionContainerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ProtectionContainer(string name, Input<string> id, ProtectionContainerState? state = null, CustomResourceOptions? options = null)
            : base("azure:siterecovery/protectionContainer:ProtectionContainer", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ProtectionContainer resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ProtectionContainer Get(string name, Input<string> id, ProtectionContainerState? state = null, CustomResourceOptions? options = null)
        {
            return new ProtectionContainer(name, id, state, options);
        }
    }

    public sealed class ProtectionContainerArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the network mapping.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Name of fabric that should contain this protection container.
        /// </summary>
        [Input("recoveryFabricName", required: true)]
        public Input<string> RecoveryFabricName { get; set; } = null!;

        /// <summary>
        /// The name of the vault that should be updated.
        /// </summary>
        [Input("recoveryVaultName", required: true)]
        public Input<string> RecoveryVaultName { get; set; } = null!;

        /// <summary>
        /// Name of the resource group where the vault that should be updated is located.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        public ProtectionContainerArgs()
        {
        }
    }

    public sealed class ProtectionContainerState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the network mapping.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Name of fabric that should contain this protection container.
        /// </summary>
        [Input("recoveryFabricName")]
        public Input<string>? RecoveryFabricName { get; set; }

        /// <summary>
        /// The name of the vault that should be updated.
        /// </summary>
        [Input("recoveryVaultName")]
        public Input<string>? RecoveryVaultName { get; set; }

        /// <summary>
        /// Name of the resource group where the vault that should be updated is located.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        public ProtectionContainerState()
        {
        }
    }
}
