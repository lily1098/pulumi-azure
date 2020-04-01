// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package trafficmanager

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type EndpointCustomHeader struct {
	// The name of the custom header.
	Name string `pulumi:"name"`
	// The value of custom header. Applicable for Http and Https protocol.
	Value string `pulumi:"value"`
}

type EndpointCustomHeaderInput interface {
	pulumi.Input

	ToEndpointCustomHeaderOutput() EndpointCustomHeaderOutput
	ToEndpointCustomHeaderOutputWithContext(context.Context) EndpointCustomHeaderOutput
}

type EndpointCustomHeaderArgs struct {
	// The name of the custom header.
	Name pulumi.StringInput `pulumi:"name"`
	// The value of custom header. Applicable for Http and Https protocol.
	Value pulumi.StringInput `pulumi:"value"`
}

func (EndpointCustomHeaderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointCustomHeader)(nil)).Elem()
}

func (i EndpointCustomHeaderArgs) ToEndpointCustomHeaderOutput() EndpointCustomHeaderOutput {
	return i.ToEndpointCustomHeaderOutputWithContext(context.Background())
}

func (i EndpointCustomHeaderArgs) ToEndpointCustomHeaderOutputWithContext(ctx context.Context) EndpointCustomHeaderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointCustomHeaderOutput)
}

type EndpointCustomHeaderArrayInput interface {
	pulumi.Input

	ToEndpointCustomHeaderArrayOutput() EndpointCustomHeaderArrayOutput
	ToEndpointCustomHeaderArrayOutputWithContext(context.Context) EndpointCustomHeaderArrayOutput
}

type EndpointCustomHeaderArray []EndpointCustomHeaderInput

func (EndpointCustomHeaderArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EndpointCustomHeader)(nil)).Elem()
}

func (i EndpointCustomHeaderArray) ToEndpointCustomHeaderArrayOutput() EndpointCustomHeaderArrayOutput {
	return i.ToEndpointCustomHeaderArrayOutputWithContext(context.Background())
}

func (i EndpointCustomHeaderArray) ToEndpointCustomHeaderArrayOutputWithContext(ctx context.Context) EndpointCustomHeaderArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointCustomHeaderArrayOutput)
}

type EndpointCustomHeaderOutput struct{ *pulumi.OutputState }

func (EndpointCustomHeaderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointCustomHeader)(nil)).Elem()
}

func (o EndpointCustomHeaderOutput) ToEndpointCustomHeaderOutput() EndpointCustomHeaderOutput {
	return o
}

func (o EndpointCustomHeaderOutput) ToEndpointCustomHeaderOutputWithContext(ctx context.Context) EndpointCustomHeaderOutput {
	return o
}

// The name of the custom header.
func (o EndpointCustomHeaderOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v EndpointCustomHeader) string { return v.Name }).(pulumi.StringOutput)
}

// The value of custom header. Applicable for Http and Https protocol.
func (o EndpointCustomHeaderOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v EndpointCustomHeader) string { return v.Value }).(pulumi.StringOutput)
}

type EndpointCustomHeaderArrayOutput struct{ *pulumi.OutputState }

func (EndpointCustomHeaderArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EndpointCustomHeader)(nil)).Elem()
}

func (o EndpointCustomHeaderArrayOutput) ToEndpointCustomHeaderArrayOutput() EndpointCustomHeaderArrayOutput {
	return o
}

func (o EndpointCustomHeaderArrayOutput) ToEndpointCustomHeaderArrayOutputWithContext(ctx context.Context) EndpointCustomHeaderArrayOutput {
	return o
}

func (o EndpointCustomHeaderArrayOutput) Index(i pulumi.IntInput) EndpointCustomHeaderOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) EndpointCustomHeader {
		return vs[0].([]EndpointCustomHeader)[vs[1].(int)]
	}).(EndpointCustomHeaderOutput)
}

type EndpointSubnet struct {
	// The First IP....
	First string `pulumi:"first"`
	// The Last IP...
	Last *string `pulumi:"last"`
	// The Scope...
	Scope *int `pulumi:"scope"`
}

