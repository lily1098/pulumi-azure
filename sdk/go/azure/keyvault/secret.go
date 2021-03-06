// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package keyvault

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Key Vault Secret.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/core"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/keyvault"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		current, err := core.GetClientConfig(ctx, nil, nil)
// 		if err != nil {
// 			return err
// 		}
// 		exampleResourceGroup, err := core.NewResourceGroup(ctx, "exampleResourceGroup", &core.ResourceGroupArgs{
// 			Location: pulumi.String("West Europe"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleKeyVault, err := keyvault.NewKeyVault(ctx, "exampleKeyVault", &keyvault.KeyVaultArgs{
// 			Location:                exampleResourceGroup.Location,
// 			ResourceGroupName:       exampleResourceGroup.Name,
// 			TenantId:                pulumi.String(current.TenantId),
// 			SkuName:                 pulumi.String("premium"),
// 			SoftDeleteRetentionDays: pulumi.Int(7),
// 			AccessPolicies: keyvault.KeyVaultAccessPolicyArray{
// 				&keyvault.KeyVaultAccessPolicyArgs{
// 					TenantId: pulumi.String(current.TenantId),
// 					ObjectId: pulumi.String(current.ObjectId),
// 					KeyPermissions: pulumi.StringArray{
// 						pulumi.String("create"),
// 						pulumi.String("get"),
// 					},
// 					SecretPermissions: pulumi.StringArray{
// 						pulumi.String("set"),
// 						pulumi.String("get"),
// 						pulumi.String("delete"),
// 						pulumi.String("purge"),
// 						pulumi.String("recover"),
// 					},
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = keyvault.NewSecret(ctx, "exampleSecret", &keyvault.SecretArgs{
// 			Value:      pulumi.String("szechuan"),
// 			KeyVaultId: exampleKeyVault.ID(),
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
// Key Vault Secrets which are Enabled can be imported using the `resource id`, e.g.
//
// ```sh
//  $ pulumi import azure:keyvault/secret:Secret example "https://example-keyvault.vault.azure.net/secrets/example/fdf067c93bbb4b22bff4d8b7a9a56217"
// ```
type Secret struct {
	pulumi.CustomResourceState

	// Specifies the content type for the Key Vault Secret.
	ContentType pulumi.StringPtrOutput `pulumi:"contentType"`
	// Expiration UTC datetime (Y-m-d'T'H:M:S'Z').
	ExpirationDate pulumi.StringPtrOutput `pulumi:"expirationDate"`
	// The ID of the Key Vault where the Secret should be created.
	KeyVaultId pulumi.StringOutput `pulumi:"keyVaultId"`
	// Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// Key not usable before the provided UTC datetime (Y-m-d'T'H:M:S'Z').
	NotBeforeDate pulumi.StringPtrOutput `pulumi:"notBeforeDate"`
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// Specifies the value of the Key Vault Secret.
	Value pulumi.StringOutput `pulumi:"value"`
	// The current version of the Key Vault Secret.
	Version pulumi.StringOutput `pulumi:"version"`
}

// NewSecret registers a new resource with the given unique name, arguments, and options.
func NewSecret(ctx *pulumi.Context,
	name string, args *SecretArgs, opts ...pulumi.ResourceOption) (*Secret, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.KeyVaultId == nil {
		return nil, errors.New("invalid value for required argument 'KeyVaultId'")
	}
	if args.Value == nil {
		return nil, errors.New("invalid value for required argument 'Value'")
	}
	var resource Secret
	err := ctx.RegisterResource("azure:keyvault/secret:Secret", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSecret gets an existing Secret resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSecret(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SecretState, opts ...pulumi.ResourceOption) (*Secret, error) {
	var resource Secret
	err := ctx.ReadResource("azure:keyvault/secret:Secret", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Secret resources.
type secretState struct {
	// Specifies the content type for the Key Vault Secret.
	ContentType *string `pulumi:"contentType"`
	// Expiration UTC datetime (Y-m-d'T'H:M:S'Z').
	ExpirationDate *string `pulumi:"expirationDate"`
	// The ID of the Key Vault where the Secret should be created.
	KeyVaultId *string `pulumi:"keyVaultId"`
	// Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// Key not usable before the provided UTC datetime (Y-m-d'T'H:M:S'Z').
	NotBeforeDate *string `pulumi:"notBeforeDate"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// Specifies the value of the Key Vault Secret.
	Value *string `pulumi:"value"`
	// The current version of the Key Vault Secret.
	Version *string `pulumi:"version"`
}

type SecretState struct {
	// Specifies the content type for the Key Vault Secret.
	ContentType pulumi.StringPtrInput
	// Expiration UTC datetime (Y-m-d'T'H:M:S'Z').
	ExpirationDate pulumi.StringPtrInput
	// The ID of the Key Vault where the Secret should be created.
	KeyVaultId pulumi.StringPtrInput
	// Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// Key not usable before the provided UTC datetime (Y-m-d'T'H:M:S'Z').
	NotBeforeDate pulumi.StringPtrInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// Specifies the value of the Key Vault Secret.
	Value pulumi.StringPtrInput
	// The current version of the Key Vault Secret.
	Version pulumi.StringPtrInput
}

func (SecretState) ElementType() reflect.Type {
	return reflect.TypeOf((*secretState)(nil)).Elem()
}

type secretArgs struct {
	// Specifies the content type for the Key Vault Secret.
	ContentType *string `pulumi:"contentType"`
	// Expiration UTC datetime (Y-m-d'T'H:M:S'Z').
	ExpirationDate *string `pulumi:"expirationDate"`
	// The ID of the Key Vault where the Secret should be created.
	KeyVaultId string `pulumi:"keyVaultId"`
	// Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// Key not usable before the provided UTC datetime (Y-m-d'T'H:M:S'Z').
	NotBeforeDate *string `pulumi:"notBeforeDate"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// Specifies the value of the Key Vault Secret.
	Value string `pulumi:"value"`
}

// The set of arguments for constructing a Secret resource.
type SecretArgs struct {
	// Specifies the content type for the Key Vault Secret.
	ContentType pulumi.StringPtrInput
	// Expiration UTC datetime (Y-m-d'T'H:M:S'Z').
	ExpirationDate pulumi.StringPtrInput
	// The ID of the Key Vault where the Secret should be created.
	KeyVaultId pulumi.StringInput
	// Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// Key not usable before the provided UTC datetime (Y-m-d'T'H:M:S'Z').
	NotBeforeDate pulumi.StringPtrInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// Specifies the value of the Key Vault Secret.
	Value pulumi.StringInput
}

func (SecretArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*secretArgs)(nil)).Elem()
}

type SecretInput interface {
	pulumi.Input

	ToSecretOutput() SecretOutput
	ToSecretOutputWithContext(ctx context.Context) SecretOutput
}

func (*Secret) ElementType() reflect.Type {
	return reflect.TypeOf((*Secret)(nil))
}

func (i *Secret) ToSecretOutput() SecretOutput {
	return i.ToSecretOutputWithContext(context.Background())
}

func (i *Secret) ToSecretOutputWithContext(ctx context.Context) SecretOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecretOutput)
}

func (i *Secret) ToSecretPtrOutput() SecretPtrOutput {
	return i.ToSecretPtrOutputWithContext(context.Background())
}

func (i *Secret) ToSecretPtrOutputWithContext(ctx context.Context) SecretPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecretPtrOutput)
}

