// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package appplatform

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to access information about an existing Spring Cloud Service.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appplatform"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		example, err := appplatform.LookupSpringCloudService(ctx, &appplatform.LookupSpringCloudServiceArgs{
// 			Name:              azurerm_spring_cloud_service.Example.Name,
// 			ResourceGroupName: azurerm_spring_cloud_service.Example.Resource_group_name,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		ctx.Export("springCloudServiceId", example.Id)
// 		return nil
// 	})
// }
// ```
func LookupSpringCloudService(ctx *pulumi.Context, args *LookupSpringCloudServiceArgs, opts ...pulumi.InvokeOption) (*LookupSpringCloudServiceResult, error) {
	var rv LookupSpringCloudServiceResult
	err := ctx.Invoke("azure:appplatform/getSpringCloudService:getSpringCloudService", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSpringCloudService.
type LookupSpringCloudServiceArgs struct {
	// Specifies The name of the Spring Cloud Service resource.
	Name string `pulumi:"name"`
	// Specifies the name of the Resource Group where the Spring Cloud Service exists.
	ResourceGroupName string `pulumi:"resourceGroupName"`
}

// A collection of values returned by getSpringCloudService.
type LookupSpringCloudServiceResult struct {
	// A `configServerGitSetting` block as defined below.
	ConfigServerGitSettings []GetSpringCloudServiceConfigServerGitSetting `pulumi:"configServerGitSettings"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The location of Spring Cloud Service.
	Location string `pulumi:"location"`
	// The name to identify on the Git repository.
	Name string `pulumi:"name"`
	// A list of the outbound Public IP Addresses used by this Spring Cloud Service.
	OutboundPublicIpAddresses []string `pulumi:"outboundPublicIpAddresses"`
	ResourceGroupName         string   `pulumi:"resourceGroupName"`
	// A mapping of tags assigned to Spring Cloud Service.
	Tags map[string]string `pulumi:"tags"`
}
