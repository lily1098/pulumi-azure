// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.CosmosDB.Outputs
{

    [OutputType]
    public sealed class CassandraTableSchemaPartitionKey
    {
        /// <summary>
        /// Name of the column to partition by.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private CassandraTableSchemaPartitionKey(string name)
        {
            Name = name;
        }
    }
}