type EndpointSubnetInput interface {
	pulumi.Input

	ToEndpointSubnetOutput() EndpointSubnetOutput
	ToEndpointSubnetOutputWithContext(context.Context) EndpointSubnetOutput
}

type EndpointSubnetArgs struct {
	// The First IP....
	First pulumi.StringInput `pulumi:"first"`
	// The Last IP...
	Last pulumi.StringPtrInput `pulumi:"last"`
	// The Scope...
	Scope pulumi.IntPtrInput `pulumi:"scope"`
}

func (EndpointSubnetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointSubnet)(nil)).Elem()
}

func (i EndpointSubnetArgs) ToEndpointSubnetOutput() EndpointSubnetOutput {
	return i.ToEndpointSubnetOutputWithContext(context.Background())
}

func (i EndpointSubnetArgs) ToEndpointSubnetOutputWithContext(ctx context.Context) EndpointSubnetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointSubnetOutput)
}

type EndpointSubnetArrayInput interface {
	pulumi.Input

	ToEndpointSubnetArrayOutput() EndpointSubnetArrayOutput
	ToEndpointSubnetArrayOutputWithContext(context.Context) EndpointSubnetArrayOutput
}

type EndpointSubnetArray []EndpointSubnetInput

func (EndpointSubnetArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EndpointSubnet)(nil)).Elem()
}

func (i EndpointSubnetArray) ToEndpointSubnetArrayOutput() EndpointSubnetArrayOutput {
	return i.ToEndpointSubnetArrayOutputWithContext(context.Background())
}

func (i EndpointSubnetArray) ToEndpointSubnetArrayOutputWithContext(ctx context.Context) EndpointSubnetArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointSubnetArrayOutput)
}

type EndpointSubnetOutput struct{ *pulumi.OutputState }

func (EndpointSubnetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointSubnet)(nil)).Elem()
}

func (o EndpointSubnetOutput) ToEndpointSubnetOutput() EndpointSubnetOutput {
	return o
}

func (o EndpointSubnetOutput) ToEndpointSubnetOutputWithContext(ctx context.Context) EndpointSubnetOutput {
	return o
}

// The First IP....
func (o EndpointSubnetOutput) First() pulumi.StringOutput {
	return o.ApplyT(func(v EndpointSubnet) string { return v.First }).(pulumi.StringOutput)
}

// The Last IP...
func (o EndpointSubnetOutput) Last() pulumi.StringPtrOutput {
	return o.ApplyT(func(v EndpointSubnet) *string { return v.Last }).(pulumi.StringPtrOutput)
}

// The Scope...
func (o EndpointSubnetOutput) Scope() pulumi.IntPtrOutput {
	return o.ApplyT(func(v EndpointSubnet) *int { return v.Scope }).(pulumi.IntPtrOutput)
}

type EndpointSubnetArrayOutput struct{ *pulumi.OutputState }

func (EndpointSubnetArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EndpointSubnet)(nil)).Elem()
}

func (o EndpointSubnetArrayOutput) ToEndpointSubnetArrayOutput() EndpointSubnetArrayOutput {
	return o
}

func (o EndpointSubnetArrayOutput) ToEndpointSubnetArrayOutputWithContext(ctx context.Context) EndpointSubnetArrayOutput {
	return o
}

func (o EndpointSubnetArrayOutput) Index(i pulumi.IntInput) EndpointSubnetOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) EndpointSubnet {
		return vs[0].([]EndpointSubnet)[vs[1].(int)]
	}).(EndpointSubnetOutput)
}

type ProfileDnsConfig struct {
	// The relative domain name, this is combined with the domain name used by Traffic Manager to form the FQDN which is exported as documented below. Changing this forces a new resource to be created.
	RelativeName string `pulumi:"relativeName"`
	// The TTL value of the Profile used by Local DNS resolvers and clients.
	Ttl int `pulumi:"ttl"`
}