type SecretPtrInput interface {
	pulumi.Input

	ToSecretPtrOutput() SecretPtrOutput
	ToSecretPtrOutputWithContext(ctx context.Context) SecretPtrOutput
}

type secretPtrType SecretArgs

func (*secretPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Secret)(nil))
}

func (i *secretPtrType) ToSecretPtrOutput() SecretPtrOutput {
	return i.ToSecretPtrOutputWithContext(context.Background())
}

func (i *secretPtrType) ToSecretPtrOutputWithContext(ctx context.Context) SecretPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecretPtrOutput)
}

// SecretArrayInput is an input type that accepts SecretArray and SecretArrayOutput values.
// You can construct a concrete instance of `SecretArrayInput` via:
//
//          SecretArray{ SecretArgs{...} }
type SecretArrayInput interface {
	pulumi.Input

	ToSecretArrayOutput() SecretArrayOutput
	ToSecretArrayOutputWithContext(context.Context) SecretArrayOutput
}

type SecretArray []SecretInput

func (SecretArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*Secret)(nil))
}

func (i SecretArray) ToSecretArrayOutput() SecretArrayOutput {
	return i.ToSecretArrayOutputWithContext(context.Background())
}

func (i SecretArray) ToSecretArrayOutputWithContext(ctx context.Context) SecretArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecretArrayOutput)
}

