// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.EventHub.Inputs
{

    public sealed class EventSubscriptionAdvancedFilterNumberInGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies the field within the event data that you want to use for filtering. Type of the field can be a number, boolean, or string.
        /// </summary>
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        [Input("values", required: true)]
        private InputList<double>? _values;

        /// <summary>
        /// Specifies an array of values to compare to when using a multiple values operator.
        /// </summary>
        public InputList<double> Values
        {
            get => _values ?? (_values = new InputList<double>());
            set => _values = value;
        }

        public EventSubscriptionAdvancedFilterNumberInGetArgs()
        {
        }
    }
}
