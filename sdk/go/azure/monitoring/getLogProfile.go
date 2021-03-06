// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package monitoring

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to access the properties of a Log Profile.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure/monitoring"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		example, err := monitoring.LookupLogProfile(ctx, &monitoring.LookupLogProfileArgs{
// 			Name: "test-logprofile",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		ctx.Export("logProfileStorageAccountId", example.StorageAccountId)
// 		return nil
// 	})
// }
// ```
func LookupLogProfile(ctx *pulumi.Context, args *LookupLogProfileArgs, opts ...pulumi.InvokeOption) (*LookupLogProfileResult, error) {
	var rv LookupLogProfileResult
	err := ctx.Invoke("azure:monitoring/getLogProfile:getLogProfile", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getLogProfile.
type LookupLogProfileArgs struct {
	// Specifies the Name of the Log Profile.
	Name string `pulumi:"name"`
}

// A collection of values returned by getLogProfile.
type LookupLogProfileResult struct {
	// List of categories of the logs.
	Categories []string `pulumi:"categories"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// List of regions for which Activity Log events are stored or streamed.
	Locations         []string                       `pulumi:"locations"`
	Name              string                         `pulumi:"name"`
	RetentionPolicies []GetLogProfileRetentionPolicy `pulumi:"retentionPolicies"`
	// The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to.
	ServicebusRuleId string `pulumi:"servicebusRuleId"`
	// The resource id of the storage account in which the Activity Log is stored.
	StorageAccountId string `pulumi:"storageAccountId"`
}
