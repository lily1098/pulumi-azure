# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Subscription']

warnings.warn("""azure.eventhub.Subscription has been deprecated in favor of azure.servicebus.Subscription""", DeprecationWarning)


class Subscription(pulumi.CustomResource):
    warnings.warn("""azure.eventhub.Subscription has been deprecated in favor of azure.servicebus.Subscription""", DeprecationWarning)

    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_delete_on_idle: Optional[pulumi.Input[str]] = None,
                 dead_lettering_on_filter_evaluation_error: Optional[pulumi.Input[bool]] = None,
                 dead_lettering_on_message_expiration: Optional[pulumi.Input[bool]] = None,
                 default_message_ttl: Optional[pulumi.Input[str]] = None,
                 enable_batched_operations: Optional[pulumi.Input[bool]] = None,
                 forward_dead_lettered_messages_to: Optional[pulumi.Input[str]] = None,
                 forward_to: Optional[pulumi.Input[str]] = None,
                 lock_duration: Optional[pulumi.Input[str]] = None,
                 max_delivery_count: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 requires_session: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 topic_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a ServiceBus Subscription.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_namespace = azure.servicebus.Namespace("exampleNamespace",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku="Standard",
            tags={
                "source": "example",
            })
        example_topic = azure.servicebus.Topic("exampleTopic",
            resource_group_name=example_resource_group.name,
            namespace_name=example_namespace.name,
            enable_partitioning=True)
        example_subscription = azure.servicebus.Subscription("exampleSubscription",
            resource_group_name=example_resource_group.name,
            namespace_name=example_namespace.name,
            topic_name=example_topic.name,
            max_delivery_count=1)
        ```

        ## Import

        Service Bus Subscriptions can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:eventhub/subscription:Subscription example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/microsoft.servicebus/namespaces/sbns1/topics/sntopic1/subscriptions/sbsub1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auto_delete_on_idle: The idle interval after which the topic is automatically deleted as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). The minimum duration is `5` minutes or `P5M`.
        :param pulumi.Input[bool] dead_lettering_on_filter_evaluation_error: Boolean flag which controls whether the Subscription has dead letter support on filter evaluation exceptions. Defaults to `true`.
        :param pulumi.Input[bool] dead_lettering_on_message_expiration: Boolean flag which controls whether the Subscription has dead letter support when a message expires. Defaults to `false`.
        :param pulumi.Input[str] default_message_ttl: The Default message timespan to live as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
        :param pulumi.Input[bool] enable_batched_operations: Boolean flag which controls whether the Subscription supports batched operations. Defaults to `false`.
        :param pulumi.Input[str] forward_dead_lettered_messages_to: The name of a Queue or Topic to automatically forward Dead Letter messages to.
        :param pulumi.Input[str] forward_to: The name of a Queue or Topic to automatically forward messages to.
        :param pulumi.Input[str] lock_duration: The lock duration for the subscription as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). The default value is `1` minute or `P1M`.
        :param pulumi.Input[int] max_delivery_count: The maximum number of deliveries.
        :param pulumi.Input[str] name: Specifies the name of the ServiceBus Subscription resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] namespace_name: The name of the ServiceBus Namespace to create this Subscription in. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] requires_session: Boolean flag which controls whether this Subscription supports the concept of a session. Defaults to `false`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] status: The status of the Subscription. Possible values are `Active`,`ReceiveDisabled`, or `Disabled`. Defaults to `Active`.
        :param pulumi.Input[str] topic_name: The name of the ServiceBus Topic to create this Subscription in. Changing this forces a new resource to be created.
        """
        pulumi.log.warn("Subscription is deprecated: azure.eventhub.Subscription has been deprecated in favor of azure.servicebus.Subscription")
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['auto_delete_on_idle'] = auto_delete_on_idle
            __props__['dead_lettering_on_filter_evaluation_error'] = dead_lettering_on_filter_evaluation_error
            __props__['dead_lettering_on_message_expiration'] = dead_lettering_on_message_expiration
            __props__['default_message_ttl'] = default_message_ttl
            __props__['enable_batched_operations'] = enable_batched_operations
            __props__['forward_dead_lettered_messages_to'] = forward_dead_lettered_messages_to
            __props__['forward_to'] = forward_to
            __props__['lock_duration'] = lock_duration
            if max_delivery_count is None and not opts.urn:
                raise TypeError("Missing required property 'max_delivery_count'")
            __props__['max_delivery_count'] = max_delivery_count
            __props__['name'] = name
            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__['namespace_name'] = namespace_name
            __props__['requires_session'] = requires_session
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['status'] = status
            if topic_name is None and not opts.urn:
                raise TypeError("Missing required property 'topic_name'")
            __props__['topic_name'] = topic_name
        super(Subscription, __self__).__init__(
            'azure:eventhub/subscription:Subscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auto_delete_on_idle: Optional[pulumi.Input[str]] = None,
            dead_lettering_on_filter_evaluation_error: Optional[pulumi.Input[bool]] = None,
            dead_lettering_on_message_expiration: Optional[pulumi.Input[bool]] = None,
            default_message_ttl: Optional[pulumi.Input[str]] = None,
            enable_batched_operations: Optional[pulumi.Input[bool]] = None,
            forward_dead_lettered_messages_to: Optional[pulumi.Input[str]] = None,
            forward_to: Optional[pulumi.Input[str]] = None,
            lock_duration: Optional[pulumi.Input[str]] = None,
            max_delivery_count: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace_name: Optional[pulumi.Input[str]] = None,
            requires_session: Optional[pulumi.Input[bool]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            topic_name: Optional[pulumi.Input[str]] = None) -> 'Subscription':
        """
        Get an existing Subscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auto_delete_on_idle: The idle interval after which the topic is automatically deleted as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). The minimum duration is `5` minutes or `P5M`.
        :param pulumi.Input[bool] dead_lettering_on_filter_evaluation_error: Boolean flag which controls whether the Subscription has dead letter support on filter evaluation exceptions. Defaults to `true`.
        :param pulumi.Input[bool] dead_lettering_on_message_expiration: Boolean flag which controls whether the Subscription has dead letter support when a message expires. Defaults to `false`.
        :param pulumi.Input[str] default_message_ttl: The Default message timespan to live as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
        :param pulumi.Input[bool] enable_batched_operations: Boolean flag which controls whether the Subscription supports batched operations. Defaults to `false`.
        :param pulumi.Input[str] forward_dead_lettered_messages_to: The name of a Queue or Topic to automatically forward Dead Letter messages to.
        :param pulumi.Input[str] forward_to: The name of a Queue or Topic to automatically forward messages to.
        :param pulumi.Input[str] lock_duration: The lock duration for the subscription as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). The default value is `1` minute or `P1M`.
        :param pulumi.Input[int] max_delivery_count: The maximum number of deliveries.
        :param pulumi.Input[str] name: Specifies the name of the ServiceBus Subscription resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] namespace_name: The name of the ServiceBus Namespace to create this Subscription in. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] requires_session: Boolean flag which controls whether this Subscription supports the concept of a session. Defaults to `false`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.
        :param pulumi.Input[str] status: The status of the Subscription. Possible values are `Active`,`ReceiveDisabled`, or `Disabled`. Defaults to `Active`.
        :param pulumi.Input[str] topic_name: The name of the ServiceBus Topic to create this Subscription in. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["auto_delete_on_idle"] = auto_delete_on_idle
        __props__["dead_lettering_on_filter_evaluation_error"] = dead_lettering_on_filter_evaluation_error
        __props__["dead_lettering_on_message_expiration"] = dead_lettering_on_message_expiration
        __props__["default_message_ttl"] = default_message_ttl
        __props__["enable_batched_operations"] = enable_batched_operations
        __props__["forward_dead_lettered_messages_to"] = forward_dead_lettered_messages_to
        __props__["forward_to"] = forward_to
        __props__["lock_duration"] = lock_duration
        __props__["max_delivery_count"] = max_delivery_count
        __props__["name"] = name
        __props__["namespace_name"] = namespace_name
        __props__["requires_session"] = requires_session
        __props__["resource_group_name"] = resource_group_name
        __props__["status"] = status
        __props__["topic_name"] = topic_name
        return Subscription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoDeleteOnIdle")
    def auto_delete_on_idle(self) -> pulumi.Output[str]:
        """
        The idle interval after which the topic is automatically deleted as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). The minimum duration is `5` minutes or `P5M`.
        """
        return pulumi.get(self, "auto_delete_on_idle")

    @property
    @pulumi.getter(name="deadLetteringOnFilterEvaluationError")
    def dead_lettering_on_filter_evaluation_error(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean flag which controls whether the Subscription has dead letter support on filter evaluation exceptions. Defaults to `true`.
        """
        return pulumi.get(self, "dead_lettering_on_filter_evaluation_error")

    @property
    @pulumi.getter(name="deadLetteringOnMessageExpiration")
    def dead_lettering_on_message_expiration(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean flag which controls whether the Subscription has dead letter support when a message expires. Defaults to `false`.
        """
        return pulumi.get(self, "dead_lettering_on_message_expiration")

    @property
    @pulumi.getter(name="defaultMessageTtl")
    def default_message_ttl(self) -> pulumi.Output[str]:
        """
        The Default message timespan to live as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
        """
        return pulumi.get(self, "default_message_ttl")

    @property
    @pulumi.getter(name="enableBatchedOperations")
    def enable_batched_operations(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean flag which controls whether the Subscription supports batched operations. Defaults to `false`.
        """
        return pulumi.get(self, "enable_batched_operations")

    @property
    @pulumi.getter(name="forwardDeadLetteredMessagesTo")
    def forward_dead_lettered_messages_to(self) -> pulumi.Output[Optional[str]]:
        """
        The name of a Queue or Topic to automatically forward Dead Letter messages to.
        """
        return pulumi.get(self, "forward_dead_lettered_messages_to")

    @property
    @pulumi.getter(name="forwardTo")
    def forward_to(self) -> pulumi.Output[Optional[str]]:
        """
        The name of a Queue or Topic to automatically forward messages to.
        """
        return pulumi.get(self, "forward_to")

    @property
    @pulumi.getter(name="lockDuration")
    def lock_duration(self) -> pulumi.Output[str]:
        """
        The lock duration for the subscription as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). The default value is `1` minute or `P1M`.
        """
        return pulumi.get(self, "lock_duration")

    @property
    @pulumi.getter(name="maxDeliveryCount")
    def max_delivery_count(self) -> pulumi.Output[int]:
        """
        The maximum number of deliveries.
        """
        return pulumi.get(self, "max_delivery_count")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the ServiceBus Subscription resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Output[str]:
        """
        The name of the ServiceBus Namespace to create this Subscription in. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "namespace_name")

    @property
    @pulumi.getter(name="requiresSession")
    def requires_session(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean flag which controls whether this Subscription supports the concept of a session. Defaults to `false`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "requires_session")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the Subscription. Possible values are `Active`,`ReceiveDisabled`, or `Disabled`. Defaults to `Active`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> pulumi.Output[str]:
        """
        The name of the ServiceBus Topic to create this Subscription in. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "topic_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