type ProfileDnsConfigInput interface {
	pulumi.Input

	ToProfileDnsConfigOutput() ProfileDnsConfigOutput
	ToProfileDnsConfigOutputWithContext(context.Context) ProfileDnsConfigOutput
}

type ProfileDnsConfigArgs struct {
	// The relative domain name, this is combined with the domain name used by Traffic Manager to form the FQDN which is exported as documented below. Changing this forces a new resource to be created.
	RelativeName pulumi.StringInput `pulumi:"relativeName"`
	// The TTL value of the Profile used by Local DNS resolvers and clients.
	Ttl pulumi.IntInput `pulumi:"ttl"`
}

func (ProfileDnsConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ProfileDnsConfig)(nil)).Elem()
}

func (i ProfileDnsConfigArgs) ToProfileDnsConfigOutput() ProfileDnsConfigOutput {
	return i.ToProfileDnsConfigOutputWithContext(context.Background())
}

func (i ProfileDnsConfigArgs) ToProfileDnsConfigOutputWithContext(ctx context.Context) ProfileDnsConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProfileDnsConfigOutput)
}

func (i ProfileDnsConfigArgs) ToProfileDnsConfigPtrOutput() ProfileDnsConfigPtrOutput {
	return i.ToProfileDnsConfigPtrOutputWithContext(context.Background())
}

func (i ProfileDnsConfigArgs) ToProfileDnsConfigPtrOutputWithContext(ctx context.Context) ProfileDnsConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProfileDnsConfigOutput).ToProfileDnsConfigPtrOutputWithContext(ctx)
}

type ProfileDnsConfigPtrInput interface {
	pulumi.Input

	ToProfileDnsConfigPtrOutput() ProfileDnsConfigPtrOutput
	ToProfileDnsConfigPtrOutputWithContext(context.Context) ProfileDnsConfigPtrOutput
}

type profileDnsConfigPtrType ProfileDnsConfigArgs

func ProfileDnsConfigPtr(v *ProfileDnsConfigArgs) ProfileDnsConfigPtrInput {
	return (*profileDnsConfigPtrType)(v)
}

func (*profileDnsConfigPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**ProfileDnsConfig)(nil)).Elem()
}

func (i *profileDnsConfigPtrType) ToProfileDnsConfigPtrOutput() ProfileDnsConfigPtrOutput {
	return i.ToProfileDnsConfigPtrOutputWithContext(context.Background())
}

func (i *profileDnsConfigPtrType) ToProfileDnsConfigPtrOutputWithContext(ctx context.Context) ProfileDnsConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProfileDnsConfigPtrOutput)
}

type ProfileDnsConfigOutput struct{ *pulumi.OutputState }

func (ProfileDnsConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ProfileDnsConfig)(nil)).Elem()
}

func (o ProfileDnsConfigOutput) ToProfileDnsConfigOutput() ProfileDnsConfigOutput {
	return o
}

func (o ProfileDnsConfigOutput) ToProfileDnsConfigOutputWithContext(ctx context.Context) ProfileDnsConfigOutput {
	return o
}

func (o ProfileDnsConfigOutput) ToProfileDnsConfigPtrOutput() ProfileDnsConfigPtrOutput {
	return o.ToProfileDnsConfigPtrOutputWithContext(context.Background())
}

func (o ProfileDnsConfigOutput) ToProfileDnsConfigPtrOutputWithContext(ctx context.Context) ProfileDnsConfigPtrOutput {
	return o.ApplyT(func(v ProfileDnsConfig) *ProfileDnsConfig {
		return &v
	}).(ProfileDnsConfigPtrOutput)
}

// The relative domain name, this is combined with the domain name used by Traffic Manager to form the FQDN which is exported as documented below. Changing this forces a new resource to be created.
func (o ProfileDnsConfigOutput) RelativeName() pulumi.StringOutput {
	return o.ApplyT(func(v ProfileDnsConfig) string { return v.RelativeName }).(pulumi.StringOutput)
}

