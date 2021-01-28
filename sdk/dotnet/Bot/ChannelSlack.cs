// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Bot
{
    /// <summary>
    /// Manages a Slack integration for a Bot Channel
    /// 
    /// &gt; **Note** A bot can only have a single Slack Channel associated with it.
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
    ///         var current = Output.Create(Azure.Core.GetClientConfig.InvokeAsync());
    ///         var exampleResourceGroup = new Azure.Core.ResourceGroup("exampleResourceGroup", new Azure.Core.ResourceGroupArgs
    ///         {
    ///             Location = "northeurope",
    ///         });
    ///         var exampleChannelsRegistration = new Azure.Bot.ChannelsRegistration("exampleChannelsRegistration", new Azure.Bot.ChannelsRegistrationArgs
    ///         {
    ///             Location = "global",
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             Sku = "F0",
    ///             MicrosoftAppId = current.Apply(current =&gt; current.ClientId),
    ///         });
    ///         var exampleChannelSlack = new Azure.Bot.ChannelSlack("exampleChannelSlack", new Azure.Bot.ChannelSlackArgs
    ///         {
    ///             BotName = exampleChannelsRegistration.Name,
    ///             Location = exampleChannelsRegistration.Location,
    ///             ResourceGroupName = exampleResourceGroup.Name,
    ///             ClientId = "exampleId",
    ///             ClientSecret = "exampleSecret",
    ///             VerificationToken = "exampleVerificationToken",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// The Slack Integration for a Bot Channel can be imported using the `resource id`, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import azure:bot/channelSlack:ChannelSlack example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example/providers/Microsoft.BotService/botServices/example/channels/SlackChannel
    /// ```
    /// </summary>
    [AzureResourceType("azure:bot/channelSlack:ChannelSlack")]
    public partial class ChannelSlack : Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        /// </summary>
        [Output("botName")]
        public Output<string> BotName { get; private set; } = null!;

        /// <summary>
        /// The Client ID that will be used to authenticate with Slack.
        /// </summary>
        [Output("clientId")]
        public Output<string> ClientId { get; private set; } = null!;

        /// <summary>
        /// The Client Secret that will be used to authenticate with Slack.
        /// </summary>
        [Output("clientSecret")]
        public Output<string> ClientSecret { get; private set; } = null!;

        /// <summary>
        /// The Slack Landing Page URL.
        /// </summary>
        [Output("landingPageUrl")]
        public Output<string?> LandingPageUrl { get; private set; } = null!;

        /// <summary>
        /// The supported Azure location where the resource exists. Changing this forces a new resource to be created.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// The name of the resource group in which to create the Bot Channel. Changing this forces a new resource to be created.
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;

        /// <summary>
        /// The Verification Token that will be used to authenticate with Slack.
        /// </summary>
        [Output("verificationToken")]
        public Output<string> VerificationToken { get; private set; } = null!;


        /// <summary>
        /// Create a ChannelSlack resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ChannelSlack(string name, ChannelSlackArgs args, CustomResourceOptions? options = null)
            : base("azure:bot/channelSlack:ChannelSlack", name, args ?? new ChannelSlackArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ChannelSlack(string name, Input<string> id, ChannelSlackState? state = null, CustomResourceOptions? options = null)
            : base("azure:bot/channelSlack:ChannelSlack", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ChannelSlack resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ChannelSlack Get(string name, Input<string> id, ChannelSlackState? state = null, CustomResourceOptions? options = null)
        {
            return new ChannelSlack(name, id, state, options);
        }
    }

    public sealed class ChannelSlackArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        /// </summary>
        [Input("botName", required: true)]
        public Input<string> BotName { get; set; } = null!;

        /// <summary>
        /// The Client ID that will be used to authenticate with Slack.
        /// </summary>
        [Input("clientId", required: true)]
        public Input<string> ClientId { get; set; } = null!;

        /// <summary>
        /// The Client Secret that will be used to authenticate with Slack.
        /// </summary>
        [Input("clientSecret", required: true)]
        public Input<string> ClientSecret { get; set; } = null!;

        /// <summary>
        /// The Slack Landing Page URL.
        /// </summary>
        [Input("landingPageUrl")]
        public Input<string>? LandingPageUrl { get; set; }

        /// <summary>
        /// The supported Azure location where the resource exists. Changing this forces a new resource to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The name of the resource group in which to create the Bot Channel. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// The Verification Token that will be used to authenticate with Slack.
        /// </summary>
        [Input("verificationToken", required: true)]
        public Input<string> VerificationToken { get; set; } = null!;

        public ChannelSlackArgs()
        {
        }
    }

    public sealed class ChannelSlackState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the Bot Resource this channel will be associated with. Changing this forces a new resource to be created.
        /// </summary>
        [Input("botName")]
        public Input<string>? BotName { get; set; }

        /// <summary>
        /// The Client ID that will be used to authenticate with Slack.
        /// </summary>
        [Input("clientId")]
        public Input<string>? ClientId { get; set; }

        /// <summary>
        /// The Client Secret that will be used to authenticate with Slack.
        /// </summary>
        [Input("clientSecret")]
        public Input<string>? ClientSecret { get; set; }

        /// <summary>
        /// The Slack Landing Page URL.
        /// </summary>
        [Input("landingPageUrl")]
        public Input<string>? LandingPageUrl { get; set; }

        /// <summary>
        /// The supported Azure location where the resource exists. Changing this forces a new resource to be created.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The name of the resource group in which to create the Bot Channel. Changing this forces a new resource to be created.
        /// </summary>
        [Input("resourceGroupName")]
        public Input<string>? ResourceGroupName { get; set; }

        /// <summary>
        /// The Verification Token that will be used to authenticate with Slack.
        /// </summary>
        [Input("verificationToken")]
        public Input<string>? VerificationToken { get; set; }

        public ChannelSlackState()
        {
        }
    }
}
