// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a SSH Public Key.
//
// ## Import
//
// SSH Public Keys can be imported using the `resource id`, e.g.
//
// ```sh
//  $ pulumi import azure:compute/sshPublicKey:SshPublicKey example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Compute/SshPublicKeys/mySshPublicKeyName1
// ```
type SshPublicKey struct {
	pulumi.CustomResourceState

	// The Azure Region where the SSH Public Key should exist. Changing this forces a new SSH Public Key to be created.
	Location pulumi.StringOutput `pulumi:"location"`
	// The name which should be used for this SSH Public Key. Changing this forces a new SSH Public Key to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// SSH public key used to authenticate to a virtual machine through ssh. the provided public key needs to be at least 2048-bit and in ssh-rsa format.
	PublicKey pulumi.StringOutput `pulumi:"publicKey"`
	// The name of the Resource Group where the SSH Public Key should exist. Changing this forces a new SSH Public Key to be created.
	ResourceGroupName pulumi.StringOutput `pulumi:"resourceGroupName"`
	// A mapping of tags which should be assigned to the SSH Public Key.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
}

// NewSshPublicKey registers a new resource with the given unique name, arguments, and options.
func NewSshPublicKey(ctx *pulumi.Context,
	name string, args *SshPublicKeyArgs, opts ...pulumi.ResourceOption) (*SshPublicKey, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.PublicKey == nil {
		return nil, errors.New("invalid value for required argument 'PublicKey'")
	}
	if args.ResourceGroupName == nil {
		return nil, errors.New("invalid value for required argument 'ResourceGroupName'")
	}
	var resource SshPublicKey
	err := ctx.RegisterResource("azure:compute/sshPublicKey:SshPublicKey", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSshPublicKey gets an existing SshPublicKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSshPublicKey(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SshPublicKeyState, opts ...pulumi.ResourceOption) (*SshPublicKey, error) {
	var resource SshPublicKey
	err := ctx.ReadResource("azure:compute/sshPublicKey:SshPublicKey", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SshPublicKey resources.
type sshPublicKeyState struct {
	// The Azure Region where the SSH Public Key should exist. Changing this forces a new SSH Public Key to be created.
	Location *string `pulumi:"location"`
	// The name which should be used for this SSH Public Key. Changing this forces a new SSH Public Key to be created.
	Name *string `pulumi:"name"`
	// SSH public key used to authenticate to a virtual machine through ssh. the provided public key needs to be at least 2048-bit and in ssh-rsa format.
	PublicKey *string `pulumi:"publicKey"`
	// The name of the Resource Group where the SSH Public Key should exist. Changing this forces a new SSH Public Key to be created.
	ResourceGroupName *string `pulumi:"resourceGroupName"`
	// A mapping of tags which should be assigned to the SSH Public Key.
	Tags map[string]string `pulumi:"tags"`
}

type SshPublicKeyState struct {
	// The Azure Region where the SSH Public Key should exist. Changing this forces a new SSH Public Key to be created.
	Location pulumi.StringPtrInput
	// The name which should be used for this SSH Public Key. Changing this forces a new SSH Public Key to be created.
	Name pulumi.StringPtrInput
	// SSH public key used to authenticate to a virtual machine through ssh. the provided public key needs to be at least 2048-bit and in ssh-rsa format.
	PublicKey pulumi.StringPtrInput
	// The name of the Resource Group where the SSH Public Key should exist. Changing this forces a new SSH Public Key to be created.
	ResourceGroupName pulumi.StringPtrInput
	// A mapping of tags which should be assigned to the SSH Public Key.
	Tags pulumi.StringMapInput
}

func (SshPublicKeyState) ElementType() reflect.Type {
	return reflect.TypeOf((*sshPublicKeyState)(nil)).Elem()
}

type sshPublicKeyArgs struct {
	// The Azure Region where the SSH Public Key should exist. Changing this forces a new SSH Public Key to be created.
	Location *string `pulumi:"location"`
	// The name which should be used for this SSH Public Key. Changing this forces a new SSH Public Key to be created.
	Name *string `pulumi:"name"`
	// SSH public key used to authenticate to a virtual machine through ssh. the provided public key needs to be at least 2048-bit and in ssh-rsa format.
	PublicKey string `pulumi:"publicKey"`
	// The name of the Resource Group where the SSH Public Key should exist. Changing this forces a new SSH Public Key to be created.
	ResourceGroupName string `pulumi:"resourceGroupName"`
	// A mapping of tags which should be assigned to the SSH Public Key.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a SshPublicKey resource.
type SshPublicKeyArgs struct {
	// The Azure Region where the SSH Public Key should exist. Changing this forces a new SSH Public Key to be created.
	Location pulumi.StringPtrInput
	// The name which should be used for this SSH Public Key. Changing this forces a new SSH Public Key to be created.
	Name pulumi.StringPtrInput
	// SSH public key used to authenticate to a virtual machine through ssh. the provided public key needs to be at least 2048-bit and in ssh-rsa format.
	PublicKey pulumi.StringInput
	// The name of the Resource Group where the SSH Public Key should exist. Changing this forces a new SSH Public Key to be created.
	ResourceGroupName pulumi.StringInput
	// A mapping of tags which should be assigned to the SSH Public Key.
	Tags pulumi.StringMapInput
}

func (SshPublicKeyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*sshPublicKeyArgs)(nil)).Elem()
}

type SshPublicKeyInput interface {
	pulumi.Input

	ToSshPublicKeyOutput() SshPublicKeyOutput
	ToSshPublicKeyOutputWithContext(ctx context.Context) SshPublicKeyOutput
}

func (*SshPublicKey) ElementType() reflect.Type {
	return reflect.TypeOf((*SshPublicKey)(nil))
}

func (i *SshPublicKey) ToSshPublicKeyOutput() SshPublicKeyOutput {
	return i.ToSshPublicKeyOutputWithContext(context.Background())
}

func (i *SshPublicKey) ToSshPublicKeyOutputWithContext(ctx context.Context) SshPublicKeyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SshPublicKeyOutput)
}

func (i *SshPublicKey) ToSshPublicKeyPtrOutput() SshPublicKeyPtrOutput {
	return i.ToSshPublicKeyPtrOutputWithContext(context.Background())
}

func (i *SshPublicKey) ToSshPublicKeyPtrOutputWithContext(ctx context.Context) SshPublicKeyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SshPublicKeyPtrOutput)
}

