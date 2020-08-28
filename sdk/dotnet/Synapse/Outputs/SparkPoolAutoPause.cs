// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Synapse.Outputs
{

    [OutputType]
    public sealed class SparkPoolAutoPause
    {
        /// <summary>
        /// Number of minutes of idle time before the Spark Pool is automatically paused. Must be between `5` and `10080`.
        /// </summary>
        public readonly int DelayInMinutes;

        [OutputConstructor]
        private SparkPoolAutoPause(int delayInMinutes)
        {
            DelayInMinutes = delayInMinutes;
        }
    }
}