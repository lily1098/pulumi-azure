// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Azure.AppService.Outputs
{

    [OutputType]
    public sealed class FunctionAppSlotSiteConfig
    {
        /// <summary>
        /// Should the Function App be loaded at all times? Defaults to `false`.
        /// </summary>
        public readonly bool? AlwaysOn;
        /// <summary>
        /// The name of the slot to automatically swap to during deployment
        /// </summary>
        public readonly string? AutoSwapSlotName;
        /// <summary>
        /// A `cors` block as defined below.
        /// </summary>
        public readonly Outputs.FunctionAppSlotSiteConfigCors? Cors;
        /// <summary>
        /// State of FTP / FTPS service for this function app. Possible values include: `AllAllowed`, `FtpsOnly` and `Disabled`.
        /// </summary>
        public readonly string? FtpsState;
        public readonly string? HealthCheckPath;
        /// <summary>
        /// Specifies whether or not the http2 protocol should be enabled. Defaults to `false`.
        /// </summary>
        public readonly bool? Http2Enabled;
        /// <summary>
        /// A [List of objects](https://www.terraform.io/docs/configuration/attr-as-blocks.html) representing ip restrictions as defined below.
        /// </summary>
        public readonly ImmutableArray<Outputs.FunctionAppSlotSiteConfigIpRestriction> IpRestrictions;
        /// <summary>
        /// Linux App Framework and version for the AppService, e.g. `DOCKER|(golang:latest)`.
        /// </summary>
        public readonly string? LinuxFxVersion;
        /// <summary>
        /// The minimum supported TLS version for the function app. Possible values are `1.0`, `1.1`, and `1.2`. Defaults to `1.2` for new function apps.
        /// </summary>
        public readonly string? MinTlsVersion;
        /// <summary>
        /// The number of pre-warmed instances for this function app. Only affects apps on the Premium plan.
        /// </summary>
        public readonly int? PreWarmedInstanceCount;
        public readonly ImmutableArray<Outputs.FunctionAppSlotSiteConfigScmIpRestriction> ScmIpRestrictions;
        public readonly string? ScmType;
        public readonly bool? ScmUseMainIpRestriction;
        /// <summary>
        /// Should the Function App run in 32 bit mode, rather than 64 bit mode? Defaults to `true`.
        /// </summary>
        public readonly bool? Use32BitWorkerProcess;
        /// <summary>
        /// Should WebSockets be enabled?
        /// </summary>
        public readonly bool? WebsocketsEnabled;

        [OutputConstructor]
        private FunctionAppSlotSiteConfig(
            bool? alwaysOn,

            string? autoSwapSlotName,

            Outputs.FunctionAppSlotSiteConfigCors? cors,

            string? ftpsState,

            string? healthCheckPath,

            bool? http2Enabled,

            ImmutableArray<Outputs.FunctionAppSlotSiteConfigIpRestriction> ipRestrictions,

            string? linuxFxVersion,

            string? minTlsVersion,

            int? preWarmedInstanceCount,

            ImmutableArray<Outputs.FunctionAppSlotSiteConfigScmIpRestriction> scmIpRestrictions,

            string? scmType,

            bool? scmUseMainIpRestriction,

            bool? use32BitWorkerProcess,

            bool? websocketsEnabled)
        {
            AlwaysOn = alwaysOn;
            AutoSwapSlotName = autoSwapSlotName;
            Cors = cors;
            FtpsState = ftpsState;
            HealthCheckPath = healthCheckPath;
            Http2Enabled = http2Enabled;
            IpRestrictions = ipRestrictions;
            LinuxFxVersion = linuxFxVersion;
            MinTlsVersion = minTlsVersion;
            PreWarmedInstanceCount = preWarmedInstanceCount;
            ScmIpRestrictions = scmIpRestrictions;
            ScmType = scmType;
            ScmUseMainIpRestriction = scmUseMainIpRestriction;
            Use32BitWorkerProcess = use32BitWorkerProcess;
            WebsocketsEnabled = websocketsEnabled;
        }
    }
}
