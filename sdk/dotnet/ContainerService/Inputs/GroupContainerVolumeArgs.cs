// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.ContainerService.Inputs
{

    public sealed class GroupContainerVolumeArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Boolean as to whether the mounted volume should be an empty directory. Defaults to `false`. Changing this forces a new resource to be created.
        /// </summary>
        [Input("emptyDir")]
        public Input<bool>? EmptyDir { get; set; }

        /// <summary>
        /// A `git_repo` block as defined below.
        /// </summary>
        [Input("gitRepo")]
        public Input<Inputs.GroupContainerVolumeGitRepoArgs>? GitRepo { get; set; }

        /// <summary>
        /// The path on which this volume is to be mounted. Changing this forces a new resource to be created.
        /// </summary>
        [Input("mountPath", required: true)]
        public Input<string> MountPath { get; set; } = null!;

        /// <summary>
        /// Specifies the name of the Container Group. Changing this forces a new resource to be created.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// Specify if the volume is to be mounted as read only or not. The default value is `false`. Changing this forces a new resource to be created.
        /// </summary>
        [Input("readOnly")]
        public Input<bool>? ReadOnly { get; set; }

        [Input("secret")]
        private InputMap<string>? _secret;

        /// <summary>
        /// A map of secrets that will be mounted as files in the volume. Changing this forces a new resource to be created.
        /// </summary>
        public InputMap<string> Secret
        {
            get => _secret ?? (_secret = new InputMap<string>());
            set => _secret = value;
        }

        /// <summary>
        /// The Azure storage share that is to be mounted as a volume. This must be created on the storage account specified as above. Changing this forces a new resource to be created.
        /// </summary>
        [Input("shareName")]
        public Input<string>? ShareName { get; set; }

        /// <summary>
        /// The access key for the Azure Storage account specified as above. Changing this forces a new resource to be created.
        /// </summary>
        [Input("storageAccountKey")]
        public Input<string>? StorageAccountKey { get; set; }

        /// <summary>
        /// The Azure storage account from which the volume is to be mounted. Changing this forces a new resource to be created.
        /// </summary>
        [Input("storageAccountName")]
        public Input<string>? StorageAccountName { get; set; }

        public GroupContainerVolumeArgs()
        {
        }
    }
}
