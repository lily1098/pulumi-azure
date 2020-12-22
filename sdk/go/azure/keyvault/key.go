// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package keyvault

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Key Vault Key.
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
// 			SoftDeleteEnabled:       pulumi.Bool(true),
// 			SoftDeleteRetentionDays: pulumi.Int(7),
// 			AccessPolicies: keyvault.KeyVaultAccessPolicyArray{
// 				&keyvault.KeyVaultAccessPolicyArgs{
// 					TenantId: pulumi.String(current.TenantId),
// 					ObjectId: pulumi.String(current.ObjectId),
// 					KeyPermissions: pulumi.StringArray{
// 						pulumi.String("create"),
// 						pulumi.String("get"),
// 						pulumi.String("purge"),
// 						pulumi.String("recover"),
// 					},
// 					SecretPermissions: pulumi.StringArray{
// 						pulumi.String("set"),
// 					},
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = keyvault.NewKey(ctx, "generated", &keyvault.KeyArgs{
// 			KeyVaultId: exampleKeyVault.ID(),
// 			KeyType:    pulumi.String("RSA"),
// 			KeySize:    pulumi.Int(2048),
// 			KeyOpts: pulumi.StringArray{
// 				pulumi.String("decrypt"),
// 				pulumi.String("encrypt"),
// 				pulumi.String("sign"),
// 				pulumi.String("unwrapKey"),
// 				pulumi.String("verify"),
// 				pulumi.String("wrapKey"),
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
// Key Vault Key which is Enabled can be imported using the `resource id`, e.g.
//
// ```sh
//  $ pulumi import azure:keyvault/key:Key example "https://example-keyvault.vault.azure.net/keys/example/fdf067c93bbb4b22bff4d8b7a9a56217"
// ```
type Key struct {
	pulumi.CustomResourceState

	// Specifies the curve to use when creating an `EC` key. Possible values are `P-256`, `P-384`, `P-521`, and `SECP256K1`. This field will be required in a future release if `keyType` is `EC` or `EC-HSM`. The API will default to `P-256` if nothing is specified. Changing this forces a new resource to be created.
	Curve pulumi.StringOutput `pulumi:"curve"`
	// The RSA public exponent of this Key Vault Key.
	E pulumi.StringOutput `pulumi:"e"`
	// Expiration UTC datetime (Y-m-d'T'H:M:S'Z').
	ExpirationDate pulumi.StringPtrOutput `pulumi:"expirationDate"`
	// A list of JSON web key operations. Possible values include: `decrypt`, `encrypt`, `sign`, `unwrapKey`, `verify` and `wrapKey`. Please note these values are case sensitive.
	KeyOpts pulumi.StringArrayOutput `pulumi:"keyOpts"`
	// Specifies the Size of the RSA key to create in bytes. For example, 1024 or 2048. *Note*: This field is required if `keyType` is `RSA` or `RSA-HSM`. Changing this forces a new resource to be created.
	KeySize pulumi.IntPtrOutput `pulumi:"keySize"`
	// Specifies the Key Type to use for this Key Vault Key. Possible values are `EC` (Elliptic Curve), `EC-HSM`, `Oct` (Octet), `RSA` and `RSA-HSM`. Changing this forces a new resource to be created.
	KeyType pulumi.StringOutput `pulumi:"keyType"`
	// The ID of the Key Vault where the Key should be created. Changing this forces a new resource to be created.
	KeyVaultId pulumi.StringOutput `pulumi:"keyVaultId"`
	// The RSA modulus of this Key Vault Key.
	N pulumi.StringOutput `pulumi:"n"`
	// Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// Key not usable before the provided UTC datetime (Y-m-d'T'H:M:S'Z').
	NotBeforeDate pulumi.StringPtrOutput `pulumi:"notBeforeDate"`
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// The current version of the Key Vault Key.
	Version pulumi.StringOutput `pulumi:"version"`
	// The EC X component of this Key Vault Key.
	X pulumi.StringOutput `pulumi:"x"`
	// The EC Y component of this Key Vault Key.
	Y pulumi.StringOutput `pulumi:"y"`
}

// NewKey registers a new resource with the given unique name, arguments, and options.
func NewKey(ctx *pulumi.Context,
	name string, args *KeyArgs, opts ...pulumi.ResourceOption) (*Key, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.KeyOpts == nil {
		return nil, errors.New("invalid value for required argument 'KeyOpts'")
	}
	if args.KeyType == nil {
		return nil, errors.New("invalid value for required argument 'KeyType'")
	}
	if args.KeyVaultId == nil {
		return nil, errors.New("invalid value for required argument 'KeyVaultId'")
	}
	var resource Key
	err := ctx.RegisterResource("azure:keyvault/key:Key", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetKey gets an existing Key resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetKey(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *KeyState, opts ...pulumi.ResourceOption) (*Key, error) {
	var resource Key
	err := ctx.ReadResource("azure:keyvault/key:Key", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Key resources.
type keyState struct {
	// Specifies the curve to use when creating an `EC` key. Possible values are `P-256`, `P-384`, `P-521`, and `SECP256K1`. This field will be required in a future release if `keyType` is `EC` or `EC-HSM`. The API will default to `P-256` if nothing is specified. Changing this forces a new resource to be created.
	Curve *string `pulumi:"curve"`
	// The RSA public exponent of this Key Vault Key.
	E *string `pulumi:"e"`
	// Expiration UTC datetime (Y-m-d'T'H:M:S'Z').
	ExpirationDate *string `pulumi:"expirationDate"`
	// A list of JSON web key operations. Possible values include: `decrypt`, `encrypt`, `sign`, `unwrapKey`, `verify` and `wrapKey`. Please note these values are case sensitive.
	KeyOpts []string `pulumi:"keyOpts"`
	// Specifies the Size of the RSA key to create in bytes. For example, 1024 or 2048. *Note*: This field is required if `keyType` is `RSA` or `RSA-HSM`. Changing this forces a new resource to be created.
	KeySize *int `pulumi:"keySize"`
	// Specifies the Key Type to use for this Key Vault Key. Possible values are `EC` (Elliptic Curve), `EC-HSM`, `Oct` (Octet), `RSA` and `RSA-HSM`. Changing this forces a new resource to be created.
	KeyType *string `pulumi:"keyType"`
	// The ID of the Key Vault where the Key should be created. Changing this forces a new resource to be created.
	KeyVaultId *string `pulumi:"keyVaultId"`
	// The RSA modulus of this Key Vault Key.
	N *string `pulumi:"n"`
	// Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// Key not usable before the provided UTC datetime (Y-m-d'T'H:M:S'Z').
	NotBeforeDate *string `pulumi:"notBeforeDate"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// The current version of the Key Vault Key.
	Version *string `pulumi:"version"`
	// The EC X component of this Key Vault Key.
	X *string `pulumi:"x"`
	// The EC Y component of this Key Vault Key.
	Y *string `pulumi:"y"`
}

type KeyState struct {
	// Specifies the curve to use when creating an `EC` key. Possible values are `P-256`, `P-384`, `P-521`, and `SECP256K1`. This field will be required in a future release if `keyType` is `EC` or `EC-HSM`. The API will default to `P-256` if nothing is specified. Changing this forces a new resource to be created.
	Curve pulumi.StringPtrInput
	// The RSA public exponent of this Key Vault Key.
	E pulumi.StringPtrInput
	// Expiration UTC datetime (Y-m-d'T'H:M:S'Z').
	ExpirationDate pulumi.StringPtrInput
	// A list of JSON web key operations. Possible values include: `decrypt`, `encrypt`, `sign`, `unwrapKey`, `verify` and `wrapKey`. Please note these values are case sensitive.
	KeyOpts pulumi.StringArrayInput
	// Specifies the Size of the RSA key to create in bytes. For example, 1024 or 2048. *Note*: This field is required if `keyType` is `RSA` or `RSA-HSM`. Changing this forces a new resource to be created.
	KeySize pulumi.IntPtrInput
	// Specifies the Key Type to use for this Key Vault Key. Possible values are `EC` (Elliptic Curve), `EC-HSM`, `Oct` (Octet), `RSA` and `RSA-HSM`. Changing this forces a new resource to be created.
	KeyType pulumi.StringPtrInput
	// The ID of the Key Vault where the Key should be created. Changing this forces a new resource to be created.
	KeyVaultId pulumi.StringPtrInput
	// The RSA modulus of this Key Vault Key.
	N pulumi.StringPtrInput
	// Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// Key not usable before the provided UTC datetime (Y-m-d'T'H:M:S'Z').
	NotBeforeDate pulumi.StringPtrInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// The current version of the Key Vault Key.
	Version pulumi.StringPtrInput
	// The EC X component of this Key Vault Key.
	X pulumi.StringPtrInput
	// The EC Y component of this Key Vault Key.
	Y pulumi.StringPtrInput
}

func (KeyState) ElementType() reflect.Type {
	return reflect.TypeOf((*keyState)(nil)).Elem()
}

type keyArgs struct {
	// Specifies the curve to use when creating an `EC` key. Possible values are `P-256`, `P-384`, `P-521`, and `SECP256K1`. This field will be required in a future release if `keyType` is `EC` or `EC-HSM`. The API will default to `P-256` if nothing is specified. Changing this forces a new resource to be created.
	Curve *string `pulumi:"curve"`
	// Expiration UTC datetime (Y-m-d'T'H:M:S'Z').
	ExpirationDate *string `pulumi:"expirationDate"`
	// A list of JSON web key operations. Possible values include: `decrypt`, `encrypt`, `sign`, `unwrapKey`, `verify` and `wrapKey`. Please note these values are case sensitive.
	KeyOpts []string `pulumi:"keyOpts"`
	// Specifies the Size of the RSA key to create in bytes. For example, 1024 or 2048. *Note*: This field is required if `keyType` is `RSA` or `RSA-HSM`. Changing this forces a new resource to be created.
	KeySize *int `pulumi:"keySize"`
	// Specifies the Key Type to use for this Key Vault Key. Possible values are `EC` (Elliptic Curve), `EC-HSM`, `Oct` (Octet), `RSA` and `RSA-HSM`. Changing this forces a new resource to be created.
	KeyType string `pulumi:"keyType"`
	// The ID of the Key Vault where the Key should be created. Changing this forces a new resource to be created.
	KeyVaultId string `pulumi:"keyVaultId"`
	// Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// Key not usable before the provided UTC datetime (Y-m-d'T'H:M:S'Z').
	NotBeforeDate *string `pulumi:"notBeforeDate"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a Key resource.
type KeyArgs struct {
	// Specifies the curve to use when creating an `EC` key. Possible values are `P-256`, `P-384`, `P-521`, and `SECP256K1`. This field will be required in a future release if `keyType` is `EC` or `EC-HSM`. The API will default to `P-256` if nothing is specified. Changing this forces a new resource to be created.
	Curve pulumi.StringPtrInput
	// Expiration UTC datetime (Y-m-d'T'H:M:S'Z').
	ExpirationDate pulumi.StringPtrInput
	// A list of JSON web key operations. Possible values include: `decrypt`, `encrypt`, `sign`, `unwrapKey`, `verify` and `wrapKey`. Please note these values are case sensitive.
	KeyOpts pulumi.StringArrayInput
	// Specifies the Size of the RSA key to create in bytes. For example, 1024 or 2048. *Note*: This field is required if `keyType` is `RSA` or `RSA-HSM`. Changing this forces a new resource to be created.
	KeySize pulumi.IntPtrInput
	// Specifies the Key Type to use for this Key Vault Key. Possible values are `EC` (Elliptic Curve), `EC-HSM`, `Oct` (Octet), `RSA` and `RSA-HSM`. Changing this forces a new resource to be created.
	KeyType pulumi.StringInput
	// The ID of the Key Vault where the Key should be created. Changing this forces a new resource to be created.
	KeyVaultId pulumi.StringInput
	// Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// Key not usable before the provided UTC datetime (Y-m-d'T'H:M:S'Z').
	NotBeforeDate pulumi.StringPtrInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapInput
}

func (KeyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*keyArgs)(nil)).Elem()
}

type KeyInput interface {
	pulumi.Input

	ToKeyOutput() KeyOutput
	ToKeyOutputWithContext(ctx context.Context) KeyOutput
}

func (Key) ElementType() reflect.Type {
	return reflect.TypeOf((*Key)(nil)).Elem()
}

func (i Key) ToKeyOutput() KeyOutput {
	return i.ToKeyOutputWithContext(context.Background())
}

func (i Key) ToKeyOutputWithContext(ctx context.Context) KeyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KeyOutput)
}

type KeyOutput struct {
	*pulumi.OutputState
}

func (KeyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*KeyOutput)(nil)).Elem()
}

func (o KeyOutput) ToKeyOutput() KeyOutput {
	return o
}

func (o KeyOutput) ToKeyOutputWithContext(ctx context.Context) KeyOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(KeyOutput{})
}
