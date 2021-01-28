// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package siterecovery

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "azure:siterecovery/fabric:Fabric":
		r, err = NewFabric(ctx, name, nil, pulumi.URN_(urn))
	case "azure:siterecovery/networkMapping:NetworkMapping":
		r, err = NewNetworkMapping(ctx, name, nil, pulumi.URN_(urn))
	case "azure:siterecovery/protectionContainer:ProtectionContainer":
		r, err = NewProtectionContainer(ctx, name, nil, pulumi.URN_(urn))
	case "azure:siterecovery/protectionContainerMapping:ProtectionContainerMapping":
		r, err = NewProtectionContainerMapping(ctx, name, nil, pulumi.URN_(urn))
	case "azure:siterecovery/replicatedVM:ReplicatedVM":
		r, err = NewReplicatedVM(ctx, name, nil, pulumi.URN_(urn))
	case "azure:siterecovery/replicationPolicy:ReplicationPolicy":
		r, err = NewReplicationPolicy(ctx, name, nil, pulumi.URN_(urn))
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	return
}

func init() {
	version, err := azure.PkgVersion()
	if err != nil {
		fmt.Println("failed to determine package version. defaulting to v1: %v", err)
	}
	pulumi.RegisterResourceModule(
		"azure",
		"siterecovery/fabric",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"siterecovery/networkMapping",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"siterecovery/protectionContainer",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"siterecovery/protectionContainerMapping",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"siterecovery/replicatedVM",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"siterecovery/replicationPolicy",
		&module{version},
	)
}
