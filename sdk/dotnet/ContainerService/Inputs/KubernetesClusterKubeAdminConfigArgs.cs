// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.ContainerService.Inputs
{

    public sealed class KubernetesClusterKubeAdminConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
        /// </summary>
        [Input("clientCertificate")]
        public Input<string>? ClientCertificate { get; set; }

        /// <summary>
        /// Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
        /// </summary>
        [Input("clientKey")]
        public Input<string>? ClientKey { get; set; }

        /// <summary>
        /// Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
        /// </summary>
        [Input("clusterCaCertificate")]
        public Input<string>? ClusterCaCertificate { get; set; }

        /// <summary>
        /// The Kubernetes cluster server host.
        /// </summary>
        [Input("host")]
        public Input<string>? Host { get; set; }

        /// <summary>
        /// A password or token used to authenticate to the Kubernetes cluster.
        /// </summary>
        [Input("password")]
        public Input<string>? Password { get; set; }

        /// <summary>
        /// A username used to authenticate to the Kubernetes cluster.
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        public KubernetesClusterKubeAdminConfigArgs()
        {
        }
    }
}
