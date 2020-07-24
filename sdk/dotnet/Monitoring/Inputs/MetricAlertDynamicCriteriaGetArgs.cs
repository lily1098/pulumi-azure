// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Monitoring.Inputs
{

    public sealed class MetricAlertDynamicCriteriaGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The statistic that runs over the metric values. Possible values are `Average`, `Count`, `Minimum`, `Maximum` and `Total`.
        /// </summary>
        [Input("aggregation", required: true)]
        public Input<string> Aggregation { get; set; } = null!;

        /// <summary>
        /// The extent of deviation required to trigger an alert. Possible values are `Low`, `Medium` and `High`.
        /// </summary>
        [Input("alertSensitivity", required: true)]
        public Input<string> AlertSensitivity { get; set; } = null!;

        [Input("dimensions")]
        private InputList<Inputs.MetricAlertDynamicCriteriaDimensionGetArgs>? _dimensions;

        /// <summary>
        /// One or more `dimension` blocks as defined below.
        /// </summary>
        public InputList<Inputs.MetricAlertDynamicCriteriaDimensionGetArgs> Dimensions
        {
            get => _dimensions ?? (_dimensions = new InputList<Inputs.MetricAlertDynamicCriteriaDimensionGetArgs>());
            set => _dimensions = value;
        }

        /// <summary>
        /// The number of violations to trigger an alert. Should be smaller or equal to `evaluation_total_count`.
        /// </summary>
        [Input("evaluationFailureCount")]
        public Input<int>? EvaluationFailureCount { get; set; }

        /// <summary>
        /// The number of aggregated lookback points. The lookback time window is calculated based on the aggregation granularity (`window_size`) and the selected number of aggregated points.
        /// </summary>
        [Input("evaluationTotalCount")]
        public Input<int>? EvaluationTotalCount { get; set; }

        /// <summary>
        /// The [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) date from which to start learning the metric historical data and calculate the dynamic thresholds.
        /// </summary>
        [Input("ignoreDataBefore")]
        public Input<string>? IgnoreDataBefore { get; set; }

        /// <summary>
        /// One of the metric names to be monitored.
        /// </summary>
        [Input("metricName", required: true)]
        public Input<string> MetricName { get; set; } = null!;

        /// <summary>
        /// One of the metric namespaces to be monitored.
        /// </summary>
        [Input("metricNamespace", required: true)]
        public Input<string> MetricNamespace { get; set; } = null!;

        /// <summary>
        /// The criteria operator. Possible values are `LessThan`, `GreaterThan` and `GreaterOrLessThan`.
        /// </summary>
        [Input("operator", required: true)]
        public Input<string> Operator { get; set; } = null!;

        public MetricAlertDynamicCriteriaGetArgs()
        {
        }
    }
}
