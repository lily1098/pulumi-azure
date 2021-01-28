// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hpc

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a HPC Cache.
//
// > **Note**: During the first several months of the GA release, a request must be made to the Azure HPC Cache team to add your subscription to the access list before it can be used to create a cache instance. Fill out [this form](https://aka.ms/onboard-hpc-cache) to request access.
//
// > **NOTE:**: By request of the service team the provider no longer automatically registering the `Microsoft.StorageCache` Resource Provider for this resource. To register it you can run `az provider register --namespace 'Microsoft.StorageCache'`.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/core"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/hpc"
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/network"
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
// 		exampleVirtualNetwork, err := network.NewVirtualNetwork(ctx, "exampleVirtualNetwork", &network.VirtualNetworkArgs{
// 			AddressSpaces: pulumi.StringArray{
// 				pulumi.String("10.0.0.0/16"),
// 			},
// 			Location:          exampleResourceGroup.Location,
// 			ResourceGroupName: exampleResourceGroup.Name,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		exampleSubnet, err := network.NewSubnet(ctx, "exampleSubnet", &network.SubnetArgs{
// 			ResourceGroupName:  exampleResourceGroup.Name,
// 			VirtualNetworkName: exampleVirtualNetwork.Name,
// 			AddressPrefixes: pulumi.StringArray{
// 				pulumi.String("10.0.1.0/24"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = hpc.NewCache(ctx, "exampleCache", &hpc.CacheArgs{
// 			ResourceGroupName: exampleResourceGroup.Name,
// 			Location:          exampleResourceGroup.Location,
// 			CacheSizeInGb:     pulumi.Int(3072),
// 			SubnetId:          exampleSubnet.ID(),
// 			SkuName:           pulumi.String("Standard_2G"),
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
// HPC Caches can be imported using the `resource id`, e.g.
//
// ```sh
//  $ pulumi import azure:hpc/cache:Cache example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroupName/providers/Microsoft.StorageCache/caches/cacheName
// ```
type Cache struct {
	pulumi.CustomResourceState

	// The size of the HPC Cache, in GB. Possible values are `3072`, `6144`, `12288`, `24576`, and `49152`. Changing this forces a new resource to be created.
	CacheSizeInGb pulumi.IntOutput `pulumi:"cacheSizeInGb"`
	// Specifies the supported Azure Region where the HPC Cache should be created. Changing this forces a new resource to be created.
	Location pulumi.StringOutput `pulumi:"location"`
	// A list of IP Addresses where the HPC Cache can be mounted.
	MountAddresses pulumi.StringArrayOutput `pulumi:"mountAddresses"`
	// The IPv4 maximum transmission unit configured for the subnet of the HPC Cache. Possible values range from 576 - 1500. Defaults to 1500.
	Mtu pulumi.IntPtrOutput `pulumi:"mtu"`
	// The name of the HPC Cache. Changing this forces a new resource to be created.
	Name pulumi.StringOutput `pulumi:"name"`
	// The name of the Resource Group in which to create the HPC Cache. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringOutput `pulumi:"resourceGroupName"`
	// Whether root squash property is enabled for this HPC Cache.
	RootSquashEnabled pulumi.BoolOutput `pulumi:"rootSquashEnabled"`
	// The SKU of HPC Cache to use. Possible values are `Standard_2G`, `Standard_4G` and `Standard_8G`. Changing this forces a new resource to be created.
	SkuName pulumi.StringOutput `pulumi:"skuName"`
	// The ID of the Subnet for the HPC Cache. Changing this forces a new resource to be created.
	SubnetId pulumi.StringOutput `pulumi:"subnetId"`
}

