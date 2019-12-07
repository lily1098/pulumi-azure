// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package network

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Associates a NAT Gateway with a Subnet within a Virtual Network.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/subnet_nat_gateway_association.html.markdown.
type SubnetNatGatewayAssociation struct {
	s *pulumi.ResourceState
}

// NewSubnetNatGatewayAssociation registers a new resource with the given unique name, arguments, and options.
func NewSubnetNatGatewayAssociation(ctx *pulumi.Context,
	name string, args *SubnetNatGatewayAssociationArgs, opts ...pulumi.ResourceOpt) (*SubnetNatGatewayAssociation, error) {
	if args == nil || args.NatGatewayId == nil {
		return nil, errors.New("missing required argument 'NatGatewayId'")
	}
	if args == nil || args.SubnetId == nil {
		return nil, errors.New("missing required argument 'SubnetId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["natGatewayId"] = nil
		inputs["subnetId"] = nil
	} else {
		inputs["natGatewayId"] = args.NatGatewayId
		inputs["subnetId"] = args.SubnetId
	}
	s, err := ctx.RegisterResource("azure:network/subnetNatGatewayAssociation:SubnetNatGatewayAssociation", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SubnetNatGatewayAssociation{s: s}, nil
}

// GetSubnetNatGatewayAssociation gets an existing SubnetNatGatewayAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSubnetNatGatewayAssociation(ctx *pulumi.Context,
	name string, id pulumi.ID, state *SubnetNatGatewayAssociationState, opts ...pulumi.ResourceOpt) (*SubnetNatGatewayAssociation, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["natGatewayId"] = state.NatGatewayId
		inputs["subnetId"] = state.SubnetId
	}
	s, err := ctx.ReadResource("azure:network/subnetNatGatewayAssociation:SubnetNatGatewayAssociation", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SubnetNatGatewayAssociation{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *SubnetNatGatewayAssociation) URN() pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *SubnetNatGatewayAssociation) ID() pulumi.IDOutput {
	return r.s.ID()
}

// The Azure resource ID of the NAT Gateway which should be associated with the Subnet. Changing this forces a new resource to be created.
func (r *SubnetNatGatewayAssociation) NatGatewayId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["natGatewayId"])
}

// The Azure resource ID of the Subnet. Changing this forces a new resource to be created.
func (r *SubnetNatGatewayAssociation) SubnetId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["subnetId"])
}

// Input properties used for looking up and filtering SubnetNatGatewayAssociation resources.
type SubnetNatGatewayAssociationState struct {
	// The Azure resource ID of the NAT Gateway which should be associated with the Subnet. Changing this forces a new resource to be created.
	NatGatewayId interface{}
	// The Azure resource ID of the Subnet. Changing this forces a new resource to be created.
	SubnetId interface{}
}

// The set of arguments for constructing a SubnetNatGatewayAssociation resource.
type SubnetNatGatewayAssociationArgs struct {
	// The Azure resource ID of the NAT Gateway which should be associated with the Subnet. Changing this forces a new resource to be created.
	NatGatewayId interface{}
	// The Azure resource ID of the Subnet. Changing this forces a new resource to be created.
	SubnetId interface{}
}
