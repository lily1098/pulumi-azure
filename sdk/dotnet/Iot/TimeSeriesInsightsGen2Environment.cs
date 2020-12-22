// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Iot
{
    /// <summary>
    /// Manages an Azure IoT Time Series Insights Gen2 Environment.
    /// 
    /// ## Import
    /// 
    /// Azure IoT Time Series Insights Gen2 Environment can be imported using the `resource id`, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import azure:iot/timeSeriesInsightsGen2Environment:TimeSeriesInsightsGen2Environment example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example/providers/Microsoft.TimeSeriesInsights/environments/example
    /// ```
    /// </summary>
    public partial class TimeSeriesInsightsGen2Environment : Pulumi.CustomResource
    {
        /// <summary>
        /// The FQDN used to access the environment data.
        /// </summary>
        [Output("dataAccessFqdn")]
        public Output<string> DataAccessFqdn { get; private set; } = null!;

        /// <summary>
        /// A list of property ids for the Azure IoT Time Series Insights Gen2 Environment
        /// </summary>
        [Output("idProperties")]
        public Output<ImmutableArray<string>> IdProperties { get; private set; } = null!;

        /// <summary>
        /// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// Specifies the name of the Azure IoT Time Series Insights Gen2 Environment. Changing this forces a new resource to be created. Must be globally unique.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The name of the resource group in which to create the Azure IoT Time Series Insights Gen2 Environment.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;

        /// <summary>
        /// Specifies the SKU Name for this IoT Time Series Insights Gen2 Environment. Currently it supports only `L1`. For gen2, capacity cannot be specified.
        /// </summary>
        [Output("skuName")]
        public Output<string> SkuName { get; private set; } = null!;

        /// <summary>
        /// A `storage` block as defined below.
        /// </summary>
        [Output("storage")]
        public Output<Outputs.TimeSeriesInsightsGen2EnvironmentStorage> Storage { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;

        [Output("warmStoreDataRetentionTime")]
        public Output<string?> WarmStoreDataRetentionTime { get; private set; } = null!;


        /// <summary>
        /// Create a TimeSeriesInsightsGen2Environment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TimeSeriesInsightsGen2Environment(string name, TimeSeriesInsightsGen2EnvironmentArgs args, CustomResourceOptions? options = null)
            : base("azure:iot/timeSeriesInsightsGen2Environment:TimeSeriesInsightsGen2Environment", name, args ?? new TimeSeriesInsightsGen2EnvironmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TimeSeriesInsightsGen2Environment(string name, Input<string> id, TimeSeriesInsightsGen2EnvironmentState? state = null, CustomResourceOptions? options = null)
            : base("azure:iot/timeSeriesInsightsGen2Environment:TimeSeriesInsightsGen2Environment", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing TimeSeriesInsightsGen2Environment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TimeSeriesInsightsGen2Environment Get(string name, Input<string> id, TimeSeriesInsightsGen2EnvironmentState? state = null, CustomResourceOptions? options = null)
        {
            return new TimeSeriesInsightsGen2Environment(name, id, state, options);
        }
    }

    public sealed class TimeSeriesInsightsGen2EnvironmentArgs : Pulumi.ResourceArgs
    {
        [Input("idProperties", required: true)]
        private InputList<string>? _idProperties;

        /// <summary>
        /// A list of property ids for the Azure IoT Time Series Insights Gen2 Environment
        /// </summary>
        public InputList<string> IdProperties
        {
            get => _idProperties ?? (_idProperties = new InputList<string>());
            set => _idProperties = value;
        }

        /// <summary>
        /// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Specifies the name of the Azure IoT Time Series Insights Gen2 Environment. Changing this forces a new resource to be created. Must be globally unique.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the resource group in which to create the Azure IoT Time Series Insights Gen2 Environment.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// Specifies the SKU Name for this IoT Time Series Insights Gen2 Environment. Currently it supports only `L1`. For gen2, capacity cannot be specified.
        /// </summary>
        [Input("skuName", required: true)]
        public Input<string> SkuName { get; set; } = null!;

        /// <summary>
        /// A `storage` block as defined below.
        /// </summary>
        [Input("storage", required: true)]
        public Input<Inputs.TimeSeriesInsightsGen2EnvironmentStorageArgs> Storage { get; set; } = null!;

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        [Input("warmStoreDataRetentionTime")]
        public Input<string>? WarmStoreDataRetentionTime { get; set; }

        public TimeSeriesInsightsGen2EnvironmentArgs()
        {
        }
    }

    public sealed class TimeSeriesInsightsGen2EnvironmentState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The FQDN used to access the environment data.
        /// </summary>
        [Input("dataAccessFqdn")]
        public Input<string>? DataAccessFqdn { get; set; }

        [Input("idProperties")]
        private InputList<string>? _idProperties;

        /// <summary>
        /// A list of property ids for the Azure IoT Time Series Insights Gen2 Environment
        /// </summary>
        public InputList<string> IdProperties
        {
            get => _idProperties ?? (_idProperties = new InputList<string>());
            set => _idProperties = value;
        }

        /// <summary>
        /// Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Specifies the name of the Azure IoT Time Series Insights Gen2 Environment. Changing this forces a new resource to be created. Must be globally unique.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the resource group in which to create the Azure IoT Time Series Insights Gen2 Environment.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        /// <summary>
        /// Specifies the SKU Name for this IoT Time Series Insights Gen2 Environment. Currently it supports only `L1`. For gen2, capacity cannot be specified.
        /// </summary>
        [Input("skuName")]
        public Input<string>? SkuName { get; set; }

        /// <summary>
        /// A `storage` block as defined below.
        /// </summary>
        [Input("storage")]
        public Input<Inputs.TimeSeriesInsightsGen2EnvironmentStorageGetArgs>? Storage { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        [Input("warmStoreDataRetentionTime")]
        public Input<string>? WarmStoreDataRetentionTime { get; set; }

        public TimeSeriesInsightsGen2EnvironmentState()
        {
        }
    }
}
