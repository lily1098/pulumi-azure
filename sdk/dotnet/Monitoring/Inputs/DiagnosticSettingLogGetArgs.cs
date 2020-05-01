// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Monitoring.Inputs
{

    public sealed class DiagnosticSettingLogGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of a Diagnostic Log Category for this Resource.
        /// </summary>
        [Input("category", required: true)]
        public Input<string> Category { get; set; } = null!;

        /// <summary>
        /// Is this Diagnostic Log enabled? Defaults to `true`.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// A `retention_policy` block as defined below.
        /// </summary>
        [Input("retentionPolicy")]
        public Input<Inputs.DiagnosticSettingLogRetentionPolicyGetArgs>? RetentionPolicy { get; set; }

        public DiagnosticSettingLogGetArgs()
        {
        }
    }
}
