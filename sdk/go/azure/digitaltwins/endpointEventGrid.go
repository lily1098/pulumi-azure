// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package digitaltwins

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Digital Twins Event Grid Endpoint.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/core"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/digitaltwins"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/eventgrid"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		exampleResourceGroup, err := core.NewResourceGroup(ctx, "exampleResourceGroup", &core.ResourceGroupArgs{
// 			Location: pulumi.String("West Europe"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleInstance, err := digitaltwins.NewInstance(ctx, "exampleInstance", &digitaltwins.InstanceArgs{
// 			ResourceGroupName: exampleResourceGroup.Name,
// 			Location:          exampleResourceGroup.Location,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleTopic, err := eventgrid.NewTopic(ctx, "exampleTopic", &eventgrid.TopicArgs{
// 			Location:          exampleResourceGroup.Location,
// 			ResourceGroupName: exampleResourceGroup.Name,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = digitaltwins.NewEndpointEventGrid(ctx, "exampleEndpointEventGrid", &digitaltwins.EndpointEventGridArgs{
// 			DigitalTwinsId:                   exampleInstance.ID(),
// 			EventgridTopicEndpoint:           exampleTopic.Endpoint,
// 			EventgridTopicPrimaryAccessKey:   exampleTopic.PrimaryAccessKey,
// 			EventgridTopicSecondaryAccessKey: exampleTopic.SecondaryAccessKey,
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
// Digital Twins Eventgrid Endpoints can be imported using the `resource id`, e.g.
//
// ```sh
//  $ pulumi import azure:digitaltwins/endpointEventGrid:EndpointEventGrid example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.DigitalTwins/digitalTwinsInstances/dt1/endpoints/ep1
// ```
type EndpointEventGrid struct {
	pulumi.CustomResourceState

	// The storage secret of the dead-lettering, whose format is `https://<storageAccountname>.blob.core.windows.net/<containerName>?<SASToken>`. When an endpoint can't deliver an event within a certain time period or after trying to deliver the event a certain number of times, it can send the undelivered event to a storage account.
	DeadLetterStorageSecret pulumi.StringPtrOutput `pulumi:"deadLetterStorageSecret"`
	// The resource ID of the Digital Twins Instance. Changing this forces a new Digital Twins Eventgrid Endpoint to be created.
	DigitalTwinsId pulumi.StringOutput `pulumi:"digitalTwinsId"`
	// The endpoint of the Event Grid Topic.
	EventgridTopicEndpoint pulumi.StringOutput `pulumi:"eventgridTopicEndpoint"`
	// The primary access key of the Event Grid Topic.
	EventgridTopicPrimaryAccessKey pulumi.StringOutput `pulumi:"eventgridTopicPrimaryAccessKey"`
	// The secondary access key of the Event Grid Topic.
	EventgridTopicSecondaryAccessKey pulumi.StringOutput `pulumi:"eventgridTopicSecondaryAccessKey"`
	// The name which should be used for this Digital Twins Eventgrid Endpoint. Changing this forces a new Digital Twins Eventgrid Endpoint to be created.
	Name pulumi.StringOutput `pulumi:"name"`
}