// NewCache registers a new resource with the given unique name, arguments, and options.
func NewCache(ctx *pulumi.Context,
	name string, args *CacheArgs, opts ...pulumi.ResourceOption) (*Cache, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CacheSizeInGb == nil {
		return nil, errors.New("invalid value for required argument 'CacheSizeInGb'")
	}
	if args.ResourceGroupName == nil {
		return nil, errors.New("invalid value for required argument 'ResourceGroupName'")
	}
	if args.SkuName == nil {
		return nil, errors.New("invalid value for required argument 'SkuName'")
	}
	if args.SubnetId == nil {
		return nil, errors.New("invalid value for required argument 'SubnetId'")
	}
	var resource Cache
	err := ctx.RegisterResource("azure:hpc/cache:Cache", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCache gets an existing Cache resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCache(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CacheState, opts ...pulumi.ResourceOption) (*Cache, error) {
	var resource Cache
	err := ctx.ReadResource("azure:hpc/cache:Cache", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Cache resources.
type cacheState struct {
	// The size of the HPC Cache, in GB. Possible values are `3072`, `6144`, `12288`, `24576`, and `49152`. Changing this forces a new resource to be created.
	CacheSizeInGb *int `pulumi:"cacheSizeInGb"`
	// Specifies the supported Azure Region where the HPC Cache should be created. Changing this forces a new resource to be created.
	Location *string `pulumi:"location"`
	// A list of IP Addresses where the HPC Cache can be mounted.
	MountAddresses []string `pulumi:"mountAddresses"`
	// The IPv4 maximum transmission unit configured for the subnet of the HPC Cache. Possible values range from 576 - 1500. Defaults to 1500.
	Mtu *int `pulumi:"mtu"`
	// The name of the HPC Cache. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// The name of the Resource Group in which to create the HPC Cache. Changing this forces a new resource to be created.
	ResourceGroupName *string `pulumi:"resourceGroupName"`
	// Whether root squash property is enabled for this HPC Cache.
	RootSquashEnabled *bool `pulumi:"rootSquashEnabled"`
	// The SKU of HPC Cache to use. Possible values are `Standard_2G`, `Standard_4G` and `Standard_8G`. Changing this forces a new resource to be created.
	SkuName *string `pulumi:"skuName"`
	// The ID of the Subnet for the HPC Cache. Changing this forces a new resource to be created.
	SubnetId *string `pulumi:"subnetId"`
}

type CacheState struct {
	// The size of the HPC Cache, in GB. Possible values are `3072`, `6144`, `12288`, `24576`, and `49152`. Changing this forces a new resource to be created.
	CacheSizeInGb pulumi.IntPtrInput
	// Specifies the supported Azure Region where the HPC Cache should be created. Changing this forces a new resource to be created.
	Location pulumi.StringPtrInput
	// A list of IP Addresses where the HPC Cache can be mounted.
	MountAddresses pulumi.StringArrayInput
	// The IPv4 maximum transmission unit configured for the subnet of the HPC Cache. Possible values range from 576 - 1500. Defaults to 1500.
	Mtu pulumi.IntPtrInput
	// The name of the HPC Cache. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// The name of the Resource Group in which to create the HPC Cache. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringPtrInput
	// Whether root squash property is enabled for this HPC Cache.
	RootSquashEnabled pulumi.BoolPtrInput
	// The SKU of HPC Cache to use. Possible values are `Standard_2G`, `Standard_4G` and `Standard_8G`. Changing this forces a new resource to be created.
	SkuName pulumi.StringPtrInput
	// The ID of the Subnet for the HPC Cache. Changing this forces a new resource to be created.
	SubnetId pulumi.StringPtrInput
}

func (CacheState) ElementType() reflect.Type {
	return reflect.TypeOf((*cacheState)(nil)).Elem()
}

type cacheArgs struct {
	// The size of the HPC Cache, in GB. Possible values are `3072`, `6144`, `12288`, `24576`, and `49152`. Changing this forces a new resource to be created.
	CacheSizeInGb int `pulumi:"cacheSizeInGb"`
	// Specifies the supported Azure Region where the HPC Cache should be created. Changing this forces a new resource to be created.
	Location *string `pulumi:"location"`
	// The IPv4 maximum transmission unit configured for the subnet of the HPC Cache. Possible values range from 576 - 1500. Defaults to 1500.
	Mtu *int `pulumi:"mtu"`
	// The name of the HPC Cache. Changing this forces a new resource to be created.
	Name *string `pulumi:"name"`
	// The name of the Resource Group in which to create the HPC Cache. Changing this forces a new resource to be created.
	ResourceGroupName string `pulumi:"resourceGroupName"`
	// Whether root squash property is enabled for this HPC Cache.
	RootSquashEnabled *bool `pulumi:"rootSquashEnabled"`
	// The SKU of HPC Cache to use. Possible values are `Standard_2G`, `Standard_4G` and `Standard_8G`. Changing this forces a new resource to be created.
	SkuName string `pulumi:"skuName"`
	// The ID of the Subnet for the HPC Cache. Changing this forces a new resource to be created.
	SubnetId string `pulumi:"subnetId"`
}

// The set of arguments for constructing a Cache resource.
type CacheArgs struct {
	// The size of the HPC Cache, in GB. Possible values are `3072`, `6144`, `12288`, `24576`, and `49152`. Changing this forces a new resource to be created.
	CacheSizeInGb pulumi.IntInput
	// Specifies the supported Azure Region where the HPC Cache should be created. Changing this forces a new resource to be created.
	Location pulumi.StringPtrInput
	// The IPv4 maximum transmission unit configured for the subnet of the HPC Cache. Possible values range from 576 - 1500. Defaults to 1500.
	Mtu pulumi.IntPtrInput
	// The name of the HPC Cache. Changing this forces a new resource to be created.
	Name pulumi.StringPtrInput
	// The name of the Resource Group in which to create the HPC Cache. Changing this forces a new resource to be created.
	ResourceGroupName pulumi.StringInput
	// Whether root squash property is enabled for this HPC Cache.
	RootSquashEnabled pulumi.BoolPtrInput
	// The SKU of HPC Cache to use. Possible values are `Standard_2G`, `Standard_4G` and `Standard_8G`. Changing this forces a new resource to be created.
	SkuName pulumi.StringInput
	// The ID of the Subnet for the HPC Cache. Changing this forces a new resource to be created.
	SubnetId pulumi.StringInput
}

func (CacheArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*cacheArgs)(nil)).Elem()
}

type CacheInput interface {
	pulumi.Input

	ToCacheOutput() CacheOutput
	ToCacheOutputWithContext(ctx context.Context) CacheOutput
}

func (*Cache) ElementType() reflect.Type {
	return reflect.TypeOf((*Cache)(nil))
}

func (i *Cache) ToCacheOutput() CacheOutput {
	return i.ToCacheOutputWithContext(context.Background())
}

func (i *Cache) ToCacheOutputWithContext(ctx context.Context) CacheOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CacheOutput)
}

type CacheOutput struct {
	*pulumi.OutputState
}

func (CacheOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Cache)(nil))
}

func (o CacheOutput) ToCacheOutput() CacheOutput {
	return o
}

func (o CacheOutput) ToCacheOutputWithContext(ctx context.Context) CacheOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(CacheOutput{})
}
