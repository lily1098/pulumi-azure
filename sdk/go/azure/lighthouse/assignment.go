// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package lighthouse

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a [Lighthouse](https://docs.microsoft.com/en-us/azure/lighthouse) Assignment to a subscription, or to a resource group.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/lighthouse"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := lighthouse.NewAssignment(ctx, "example", &lighthouse.AssignmentArgs{
// 			LighthouseDefinitionId: pulumi.String("/subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.ManagedServices/registrationDefinitions/00000000-0000-0000-0000-000000000000"),
// 			Scope:                  pulumi.String("/subscription/00000000-0000-0000-0000-000000000000"),
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
// Lighthouse Assignments can be imported using the `resource id`, e.g.
//
// ```sh
//  $ pulumi import azure:lighthouse/assignment:Assignment example /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.ManagedServices/registrationAssignments/00000000-0000-0000-0000-000000000000
// ```
type Assignment struct {
	pulumi.CustomResourceState

	// A Fully qualified path of the lighthouse definition, such as `/subscriptions/0afefe50-734e-4610-8c82-a144aff49dea/providers/Microsoft.ManagedServices/registrationDefinitions/26c128c2-fefa-4340-9bb1-8e081c90ada2`. Changing this forces a new resource to be created.
	LighthouseDefinitionId pulumi.StringOutput `pulumi:"lighthouseDefinitionId"`
	// A unique UUID/GUID which identifies this lighthouse assignment- one will be generated if not specified. Changing this forces a new resource to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// The scope at which the Lighthouse Assignment applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333` or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`. Changing this forces a new resource to be created.
	Scope pulumi.StringOutput `pulumi:"scope"`
}

// NewAssignment registers a new resource with the given unique name, arguments, and options.
func NewAssignment(ctx *pulumi.Context,
	name string, args *AssignmentArgs, opts ...pulumi.ResourceOption) (*Assignment, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.LighthouseDefinitionId == nil {
		return nil, errors.New("invalid value for required argument 'LighthouseDefinitionId'")
	}
	if args.Scope == nil {
		return nil, errors.New("invalid value for required argument 'Scope'")
	}
	var resource Assignment
	err := ctx.RegisterResource("azure:lighthouse/assignment:Assignment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAssignment gets an existing Assignment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAssignment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AssignmentState, opts ...pulumi.ResourceOption) (*Assignment, error) {
	var resource Assignment
	err := ctx.ReadResource("azure:lighthouse/assignment:Assignment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Assignment resources.
type assignmentState struct {
	// A Fully qualified path of the lighthouse definition, such as `/subscriptions/0afefe50-734e-4610-8c82-a144aff49dea/providers/Microsoft.ManagedServices/registrationDefinitions/26c128c2-fefa-4340-9bb1-8e081c90ada2`. Changing this forces a new resource to be created.
	LighthouseDefinitionId *string `pulumi:"lighthouseDefinitionId"`
	// A unique UUID/GUID which identifies this lighthouse assignment- one will be generated if not specified. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// The scope at which the Lighthouse Assignment applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333` or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`. Changing this forces a new resource to be created.
	Scope *string `pulumi:"scope"`
}

type AssignmentState struct {
	// A Fully qualified path of the lighthouse definition, such as `/subscriptions/0afefe50-734e-4610-8c82-a144aff49dea/providers/Microsoft.ManagedServices/registrationDefinitions/26c128c2-fefa-4340-9bb1-8e081c90ada2`. Changing this forces a new resource to be created.
	LighthouseDefinitionId pulumi.StringPtrInput
	// A unique UUID/GUID which identifies this lighthouse assignment- one will be generated if not specified. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// The scope at which the Lighthouse Assignment applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333` or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`. Changing this forces a new resource to be created.
	Scope pulumi.StringPtrInput
}

func (AssignmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*assignmentState)(nil)).Elem()
}

type assignmentArgs struct {
	// A Fully qualified path of the lighthouse definition, such as `/subscriptions/0afefe50-734e-4610-8c82-a144aff49dea/providers/Microsoft.ManagedServices/registrationDefinitions/26c128c2-fefa-4340-9bb1-8e081c90ada2`. Changing this forces a new resource to be created.
	LighthouseDefinitionId string `pulumi:"lighthouseDefinitionId"`
	// A unique UUID/GUID which identifies this lighthouse assignment- one will be generated if not specified. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// The scope at which the Lighthouse Assignment applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333` or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`. Changing this forces a new resource to be created.
	Scope string `pulumi:"scope"`
}

// The set of arguments for constructing a Assignment resource.
type AssignmentArgs struct {
	// A Fully qualified path of the lighthouse definition, such as `/subscriptions/0afefe50-734e-4610-8c82-a144aff49dea/providers/Microsoft.ManagedServices/registrationDefinitions/26c128c2-fefa-4340-9bb1-8e081c90ada2`. Changing this forces a new resource to be created.
	LighthouseDefinitionId pulumi.StringInput
	// A unique UUID/GUID which identifies this lighthouse assignment- one will be generated if not specified. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// The scope at which the Lighthouse Assignment applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333` or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`. Changing this forces a new resource to be created.
	Scope pulumi.StringInput
}

func (AssignmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*assignmentArgs)(nil)).Elem()
}

type AssignmentInput interface {
	pulumi.Input

	ToAssignmentOutput() AssignmentOutput
	ToAssignmentOutputWithContext(ctx context.Context) AssignmentOutput
}

func (Assignment) ElementType() reflect.Type {
	return reflect.TypeOf((*Assignment)(nil)).Elem()
}

func (i Assignment) ToAssignmentOutput() AssignmentOutput {
	return i.ToAssignmentOutputWithContext(context.Background())
}

func (i Assignment) ToAssignmentOutputWithContext(ctx context.Context) AssignmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AssignmentOutput)
}

type AssignmentOutput struct {
	*pulumi.OutputState
}

func (AssignmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AssignmentOutput)(nil)).Elem()
}

func (o AssignmentOutput) ToAssignmentOutput() AssignmentOutput {
	return o
}

func (o AssignmentOutput) ToAssignmentOutputWithContext(ctx context.Context) AssignmentOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(AssignmentOutput{})
}
