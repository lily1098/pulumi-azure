// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package policy

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
	case "azure:policy/assignment:Assignment":
		r, err = NewAssignment(ctx, name, nil, pulumi.URN_(urn))
	case "azure:policy/definition:Definition":
		r, err = NewDefinition(ctx, name, nil, pulumi.URN_(urn))
	case "azure:policy/policySetDefinition:PolicySetDefinition":
		r, err = NewPolicySetDefinition(ctx, name, nil, pulumi.URN_(urn))
	case "azure:policy/remediation:Remediation":
		r, err = NewRemediation(ctx, name, nil, pulumi.URN_(urn))
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
		"policy/assignment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"policy/definition",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"policy/policySetDefinition",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"policy/remediation",
		&module{version},
	)
}
