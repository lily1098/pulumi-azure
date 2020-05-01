// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sentinel

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to access information about an existing Sentinel Alert Rule.
func GetAlertRule(ctx *pulumi.Context, args *GetAlertRuleArgs, opts ...pulumi.InvokeOption) (*GetAlertRuleResult, error) {
	var rv GetAlertRuleResult
	err := ctx.Invoke("azure:sentinel/getAlertRule:getAlertRule", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAlertRule.
type GetAlertRuleArgs struct {
	// The ID of the Log Analytics Workspace this Sentinel Alert Rule belongs to.
	LogAnalyticsWorkspaceId string `pulumi:"logAnalyticsWorkspaceId"`
	// The name which should be used for this Sentinel Alert Rule.
	Name string `pulumi:"name"`
}

// A collection of values returned by getAlertRule.
type GetAlertRuleResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id                      string `pulumi:"id"`
	LogAnalyticsWorkspaceId string `pulumi:"logAnalyticsWorkspaceId"`
	Name                    string `pulumi:"name"`
}
