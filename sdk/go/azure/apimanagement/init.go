// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apimanagement

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
	case "azure:apimanagement/api:Api":
		r, err = NewApi(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/apiDiagnostic:ApiDiagnostic":
		r, err = NewApiDiagnostic(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/apiOperation:ApiOperation":
		r, err = NewApiOperation(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/apiOperationPolicy:ApiOperationPolicy":
		r, err = NewApiOperationPolicy(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/apiPolicy:ApiPolicy":
		r, err = NewApiPolicy(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/apiSchema:ApiSchema":
		r, err = NewApiSchema(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/apiVersionSet:ApiVersionSet":
		r, err = NewApiVersionSet(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/authorizationServer:AuthorizationServer":
		r, err = NewAuthorizationServer(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/backend:Backend":
		r, err = NewBackend(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/certificate:Certificate":
		r, err = NewCertificate(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/customDomain:CustomDomain":
		r, err = NewCustomDomain(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/diagnostic:Diagnostic":
		r, err = NewDiagnostic(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/group:Group":
		r, err = NewGroup(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/groupUser:GroupUser":
		r, err = NewGroupUser(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/identityProviderAad:IdentityProviderAad":
		r, err = NewIdentityProviderAad(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/identityProviderAadb2c:IdentityProviderAadb2c":
		r, err = NewIdentityProviderAadb2c(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/identityProviderFacebook:IdentityProviderFacebook":
		r, err = NewIdentityProviderFacebook(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/identityProviderGoogle:IdentityProviderGoogle":
		r, err = NewIdentityProviderGoogle(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/identityProviderMicrosoft:IdentityProviderMicrosoft":
		r, err = NewIdentityProviderMicrosoft(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/identityProviderTwitter:IdentityProviderTwitter":
		r, err = NewIdentityProviderTwitter(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/logger:Logger":
		r, err = NewLogger(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/namedValue:NamedValue":
		r, err = NewNamedValue(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/openIdConnectProvider:OpenIdConnectProvider":
		r, err = NewOpenIdConnectProvider(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/policy:Policy":
		r, err = NewPolicy(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/product:Product":
		r, err = NewProduct(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/productApi:ProductApi":
		r, err = NewProductApi(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/productGroup:ProductGroup":
		r, err = NewProductGroup(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/productPolicy:ProductPolicy":
		r, err = NewProductPolicy(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/property:Property":
		r, err = NewProperty(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/service:Service":
		r, err = NewService(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/subscription:Subscription":
		r, err = NewSubscription(ctx, name, nil, pulumi.URN_(urn))
	case "azure:apimanagement/user:User":
		r, err = NewUser(ctx, name, nil, pulumi.URN_(urn))
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
		"apimanagement/api",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/apiDiagnostic",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/apiOperation",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/apiOperationPolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/apiPolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/apiSchema",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/apiVersionSet",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/authorizationServer",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/backend",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/certificate",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/customDomain",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/diagnostic",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/group",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/groupUser",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/identityProviderAad",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/identityProviderAadb2c",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/identityProviderFacebook",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/identityProviderGoogle",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/identityProviderMicrosoft",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/identityProviderTwitter",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/logger",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/namedValue",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/openIdConnectProvider",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/policy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/product",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/productApi",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/productGroup",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/productPolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/property",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/service",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/subscription",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"apimanagement/user",
		&module{version},
	)
}