type SshPublicKeyPtrInput interface {
	pulumi.Input

	ToSshPublicKeyPtrOutput() SshPublicKeyPtrOutput
	ToSshPublicKeyPtrOutputWithContext(ctx context.Context) SshPublicKeyPtrOutput
}

type sshPublicKeyPtrType SshPublicKeyArgs

func (*sshPublicKeyPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**SshPublicKey)(nil))
}

func (i *sshPublicKeyPtrType) ToSshPublicKeyPtrOutput() SshPublicKeyPtrOutput {
	return i.ToSshPublicKeyPtrOutputWithContext(context.Background())
}

func (i *sshPublicKeyPtrType) ToSshPublicKeyPtrOutputWithContext(ctx context.Context) SshPublicKeyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SshPublicKeyPtrOutput)
}

// SshPublicKeyArrayInput is an input type that accepts SshPublicKeyArray and SshPublicKeyArrayOutput values.
// You can construct a concrete instance of `SshPublicKeyArrayInput` via:
//
//          SshPublicKeyArray{ SshPublicKeyArgs{...} }
type SshPublicKeyArrayInput interface {
	pulumi.Input

	ToSshPublicKeyArrayOutput() SshPublicKeyArrayOutput
	ToSshPublicKeyArrayOutputWithContext(context.Context) SshPublicKeyArrayOutput
}

type SshPublicKeyArray []SshPublicKeyInput

func (SshPublicKeyArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*SshPublicKey)(nil))
}

func (i SshPublicKeyArray) ToSshPublicKeyArrayOutput() SshPublicKeyArrayOutput {
	return i.ToSshPublicKeyArrayOutputWithContext(context.Background())
}

func (i SshPublicKeyArray) ToSshPublicKeyArrayOutputWithContext(ctx context.Context) SshPublicKeyArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SshPublicKeyArrayOutput)
}