// The TTL value of the Profile used by Local DNS resolvers and clients.
func (o ProfileDnsConfigOutput) Ttl() pulumi.IntOutput {
	return o.ApplyT(func(v ProfileDnsConfig) int { return v.Ttl }).(pulumi.IntOutput)
}

type ProfileDnsConfigPtrOutput struct{ *pulumi.OutputState }

func (ProfileDnsConfigPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ProfileDnsConfig)(nil)).Elem()
}

func (o ProfileDnsConfigPtrOutput) ToProfileDnsConfigPtrOutput() ProfileDnsConfigPtrOutput {
	return o
}

func (o ProfileDnsConfigPtrOutput) ToProfileDnsConfigPtrOutputWithContext(ctx context.Context) ProfileDnsConfigPtrOutput {
	return o
}

func (o ProfileDnsConfigPtrOutput) Elem() ProfileDnsConfigOutput {
	return o.ApplyT(func(v *ProfileDnsConfig) ProfileDnsConfig { return *v }).(ProfileDnsConfigOutput)
}

// The relative domain name, this is combined with the domain name used by Traffic Manager to form the FQDN which is exported as documented below. Changing this forces a new resource to be created.
func (o ProfileDnsConfigPtrOutput) RelativeName() pulumi.StringOutput {
	return o.ApplyT(func(v ProfileDnsConfig) string { return v.RelativeName }).(pulumi.StringOutput)
}

// The TTL value of the Profile used by Local DNS resolvers and clients.
func (o ProfileDnsConfigPtrOutput) Ttl() pulumi.IntOutput {
	return o.ApplyT(func(v ProfileDnsConfig) int { return v.Ttl }).(pulumi.IntOutput)
}

type ProfileMonitorConfig struct {
	// One or more `customHeader` blocks as defined below.
	CustomHeaders []ProfileMonitorConfigCustomHeader `pulumi:"customHeaders"`
	// A list of status code ranges in the format of `100-101`.
	ExpectedStatusCodeRanges []string `pulumi:"expectedStatusCodeRanges"`
	// The interval used to check the endpoint health from a Traffic Manager probing agent. You can specify two values here: `30` (normal probing) and `10` (fast probing). The default value is `30`.
	IntervalInSeconds *int `pulumi:"intervalInSeconds"`
	// The path used by the monitoring checks. Required when `protocol` is set to `HTTP` or `HTTPS` - cannot be set when `protocol` is set to `TCP`.
	Path *string `pulumi:"path"`
	// The port number used by the monitoring checks.
	Port int `pulumi:"port"`
	// The protocol used by the monitoring checks, supported values are `HTTP`, `HTTPS` and `TCP`.
	Protocol string `pulumi:"protocol"`
	// The amount of time the Traffic Manager probing agent should wait before considering that check a failure when a health check probe is sent to the endpoint. If `intervalInSeconds` is set to `30`, then `timeoutInSeconds` can be between `5` and `10`. The default value is `10`. If `intervalInSeconds` is set to `10`, then valid values are between `5` and `9` and `timeoutInSeconds` is required.
	TimeoutInSeconds *int `pulumi:"timeoutInSeconds"`
	// The number of failures a Traffic Manager probing agent tolerates before marking that endpoint as unhealthy. Valid values are between `0` and `9`. The default value is `3`
	ToleratedNumberOfFailures *int `pulumi:"toleratedNumberOfFailures"`
}

type ProfileMonitorConfigInput interface {
	pulumi.Input

	ToProfileMonitorConfigOutput() ProfileMonitorConfigOutput
	ToProfileMonitorConfigOutputWithContext(context.Context) ProfileMonitorConfigOutput
}

