// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package servicebus

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-azure/sdk/v3/go/azure"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "azure:servicebus/namespace:Namespace":
		r, err = NewNamespace(ctx, name, nil, pulumi.URN_(urn))
	case "azure:servicebus/namespaceAuthorizationRule:NamespaceAuthorizationRule":
		r, err = NewNamespaceAuthorizationRule(ctx, name, nil, pulumi.URN_(urn))
	case "azure:servicebus/namespaceNetworkRuleSet:NamespaceNetworkRuleSet":
		r, err = NewNamespaceNetworkRuleSet(ctx, name, nil, pulumi.URN_(urn))
	case "azure:servicebus/queue:Queue":
		r, err = NewQueue(ctx, name, nil, pulumi.URN_(urn))
	case "azure:servicebus/queueAuthorizationRule:QueueAuthorizationRule":
		r, err = NewQueueAuthorizationRule(ctx, name, nil, pulumi.URN_(urn))
	case "azure:servicebus/subscription:Subscription":
		r, err = NewSubscription(ctx, name, nil, pulumi.URN_(urn))
	case "azure:servicebus/subscriptionRule:SubscriptionRule":
		r, err = NewSubscriptionRule(ctx, name, nil, pulumi.URN_(urn))
	case "azure:servicebus/topic:Topic":
		r, err = NewTopic(ctx, name, nil, pulumi.URN_(urn))
	case "azure:servicebus/topicAuthorizationRule:TopicAuthorizationRule":
		r, err = NewTopicAuthorizationRule(ctx, name, nil, pulumi.URN_(urn))
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	return
}

func init() {
	version, err := azure.PkgVersion()
	if err != nil {
		fmt.Println("failed to determine package version. defaulting to v1: %v", err)
	}
	pulumi.RegisterResourceModule(
		"azure",
		"servicebus/namespace",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"servicebus/namespaceAuthorizationRule",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"servicebus/namespaceNetworkRuleSet",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"servicebus/queue",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"servicebus/queueAuthorizationRule",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"servicebus/subscription",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"servicebus/subscriptionRule",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"servicebus/topic",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"azure",
		"servicebus/topicAuthorizationRule",
		&module{version},
	)
}