// SshPublicKeyMapInput is an input type that accepts SshPublicKeyMap and SshPublicKeyMapOutput values.
// You can construct a concrete instance of `SshPublicKeyMapInput` via:
//
//          SshPublicKeyMap{ "key": SshPublicKeyArgs{...} }
type SshPublicKeyMapInput interface {
	pulumi.Input

	ToSshPublicKeyMapOutput() SshPublicKeyMapOutput
	ToSshPublicKeyMapOutputWithContext(context.Context) SshPublicKeyMapOutput
}

type SshPublicKeyMap map[string]SshPublicKeyInput

func (SshPublicKeyMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*SshPublicKey)(nil))
}

func (i SshPublicKeyMap) ToSshPublicKeyMapOutput() SshPublicKeyMapOutput {
	return i.ToSshPublicKeyMapOutputWithContext(context.Background())
}

func (i SshPublicKeyMap) ToSshPublicKeyMapOutputWithContext(ctx context.Context) SshPublicKeyMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SshPublicKeyMapOutput)
}

type SshPublicKeyOutput struct {
	*pulumi.OutputState
}

func (SshPublicKeyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SshPublicKey)(nil))
}

func (o SshPublicKeyOutput) ToSshPublicKeyOutput() SshPublicKeyOutput {
	return o
}

func (o SshPublicKeyOutput) ToSshPublicKeyOutputWithContext(ctx context.Context) SshPublicKeyOutput {
	return o
}

func (o SshPublicKeyOutput) ToSshPublicKeyPtrOutput() SshPublicKeyPtrOutput {
	return o.ToSshPublicKeyPtrOutputWithContext(context.Background())
}

func (o SshPublicKeyOutput) ToSshPublicKeyPtrOutputWithContext(ctx context.Context) SshPublicKeyPtrOutput {
	return o.ApplyT(func(v SshPublicKey) *SshPublicKey {
		return &v
	}).(SshPublicKeyPtrOutput)
}

type SshPublicKeyPtrOutput struct {
	*pulumi.OutputState
}

func (SshPublicKeyPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SshPublicKey)(nil))
}

func (o SshPublicKeyPtrOutput) ToSshPublicKeyPtrOutput() SshPublicKeyPtrOutput {
	return o
}

func (o SshPublicKeyPtrOutput) ToSshPublicKeyPtrOutputWithContext(ctx context.Context) SshPublicKeyPtrOutput {
	return o
}

type SshPublicKeyArrayOutput struct{ *pulumi.OutputState }

func (SshPublicKeyArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]SshPublicKey)(nil))
}

func (o SshPublicKeyArrayOutput) ToSshPublicKeyArrayOutput() SshPublicKeyArrayOutput {
	return o
}

func (o SshPublicKeyArrayOutput) ToSshPublicKeyArrayOutputWithContext(ctx context.Context) SshPublicKeyArrayOutput {
	return o
}

func (o SshPublicKeyArrayOutput) Index(i pulumi.IntInput) SshPublicKeyOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) SshPublicKey {
		return vs[0].([]SshPublicKey)[vs[1].(int)]
	}).(SshPublicKeyOutput)
}

type SshPublicKeyMapOutput struct{ *pulumi.OutputState }

func (SshPublicKeyMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]SshPublicKey)(nil))
}

func (o SshPublicKeyMapOutput) ToSshPublicKeyMapOutput() SshPublicKeyMapOutput {
	return o
}

func (o SshPublicKeyMapOutput) ToSshPublicKeyMapOutputWithContext(ctx context.Context) SshPublicKeyMapOutput {
	return o
}

func (o SshPublicKeyMapOutput) MapIndex(k pulumi.StringInput) SshPublicKeyOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) SshPublicKey {
		return vs[0].(map[string]SshPublicKey)[vs[1].(string)]
	}).(SshPublicKeyOutput)
}

func init() {
	pulumi.RegisterOutputType(SshPublicKeyOutput{})
	pulumi.RegisterOutputType(SshPublicKeyPtrOutput{})
	pulumi.RegisterOutputType(SshPublicKeyArrayOutput{})
	pulumi.RegisterOutputType(SshPublicKeyMapOutput{})
}