// SecretMapInput is an input type that accepts SecretMap and SecretMapOutput values.
// You can construct a concrete instance of `SecretMapInput` via:
//
//          SecretMap{ "key": SecretArgs{...} }
type SecretMapInput interface {
	pulumi.Input

	ToSecretMapOutput() SecretMapOutput
	ToSecretMapOutputWithContext(context.Context) SecretMapOutput
}

type SecretMap map[string]SecretInput

func (SecretMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*Secret)(nil))
}

func (i SecretMap) ToSecretMapOutput() SecretMapOutput {
	return i.ToSecretMapOutputWithContext(context.Background())
}

func (i SecretMap) ToSecretMapOutputWithContext(ctx context.Context) SecretMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecretMapOutput)
}

type SecretOutput struct {
	*pulumi.OutputState
}

func (SecretOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Secret)(nil))
}

func (o SecretOutput) ToSecretOutput() SecretOutput {
	return o
}

func (o SecretOutput) ToSecretOutputWithContext(ctx context.Context) SecretOutput {
	return o
}

func (o SecretOutput) ToSecretPtrOutput() SecretPtrOutput {
	return o.ToSecretPtrOutputWithContext(context.Background())
}

func (o SecretOutput) ToSecretPtrOutputWithContext(ctx context.Context) SecretPtrOutput {
	return o.ApplyT(func(v Secret) *Secret {
		return &v
	}).(SecretPtrOutput)
}

type SecretPtrOutput struct {
	*pulumi.OutputState
}

func (SecretPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Secret)(nil))
}

func (o SecretPtrOutput) ToSecretPtrOutput() SecretPtrOutput {
	return o
}

func (o SecretPtrOutput) ToSecretPtrOutputWithContext(ctx context.Context) SecretPtrOutput {
	return o
}

type SecretArrayOutput struct{ *pulumi.OutputState }

func (SecretArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Secret)(nil))
}

func (o SecretArrayOutput) ToSecretArrayOutput() SecretArrayOutput {
	return o
}

func (o SecretArrayOutput) ToSecretArrayOutputWithContext(ctx context.Context) SecretArrayOutput {
	return o
}

func (o SecretArrayOutput) Index(i pulumi.IntInput) SecretOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Secret {
		return vs[0].([]Secret)[vs[1].(int)]
	}).(SecretOutput)
}

type SecretMapOutput struct{ *pulumi.OutputState }

func (SecretMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]Secret)(nil))
}

func (o SecretMapOutput) ToSecretMapOutput() SecretMapOutput {
	return o
}

func (o SecretMapOutput) ToSecretMapOutputWithContext(ctx context.Context) SecretMapOutput {
	return o
}

func (o SecretMapOutput) MapIndex(k pulumi.StringInput) SecretOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) Secret {
		return vs[0].(map[string]Secret)[vs[1].(string)]
	}).(SecretOutput)
}

func init() {
	pulumi.RegisterOutputType(SecretOutput{})
	pulumi.RegisterOutputType(SecretPtrOutput{})
	pulumi.RegisterOutputType(SecretArrayOutput{})
	pulumi.RegisterOutputType(SecretMapOutput{})
}
