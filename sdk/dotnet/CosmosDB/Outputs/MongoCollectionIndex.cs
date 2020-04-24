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
    public sealed class MongoCollectionIndex
    {
        /// <summary>
        /// Specifies the list of user settable keys for each Cosmos DB Mongo Collection.
        /// </summary>
        public readonly ImmutableArray<string> Keys;
        /// <summary>
        /// Is the index unique or not? Defaults to `false`.
        /// </summary>
        public readonly bool? Unique;

        [OutputConstructor]
        private MongoCollectionIndex(
            ImmutableArray<string> keys,

            bool? unique)
        {
            Keys = keys;
            Unique = unique;
        }
    }
}
