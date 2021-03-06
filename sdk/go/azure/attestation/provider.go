// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package attestation

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type Provider struct {
	pulumi.CustomResourceState

	AttestationUri               pulumi.StringOutput    `pulumi:"attestationUri"`
	Location                     pulumi.StringOutput    `pulumi:"location"`
	Name                         pulumi.StringOutput    `pulumi:"name"`
	PolicySigningCertificateData pulumi.StringPtrOutput `pulumi:"policySigningCertificateData"`
	ResourceGroupName            pulumi.StringOutput    `pulumi:"resourceGroupName"`
	Tags                         pulumi.StringMapOutput `pulumi:"tags"`
	TrustModel                   pulumi.StringOutput    `pulumi:"trustModel"`
}

// NewProvider registers a new resource with the given unique name, arguments, and options.
func NewProvider(ctx *pulumi.Context,
	name string, args *ProviderArgs, opts ...pulumi.ResourceOption) (*Provider, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ResourceGroupName == nil {
		return nil, errors.New("invalid value for required argument 'ResourceGroupName'")
	}
	var resource Provider
	err := ctx.RegisterResource("azure:attestation/provider:Provider", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetProvider gets an existing Provider resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetProvider(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ProviderState, opts ...pulumi.ResourceOption) (*Provider, error) {
	var resource Provider
	err := ctx.ReadResource("azure:attestation/provider:Provider", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Provider resources.
type providerState struct {
	AttestationUri               *string           `pulumi:"attestationUri"`
	Location                     *string           `pulumi:"location"`
	Name                         *string           `pulumi:"name"`
	PolicySigningCertificateData *string           `pulumi:"policySigningCertificateData"`
	ResourceGroupName            *string           `pulumi:"resourceGroupName"`
	Tags                         map[string]string `pulumi:"tags"`
	TrustModel                   *string           `pulumi:"trustModel"`
}

type ProviderState struct {
	AttestationUri               pulumi.StringPtrInput
	Location                     pulumi.StringPtrInput
	Name                         pulumi.StringPtrInput
	PolicySigningCertificateData pulumi.StringPtrInput
	ResourceGroupName            pulumi.StringPtrInput
	Tags                         pulumi.StringMapInput
	TrustModel                   pulumi.StringPtrInput
}

func (ProviderState) ElementType() reflect.Type {
	return reflect.TypeOf((*providerState)(nil)).Elem()
}

type providerArgs struct {
	Location                     *string           `pulumi:"location"`
	Name                         *string           `pulumi:"name"`
	PolicySigningCertificateData *string           `pulumi:"policySigningCertificateData"`
	ResourceGroupName            string            `pulumi:"resourceGroupName"`
	Tags                         map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a Provider resource.
type ProviderArgs struct {
	Location                     pulumi.StringPtrInput
	Name                         pulumi.StringPtrInput
	PolicySigningCertificateData pulumi.StringPtrInput
	ResourceGroupName            pulumi.StringInput
	Tags                         pulumi.StringMapInput
}

func (ProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*providerArgs)(nil)).Elem()
}

type ProviderInput interface {
	pulumi.Input

	ToProviderOutput() ProviderOutput
	ToProviderOutputWithContext(ctx context.Context) ProviderOutput
}

func (*Provider) ElementType() reflect.Type {
	return reflect.TypeOf((*Provider)(nil))
}

func (i *Provider) ToProviderOutput() ProviderOutput {
	return i.ToProviderOutputWithContext(context.Background())
}

func (i *Provider) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderOutput)
}

func (i *Provider) ToProviderPtrOutput() ProviderPtrOutput {
	return i.ToProviderPtrOutputWithContext(context.Background())
}

func (i *Provider) ToProviderPtrOutputWithContext(ctx context.Context) ProviderPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderPtrOutput)
}

type ProviderPtrInput interface {
	pulumi.Input

	ToProviderPtrOutput() ProviderPtrOutput
	ToProviderPtrOutputWithContext(ctx context.Context) ProviderPtrOutput
}

type providerPtrType ProviderArgs

func (*providerPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil))
}

func (i *providerPtrType) ToProviderPtrOutput() ProviderPtrOutput {
	return i.ToProviderPtrOutputWithContext(context.Background())
}