type ProfileMonitorConfigArgs struct {
	// One or more `customHeader` blocks as defined below.
	CustomHeaders ProfileMonitorConfigCustomHeaderArrayInput `pulumi:"customHeaders"`
	// A list of status code ranges in the format of `100-101`.
	ExpectedStatusCodeRanges pulumi.StringArrayInput `pulumi:"expectedStatusCodeRanges"`
	// The interval used to check the endpoint health from a Traffic Manager probing agent. You can specify two values here: `30` (normal probing) and `10` (fast probing). The default value is `30`.
	IntervalInSeconds pulumi.IntPtrInput `pulumi:"intervalInSeconds"`
	// The path used by the monitoring checks. Required when `protocol` is set to `HTTP` or `HTTPS` - cannot be set when `protocol` is set to `TCP`.
	Path pulumi.StringPtrInput `pulumi:"path"`
	// The port number used by the monitoring checks.
	Port pulumi.IntInput `pulumi:"port"`
	// The protocol used by the monitoring checks, supported values are `HTTP`, `HTTPS` and `TCP`.
	Protocol pulumi.StringInput `pulumi:"protocol"`
	// The amount of time the Traffic Manager probing agent should wait before considering that check a failure when a health check probe is sent to the endpoint. If `intervalInSeconds` is set to `30`, then `timeoutInSeconds` can be between `5` and `10`. The default value is `10`. If `intervalInSeconds` is set to `10`, then valid values are between `5` and `9` and `timeoutInSeconds` is required.
	TimeoutInSeconds pulumi.IntPtrInput `pulumi:"timeoutInSeconds"`
	// The number of failures a Traffic Manager probing agent tolerates before marking that endpoint as unhealthy. Valid values are between `0` and `9`. The default value is `3`
	ToleratedNumberOfFailures pulumi.IntPtrInput `pulumi:"toleratedNumberOfFailures"`
}

func (ProfileMonitorConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ProfileMonitorConfig)(nil)).Elem()
}

func (i ProfileMonitorConfigArgs) ToProfileMonitorConfigOutput() ProfileMonitorConfigOutput {
	return i.ToProfileMonitorConfigOutputWithContext(context.Background())
}

func (i ProfileMonitorConfigArgs) ToProfileMonitorConfigOutputWithContext(ctx context.Context) ProfileMonitorConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProfileMonitorConfigOutput)
}

func (i ProfileMonitorConfigArgs) ToProfileMonitorConfigPtrOutput() ProfileMonitorConfigPtrOutput {
	return i.ToProfileMonitorConfigPtrOutputWithContext(context.Background())
}

func (i ProfileMonitorConfigArgs) ToProfileMonitorConfigPtrOutputWithContext(ctx context.Context) ProfileMonitorConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProfileMonitorConfigOutput).ToProfileMonitorConfigPtrOutputWithContext(ctx)
}

type ProfileMonitorConfigPtrInput interface {
	pulumi.Input

	ToProfileMonitorConfigPtrOutput() ProfileMonitorConfigPtrOutput
	ToProfileMonitorConfigPtrOutputWithContext(context.Context) ProfileMonitorConfigPtrOutput
}

type profileMonitorConfigPtrType ProfileMonitorConfigArgs

func ProfileMonitorConfigPtr(v *ProfileMonitorConfigArgs) ProfileMonitorConfigPtrInput {
	return (*profileMonitorConfigPtrType)(v)
}

func (*profileMonitorConfigPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**ProfileMonitorConfig)(nil)).Elem()
}

func (i *profileMonitorConfigPtrType) ToProfileMonitorConfigPtrOutput() ProfileMonitorConfigPtrOutput {
	return i.ToProfileMonitorConfigPtrOutputWithContext(context.Background())
}

func (i *profileMonitorConfigPtrType) ToProfileMonitorConfigPtrOutputWithContext(ctx context.Context) ProfileMonitorConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProfileMonitorConfigPtrOutput)
}

type ProfileMonitorConfigOutput struct{ *pulumi.OutputState }

func (ProfileMonitorConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ProfileMonitorConfig)(nil)).Elem()
}

func (o ProfileMonitorConfigOutput) ToProfileMonitorConfigOutput() ProfileMonitorConfigOutput {
	return o
}

func (o ProfileMonitorConfigOutput) ToProfileMonitorConfigOutputWithContext(ctx context.Context) ProfileMonitorConfigOutput {
	return o
}

