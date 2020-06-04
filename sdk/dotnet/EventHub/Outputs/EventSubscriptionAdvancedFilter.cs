// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.EventHub.Outputs
{

    [OutputType]
    public sealed class EventSubscriptionAdvancedFilter
    {
        /// <summary>
        /// Compares a value of an event using a single boolean value.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventSubscriptionAdvancedFilterBoolEqual> BoolEquals;
        /// <summary>
        /// Compares a value of an event using a single floating point number.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventSubscriptionAdvancedFilterNumberGreaterThanOrEqual> NumberGreaterThanOrEquals;
        /// <summary>
        /// Compares a value of an event using a single floating point number.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventSubscriptionAdvancedFilterNumberGreaterThan> NumberGreaterThans;
        /// <summary>
        /// Compares a value of an event using multiple floating point numbers.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventSubscriptionAdvancedFilterNumberIn> NumberIns;
        /// <summary>
        /// Compares a value of an event using a single floating point number.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventSubscriptionAdvancedFilterNumberLessThanOrEqual> NumberLessThanOrEquals;
        /// <summary>
        /// Compares a value of an event using a single floating point number.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventSubscriptionAdvancedFilterNumberLessThan> NumberLessThans;
        /// <summary>
        /// Compares a value of an event using multiple floating point numbers.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventSubscriptionAdvancedFilterNumberNotIn> NumberNotIns;
        /// <summary>
        /// Compares a value of an event using multiple string values.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventSubscriptionAdvancedFilterStringBeginsWith> StringBeginsWiths;
        /// <summary>
        /// Compares a value of an event using multiple string values.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventSubscriptionAdvancedFilterStringContain> StringContains;
        /// <summary>
        /// Compares a value of an event using multiple string values.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventSubscriptionAdvancedFilterStringEndsWith> StringEndsWiths;
        /// <summary>
        /// Compares a value of an event using multiple string values.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventSubscriptionAdvancedFilterStringIn> StringIns;
        /// <summary>
        /// Compares a value of an event using multiple string values.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventSubscriptionAdvancedFilterStringNotIn> StringNotIns;

        [OutputConstructor]
        private EventSubscriptionAdvancedFilter(
            ImmutableArray<Outputs.EventSubscriptionAdvancedFilterBoolEqual> boolEquals,

            ImmutableArray<Outputs.EventSubscriptionAdvancedFilterNumberGreaterThanOrEqual> numberGreaterThanOrEquals,

            ImmutableArray<Outputs.EventSubscriptionAdvancedFilterNumberGreaterThan> numberGreaterThans,

            ImmutableArray<Outputs.EventSubscriptionAdvancedFilterNumberIn> numberIns,

            ImmutableArray<Outputs.EventSubscriptionAdvancedFilterNumberLessThanOrEqual> numberLessThanOrEquals,

            ImmutableArray<Outputs.EventSubscriptionAdvancedFilterNumberLessThan> numberLessThans,

            ImmutableArray<Outputs.EventSubscriptionAdvancedFilterNumberNotIn> numberNotIns,

            ImmutableArray<Outputs.EventSubscriptionAdvancedFilterStringBeginsWith> stringBeginsWiths,

            ImmutableArray<Outputs.EventSubscriptionAdvancedFilterStringContain> stringContains,

            ImmutableArray<Outputs.EventSubscriptionAdvancedFilterStringEndsWith> stringEndsWiths,

            ImmutableArray<Outputs.EventSubscriptionAdvancedFilterStringIn> stringIns,

            ImmutableArray<Outputs.EventSubscriptionAdvancedFilterStringNotIn> stringNotIns)
        {
            BoolEquals = boolEquals;
            NumberGreaterThanOrEquals = numberGreaterThanOrEquals;
            NumberGreaterThans = numberGreaterThans;
            NumberIns = numberIns;
            NumberLessThanOrEquals = numberLessThanOrEquals;
            NumberLessThans = numberLessThans;
            NumberNotIns = numberNotIns;
            StringBeginsWiths = stringBeginsWiths;
            StringContains = stringContains;
            StringEndsWiths = stringEndsWiths;
            StringIns = stringIns;
            StringNotIns = stringNotIns;
        }
    }
}
