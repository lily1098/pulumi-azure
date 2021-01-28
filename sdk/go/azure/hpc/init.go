// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hpc

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
	case "azure:hpc/cache:Cache":
		r, err = NewCache(ctx, name, nil, pulumi.URN_(urn))
	case "azure:hpc/cacheBlobTarget:CacheBlobTarget":
		r, err = NewCacheBlobTarget(ctx, name, nil, pulumi.URN_(urn))
	case "azure:hpc/cacheNfsTarget:CacheNfsTarget":
		r, err = NewCacheNfsTarget(ctx, name, nil, pulumi.URN_(urn))
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
		"hpc/cache",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"hpc/cacheBlobTarget",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"hpc/cacheNfsTarget",
		&module{version},
	)
}
