// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Monitoring.Inputs
{

    public sealed class MetricAlertApplicationInsightsWebTestLocationAvailabilityCriteriaArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the Application Insights Resource.
        /// </summary>
        [Input("componentId", required: true)]
        public Input<string> ComponentId { get; set; } = null!;

        /// <summary>
        /// The number of failed locations.
        /// </summary>
        [Input("failedLocationCount", required: true)]
        public Input<int> FailedLocationCount { get; set; } = null!;

        /// <summary>
        /// The ID of the Application Insights Web Test.
        /// </summary>
        [Input("webTestId", required: true)]
        public Input<string> WebTestId { get; set; } = null!;

        public MetricAlertApplicationInsightsWebTestLocationAvailabilityCriteriaArgs()
        {
        }
    }
}
