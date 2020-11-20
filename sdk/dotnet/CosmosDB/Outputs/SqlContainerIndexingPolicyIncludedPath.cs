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
    public sealed class SqlContainerIndexingPolicyIncludedPath
    {
        /// <summary>
        /// Path for which the indexing behaviour applies to.
        /// </summary>
        public readonly string Path;

        [OutputConstructor]
        private SqlContainerIndexingPolicyIncludedPath(string path)
        {
            Path = path;
        }
    }
}
