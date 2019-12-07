// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Iot
{
    /// <summary>
    /// Manages an IotHub Fallback Route
    /// 
    /// &gt; **NOTE:** Fallback route can be defined either directly on the `azure.iot.IoTHub` resource, or using the `azure.iot.FallbackRoute` resource - but the two cannot be used together. If both are used against the same IoTHub, spurious changes will occur.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_fallback_route.html.markdown.
    /// </summary>
    public partial class FallbackRoute : Pulumi.CustomResource
    {
        /// <summary>
        /// The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to `true` by default. For grammar, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language.
        /// </summary>
        [Output("condition")]
        public Output<string?> Condition { get; private set; } = null!;

        /// <summary>
        /// Used to specify whether the fallback route is enabled.
        /// </summary>
        [Output("enabled")]
        public Output<bool> Enabled { get; private set; } = null!;

        /// <summary>
        /// The endpoints to which messages that satisfy the condition are routed. Currently only 1 endpoint is allowed.
        /// </summary>
        [Output("endpointNames")]
        public Output<string> EndpointNames { get; private set; } = null!;

        /// <summary>
        /// The name of the IoTHub to which this Fallback Route belongs. Changing this forces a new resource to be created.
        /// </summary>
        [Output("iothubName")]
        public Output<string> IothubName { get; private set; } = null!;

        /// <summary>
        /// The name of the resource group under which the IotHub Storage Container Endpoint resource has to be created. Changing this forces a new resource to be created.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;


        /// <summary>
        /// Create a FallbackRoute resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FallbackRoute(string name, FallbackRouteArgs args, CustomResourceOptions? options = null)
            : base("azure:iot/fallbackRoute:FallbackRoute", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private FallbackRoute(string name, Input<string> id, FallbackRouteState? state = null, CustomResourceOptions? options = null)
            : base("azure:iot/fallbackRoute:FallbackRoute", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing FallbackRoute resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FallbackRoute Get(string name, Input<string> id, FallbackRouteState? state = null, CustomResourceOptions? options = null)
        {
            return new FallbackRoute(name, id, state, options);
        }
    }

    public sealed class FallbackRouteArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to `true` by default. For grammar, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language.
        /// </summary>
        [Input("condition")]
        public Input<string>? Condition { get; set; }

        /// <summary>
        /// Used to specify whether the fallback route is enabled.
        /// </summary>
        [Input("enabled", required: true)]
        public Input<bool> Enabled { get; set; } = null!;

        /// <summary>
        /// The endpoints to which messages that satisfy the condition are routed. Currently only 1 endpoint is allowed.
        /// </summary>
        [Input("endpointNames", required: true)]
        public Input<string> EndpointNames { get; set; } = null!;

        /// <summary>
        /// The name of the IoTHub to which this Fallback Route belongs. Changing this forces a new resource to be created.
        /// </summary>
        [Input("iothubName", required: true)]
        public Input<string> IothubName { get; set; } = null!;

        /// <summary>
        /// The name of the resource group under which the IotHub Storage Container Endpoint resource has to be created. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        public FallbackRouteArgs()
        {
        }
    }

    public sealed class FallbackRouteState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to `true` by default. For grammar, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language.
        /// </summary>
        [Input("condition")]
        public Input<string>? Condition { get; set; }

        /// <summary>
        /// Used to specify whether the fallback route is enabled.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The endpoints to which messages that satisfy the condition are routed. Currently only 1 endpoint is allowed.
        /// </summary>
        [Input("endpointNames")]
        public Input<string>? EndpointNames { get; set; }

        /// <summary>
        /// The name of the IoTHub to which this Fallback Route belongs. Changing this forces a new resource to be created.
        /// </summary>
        [Input("iothubName")]
        public Input<string>? IothubName { get; set; }

        /// <summary>
        /// The name of the resource group under which the IotHub Storage Container Endpoint resource has to be created. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        public FallbackRouteState()
        {
        }
    }
}
