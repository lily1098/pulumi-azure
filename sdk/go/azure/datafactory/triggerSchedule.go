// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package datafactory

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a Trigger Schedule inside a Azure Data Factory.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/data_factory_trigger_schedule.html.markdown.
type TriggerSchedule struct {
	s *pulumi.ResourceState
}

// NewTriggerSchedule registers a new resource with the given unique name, arguments, and options.
func NewTriggerSchedule(ctx *pulumi.Context,
	name string, args *TriggerScheduleArgs, opts ...pulumi.ResourceOpt) (*TriggerSchedule, error) {
	if args == nil || args.DataFactoryName == nil {
		return nil, errors.New("missing required argument 'DataFactoryName'")
	}
	if args == nil || args.PipelineName == nil {
		return nil, errors.New("missing required argument 'PipelineName'")
	}
	if args == nil || args.ResourceGroupName == nil {
		return nil, errors.New("missing required argument 'ResourceGroupName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["annotations"] = nil
		inputs["dataFactoryName"] = nil
		inputs["endTime"] = nil
		inputs["frequency"] = nil
		inputs["interval"] = nil
		inputs["name"] = nil
		inputs["pipelineName"] = nil
		inputs["pipelineParameters"] = nil
		inputs["resourceGroupName"] = nil
		inputs["startTime"] = nil
	} else {
		inputs["annotations"] = args.Annotations
		inputs["dataFactoryName"] = args.DataFactoryName
		inputs["endTime"] = args.EndTime
		inputs["frequency"] = args.Frequency
		inputs["interval"] = args.Interval
		inputs["name"] = args.Name
		inputs["pipelineName"] = args.PipelineName
		inputs["pipelineParameters"] = args.PipelineParameters
		inputs["resourceGroupName"] = args.ResourceGroupName
		inputs["startTime"] = args.StartTime
	}
	s, err := ctx.RegisterResource("azure:datafactory/triggerSchedule:TriggerSchedule", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &TriggerSchedule{s: s}, nil
}

// GetTriggerSchedule gets an existing TriggerSchedule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTriggerSchedule(ctx *pulumi.Context,
	name string, id pulumi.ID, state *TriggerScheduleState, opts ...pulumi.ResourceOpt) (*TriggerSchedule, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["annotations"] = state.Annotations
		inputs["dataFactoryName"] = state.DataFactoryName
		inputs["endTime"] = state.EndTime
		inputs["frequency"] = state.Frequency
		inputs["interval"] = state.Interval
		inputs["name"] = state.Name
		inputs["pipelineName"] = state.PipelineName
		inputs["pipelineParameters"] = state.PipelineParameters
		inputs["resourceGroupName"] = state.ResourceGroupName
		inputs["startTime"] = state.StartTime
	}
	s, err := ctx.ReadResource("azure:datafactory/triggerSchedule:TriggerSchedule", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &TriggerSchedule{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *TriggerSchedule) URN() pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *TriggerSchedule) ID() pulumi.IDOutput {
	return r.s.ID()
}

// List of tags that can be used for describing the Data Factory Schedule Trigger.
func (r *TriggerSchedule) Annotations() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["annotations"])
}

// The Data Factory name in which to associate the Schedule Trigger with. Changing this forces a new resource.
func (r *TriggerSchedule) DataFactoryName() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["dataFactoryName"])
}

// The time the Schedule Trigger should end. The time will be represented in UTC. 
func (r *TriggerSchedule) EndTime() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["endTime"])
}

// The trigger freqency. Valid values include `Minute`, `Hour`, `Day`, `Week`, `Month`. Defaults to `Minute`.
func (r *TriggerSchedule) Frequency() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["frequency"])
}

// The interval for how often the trigger occurs. This defaults to 1.
func (r *TriggerSchedule) Interval() pulumi.IntOutput {
	return (pulumi.IntOutput)(r.s.State["interval"])
}

// Specifies the name of the Data Factory Schedule Trigger. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
func (r *TriggerSchedule) Name() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["name"])
}

// The Data Factory Pipeline name that the trigger will act on.
func (r *TriggerSchedule) PipelineName() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["pipelineName"])
}

// The pipeline parameters that the trigger will act upon.
func (r *TriggerSchedule) PipelineParameters() pulumi.MapOutput {
	return (pulumi.MapOutput)(r.s.State["pipelineParameters"])
}

// The name of the resource group in which to create the Data Factory Schedule Trigger. Changing this forces a new resource
func (r *TriggerSchedule) ResourceGroupName() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["resourceGroupName"])
}

// The time the Schedule Trigger will start. This defaults to the current time. The time will be represented in UTC. 
func (r *TriggerSchedule) StartTime() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["startTime"])
}

// Input properties used for looking up and filtering TriggerSchedule resources.
type TriggerScheduleState struct {
	// List of tags that can be used for describing the Data Factory Schedule Trigger.
	Annotations interface{}
	// The Data Factory name in which to associate the Schedule Trigger with. Changing this forces a new resource.
	DataFactoryName interface{}
	// The time the Schedule Trigger should end. The time will be represented in UTC. 
	EndTime interface{}
	// The trigger freqency. Valid values include `Minute`, `Hour`, `Day`, `Week`, `Month`. Defaults to `Minute`.
	Frequency interface{}
	// The interval for how often the trigger occurs. This defaults to 1.
	Interval interface{}
	// Specifies the name of the Data Factory Schedule Trigger. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
	Name interface{}
	// The Data Factory Pipeline name that the trigger will act on.
	PipelineName interface{}
	// The pipeline parameters that the trigger will act upon.
	PipelineParameters interface{}
	// The name of the resource group in which to create the Data Factory Schedule Trigger. Changing this forces a new resource
	ResourceGroupName interface{}
	// The time the Schedule Trigger will start. This defaults to the current time. The time will be represented in UTC. 
	StartTime interface{}
}

// The set of arguments for constructing a TriggerSchedule resource.
type TriggerScheduleArgs struct {
	// List of tags that can be used for describing the Data Factory Schedule Trigger.
	Annotations interface{}
	// The Data Factory name in which to associate the Schedule Trigger with. Changing this forces a new resource.
	DataFactoryName interface{}
	// The time the Schedule Trigger should end. The time will be represented in UTC. 
	EndTime interface{}
	// The trigger freqency. Valid values include `Minute`, `Hour`, `Day`, `Week`, `Month`. Defaults to `Minute`.
	Frequency interface{}
	// The interval for how often the trigger occurs. This defaults to 1.
	Interval interface{}
	// Specifies the name of the Data Factory Schedule Trigger. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
	Name interface{}
	// The Data Factory Pipeline name that the trigger will act on.
	PipelineName interface{}
	// The pipeline parameters that the trigger will act upon.
	PipelineParameters interface{}
	// The name of the resource group in which to create the Data Factory Schedule Trigger. Changing this forces a new resource
	ResourceGroupName interface{}
	// The time the Schedule Trigger will start. This defaults to the current time. The time will be represented in UTC. 
	StartTime interface{}
}
