// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Network.Outputs
{

    [OutputType]
    public sealed class RouteFilterRule
    {
        /// <summary>
        /// The access type of the rule. The only possible value is `Allow`.
        /// </summary>
        public readonly string Access;
        /// <summary>
        /// The collection for bgp community values to filter on. e.g. ['12076:5010','12076:5020'].
        /// </summary>
        public readonly ImmutableArray<string> Communities;
        /// <summary>
        /// The name of the route filter rule.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The rule type of the rule. The only possible value is `Community`.
        /// </summary>
        public readonly string RuleType;

        [OutputConstructor]
        private RouteFilterRule(
            string access,

            ImmutableArray<string> communities,

            string name,

            string ruleType)
        {
            Access = access;
            Communities = communities;
            Name = name;
            RuleType = ruleType;
        }
    }
}
