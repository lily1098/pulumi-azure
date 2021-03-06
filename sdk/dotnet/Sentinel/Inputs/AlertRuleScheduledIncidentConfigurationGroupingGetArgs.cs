// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Sentinel.Inputs
{

    public sealed class AlertRuleScheduledIncidentConfigurationGroupingGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Enable grouping incidents created from alerts triggered by this Sentinel Scheduled Alert Rule. Defaults to `true`.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The method used to group incidents. Possible values are `All`, `Custom` and `None`. Defaults to `None`.
        /// </summary>
        [Input("entityMatchingMethod")]
        public Input<string>? EntityMatchingMethod { get; set; }

        [Input("groupBies")]
        private InputList<string>? _groupBies;

        /// <summary>
        /// A list of entity types to group by, only when the `entity_matching_method` is `Custom`. Possible values are `Account`, `Host`, `Url`, `Ip`.
        /// </summary>
        public InputList<string> GroupBies
        {
            get => _groupBies ?? (_groupBies = new InputList<string>());
            set => _groupBies = value;
        }

        /// <summary>
        /// Limit the group to alerts created within the lookback duration (in ISO 8601 duration format). Defaults to `PT5M`.
        /// </summary>
        [Input("lookbackDuration")]
        public Input<string>? LookbackDuration { get; set; }

        /// <summary>
        /// Whether to re-open closed matching incidents? Defaults to `false`.
        /// </summary>
        [Input("reopenClosedIncidents")]
        public Input<bool>? ReopenClosedIncidents { get; set; }

        public AlertRuleScheduledIncidentConfigurationGroupingGetArgs()
        {
        }
    }
}
