// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Monitoring.Inputs
{

    public sealed class ActionRuleActionGroupScopeArgs : Pulumi.ResourceArgs
    {
        [Input("resourceIds", required: true)]
        private InputList<string>? _resourceIds;

        /// <summary>
        /// A list of resource IDs of the given scope type which will be the target of action rule.
        /// </summary>
        public InputList<string> ResourceIds
        {
            get => _resourceIds ?? (_resourceIds = new InputList<string>());
            set => _resourceIds = value;
        }

        /// <summary>
        /// Specifies the type of target scope. Possible values are `ResourceGroup` and `Resource`.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public ActionRuleActionGroupScopeArgs()
        {
        }
    }
}
