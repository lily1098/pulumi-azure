// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Dns.Inputs
{

    public sealed class MxRecordRecordArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The mail server responsible for the domain covered by the MX record.
        /// </summary>
        [Input("exchange", required: true)]
        public Input<string> Exchange { get; set; } = null!;

        /// <summary>
        /// String representing the "preference” value of the MX records. Records with lower preference value take priority.
        /// </summary>
        [Input("preference", required: true)]
        public Input<string> Preference { get; set; } = null!;

        public MxRecordRecordArgs()
        {
        }
    }
}