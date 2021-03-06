// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Storage
{
    /// <summary>
    /// Manages an Azure Storage Account Management Policy.
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
    ///         var exampleResourceGroup = new Azure.Core.ResourceGroup("exampleResourceGroup", new Azure.Core.ResourceGroupArgs
    ///         {
    ///             Location = "westus",
    ///         });
    ///         var exampleAccount = new Azure.Storage.Account("exampleAccount", new Azure.Storage.AccountArgs
    ///         {
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             Location = exampleResourceGroup.Location,
    ///             AccountTier = "Standard",
    ///             AccountReplicationType = "LRS",
    ///             AccountKind = "BlobStorage",
    ///         });
    ///         var exampleManagementPolicy = new Azure.Storage.ManagementPolicy("exampleManagementPolicy", new Azure.Storage.ManagementPolicyArgs
    ///         {
    ///             StorageAccountId = exampleAccount.Id,
    ///             Rules = 
    ///             {
    ///                 new Azure.Storage.Inputs.ManagementPolicyRuleArgs
    ///                 {
    ///                     Name = "rule1",
    ///                     Enabled = true,
    ///                     Filters = new Azure.Storage.Inputs.ManagementPolicyRuleFiltersArgs
    ///                     {
    ///                         PrefixMatches = 
    ///                         {
    ///                             "container1/prefix1",
    ///                         },
    ///                         BlobTypes = 
    ///                         {
    ///                             "blockBlob",
    ///                         },
    ///                     },
    ///                     Actions = new Azure.Storage.Inputs.ManagementPolicyRuleActionsArgs
    ///                     {
    ///                         BaseBlob = new Azure.Storage.Inputs.ManagementPolicyRuleActionsBaseBlobArgs
    ///                         {
    ///                             TierToCoolAfterDaysSinceModificationGreaterThan = 10,
    ///                             TierToArchiveAfterDaysSinceModificationGreaterThan = 50,
    ///                             DeleteAfterDaysSinceModificationGreaterThan = 100,
    ///                         },
    ///                         Snapshot = new Azure.Storage.Inputs.ManagementPolicyRuleActionsSnapshotArgs
    ///                         {
    ///                             DeleteAfterDaysSinceCreationGreaterThan = 30,
    ///                         },
    ///                     },
    ///                 },
    ///                 new Azure.Storage.Inputs.ManagementPolicyRuleArgs
    ///                 {
    ///                     Name = "rule2",
    ///                     Enabled = false,
    ///                     Filters = new Azure.Storage.Inputs.ManagementPolicyRuleFiltersArgs
    ///                     {
    ///                         PrefixMatches = 
    ///                         {
    ///                             "container2/prefix1",
    ///                             "container2/prefix2",
    ///                         },
    ///                         BlobTypes = 
    ///                         {
    ///                             "blockBlob",
    ///                         },
    ///                     },
    ///                     Actions = new Azure.Storage.Inputs.ManagementPolicyRuleActionsArgs
    ///                     {
    ///                         BaseBlob = new Azure.Storage.Inputs.ManagementPolicyRuleActionsBaseBlobArgs
    ///                         {
    ///                             TierToCoolAfterDaysSinceModificationGreaterThan = 11,
    ///                             TierToArchiveAfterDaysSinceModificationGreaterThan = 51,
    ///                             DeleteAfterDaysSinceModificationGreaterThan = 101,
    ///                         },
    ///                         Snapshot = new Azure.Storage.Inputs.ManagementPolicyRuleActionsSnapshotArgs
    ///                         {
    ///                             DeleteAfterDaysSinceCreationGreaterThan = 31,
    ///                         },
    ///                     },
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Storage Account Management Policies can be imported using the `resource id`, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import azure:storage/managementPolicy:ManagementPolicy example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Storage/storageAccounts/myaccountname/managementPolicies/default
    /// ```
    /// </summary>
    [AzureResourceType("azure:storage/managementPolicy:ManagementPolicy")]
    public partial class ManagementPolicy : Pulumi.CustomResource
    {
        /// <summary>
        /// A `rule` block as documented below.
        /// </summary>
        [Output("rules")]
        public Output<ImmutableArray<Outputs.ManagementPolicyRule>> Rules { get; private set; } = null!;

        /// <summary>
        /// Specifies the id of the storage account to apply the management policy to.
        /// </summary>
        [Output("storageAccountId")]
        public Output<string> StorageAccountId { get; private set; } = null!;


        /// <summary>
        /// Create a ManagementPolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ManagementPolicy(string name, ManagementPolicyArgs args, CustomResourceOptions? options = null)
            : base("azure:storage/managementPolicy:ManagementPolicy", name, args ?? new ManagementPolicyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ManagementPolicy(string name, Input<string> id, ManagementPolicyState? state = null, CustomResourceOptions? options = null)
            : base("azure:storage/managementPolicy:ManagementPolicy", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ManagementPolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ManagementPolicy Get(string name, Input<string> id, ManagementPolicyState? state = null, CustomResourceOptions? options = null)
        {
            return new ManagementPolicy(name, id, state, options);
        }
    }

    public sealed class ManagementPolicyArgs : Pulumi.ResourceArgs
    {
        [Input("rules")]
        private InputList<Inputs.ManagementPolicyRuleArgs>? _rules;

        /// <summary>
        /// A `rule` block as documented below.
        /// </summary>
        public InputList<Inputs.ManagementPolicyRuleArgs> Rules
        {
            get => _rules ?? (_rules = new InputList<Inputs.ManagementPolicyRuleArgs>());
            set => _rules = value;
        }

        /// <summary>
        /// Specifies the id of the storage account to apply the management policy to.
        /// </summary>
        [Input("storageAccountId", required: true)]
        public Input<string> StorageAccountId { get; set; } = null!;

        public ManagementPolicyArgs()
        {
        }
    }

    public sealed class ManagementPolicyState : Pulumi.ResourceArgs
    {
        [Input("rules")]
        private InputList<Inputs.ManagementPolicyRuleGetArgs>? _rules;

        /// <summary>
        /// A `rule` block as documented below.
        /// </summary>
        public InputList<Inputs.ManagementPolicyRuleGetArgs> Rules
        {
            get => _rules ?? (_rules = new InputList<Inputs.ManagementPolicyRuleGetArgs>());
            set => _rules = value;
        }

        /// <summary>
        /// Specifies the id of the storage account to apply the management policy to.
        /// </summary>
        [Input("storageAccountId")]
        public Input<string>? StorageAccountId { get; set; }

        public ManagementPolicyState()
        {
        }
    }
}
