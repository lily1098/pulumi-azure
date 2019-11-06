// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.SignalR
{
    /// <summary>
    /// Manages an Azure SignalR service.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/signalr_service.html.markdown.
    /// </summary>
    public partial class Service : Pulumi.CustomResource
    {
        /// <summary>
        /// The FQDN of the SignalR service.
        /// </summary>
        [Output("hostname")]
        public Output<string> Hostname { get; private set; } = null!;

        /// <summary>
        /// The publicly accessible IP of the SignalR service.
        /// </summary>
        [Output("ipAddress")]
        public Output<string> IpAddress { get; private set; } = null!;

        /// <summary>
        /// Specifies the supported Azure location where the SignalR service exists. Changing this forces a new resource to be created.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// The name of the SignalR service. Changing this forces a new resource to be created.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The primary access key for the SignalR service.
        /// </summary>
        [Output("primaryAccessKey")]
        public Output<string> PrimaryAccessKey { get; private set; } = null!;

        /// <summary>
        /// The primary connection string for the SignalR service.
        /// </summary>
        [Output("primaryConnectionString")]
        public Output<string> PrimaryConnectionString { get; private set; } = null!;

        /// <summary>
        /// The publicly accessible port of the SignalR service which is designed for browser/client use.
        /// </summary>
        [Output("publicPort")]
        public Output<int> PublicPort { get; private set; } = null!;

        /// <summary>
        /// The name of the resource group in which to create the SignalR service. Changing this forces a new resource to be created.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;

        /// <summary>
        /// The secondary access key for the SignalR service.
        /// </summary>
        [Output("secondaryAccessKey")]
        public Output<string> SecondaryAccessKey { get; private set; } = null!;

        /// <summary>
        /// The secondary connection string for the SignalR service.
        /// </summary>
        [Output("secondaryConnectionString")]
        public Output<string> SecondaryConnectionString { get; private set; } = null!;

        /// <summary>
        /// The publicly accessible port of the SignalR service which is designed for customer server side use.
        /// </summary>
        [Output("serverPort")]
        public Output<int> ServerPort { get; private set; } = null!;

        /// <summary>
        /// A `sku` block as documented below.
        /// </summary>
        [Output("sku")]
        public Output<Outputs.ServiceSku> Sku { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Service resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Service(string name, ServiceArgs args, CustomResourceOptions? options = null)
            : base("azure:signalr/service:Service", name, args, MakeResourceOptions(options, ""))
        {
        }

        private Service(string name, Input<string> id, ServiceState? state = null, CustomResourceOptions? options = null)
            : base("azure:signalr/service:Service", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Service resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Service Get(string name, Input<string> id, ServiceState? state = null, CustomResourceOptions? options = null)
        {
            return new Service(name, id, state, options);
        }
    }

    public sealed class ServiceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies the supported Azure location where the SignalR service exists. Changing this forces a new resource to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The name of the SignalR service. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the resource group in which to create the SignalR service. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// A `sku` block as documented below.
        /// </summary>
        [Input("sku", required: true)]
        public Input<Inputs.ServiceSkuArgs> Sku { get; set; } = null!;

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public ServiceArgs()
        {
        }
    }

    public sealed class ServiceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The FQDN of the SignalR service.
        /// </summary>
        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        /// <summary>
        /// The publicly accessible IP of the SignalR service.
        /// </summary>
        [Input("ipAddress")]
        public Input<string>? IpAddress { get; set; }

        /// <summary>
        /// Specifies the supported Azure location where the SignalR service exists. Changing this forces a new resource to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The name of the SignalR service. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The primary access key for the SignalR service.
        /// </summary>
        [Input("primaryAccessKey")]
        public Input<string>? PrimaryAccessKey { get; set; }

        /// <summary>
        /// The primary connection string for the SignalR service.
        /// </summary>
        [Input("primaryConnectionString")]
        public Input<string>? PrimaryConnectionString { get; set; }

        /// <summary>
        /// The publicly accessible port of the SignalR service which is designed for browser/client use.
        /// </summary>
        [Input("publicPort")]
        public Input<int>? PublicPort { get; set; }

        /// <summary>
        /// The name of the resource group in which to create the SignalR service. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        /// <summary>
        /// The secondary access key for the SignalR service.
        /// </summary>
        [Input("secondaryAccessKey")]
        public Input<string>? SecondaryAccessKey { get; set; }

        /// <summary>
        /// The secondary connection string for the SignalR service.
        /// </summary>
        [Input("secondaryConnectionString")]
        public Input<string>? SecondaryConnectionString { get; set; }

        /// <summary>
        /// The publicly accessible port of the SignalR service which is designed for customer server side use.
        /// </summary>
        [Input("serverPort")]
        public Input<int>? ServerPort { get; set; }

        /// <summary>
        /// A `sku` block as documented below.
        /// </summary>
        [Input("sku")]
        public Input<Inputs.ServiceSkuGetArgs>? Sku { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public ServiceState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class ServiceSkuArgs : Pulumi.ResourceArgs
    {
        [Input("capacity", required: true)]
        public Input<int> Capacity { get; set; } = null!;

        /// <summary>
        /// The name of the SignalR service. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public ServiceSkuArgs()
        {
        }
    }

    public sealed class ServiceSkuGetArgs : Pulumi.ResourceArgs
    {
        [Input("capacity", required: true)]
        public Input<int> Capacity { get; set; } = null!;

        /// <summary>
        /// The name of the SignalR service. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public ServiceSkuGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class ServiceSku
    {
        public readonly int Capacity;
        /// <summary>
        /// The name of the SignalR service. Changing this forces a new resource to be created.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private ServiceSku(
            int capacity,
            string name)
        {
            Capacity = capacity;
            Name = name;
        }
    }
    }
}