// NewEndpointEventGrid registers a new resource with the given unique name, arguments, and options.
func NewEndpointEventGrid(ctx *pulumi.Context,
	name string, args *EndpointEventGridArgs, opts ...pulumi.ResourceOption) (*EndpointEventGrid, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DigitalTwinsId == nil {
		return nil, errors.New("invalid value for required argument 'DigitalTwinsId'")
	}
	if args.EventgridTopicEndpoint == nil {
		return nil, errors.New("invalid value for required argument 'EventgridTopicEndpoint'")
	}
	if args.EventgridTopicPrimaryAccessKey == nil {
		return nil, errors.New("invalid value for required argument 'EventgridTopicPrimaryAccessKey'")
	}
	if args.EventgridTopicSecondaryAccessKey == nil {
		return nil, errors.New("invalid value for required argument 'EventgridTopicSecondaryAccessKey'")
	}
	var resource EndpointEventGrid
	err := ctx.RegisterResource("azure:digitaltwins/endpointEventGrid:EndpointEventGrid", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEndpointEventGrid gets an existing EndpointEventGrid resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEndpointEventGrid(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EndpointEventGridState, opts ...pulumi.ResourceOption) (*EndpointEventGrid, error) {
	var resource EndpointEventGrid
	err := ctx.ReadResource("azure:digitaltwins/endpointEventGrid:EndpointEventGrid", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EndpointEventGrid resources.
type endpointEventGridState struct {
	// The storage secret of the dead-lettering, whose format is `https://<storageAccountname>.blob.core.windows.net/<containerName>?<SASToken>`. When an endpoint can't deliver an event within a certain time period or after trying to deliver the event a certain number of times, it can send the undelivered event to a storage account.
	DeadLetterStorageSecret *string `pulumi:"deadLetterStorageSecret"`
	// The resource ID of the Digital Twins Instance. Changing this forces a new Digital Twins Eventgrid Endpoint to be created.
	DigitalTwinsId *string `pulumi:"digitalTwinsId"`
	// The endpoint of the Event Grid Topic.
	EventgridTopicEndpoint *string `pulumi:"eventgridTopicEndpoint"`
	// The primary access key of the Event Grid Topic.
	EventgridTopicPrimaryAccessKey *string `pulumi:"eventgridTopicPrimaryAccessKey"`
	// The secondary access key of the Event Grid Topic.
	EventgridTopicSecondaryAccessKey *string `pulumi:"eventgridTopicSecondaryAccessKey"`
	// The name which should be used for this Digital Twins Eventgrid Endpoint. Changing this forces a new Digital Twins Eventgrid Endpoint to be created.
	Name *string `pulumi:"name"`
}

type EndpointEventGridState struct {
	// The storage secret of the dead-lettering, whose format is `https://<storageAccountname>.blob.core.windows.net/<containerName>?<SASToken>`. When an endpoint can't deliver an event within a certain time period or after trying to deliver the event a certain number of times, it can send the undelivered event to a storage account.
	DeadLetterStorageSecret pulumi.StringPtrInput
	// The resource ID of the Digital Twins Instance. Changing this forces a new Digital Twins Eventgrid Endpoint to be created.
	DigitalTwinsId pulumi.StringPtrInput
	// The endpoint of the Event Grid Topic.
	EventgridTopicEndpoint pulumi.StringPtrInput
	// The primary access key of the Event Grid Topic.
	EventgridTopicPrimaryAccessKey pulumi.StringPtrInput
	// The secondary access key of the Event Grid Topic.
	EventgridTopicSecondaryAccessKey pulumi.StringPtrInput
	// The name which should be used for this Digital Twins Eventgrid Endpoint. Changing this forces a new Digital Twins Eventgrid Endpoint to be created.
	Name pulumi.StringPtrInput
}

func (EndpointEventGridState) ElementType() reflect.Type {
	return reflect.TypeOf((*endpointEventGridState)(nil)).Elem()
}

type endpointEventGridArgs struct {
	// The storage secret of the dead-lettering, whose format is `https://<storageAccountname>.blob.core.windows.net/<containerName>?<SASToken>`. When an endpoint can't deliver an event within a certain time period or after trying to deliver the event a certain number of times, it can send the undelivered event to a storage account.
	DeadLetterStorageSecret *string `pulumi:"deadLetterStorageSecret"`
	// The resource ID of the Digital Twins Instance. Changing this forces a new Digital Twins Eventgrid Endpoint to be created.
	DigitalTwinsId string `pulumi:"digitalTwinsId"`
	// The endpoint of the Event Grid Topic.
	EventgridTopicEndpoint string `pulumi:"eventgridTopicEndpoint"`
	// The primary access key of the Event Grid Topic.
	EventgridTopicPrimaryAccessKey string `pulumi:"eventgridTopicPrimaryAccessKey"`
	// The secondary access key of the Event Grid Topic.
	EventgridTopicSecondaryAccessKey string `pulumi:"eventgridTopicSecondaryAccessKey"`
	// The name which should be used for this Digital Twins Eventgrid Endpoint. Changing this forces a new Digital Twins Eventgrid Endpoint to be created.
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a EndpointEventGrid resource.
type EndpointEventGridArgs struct {
	// The storage secret of the dead-lettering, whose format is `https://<storageAccountname>.blob.core.windows.net/<containerName>?<SASToken>`. When an endpoint can't deliver an event within a certain time period or after trying to deliver the event a certain number of times, it can send the undelivered event to a storage account.
	DeadLetterStorageSecret pulumi.StringPtrInput
	// The resource ID of the Digital Twins Instance. Changing this forces a new Digital Twins Eventgrid Endpoint to be created.
	DigitalTwinsId pulumi.StringInput
	// The endpoint of the Event Grid Topic.
	EventgridTopicEndpoint pulumi.StringInput
	// The primary access key of the Event Grid Topic.
	EventgridTopicPrimaryAccessKey pulumi.StringInput
	// The secondary access key of the Event Grid Topic.
	EventgridTopicSecondaryAccessKey pulumi.StringInput
	// The name which should be used for this Digital Twins Eventgrid Endpoint. Changing this forces a new Digital Twins Eventgrid Endpoint to be created.
	Name pulumi.StringPtrInput
}

func (EndpointEventGridArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*endpointEventGridArgs)(nil)).Elem()
}

type EndpointEventGridInput interface {
	pulumi.Input

	ToEndpointEventGridOutput() EndpointEventGridOutput
	ToEndpointEventGridOutputWithContext(ctx context.Context) EndpointEventGridOutput
}

func (EndpointEventGrid) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointEventGrid)(nil)).Elem()
}

func (i EndpointEventGrid) ToEndpointEventGridOutput() EndpointEventGridOutput {
	return i.ToEndpointEventGridOutputWithContext(context.Background())
}

func (i EndpointEventGrid) ToEndpointEventGridOutputWithContext(ctx context.Context) EndpointEventGridOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointEventGridOutput)
}

type EndpointEventGridOutput struct {
	*pulumi.OutputState
}

func (EndpointEventGridOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointEventGridOutput)(nil)).Elem()
}

func (o EndpointEventGridOutput) ToEndpointEventGridOutput() EndpointEventGridOutput {
	return o
}

func (o EndpointEventGridOutput) ToEndpointEventGridOutputWithContext(ctx context.Context) EndpointEventGridOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(EndpointEventGridOutput{})
}