func (i *providerPtrType) ToProviderPtrOutputWithContext(ctx context.Context) ProviderPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderPtrOutput)
}

// ProviderArrayInput is an input type that accepts ProviderArray and ProviderArrayOutput values.
// You can construct a concrete instance of `ProviderArrayInput` via:
//
//          ProviderArray{ ProviderArgs{...} }
type ProviderArrayInput interface {
	pulumi.Input

	ToProviderArrayOutput() ProviderArrayOutput
	ToProviderArrayOutputWithContext(context.Context) ProviderArrayOutput
}

type ProviderArray []ProviderInput

func (ProviderArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*Provider)(nil))
}

func (i ProviderArray) ToProviderArrayOutput() ProviderArrayOutput {
	return i.ToProviderArrayOutputWithContext(context.Background())
}

func (i ProviderArray) ToProviderArrayOutputWithContext(ctx context.Context) ProviderArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderArrayOutput)
}

// ProviderMapInput is an input type that accepts ProviderMap and ProviderMapOutput values.
// You can construct a concrete instance of `ProviderMapInput` via:
//
//          ProviderMap{ "key": ProviderArgs{...} }
type ProviderMapInput interface {
	pulumi.Input

	ToProviderMapOutput() ProviderMapOutput
	ToProviderMapOutputWithContext(context.Context) ProviderMapOutput
}

type ProviderMap map[string]ProviderInput

func (ProviderMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*Provider)(nil))
}

func (i ProviderMap) ToProviderMapOutput() ProviderMapOutput {
	return i.ToProviderMapOutputWithContext(context.Background())
}

func (i ProviderMap) ToProviderMapOutputWithContext(ctx context.Context) ProviderMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderMapOutput)
}

type ProviderOutput struct {
	*pulumi.OutputState
}

func (ProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Provider)(nil))
}

func (o ProviderOutput) ToProviderOutput() ProviderOutput {
	return o
}

func (o ProviderOutput) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return o
}

func (o ProviderOutput) ToProviderPtrOutput() ProviderPtrOutput {
	return o.ToProviderPtrOutputWithContext(context.Background())
}

func (o ProviderOutput) ToProviderPtrOutputWithContext(ctx context.Context) ProviderPtrOutput {
	return o.ApplyT(func(v Provider) *Provider {
		return &v
	}).(ProviderPtrOutput)
}

type ProviderPtrOutput struct {
	*pulumi.OutputState
}

func (ProviderPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil))
}

func (o ProviderPtrOutput) ToProviderPtrOutput() ProviderPtrOutput {
	return o
}

func (o ProviderPtrOutput) ToProviderPtrOutputWithContext(ctx context.Context) ProviderPtrOutput {
	return o
}

type ProviderArrayOutput struct{ *pulumi.OutputState }

func (ProviderArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Provider)(nil))
}

func (o ProviderArrayOutput) ToProviderArrayOutput() ProviderArrayOutput {
	return o
}

func (o ProviderArrayOutput) ToProviderArrayOutputWithContext(ctx context.Context) ProviderArrayOutput {
	return o
}

func (o ProviderArrayOutput) Index(i pulumi.IntInput) ProviderOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Provider {
		return vs[0].([]Provider)[vs[1].(int)]
	}).(ProviderOutput)
}

type ProviderMapOutput struct{ *pulumi.OutputState }

func (ProviderMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]Provider)(nil))
}

func (o ProviderMapOutput) ToProviderMapOutput() ProviderMapOutput {
	return o
}

func (o ProviderMapOutput) ToProviderMapOutputWithContext(ctx context.Context) ProviderMapOutput {
	return o
}

func (o ProviderMapOutput) MapIndex(k pulumi.StringInput) ProviderOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) Provider {
		return vs[0].(map[string]Provider)[vs[1].(string)]
	}).(ProviderOutput)
}

func init() {
	pulumi.RegisterOutputType(ProviderOutput{})
	pulumi.RegisterOutputType(ProviderPtrOutput{})
	pulumi.RegisterOutputType(ProviderArrayOutput{})
	pulumi.RegisterOutputType(ProviderMapOutput{})
}
