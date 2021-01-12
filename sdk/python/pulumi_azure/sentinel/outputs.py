# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'AlertRuleScheduledIncidentConfiguration',
    'AlertRuleScheduledIncidentConfigurationGrouping',
]

@pulumi.output_type
class AlertRuleScheduledIncidentConfiguration(dict):
    def __init__(__self__, *,
                 create_incident: bool,
                 grouping: 'outputs.AlertRuleScheduledIncidentConfigurationGrouping'):
        """
        :param bool create_incident: Whether to create an incident from alerts triggered by this Sentinel Scheduled Alert Rule?
        :param 'AlertRuleScheduledIncidentConfigurationGroupingArgs' grouping: A `grouping` block as defined below.
        """
        pulumi.set(__self__, "create_incident", create_incident)
        pulumi.set(__self__, "grouping", grouping)

    @property
    @pulumi.getter(name="createIncident")
    def create_incident(self) -> bool:
        """
        Whether to create an incident from alerts triggered by this Sentinel Scheduled Alert Rule?
        """
        return pulumi.get(self, "create_incident")

    @property
    @pulumi.getter
    def grouping(self) -> 'outputs.AlertRuleScheduledIncidentConfigurationGrouping':
        """
        A `grouping` block as defined below.
        """
        return pulumi.get(self, "grouping")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class AlertRuleScheduledIncidentConfigurationGrouping(dict):
    def __init__(__self__, *,
                 enabled: Optional[bool] = None,
                 entity_matching_method: Optional[str] = None,
                 group_bies: Optional[Sequence[str]] = None,
                 lookback_duration: Optional[str] = None,
                 reopen_closed_incidents: Optional[bool] = None):
        """
        :param bool enabled: Enable grouping incidents created from alerts triggered by this Sentinel Scheduled Alert Rule. Defaults to `true`.
        :param str entity_matching_method: The method used to group incidents. Possible values are `All`, `Custom` and `None`. Defaults to `None`.
        :param Sequence[str] group_bies: A list of entity types to group by, only when the `entity_matching_method` is `Custom`. Possible values are `Account`, `Host`, `Url`, `Ip`.
        :param str lookback_duration: Limit the group to alerts created within the lookback duration (in ISO 8601 duration format). Defaults to `PT5M`.
        :param bool reopen_closed_incidents: Whether to re-open closed matching incidents? Defaults to `false`.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if entity_matching_method is not None:
            pulumi.set(__self__, "entity_matching_method", entity_matching_method)
        if group_bies is not None:
            pulumi.set(__self__, "group_bies", group_bies)
        if lookback_duration is not None:
            pulumi.set(__self__, "lookback_duration", lookback_duration)
        if reopen_closed_incidents is not None:
            pulumi.set(__self__, "reopen_closed_incidents", reopen_closed_incidents)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Enable grouping incidents created from alerts triggered by this Sentinel Scheduled Alert Rule. Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="entityMatchingMethod")
    def entity_matching_method(self) -> Optional[str]:
        """
        The method used to group incidents. Possible values are `All`, `Custom` and `None`. Defaults to `None`.
        """
        return pulumi.get(self, "entity_matching_method")

    @property
    @pulumi.getter(name="groupBies")
    def group_bies(self) -> Optional[Sequence[str]]:
        """
        A list of entity types to group by, only when the `entity_matching_method` is `Custom`. Possible values are `Account`, `Host`, `Url`, `Ip`.
        """
        return pulumi.get(self, "group_bies")

    @property
    @pulumi.getter(name="lookbackDuration")
    def lookback_duration(self) -> Optional[str]:
        """
        Limit the group to alerts created within the lookback duration (in ISO 8601 duration format). Defaults to `PT5M`.
        """
        return pulumi.get(self, "lookback_duration")

    @property
    @pulumi.getter(name="reopenClosedIncidents")
    def reopen_closed_incidents(self) -> Optional[bool]:
        """
        Whether to re-open closed matching incidents? Defaults to `false`.
        """
        return pulumi.get(self, "reopen_closed_incidents")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

