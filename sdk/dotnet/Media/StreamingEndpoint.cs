// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Media
{
    /// <summary>
    /// Manages a Streaming Endpoint.
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
    ///             Location = "West Europe",
    ///         });
    ///         var exampleAccount = new Azure.Storage.Account("exampleAccount", new Azure.Storage.AccountArgs
    ///         {
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             Location = exampleResourceGroup.Location,
    ///             AccountTier = "Standard",
    ///             AccountReplicationType = "GRS",
    ///         });
    ///         var exampleServiceAccount = new Azure.Media.ServiceAccount("exampleServiceAccount", new Azure.Media.ServiceAccountArgs
    ///         {
    ///             Location = exampleResourceGroup.Location,
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             StorageAccounts = 
    ///             {
    ///                 new Azure.Media.Inputs.ServiceAccountStorageAccountArgs
    ///                 {
    ///                     Id = exampleAccount.Id,
    ///                     IsPrimary = true,
    ///                 },
    ///             },
    ///         });
    ///         var exampleStreamingEndpoint = new Azure.Media.StreamingEndpoint("exampleStreamingEndpoint", new Azure.Media.StreamingEndpointArgs
    ///         {
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             Location = exampleResourceGroup.Location,
    ///             MediaServicesAccountName = exampleServiceAccount.Name,
    ///             ScaleUnits = 2,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ### With Access Control
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
    ///             Location = "West Europe",
    ///         });
    ///         var exampleAccount = new Azure.Storage.Account("exampleAccount", new Azure.Storage.AccountArgs
    ///         {
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             Location = exampleResourceGroup.Location,
    ///             AccountTier = "Standard",
    ///             AccountReplicationType = "GRS",
    ///         });
    ///         var exampleServiceAccount = new Azure.Media.ServiceAccount("exampleServiceAccount", new Azure.Media.ServiceAccountArgs
    ///         {
    ///             Location = exampleResourceGroup.Location,
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             StorageAccounts = 
    ///             {
    ///                 new Azure.Media.Inputs.ServiceAccountStorageAccountArgs
    ///                 {
    ///                     Id = exampleAccount.Id,
    ///                     IsPrimary = true,
    ///                 },
    ///             },
    ///         });
    ///         var exampleStreamingEndpoint = new Azure.Media.StreamingEndpoint("exampleStreamingEndpoint", new Azure.Media.StreamingEndpointArgs
    ///         {
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             Location = exampleResourceGroup.Location,
    ///             MediaServicesAccountName = exampleServiceAccount.Name,
    ///             ScaleUnits = 2,
    ///             AccessControl = new Azure.Media.Inputs.StreamingEndpointAccessControlArgs
    ///             {
    ///                 IpAllows = 
    ///                 {
    ///                     new Azure.Media.Inputs.StreamingEndpointAccessControlIpAllowArgs
    ///                     {
    ///                         Name = "AllowedIP",
    ///                         Address = "192.168.1.1",
    ///                     },
    ///                     new Azure.Media.Inputs.StreamingEndpointAccessControlIpAllowArgs
    ///                     {
    ///                         Name = "AnotherIp",
    ///                         Address = "192.168.1.2",
    ///                     },
    ///                 },
    ///                 AkamaiSignatureHeaderAuthenticationKeys = 
    ///                 {
    ///                     new Azure.Media.Inputs.StreamingEndpointAccessControlAkamaiSignatureHeaderAuthenticationKeyArgs
    ///                     {
    ///                         Identifier = "id1",
    ///                         Expiration = "2030-12-31T16:00:00Z",
    ///                         Base64Key = "dGVzdGlkMQ==",
    ///                     },
    ///                     new Azure.Media.Inputs.StreamingEndpointAccessControlAkamaiSignatureHeaderAuthenticationKeyArgs
    ///                     {
    ///                         Identifier = "id2",
    ///                         Expiration = "2032-01-28T16:00:00Z",
    ///                         Base64Key = "dGVzdGlkMQ==",
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
    /// Streaming Endpoints can be imported using the `resource id`, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import azure:media/streamingEndpoint:StreamingEndpoint example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/mediaservices/service1/streamingendpoints/endpoint1
    /// ```
    /// </summary>
    [AzureResourceType("azure:media/streamingEndpoint:StreamingEndpoint")]
    public partial class StreamingEndpoint : Pulumi.CustomResource
    {
        /// <summary>
        /// A `access_control` block as defined below.
        /// </summary>
        [Output("accessControl")]
        public Output<Outputs.StreamingEndpointAccessControl?> AccessControl { get; private set; } = null!;

        /// <summary>
        /// The flag indicates if the resource should be automatically started on creation.
        /// </summary>
        [Output("autoStartEnabled")]
        public Output<bool> AutoStartEnabled { get; private set; } = null!;

        /// <summary>
        /// The CDN enabled flag.
        /// </summary>
        [Output("cdnEnabled")]
        public Output<bool?> CdnEnabled { get; private set; } = null!;

        /// <summary>
        /// The CDN profile name.
        /// </summary>
        [Output("cdnProfile")]
        public Output<string> CdnProfile { get; private set; } = null!;

        /// <summary>
        /// The CDN provider name. Supported value are `StandardVerizon`,`PremiumVerizon` and `StandardAkamai`
        /// </summary>
        [Output("cdnProvider")]
        public Output<string> CdnProvider { get; private set; } = null!;

        /// <summary>
        /// A `cross_site_access_policy` block as defined below.
        /// </summary>
        [Output("crossSiteAccessPolicy")]
        public Output<Outputs.StreamingEndpointCrossSiteAccessPolicy?> CrossSiteAccessPolicy { get; private set; } = null!;

        /// <summary>
        /// The custom host names of the streaming endpoint.
        /// </summary>
        [Output("customHostNames")]
        public Output<ImmutableArray<string>> CustomHostNames { get; private set; } = null!;

        /// <summary>
        /// The streaming endpoint description.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The Azure Region where the Streaming Endpoint should exist. Changing this forces a new Streaming Endpoint to be created.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// Max cache age in seconds.
        /// </summary>
        [Output("maxCacheAgeSeconds")]
        public Output<int?> MaxCacheAgeSeconds { get; private set; } = null!;

        /// <summary>
        /// The Media Services account name. Changing this forces a new Streaming Endpoint to be created.
        /// </summary>
        [Output("mediaServicesAccountName")]
        public Output<string> MediaServicesAccountName { get; private set; } = null!;

        /// <summary>
        /// The name which should be used for this Streaming Endpoint maximum length is 24. Changing this forces a new Streaming Endpoint to be created.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The name of the Resource Group where the Streaming Endpoint should exist. Changing this forces a new Streaming Endpoint to be created.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;

        /// <summary>
        /// The number of scale units.
        /// </summary>
        [Output("scaleUnits")]
        public Output<int> ScaleUnits { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags which should be assigned to the Streaming Endpoint.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a StreamingEndpoint resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public StreamingEndpoint(string name, StreamingEndpointArgs args, CustomResourceOptions? options = null)
            : base("azure:media/streamingEndpoint:StreamingEndpoint", name, args ?? new StreamingEndpointArgs(), MakeResourceOptions(options, ""))
        {
        }

        private StreamingEndpoint(string name, Input<string> id, StreamingEndpointState? state = null, CustomResourceOptions? options = null)
            : base("azure:media/streamingEndpoint:StreamingEndpoint", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing StreamingEndpoint resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static StreamingEndpoint Get(string name, Input<string> id, StreamingEndpointState? state = null, CustomResourceOptions? options = null)
        {
            return new StreamingEndpoint(name, id, state, options);
        }
    }

    public sealed class StreamingEndpointArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A `access_control` block as defined below.
        /// </summary>
        [Input("accessControl")]
        public Input<Inputs.StreamingEndpointAccessControlArgs>? AccessControl { get; set; }

        /// <summary>
        /// The flag indicates if the resource should be automatically started on creation.
        /// </summary>
        [Input("autoStartEnabled")]
        public Input<bool>? AutoStartEnabled { get; set; }

        /// <summary>
        /// The CDN enabled flag.
        /// </summary>
        [Input("cdnEnabled")]
        public Input<bool>? CdnEnabled { get; set; }

        /// <summary>
        /// The CDN profile name.
        /// </summary>
        [Input("cdnProfile")]
        public Input<string>? CdnProfile { get; set; }

        /// <summary>
        /// The CDN provider name. Supported value are `StandardVerizon`,`PremiumVerizon` and `StandardAkamai`
        /// </summary>
        [Input("cdnProvider")]
        public Input<string>? CdnProvider { get; set; }

        /// <summary>
        /// A `cross_site_access_policy` block as defined below.
        /// </summary>
        [Input("crossSiteAccessPolicy")]
        public Input<Inputs.StreamingEndpointCrossSiteAccessPolicyArgs>? CrossSiteAccessPolicy { get; set; }

        [Input("customHostNames")]
        private InputList<string>? _customHostNames;

        /// <summary>
        /// The custom host names of the streaming endpoint.
        /// </summary>
        public InputList<string> CustomHostNames
        {
            get => _customHostNames ?? (_customHostNames = new InputList<string>());
            set => _customHostNames = value;
        }

        /// <summary>
        /// The streaming endpoint description.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The Azure Region where the Streaming Endpoint should exist. Changing this forces a new Streaming Endpoint to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Max cache age in seconds.
        /// </summary>
        [Input("maxCacheAgeSeconds")]
        public Input<int>? MaxCacheAgeSeconds { get; set; }

        /// <summary>
        /// The Media Services account name. Changing this forces a new Streaming Endpoint to be created.
        /// </summary>
        [Input("mediaServicesAccountName", required: true)]
        public Input<string> MediaServicesAccountName { get; set; } = null!;

        /// <summary>
        /// The name which should be used for this Streaming Endpoint maximum length is 24. Changing this forces a new Streaming Endpoint to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the Resource Group where the Streaming Endpoint should exist. Changing this forces a new Streaming Endpoint to be created.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// The number of scale units.
        /// </summary>
        [Input("scaleUnits", required: true)]
        public Input<int> ScaleUnits { get; set; } = null!;

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A mapping of tags which should be assigned to the Streaming Endpoint.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        public StreamingEndpointArgs()
        {
        }
    }

    public sealed class StreamingEndpointState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A `access_control` block as defined below.
        /// </summary>
        [Input("accessControl")]
        public Input<Inputs.StreamingEndpointAccessControlGetArgs>? AccessControl { get; set; }

        /// <summary>
        /// The flag indicates if the resource should be automatically started on creation.
        /// </summary>
        [Input("autoStartEnabled")]
        public Input<bool>? AutoStartEnabled { get; set; }

        /// <summary>
        /// The CDN enabled flag.
        /// </summary>
        [Input("cdnEnabled")]
        public Input<bool>? CdnEnabled { get; set; }

        /// <summary>
        /// The CDN profile name.
        /// </summary>
        [Input("cdnProfile")]
        public Input<string>? CdnProfile { get; set; }

        /// <summary>
        /// The CDN provider name. Supported value are `StandardVerizon`,`PremiumVerizon` and `StandardAkamai`
        /// </summary>
        [Input("cdnProvider")]
        public Input<string>? CdnProvider { get; set; }

        /// <summary>
        /// A `cross_site_access_policy` block as defined below.
        /// </summary>
        [Input("crossSiteAccessPolicy")]
        public Input<Inputs.StreamingEndpointCrossSiteAccessPolicyGetArgs>? CrossSiteAccessPolicy { get; set; }

        [Input("customHostNames")]
        private InputList<string>? _customHostNames;

        /// <summary>
        /// The custom host names of the streaming endpoint.
        /// </summary>
        public InputList<string> CustomHostNames
        {
            get => _customHostNames ?? (_customHostNames = new InputList<string>());
            set => _customHostNames = value;
        }

        /// <summary>
        /// The streaming endpoint description.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The Azure Region where the Streaming Endpoint should exist. Changing this forces a new Streaming Endpoint to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Max cache age in seconds.
        /// </summary>
        [Input("maxCacheAgeSeconds")]
        public Input<int>? MaxCacheAgeSeconds { get; set; }

        /// <summary>
        /// The Media Services account name. Changing this forces a new Streaming Endpoint to be created.
        /// </summary>
        [Input("mediaServicesAccountName")]
        public Input<string>? MediaServicesAccountName { get; set; }

        /// <summary>
        /// The name which should be used for this Streaming Endpoint maximum length is 24. Changing this forces a new Streaming Endpoint to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the Resource Group where the Streaming Endpoint should exist. Changing this forces a new Streaming Endpoint to be created.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        /// <summary>
        /// The number of scale units.
        /// </summary>
        [Input("scaleUnits")]
        public Input<int>? ScaleUnits { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A mapping of tags which should be assigned to the Streaming Endpoint.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        public StreamingEndpointState()
        {
        }
    }
}