func (o ProfileMonitorConfigOutput) ToProfileMonitorConfigPtrOutput() ProfileMonitorConfigPtrOutput {
	return o.ToProfileMonitorConfigPtrOutputWithContext(context.Background())
}

func (o ProfileMonitorConfigOutput) ToProfileMonitorConfigPtrOutputWithContext(ctx context.Context) ProfileMonitorConfigPtrOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) *ProfileMonitorConfig {
		return &v
	}).(ProfileMonitorConfigPtrOutput)
}

// One or more `customHeader` blocks as defined below.
func (o ProfileMonitorConfigOutput) CustomHeaders() ProfileMonitorConfigCustomHeaderArrayOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) []ProfileMonitorConfigCustomHeader { return v.CustomHeaders }).(ProfileMonitorConfigCustomHeaderArrayOutput)
}

// A list of status code ranges in the format of `100-101`.
func (o ProfileMonitorConfigOutput) ExpectedStatusCodeRanges() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) []string { return v.ExpectedStatusCodeRanges }).(pulumi.StringArrayOutput)
}

// The interval used to check the endpoint health from a Traffic Manager probing agent. You can specify two values here: `30` (normal probing) and `10` (fast probing). The default value is `30`.
func (o ProfileMonitorConfigOutput) IntervalInSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) *int { return v.IntervalInSeconds }).(pulumi.IntPtrOutput)
}

// The path used by the monitoring checks. Required when `protocol` is set to `HTTP` or `HTTPS` - cannot be set when `protocol` is set to `TCP`.
func (o ProfileMonitorConfigOutput) Path() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) *string { return v.Path }).(pulumi.StringPtrOutput)
}

// The port number used by the monitoring checks.
func (o ProfileMonitorConfigOutput) Port() pulumi.IntOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) int { return v.Port }).(pulumi.IntOutput)
}

// The protocol used by the monitoring checks, supported values are `HTTP`, `HTTPS` and `TCP`.
func (o ProfileMonitorConfigOutput) Protocol() pulumi.StringOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) string { return v.Protocol }).(pulumi.StringOutput)
}

// The amount of time the Traffic Manager probing agent should wait before considering that check a failure when a health check probe is sent to the endpoint. If `intervalInSeconds` is set to `30`, then `timeoutInSeconds` can be between `5` and `10`. The default value is `10`. If `intervalInSeconds` is set to `10`, then valid values are between `5` and `9` and `timeoutInSeconds` is required.
func (o ProfileMonitorConfigOutput) TimeoutInSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) *int { return v.TimeoutInSeconds }).(pulumi.IntPtrOutput)
}

// The number of failures a Traffic Manager probing agent tolerates before marking that endpoint as unhealthy. Valid values are between `0` and `9`. The default value is `3`
func (o ProfileMonitorConfigOutput) ToleratedNumberOfFailures() pulumi.IntPtrOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) *int { return v.ToleratedNumberOfFailures }).(pulumi.IntPtrOutput)
}

type ProfileMonitorConfigPtrOutput struct{ *pulumi.OutputState }

func (ProfileMonitorConfigPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ProfileMonitorConfig)(nil)).Elem()
}

func (o ProfileMonitorConfigPtrOutput) ToProfileMonitorConfigPtrOutput() ProfileMonitorConfigPtrOutput {
	return o
}

func (o ProfileMonitorConfigPtrOutput) ToProfileMonitorConfigPtrOutputWithContext(ctx context.Context) ProfileMonitorConfigPtrOutput {
	return o
}

func (o ProfileMonitorConfigPtrOutput) Elem() ProfileMonitorConfigOutput {
	return o.ApplyT(func(v *ProfileMonitorConfig) ProfileMonitorConfig { return *v }).(ProfileMonitorConfigOutput)
}

// One or more `customHeader` blocks as defined below.
func (o ProfileMonitorConfigPtrOutput) CustomHeaders() ProfileMonitorConfigCustomHeaderArrayOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) []ProfileMonitorConfigCustomHeader { return v.CustomHeaders }).(ProfileMonitorConfigCustomHeaderArrayOutput)
}

