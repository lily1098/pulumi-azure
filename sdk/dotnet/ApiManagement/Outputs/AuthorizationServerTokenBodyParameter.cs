// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.ApiManagement.Outputs
{

    [OutputType]
    public sealed class AuthorizationServerTokenBodyParameter
    {
        /// <summary>
        /// The Name of the Parameter.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The Value of the Parameter.
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private AuthorizationServerTokenBodyParameter(
            string name,

            string value)
        {
            Name = name;
            Value = value;
        }
    }
}