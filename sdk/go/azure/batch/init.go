// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package batch

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
	case "azure:batch/account:Account":
		r, err = NewAccount(ctx, name, nil, pulumi.URN_(urn))
	case "azure:batch/application:Application":
		r, err = NewApplication(ctx, name, nil, pulumi.URN_(urn))
	case "azure:batch/certificate:Certificate":
		r, err = NewCertificate(ctx, name, nil, pulumi.URN_(urn))
	case "azure:batch/pool:Pool":
		r, err = NewPool(ctx, name, nil, pulumi.URN_(urn))
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
		"batch/account",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"batch/application",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"batch/certificate",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"batch/pool",
		&module{version},
	)
}