// A list of status code ranges in the format of `100-101`.
func (o ProfileMonitorConfigPtrOutput) ExpectedStatusCodeRanges() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) []string { return v.ExpectedStatusCodeRanges }).(pulumi.StringArrayOutput)
}

// The interval used to check the endpoint health from a Traffic Manager probing agent. You can specify two values here: `30` (normal probing) and `10` (fast probing). The default value is `30`.
func (o ProfileMonitorConfigPtrOutput) IntervalInSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) *int { return v.IntervalInSeconds }).(pulumi.IntPtrOutput)
}

// The path used by the monitoring checks. Required when `protocol` is set to `HTTP` or `HTTPS` - cannot be set when `protocol` is set to `TCP`.
func (o ProfileMonitorConfigPtrOutput) Path() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) *string { return v.Path }).(pulumi.StringPtrOutput)
}

// The port number used by the monitoring checks.
func (o ProfileMonitorConfigPtrOutput) Port() pulumi.IntOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) int { return v.Port }).(pulumi.IntOutput)
}

// The protocol used by the monitoring checks, supported values are `HTTP`, `HTTPS` and `TCP`.
func (o ProfileMonitorConfigPtrOutput) Protocol() pulumi.StringOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) string { return v.Protocol }).(pulumi.StringOutput)
}

// The amount of time the Traffic Manager probing agent should wait before considering that check a failure when a health check probe is sent to the endpoint. If `intervalInSeconds` is set to `30`, then `timeoutInSeconds` can be between `5` and `10`. The default value is `10`. If `intervalInSeconds` is set to `10`, then valid values are between `5` and `9` and `timeoutInSeconds` is required.
func (o ProfileMonitorConfigPtrOutput) TimeoutInSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) *int { return v.TimeoutInSeconds }).(pulumi.IntPtrOutput)
}

// The number of failures a Traffic Manager probing agent tolerates before marking that endpoint as unhealthy. Valid values are between `0` and `9`. The default value is `3`
func (o ProfileMonitorConfigPtrOutput) ToleratedNumberOfFailures() pulumi.IntPtrOutput {
	return o.ApplyT(func(v ProfileMonitorConfig) *int { return v.ToleratedNumberOfFailures }).(pulumi.IntPtrOutput)
}

type ProfileMonitorConfigCustomHeader struct {
	// The name of the custom header.
	Name string `pulumi:"name"`
	// The value of custom header. Applicable for Http and Https protocol.
	Value string `pulumi:"value"`
}

type ProfileMonitorConfigCustomHeaderInput interface {
	pulumi.Input

	ToProfileMonitorConfigCustomHeaderOutput() ProfileMonitorConfigCustomHeaderOutput
	ToProfileMonitorConfigCustomHeaderOutputWithContext(context.Context) ProfileMonitorConfigCustomHeaderOutput
}

type ProfileMonitorConfigCustomHeaderArgs struct {
	// The name of the custom header.
	Name pulumi.StringInput `pulumi:"name"`
	// The value of custom header. Applicable for Http and Https protocol.
	Value pulumi.StringInput `pulumi:"value"`
}

func (ProfileMonitorConfigCustomHeaderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ProfileMonitorConfigCustomHeader)(nil)).Elem()
}

func (i ProfileMonitorConfigCustomHeaderArgs) ToProfileMonitorConfigCustomHeaderOutput() ProfileMonitorConfigCustomHeaderOutput {
	return i.ToProfileMonitorConfigCustomHeaderOutputWithContext(context.Background())
}

func (i ProfileMonitorConfigCustomHeaderArgs) ToProfileMonitorConfigCustomHeaderOutputWithContext(ctx context.Context) ProfileMonitorConfigCustomHeaderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProfileMonitorConfigCustomHeaderOutput)
}

