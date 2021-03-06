// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package synapse

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
	case "azure:synapse/firewallRule:FirewallRule":
		r, err = NewFirewallRule(ctx, name, nil, pulumi.URN_(urn))
	case "azure:synapse/managedPrivateEndpoint:ManagedPrivateEndpoint":
		r, err = NewManagedPrivateEndpoint(ctx, name, nil, pulumi.URN_(urn))
	case "azure:synapse/roleAssignment:RoleAssignment":
		r, err = NewRoleAssignment(ctx, name, nil, pulumi.URN_(urn))
	case "azure:synapse/sparkPool:SparkPool":
		r, err = NewSparkPool(ctx, name, nil, pulumi.URN_(urn))
	case "azure:synapse/sqlPool:SqlPool":
		r, err = NewSqlPool(ctx, name, nil, pulumi.URN_(urn))
	case "azure:synapse/workspace:Workspace":
		r, err = NewWorkspace(ctx, name, nil, pulumi.URN_(urn))
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
		"synapse/firewallRule",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"synapse/managedPrivateEndpoint",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"synapse/roleAssignment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"synapse/sparkPool",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"synapse/sqlPool",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"synapse/workspace",
		&module{version},
	)
}
