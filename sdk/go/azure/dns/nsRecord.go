// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package dns

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Enables you to manage DNS NS Records within Azure DNS.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/dns_ns_record.html.markdown.
type NsRecord struct {
	s *pulumi.ResourceState
}

// NewNsRecord registers a new resource with the given unique name, arguments, and options.
func NewNsRecord(ctx *pulumi.Context,
	name string, args *NsRecordArgs, opts ...pulumi.ResourceOpt) (*NsRecord, error) {
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	if args == nil || args.Ttl == nil {
		return nil, errors.New("missing required argument 'Ttl'")
	}
	if args == nil || args.ZoneName == nil {
		return nil, errors.New("missing required argument 'ZoneName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["name"] = nil
		inputs["record"] = nil
		inputs["records"] = nil
		inputs["resourceGroupName"] = nil
		inputs["tags"] = nil
		inputs["ttl"] = nil
		inputs["zoneName"] = nil
	} else {
		inputs["name"] = args.Name
		inputs["record"] = args.Record
		inputs["records"] = args.Records
		inputs["resourceGroupName"] = args.ResourceGroupName
		inputs["tags"] = args.Tags
		inputs["ttl"] = args.Ttl
		inputs["zoneName"] = args.ZoneName
	}
	inputs["fqdn"] = nil
	s, err := ctx.RegisterResource("azure:dns/nsRecord:NsRecord", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &NsRecord{s: s}, nil
}

// GetNsRecord gets an existing NsRecord resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNsRecord(ctx *pulumi.Context,
	name string, id pulumi.ID, state *NsRecordState, opts ...pulumi.ResourceOpt) (*NsRecord, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["fqdn"] = state.Fqdn
		inputs["name"] = state.Name
		inputs["record"] = state.Record
		inputs["records"] = state.Records
		inputs["resourceGroupName"] = state.ResourceGroupName
		inputs["tags"] = state.Tags
		inputs["ttl"] = state.Ttl
		inputs["zoneName"] = state.ZoneName
	}
	s, err := ctx.ReadResource("azure:dns/nsRecord:NsRecord", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &NsRecord{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *NsRecord) URN() pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *NsRecord) ID() pulumi.IDOutput {
	return r.s.ID()
}

// The FQDN of the DNS NS Record.
func (r *NsRecord) Fqdn() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["fqdn"])
}

// The name of the DNS NS Record.
func (r *NsRecord) Name() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["name"])
}

// A list of values that make up the NS record. Each `record` block supports fields documented below. This field has been deprecated and will be removed in a future release.
func (r *NsRecord) Record() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["record"])
}

// A list of values that make up the NS record. *WARNING*: Either `records` or `record` is required.
func (r *NsRecord) Records() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["records"])
}

// Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
func (r *NsRecord) ResourceGroupName() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["resourceGroupName"])
}

// A mapping of tags to assign to the resource.
func (r *NsRecord) Tags() pulumi.MapOutput {
	return (pulumi.MapOutput)(r.s.State["tags"])
}

// The Time To Live (TTL) of the DNS record in seconds.
func (r *NsRecord) Ttl() pulumi.IntOutput {
	return (pulumi.IntOutput)(r.s.State["ttl"])
}

// Specifies the DNS Zone where the DNS Zone (parent resource) exists. Changing this forces a new resource to be created.
func (r *NsRecord) ZoneName() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["zoneName"])
}

// Input properties used for looking up and filtering NsRecord resources.
type NsRecordState struct {
	// The FQDN of the DNS NS Record.
	Fqdn interface{}
	// The name of the DNS NS Record.
	Name interface{}
	// A list of values that make up the NS record. Each `record` block supports fields documented below. This field has been deprecated and will be removed in a future release.
	Record interface{}
	// A list of values that make up the NS record. *WARNING*: Either `records` or `record` is required.
	Records interface{}
	// Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
	ResourceGroupName interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
	// The Time To Live (TTL) of the DNS record in seconds.
	Ttl interface{}
	// Specifies the DNS Zone where the DNS Zone (parent resource) exists. Changing this forces a new resource to be created.
	ZoneName interface{}
}

// The set of arguments for constructing a NsRecord resource.
type NsRecordArgs struct {
	// The name of the DNS NS Record.
	Name interface{}
	// A list of values that make up the NS record. Each `record` block supports fields documented below. This field has been deprecated and will be removed in a future release.
	Record interface{}
	// A list of values that make up the NS record. *WARNING*: Either `records` or `record` is required.
	Records interface{}
	// Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
	ResourceGroupName interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
	// The Time To Live (TTL) of the DNS record in seconds.
	Ttl interface{}
	// Specifies the DNS Zone where the DNS Zone (parent resource) exists. Changing this forces a new resource to be created.
	ZoneName interface{}
}