type ProfileMonitorConfigCustomHeaderArrayInput interface {
	pulumi.Input

	ToProfileMonitorConfigCustomHeaderArrayOutput() ProfileMonitorConfigCustomHeaderArrayOutput
	ToProfileMonitorConfigCustomHeaderArrayOutputWithContext(context.Context) ProfileMonitorConfigCustomHeaderArrayOutput
}

type ProfileMonitorConfigCustomHeaderArray []ProfileMonitorConfigCustomHeaderInput

func (ProfileMonitorConfigCustomHeaderArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ProfileMonitorConfigCustomHeader)(nil)).Elem()
}

func (i ProfileMonitorConfigCustomHeaderArray) ToProfileMonitorConfigCustomHeaderArrayOutput() ProfileMonitorConfigCustomHeaderArrayOutput {
	return i.ToProfileMonitorConfigCustomHeaderArrayOutputWithContext(context.Background())
}

func (i ProfileMonitorConfigCustomHeaderArray) ToProfileMonitorConfigCustomHeaderArrayOutputWithContext(ctx context.Context) ProfileMonitorConfigCustomHeaderArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProfileMonitorConfigCustomHeaderArrayOutput)
}

type ProfileMonitorConfigCustomHeaderOutput struct{ *pulumi.OutputState }

func (ProfileMonitorConfigCustomHeaderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ProfileMonitorConfigCustomHeader)(nil)).Elem()
}

func (o ProfileMonitorConfigCustomHeaderOutput) ToProfileMonitorConfigCustomHeaderOutput() ProfileMonitorConfigCustomHeaderOutput {
	return o
}

func (o ProfileMonitorConfigCustomHeaderOutput) ToProfileMonitorConfigCustomHeaderOutputWithContext(ctx context.Context) ProfileMonitorConfigCustomHeaderOutput {
	return o
}

// The name of the custom header.
func (o ProfileMonitorConfigCustomHeaderOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v ProfileMonitorConfigCustomHeader) string { return v.Name }).(pulumi.StringOutput)
}

// The value of custom header. Applicable for Http and Https protocol.
func (o ProfileMonitorConfigCustomHeaderOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v ProfileMonitorConfigCustomHeader) string { return v.Value }).(pulumi.StringOutput)
}

type ProfileMonitorConfigCustomHeaderArrayOutput struct{ *pulumi.OutputState }

func (ProfileMonitorConfigCustomHeaderArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ProfileMonitorConfigCustomHeader)(nil)).Elem()
}

func (o ProfileMonitorConfigCustomHeaderArrayOutput) ToProfileMonitorConfigCustomHeaderArrayOutput() ProfileMonitorConfigCustomHeaderArrayOutput {
	return o
}

func (o ProfileMonitorConfigCustomHeaderArrayOutput) ToProfileMonitorConfigCustomHeaderArrayOutputWithContext(ctx context.Context) ProfileMonitorConfigCustomHeaderArrayOutput {
	return o
}

func (o ProfileMonitorConfigCustomHeaderArrayOutput) Index(i pulumi.IntInput) ProfileMonitorConfigCustomHeaderOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ProfileMonitorConfigCustomHeader {
		return vs[0].([]ProfileMonitorConfigCustomHeader)[vs[1].(int)]
	}).(ProfileMonitorConfigCustomHeaderOutput)
}

func init() {
	pulumi.RegisterOutputType(EndpointCustomHeaderOutput{})
	pulumi.RegisterOutputType(EndpointCustomHeaderArrayOutput{})
	pulumi.RegisterOutputType(EndpointSubnetOutput{})
	pulumi.RegisterOutputType(EndpointSubnetArrayOutput{})
	pulumi.RegisterOutputType(ProfileDnsConfigOutput{})
	pulumi.RegisterOutputType(ProfileDnsConfigPtrOutput{})
	pulumi.RegisterOutputType(ProfileMonitorConfigOutput{})
	pulumi.RegisterOutputType(ProfileMonitorConfigPtrOutput{})
	pulumi.RegisterOutputType(ProfileMonitorConfigCustomHeaderOutput{})
	pulumi.RegisterOutputType(ProfileMonitorConfigCustomHeaderArrayOutput{})
}
