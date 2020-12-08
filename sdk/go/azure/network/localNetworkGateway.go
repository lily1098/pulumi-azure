// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package network

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a local network gateway connection over which specific connections can be configured.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/core"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/network"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		example, err := core.NewResourceGroup(ctx, "example", &core.ResourceGroupArgs{
// 			Location: pulumi.String("West US"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = network.NewLocalNetworkGateway(ctx, "home", &network.LocalNetworkGatewayArgs{
// 			ResourceGroupName: example.Name,
// 			Location:          example.Location,
// 			GatewayAddress:    pulumi.String("12.13.14.15"),
// 			AddressSpaces: pulumi.StringArray{
// 				pulumi.String("10.0.0.0/16"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// Local Network Gateways can be imported using the `resource id`, e.g.
//
// ```sh
//  $ pulumi import azure:network/localNetworkGateway:LocalNetworkGateway lng1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/localNetworkGateways/lng1
// ```
type LocalNetworkGateway struct {
	pulumi.CustomResourceState

	// The list of string CIDRs representing the
	// address spaces the gateway exposes.
	AddressSpaces pulumi.StringArrayOutput `pulumi:"addressSpaces"`
	// A `bgpSettings` block as defined below containing the
	// Local Network Gateway's BGP speaker settings.
	BgpSettings LocalNetworkGatewayBgpSettingsPtrOutput `pulumi:"bgpSettings"`
	// The gateway IP address to connect with.
	GatewayAddress pulumi.StringPtrOutput `pulumi:"gatewayAddress"`
	// The gateway FQDN to connect with.
	GatewayFqdn pulumi.StringPtrOutput `pulumi:"gatewayFqdn"`
	// The location/region where the local network gateway is
	// created. Changing this forces a new resource to be created.
	Location pulumi.StringOutput `pulumi:"location"`
	// The name of the local network gateway. Changing this
	// forces a new resource to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// The name of the resource group in which to
	// create the local network gateway.
	ResourceGroupName pulumi.StringOutput `pulumi:"resourceGroupName"`
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
}

// NewLocalNetworkGateway registers a new resource with the given unique name, arguments, and options.
func NewLocalNetworkGateway(ctx *pulumi.Context,
	name string, args *LocalNetworkGatewayArgs, opts ...pulumi.ResourceOption) (*LocalNetworkGateway, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AddressSpaces == nil {
		return nil, errors.New("invalid value for required argument 'AddressSpaces'")
	}
	if args.ResourceGroupName == nil {
		return nil, errors.New("invalid value for required argument 'ResourceGroupName'")
	}
	var resource LocalNetworkGateway
	err := ctx.RegisterResource("azure:network/localNetworkGateway:LocalNetworkGateway", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLocalNetworkGateway gets an existing LocalNetworkGateway resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLocalNetworkGateway(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LocalNetworkGatewayState, opts ...pulumi.ResourceOption) (*LocalNetworkGateway, error) {
	var resource LocalNetworkGateway
	err := ctx.ReadResource("azure:network/localNetworkGateway:LocalNetworkGateway", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LocalNetworkGateway resources.
type localNetworkGatewayState struct {
	// The list of string CIDRs representing the
	// address spaces the gateway exposes.
	AddressSpaces []string `pulumi:"addressSpaces"`
	// A `bgpSettings` block as defined below containing the
	// Local Network Gateway's BGP speaker settings.
	BgpSettings *LocalNetworkGatewayBgpSettings `pulumi:"bgpSettings"`
	// The gateway IP address to connect with.
	GatewayAddress *string `pulumi:"gatewayAddress"`
	// The gateway FQDN to connect with.
	GatewayFqdn *string `pulumi:"gatewayFqdn"`
	// The location/region where the local network gateway is
	// created. Changing this forces a new resource to be created.
	Location *string `pulumi:"location"`
	// The name of the local network gateway. Changing this
	// forces a new resource to be created.
	Name *string `pulumi:"name"`
	// The name of the resource group in which to
	// create the local network gateway.
	ResourceGroupName *string `pulumi:"resourceGroupName"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
}

type LocalNetworkGatewayState struct {
	// The list of string CIDRs representing the
	// address spaces the gateway exposes.
	AddressSpaces pulumi.StringArrayInput
	// A `bgpSettings` block as defined below containing the
	// Local Network Gateway's BGP speaker settings.
	BgpSettings LocalNetworkGatewayBgpSettingsPtrInput
	// The gateway IP address to connect with.
	GatewayAddress pulumi.StringPtrInput
	// The gateway FQDN to connect with.
	GatewayFqdn pulumi.StringPtrInput
	// The location/region where the local network gateway is
	// created. Changing this forces a new resource to be created.
	Location pulumi.StringPtrInput
	// The name of the local network gateway. Changing this
	// forces a new resource to be created.
	Name pulumi.StringPtrInput
	// The name of the resource group in which to
	// create the local network gateway.
	ResourceGroupName pulumi.StringPtrInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapInput
}

func (LocalNetworkGatewayState) ElementType() reflect.Type {
	return reflect.TypeOf((*localNetworkGatewayState)(nil)).Elem()
}

type localNetworkGatewayArgs struct {
	// The list of string CIDRs representing the
	// address spaces the gateway exposes.
	AddressSpaces []string `pulumi:"addressSpaces"`
	// A `bgpSettings` block as defined below containing the
	// Local Network Gateway's BGP speaker settings.
	BgpSettings *LocalNetworkGatewayBgpSettings `pulumi:"bgpSettings"`
	// The gateway IP address to connect with.
	GatewayAddress *string `pulumi:"gatewayAddress"`
	// The gateway FQDN to connect with.
	GatewayFqdn *string `pulumi:"gatewayFqdn"`
	// The location/region where the local network gateway is
	// created. Changing this forces a new resource to be created.
	Location *string `pulumi:"location"`
	// The name of the local network gateway. Changing this
	// forces a new resource to be created.
	Name *string `pulumi:"name"`
	// The name of the resource group in which to
	// create the local network gateway.
	ResourceGroupName string `pulumi:"resourceGroupName"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a LocalNetworkGateway resource.
type LocalNetworkGatewayArgs struct {
	// The list of string CIDRs representing the
	// address spaces the gateway exposes.
	AddressSpaces pulumi.StringArrayInput
	// A `bgpSettings` block as defined below containing the
	// Local Network Gateway's BGP speaker settings.
	BgpSettings LocalNetworkGatewayBgpSettingsPtrInput
	// The gateway IP address to connect with.
	GatewayAddress pulumi.StringPtrInput
	// The gateway FQDN to connect with.
	GatewayFqdn pulumi.StringPtrInput
	// The location/region where the local network gateway is
	// created. Changing this forces a new resource to be created.
	Location pulumi.StringPtrInput
	// The name of the local network gateway. Changing this
	// forces a new resource to be created.
	Name pulumi.StringPtrInput
	// The name of the resource group in which to
	// create the local network gateway.
	ResourceGroupName pulumi.StringInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapInput
}

func (LocalNetworkGatewayArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*localNetworkGatewayArgs)(nil)).Elem()
}

type LocalNetworkGatewayInput interface {
	pulumi.Input

	ToLocalNetworkGatewayOutput() LocalNetworkGatewayOutput
	ToLocalNetworkGatewayOutputWithContext(ctx context.Context) LocalNetworkGatewayOutput
}

func (LocalNetworkGateway) ElementType() reflect.Type {
	return reflect.TypeOf((*LocalNetworkGateway)(nil)).Elem()
}

func (i LocalNetworkGateway) ToLocalNetworkGatewayOutput() LocalNetworkGatewayOutput {
	return i.ToLocalNetworkGatewayOutputWithContext(context.Background())
}

func (i LocalNetworkGateway) ToLocalNetworkGatewayOutputWithContext(ctx context.Context) LocalNetworkGatewayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LocalNetworkGatewayOutput)
}

type LocalNetworkGatewayOutput struct {
	*pulumi.OutputState
}

func (LocalNetworkGatewayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LocalNetworkGatewayOutput)(nil)).Elem()
}

func (o LocalNetworkGatewayOutput) ToLocalNetworkGatewayOutput() LocalNetworkGatewayOutput {
	return o
}

func (o LocalNetworkGatewayOutput) ToLocalNetworkGatewayOutputWithContext(ctx context.Context) LocalNetworkGatewayOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(LocalNetworkGatewayOutput{})
}
