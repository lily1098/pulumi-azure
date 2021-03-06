// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package network

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
	case "azure:network/applicationGateway:ApplicationGateway":
		r, err = NewApplicationGateway(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/applicationSecurityGroup:ApplicationSecurityGroup":
		r, err = NewApplicationSecurityGroup(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/bgpConnection:BgpConnection":
		r, err = NewBgpConnection(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/ddosProtectionPlan:DdosProtectionPlan":
		r, err = NewDdosProtectionPlan(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/expressRouteCircuit:ExpressRouteCircuit":
		r, err = NewExpressRouteCircuit(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/expressRouteCircuitAuthorization:ExpressRouteCircuitAuthorization":
		r, err = NewExpressRouteCircuitAuthorization(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/expressRouteCircuitPeering:ExpressRouteCircuitPeering":
		r, err = NewExpressRouteCircuitPeering(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/expressRouteGateway:ExpressRouteGateway":
		r, err = NewExpressRouteGateway(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/firewall:Firewall":
		r, err = NewFirewall(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/firewallApplicationRuleCollection:FirewallApplicationRuleCollection":
		r, err = NewFirewallApplicationRuleCollection(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/firewallNatRuleCollection:FirewallNatRuleCollection":
		r, err = NewFirewallNatRuleCollection(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/firewallNetworkRuleCollection:FirewallNetworkRuleCollection":
		r, err = NewFirewallNetworkRuleCollection(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/firewallPolicy:FirewallPolicy":
		r, err = NewFirewallPolicy(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/firewallPolicyRuleCollectionGroup:FirewallPolicyRuleCollectionGroup":
		r, err = NewFirewallPolicyRuleCollectionGroup(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/iPGroup:IPGroup":
		r, err = NewIPGroup(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/localNetworkGateway:LocalNetworkGateway":
		r, err = NewLocalNetworkGateway(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/natGateway:NatGateway":
		r, err = NewNatGateway(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/natGatewayPublicIpAssociation:NatGatewayPublicIpAssociation":
		r, err = NewNatGatewayPublicIpAssociation(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/networkConnectionMonitor:NetworkConnectionMonitor":
		r, err = NewNetworkConnectionMonitor(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/networkInterface:NetworkInterface":
		r, err = NewNetworkInterface(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation:NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation":
		r, err = NewNetworkInterfaceApplicationGatewayBackendAddressPoolAssociation(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/networkInterfaceApplicationSecurityGroupAssociation:NetworkInterfaceApplicationSecurityGroupAssociation":
		r, err = NewNetworkInterfaceApplicationSecurityGroupAssociation(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/networkInterfaceBackendAddressPoolAssociation:NetworkInterfaceBackendAddressPoolAssociation":
		r, err = NewNetworkInterfaceBackendAddressPoolAssociation(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/networkInterfaceNatRuleAssociation:NetworkInterfaceNatRuleAssociation":
		r, err = NewNetworkInterfaceNatRuleAssociation(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/networkInterfaceSecurityGroupAssociation:NetworkInterfaceSecurityGroupAssociation":
		r, err = NewNetworkInterfaceSecurityGroupAssociation(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/networkPacketCapture:NetworkPacketCapture":
		r, err = NewNetworkPacketCapture(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/networkSecurityGroup:NetworkSecurityGroup":
		r, err = NewNetworkSecurityGroup(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/networkSecurityRule:NetworkSecurityRule":
		r, err = NewNetworkSecurityRule(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/networkWatcher:NetworkWatcher":
		r, err = NewNetworkWatcher(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/networkWatcherFlowLog:NetworkWatcherFlowLog":
		r, err = NewNetworkWatcherFlowLog(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/packetCapture:PacketCapture":
		r, err = NewPacketCapture(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/pointToPointVpnGateway:PointToPointVpnGateway":
		r, err = NewPointToPointVpnGateway(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/profile:Profile":
		r, err = NewProfile(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/publicIp:PublicIp":
		r, err = NewPublicIp(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/publicIpPrefix:PublicIpPrefix":
		r, err = NewPublicIpPrefix(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/route:Route":
		r, err = NewRoute(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/routeFilter:RouteFilter":
		r, err = NewRouteFilter(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/routeTable:RouteTable":
		r, err = NewRouteTable(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/securityPartnerProvider:SecurityPartnerProvider":
		r, err = NewSecurityPartnerProvider(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/subnet:Subnet":
		r, err = NewSubnet(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/subnetNatGatewayAssociation:SubnetNatGatewayAssociation":
		r, err = NewSubnetNatGatewayAssociation(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/subnetNetworkSecurityGroupAssociation:SubnetNetworkSecurityGroupAssociation":
		r, err = NewSubnetNetworkSecurityGroupAssociation(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/subnetRouteTableAssociation:SubnetRouteTableAssociation":
		r, err = NewSubnetRouteTableAssociation(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/subnetServiceEndpointStoragePolicy:SubnetServiceEndpointStoragePolicy":
		r, err = NewSubnetServiceEndpointStoragePolicy(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/trafficManagerEndpoint:TrafficManagerEndpoint":
		r, err = NewTrafficManagerEndpoint(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/trafficManagerProfile:TrafficManagerProfile":
		r, err = NewTrafficManagerProfile(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/virtualHub:VirtualHub":
		r, err = NewVirtualHub(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/virtualHubConnection:VirtualHubConnection":
		r, err = NewVirtualHubConnection(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/virtualHubIp:VirtualHubIp":
		r, err = NewVirtualHubIp(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/virtualHubRouteTable:VirtualHubRouteTable":
		r, err = NewVirtualHubRouteTable(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/virtualNetwork:VirtualNetwork":
		r, err = NewVirtualNetwork(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/virtualNetworkGateway:VirtualNetworkGateway":
		r, err = NewVirtualNetworkGateway(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/virtualNetworkGatewayConnection:VirtualNetworkGatewayConnection":
		r, err = NewVirtualNetworkGatewayConnection(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/virtualNetworkPeering:VirtualNetworkPeering":
		r, err = NewVirtualNetworkPeering(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/virtualWan:VirtualWan":
		r, err = NewVirtualWan(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/vpnGateway:VpnGateway":
		r, err = NewVpnGateway(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/vpnGatewayConnection:VpnGatewayConnection":
		r, err = NewVpnGatewayConnection(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/vpnServerConfiguration:VpnServerConfiguration":
		r, err = NewVpnServerConfiguration(ctx, name, nil, pulumi.URN_(urn))
	case "azure:network/vpnSite:VpnSite":
		r, err = NewVpnSite(ctx, name, nil, pulumi.URN_(urn))
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
		"network/applicationGateway",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/applicationSecurityGroup",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/bgpConnection",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/ddosProtectionPlan",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/expressRouteCircuit",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/expressRouteCircuitAuthorization",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/expressRouteCircuitPeering",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/expressRouteGateway",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/firewall",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/firewallApplicationRuleCollection",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/firewallNatRuleCollection",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/firewallNetworkRuleCollection",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/firewallPolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/firewallPolicyRuleCollectionGroup",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/iPGroup",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/localNetworkGateway",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/natGateway",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/natGatewayPublicIpAssociation",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/networkConnectionMonitor",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/networkInterface",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/networkInterfaceApplicationGatewayBackendAddressPoolAssociation",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/networkInterfaceApplicationSecurityGroupAssociation",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/networkInterfaceBackendAddressPoolAssociation",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/networkInterfaceNatRuleAssociation",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/networkInterfaceSecurityGroupAssociation",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/networkPacketCapture",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/networkSecurityGroup",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/networkSecurityRule",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/networkWatcher",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/networkWatcherFlowLog",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/packetCapture",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/pointToPointVpnGateway",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/profile",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/publicIp",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/publicIpPrefix",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/route",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/routeFilter",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/routeTable",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/securityPartnerProvider",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/subnet",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/subnetNatGatewayAssociation",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/subnetNetworkSecurityGroupAssociation",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/subnetRouteTableAssociation",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/subnetServiceEndpointStoragePolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/trafficManagerEndpoint",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/trafficManagerProfile",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/virtualHub",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/virtualHubConnection",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/virtualHubIp",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/virtualHubRouteTable",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/virtualNetwork",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/virtualNetworkGateway",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/virtualNetworkGatewayConnection",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/virtualNetworkPeering",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/virtualWan",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/vpnGateway",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/vpnGatewayConnection",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/vpnServerConfiguration",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"network/vpnSite",
		&module{version},
	)
}
