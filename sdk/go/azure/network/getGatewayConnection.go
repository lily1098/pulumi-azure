// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package network

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to access information about an existing Virtual Network Gateway Connection.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/network"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		example, err := network.GetGatewayConnection(ctx, &network.GetGatewayConnectionArgs{
// 			Name:              "production",
// 			ResourceGroupName: "networking",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		ctx.Export("virtualNetworkGatewayConnectionId", example.Id)
// 		return nil
// 	})
// }
// ```
func GetGatewayConnection(ctx *pulumi.Context, args *GetGatewayConnectionArgs, opts ...pulumi.InvokeOption) (*GetGatewayConnectionResult, error) {
	var rv GetGatewayConnectionResult
	err := ctx.Invoke("azure:network/getGatewayConnection:getGatewayConnection", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getGatewayConnection.
type GetGatewayConnectionArgs struct {
	// Specifies the name of the Virtual Network Gateway Connection.
	Name string `pulumi:"name"`
	// Specifies the name of the resource group the Virtual Network Gateway Connection is located in.
	ResourceGroupName string `pulumi:"resourceGroupName"`
}

// A collection of values returned by getGatewayConnection.
type GetGatewayConnectionResult struct {
	// The authorization key associated with the
	// Express Route Circuit. This field is present only if the type is an
	// ExpressRoute connection.
	AuthorizationKey   string `pulumi:"authorizationKey"`
	ConnectionProtocol string `pulumi:"connectionProtocol"`
	// The dead peer detection timeout of this connection in seconds.
	DpdTimeoutSeconds      int `pulumi:"dpdTimeoutSeconds"`
	EgressBytesTransferred int `pulumi:"egressBytesTransferred"`
	// If `true`, BGP (Border Gateway Protocol) is enabled
	// for this connection.
	EnableBgp bool `pulumi:"enableBgp"`
	// The ID of the Express Route Circuit
	// (i.e. when `type` is `ExpressRoute`).
	ExpressRouteCircuitId string `pulumi:"expressRouteCircuitId"`
	// If `true`, data packets will bypass ExpressRoute Gateway for data forwarding. This is only valid for ExpressRoute connections.
	ExpressRouteGatewayBypass bool `pulumi:"expressRouteGatewayBypass"`
	// The provider-assigned unique ID for this managed resource.
	Id                      string                            `pulumi:"id"`
	IngressBytesTransferred int                               `pulumi:"ingressBytesTransferred"`
	IpsecPolicies           []GetGatewayConnectionIpsecPolicy `pulumi:"ipsecPolicies"`
	// Use private local Azure IP for the connection.
	LocalAzureIpAddressEnabled bool `pulumi:"localAzureIpAddressEnabled"`
	// The ID of the local network gateway
	// when a Site-to-Site connection (i.e. when `type` is `IPsec`).
	LocalNetworkGatewayId string `pulumi:"localNetworkGatewayId"`
	// The location/region where the connection is
	// located.
	Location string `pulumi:"location"`
	Name     string `pulumi:"name"`
	// The ID of the peer virtual
	// network gateway when a VNet-to-VNet connection (i.e. when `type`
	// is `Vnet2Vnet`).
	PeerVirtualNetworkGatewayId string `pulumi:"peerVirtualNetworkGatewayId"`
	ResourceGroupName           string `pulumi:"resourceGroupName"`
	ResourceGuid                string `pulumi:"resourceGuid"`
	// The routing weight.
	RoutingWeight int `pulumi:"routingWeight"`
	// The shared IPSec key.
	SharedKey string `pulumi:"sharedKey"`
	// A mapping of tags to assign to the resource.
	Tags                  map[string]string                         `pulumi:"tags"`
	TrafficSelectorPolicy GetGatewayConnectionTrafficSelectorPolicy `pulumi:"trafficSelectorPolicy"`
	// The type of connection. Valid options are `IPsec`
	// (Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
	Type string `pulumi:"type"`
	// If `true`, policy-based traffic
	// selectors are enabled for this connection. Enabling policy-based traffic
	// selectors requires an `ipsecPolicy` block.
	UsePolicyBasedTrafficSelectors bool `pulumi:"usePolicyBasedTrafficSelectors"`
	// The ID of the Virtual Network Gateway
	// in which the connection is created.
	VirtualNetworkGatewayId string `pulumi:"virtualNetworkGatewayId"`
}
