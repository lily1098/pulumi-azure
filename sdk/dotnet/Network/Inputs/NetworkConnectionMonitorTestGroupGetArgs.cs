// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.Network.Inputs
{

    public sealed class NetworkConnectionMonitorTestGroupGetArgs : Pulumi.ResourceArgs
    {
        [Input("destinationEndpoints", required: true)]
        private InputList<string>? _destinationEndpoints;

        /// <summary>
        /// A list of destination endpoint names.
        /// </summary>
        public InputList<string> DestinationEndpoints
        {
            get => _destinationEndpoints ?? (_destinationEndpoints = new InputList<string>());
            set => _destinationEndpoints = value;
        }

        /// <summary>
        /// Should the test group be enabled? Defaults to `true`.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The name of the test group for the Network Connection Monitor.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("sourceEndpoints", required: true)]
        private InputList<string>? _sourceEndpoints;

        /// <summary>
        /// A list of source endpoint names.
        /// </summary>
        public InputList<string> SourceEndpoints
        {
            get => _sourceEndpoints ?? (_sourceEndpoints = new InputList<string>());
            set => _sourceEndpoints = value;
        }

        [Input("testConfigurationNames", required: true)]
        private InputList<string>? _testConfigurationNames;

        /// <summary>
        /// A list of test configuration names.
        /// </summary>
        public InputList<string> TestConfigurationNames
        {
            get => _testConfigurationNames ?? (_testConfigurationNames = new InputList<string>());
            set => _testConfigurationNames = value;
        }

        public NetworkConnectionMonitorTestGroupGetArgs()
        {
        }
    }
}
