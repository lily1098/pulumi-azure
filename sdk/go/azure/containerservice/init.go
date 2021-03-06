// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package containerservice

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
	case "azure:containerservice/group:Group":
		r, err = NewGroup(ctx, name, nil, pulumi.URN_(urn))
	case "azure:containerservice/kubernetesCluster:KubernetesCluster":
		r, err = NewKubernetesCluster(ctx, name, nil, pulumi.URN_(urn))
	case "azure:containerservice/kubernetesClusterNodePool:KubernetesClusterNodePool":
		r, err = NewKubernetesClusterNodePool(ctx, name, nil, pulumi.URN_(urn))
	case "azure:containerservice/registry:Registry":
		r, err = NewRegistry(ctx, name, nil, pulumi.URN_(urn))
	case "azure:containerservice/registryWebhook:RegistryWebhook":
		r, err = NewRegistryWebhook(ctx, name, nil, pulumi.URN_(urn))
	case "azure:containerservice/registryWebook:RegistryWebook":
		r, err = NewRegistryWebook(ctx, name, nil, pulumi.URN_(urn))
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
		"containerservice/group",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"containerservice/kubernetesCluster",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"containerservice/kubernetesClusterNodePool",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"containerservice/registry",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"containerservice/registryWebhook",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"containerservice/registryWebook",
		&module{version},
	)
}
