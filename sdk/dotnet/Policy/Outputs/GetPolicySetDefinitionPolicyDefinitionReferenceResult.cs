// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Policy.Outputs
{

    [OutputType]
    public sealed class GetPolicySetDefinitionPolicyDefinitionReferenceResult
    {
        /// <summary>
        /// Any Parameters defined in the Policy Set Definition.
        /// </summary>
        public readonly ImmutableDictionary<string, object> Parameters;
        public readonly string PolicyDefinitionId;
        public readonly string ReferenceId;

        [OutputConstructor]
        private GetPolicySetDefinitionPolicyDefinitionReferenceResult(
            ImmutableDictionary<string, object> parameters,

            string policyDefinitionId,

            string referenceId)
        {
            Parameters = parameters;
            PolicyDefinitionId = policyDefinitionId;
            ReferenceId = referenceId;
        }
    }
}
