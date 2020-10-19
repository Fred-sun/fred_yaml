#!/usr/bin/python
#
# Copyright (c) 2020 GuopengLin, (@t-glin)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_autoscalesetting
version_added: '2.9'
short_description: Manage Azure AutoscaleSetting instance.
description:
  - 'Create, update and delete instance of Azure AutoscaleSetting.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  autoscale_setting_name:
    description:
      - The autoscale setting name.
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  profiles:
    description:
      - >-
        the collection of automatic scaling profiles that specify different
        scaling parameters for different time periods. A maximum of 20 profiles
        can be specified.
    type: list
    suboptions:
      name:
        description:
          - the name of the profile.
        required: true
        type: str
      capacity:
        description:
          - the number of instances that can be used during this profile.
        required: true
        type: dict
        suboptions:
          minimum:
            description:
              - the minimum number of instances for the resource.
            required: true
            type: str
          maximum:
            description:
              - >-
                the maximum number of instances for the resource. The actual
                maximum number of instances is limited by the cores that are
                available in the subscription.
            required: true
            type: str
          default:
            description:
              - >-
                the number of instances that will be set if metrics are not
                available for evaluation. The default is only used if the
                current instance count is lower than the default.
            required: true
            type: str
      rules:
        description:
          - >-
            the collection of rules that provide the triggers and parameters for
            the scaling action. A maximum of 10 rules can be specified.
        required: true
        type: list
        suboptions:
          metric_trigger:
            description:
              - the trigger that results in a scaling action.
            required: true
            type: dict
            suboptions:
              metric_name:
                description:
                  - the name of the metric that defines what the rule monitors.
                required: true
                type: str
              metric_namespace:
                description:
                  - >-
                    the namespace of the metric that defines what the rule
                    monitors.
                type: str
              metric_resource_uri:
                description:
                  - the resource identifier of the resource the rule monitors.
                required: true
                type: str
              time_grain:
                description:
                  - >-
                    the granularity of metrics the rule monitors. Must be one of
                    the predefined values returned from metric definitions for
                    the metric. Must be between 12 hours and 1 minute.
                required: true
                type: duration
              statistic:
                description:
                  - >-
                    the metric statistic type. How the metrics from multiple
                    instances are combined.
                required: true
                type: sealed-choice
              time_window:
                description:
                  - >-
                    the range of time in which instance data is collected. This
                    value must be greater than the delay in metric collection,
                    which can vary from resource-to-resource. Must be between 12
                    hours and 5 minutes.
                required: true
                type: duration
              time_aggregation:
                description:
                  - >-
                    time aggregation type. How the data that is collected should
                    be combined over time. The default value is Average.
                required: true
                type: sealed-choice
              operator:
                description:
                  - >-
                    the operator that is used to compare the metric data and the
                    threshold.
                required: true
                type: sealed-choice
              threshold:
                description:
                  - the threshold of the metric that triggers the scale action.
                required: true
                type: number
              dimensions:
                description:
                  - >-
                    List of dimension conditions. For example:
                    [{"DimensionName":"AppName","Operator":"Equals","Values":["App1"]},{"DimensionName":"Deployment","Operator":"Equals","Values":["default"]}].
                type: list
                suboptions:
                  dimension_name:
                    description:
                      - Name of the dimension.
                    required: true
                    type: str
                  operator:
                    description:
                      - >-
                        the dimension operator. Only 'Equals' and 'NotEquals'
                        are supported. 'Equals' being equal to any of the
                        values. 'NotEquals' being not equal to all of the values
                    required: true
                    type: str
                    choices:
                      - Equals
                      - NotEquals
                  values:
                    description:
                      - 'list of dimension values. For example: ["App1","App2"].'
                    required: true
                    type: list
          scale_action:
            description:
              - the parameters for the scaling action.
            required: true
            type: dict
            suboptions:
              direction:
                description:
                  - >-
                    the scale direction. Whether the scaling action increases or
                    decreases the number of instances.
                required: true
                type: sealed-choice
              type:
                description:
                  - >-
                    the type of action that should occur when the scale rule
                    fires.
                required: true
                type: sealed-choice
              value:
                description:
                  - >-
                    the number of instances that are involved in the scaling
                    action. This value must be 1 or greater. The default value
                    is 1.
                type: str
              cooldown:
                description:
                  - >-
                    the amount of time to wait since the last scaling action
                    before this action occurs. It must be between 1 week and 1
                    minute in ISO 8601 format.
                required: true
                type: duration
      fixed_date:
        description:
          - >-
            the specific date-time for the profile. This element is not used if
            the Recurrence element is used.
        type: dict
        suboptions:
          time_zone:
            description:
              - >-
                the timezone of the start and end times for the profile. Some
                examples of valid time zones are: Dateline Standard Time,
                UTC-11, Hawaiian Standard Time, Alaskan Standard Time, Pacific
                Standard Time (Mexico), Pacific Standard Time, US Mountain
                Standard Time, Mountain Standard Time (Mexico), Mountain
                Standard Time, Central America Standard Time, Central Standard
                Time, Central Standard Time (Mexico), Canada Central Standard
                Time, SA Pacific Standard Time, Eastern Standard Time, US
                Eastern Standard Time, Venezuela Standard Time, Paraguay
                Standard Time, Atlantic Standard Time, Central Brazilian
                Standard Time, SA Western Standard Time, Pacific SA Standard
                Time, Newfoundland Standard Time, E. South America Standard
                Time, Argentina Standard Time, SA Eastern Standard Time,
                Greenland Standard Time, Montevideo Standard Time, Bahia
                Standard Time, UTC-02, Mid-Atlantic Standard Time, Azores
                Standard Time, Cape Verde Standard Time, Morocco Standard Time,
                UTC, GMT Standard Time, Greenwich Standard Time, W. Europe
                Standard Time, Central Europe Standard Time, Romance Standard
                Time, Central European Standard Time, W. Central Africa Standard
                Time, Namibia Standard Time, Jordan Standard Time, GTB Standard
                Time, Middle East Standard Time, Egypt Standard Time, Syria
                Standard Time, E. Europe Standard Time, South Africa Standard
                Time, FLE Standard Time, Turkey Standard Time, Israel Standard
                Time, Kaliningrad Standard Time, Libya Standard Time, Arabic
                Standard Time, Arab Standard Time, Belarus Standard Time,
                Russian Standard Time, E. Africa Standard Time, Iran Standard
                Time, Arabian Standard Time, Azerbaijan Standard Time, Russia
                Time Zone 3, Mauritius Standard Time, Georgian Standard Time,
                Caucasus Standard Time, Afghanistan Standard Time, West Asia
                Standard Time, Ekaterinburg Standard Time, Pakistan Standard
                Time, India Standard Time, Sri Lanka Standard Time, Nepal
                Standard Time, Central Asia Standard Time, Bangladesh Standard
                Time, N. Central Asia Standard Time, Myanmar Standard Time, SE
                Asia Standard Time, North Asia Standard Time, China Standard
                Time, North Asia East Standard Time, Singapore Standard Time, W.
                Australia Standard Time, Taipei Standard Time, Ulaanbaatar
                Standard Time, Tokyo Standard Time, Korea Standard Time, Yakutsk
                Standard Time, Cen. Australia Standard Time, AUS Central
                Standard Time, E. Australia Standard Time, AUS Eastern Standard
                Time, West Pacific Standard Time, Tasmania Standard Time,
                Magadan Standard Time, Vladivostok Standard Time, Russia Time
                Zone 10, Central Pacific Standard Time, Russia Time Zone 11, New
                Zealand Standard Time, UTC+12, Fiji Standard Time, Kamchatka
                Standard Time, Tonga Standard Time, Samoa Standard Time, Line
                Islands Standard Time
            type: str
          start:
            description:
              - the start time for the profile in ISO 8601 format.
            required: true
            type: str
          end:
            description:
              - the end time for the profile in ISO 8601 format.
            required: true
            type: str
      recurrence:
        description:
          - >-
            the repeating times at which this profile begins. This element is
            not used if the FixedDate element is used.
        type: dict
        suboptions:
          frequency:
            description:
              - >-
                the recurrence frequency. How often the schedule profile should
                take effect. This value must be Week, meaning each week will
                have the same set of profiles. For example, to set a daily
                schedule, set **schedule** to every day of the week. The
                frequency property specifies that the schedule is repeated
                weekly.
            required: true
            type: sealed-choice
          schedule:
            description:
              - the scheduling constraints for when the profile begins.
            required: true
            type: dict
            suboptions:
              time_zone:
                description:
                  - >-
                    the timezone for the hours of the profile. Some examples of
                    valid time zones are: Dateline Standard Time, UTC-11,
                    Hawaiian Standard Time, Alaskan Standard Time, Pacific
                    Standard Time (Mexico), Pacific Standard Time, US Mountain
                    Standard Time, Mountain Standard Time (Mexico), Mountain
                    Standard Time, Central America Standard Time, Central
                    Standard Time, Central Standard Time (Mexico), Canada
                    Central Standard Time, SA Pacific Standard Time, Eastern
                    Standard Time, US Eastern Standard Time, Venezuela Standard
                    Time, Paraguay Standard Time, Atlantic Standard Time,
                    Central Brazilian Standard Time, SA Western Standard Time,
                    Pacific SA Standard Time, Newfoundland Standard Time, E.
                    South America Standard Time, Argentina Standard Time, SA
                    Eastern Standard Time, Greenland Standard Time, Montevideo
                    Standard Time, Bahia Standard Time, UTC-02, Mid-Atlantic
                    Standard Time, Azores Standard Time, Cape Verde Standard
                    Time, Morocco Standard Time, UTC, GMT Standard Time,
                    Greenwich Standard Time, W. Europe Standard Time, Central
                    Europe Standard Time, Romance Standard Time, Central
                    European Standard Time, W. Central Africa Standard Time,
                    Namibia Standard Time, Jordan Standard Time, GTB Standard
                    Time, Middle East Standard Time, Egypt Standard Time, Syria
                    Standard Time, E. Europe Standard Time, South Africa
                    Standard Time, FLE Standard Time, Turkey Standard Time,
                    Israel Standard Time, Kaliningrad Standard Time, Libya
                    Standard Time, Arabic Standard Time, Arab Standard Time,
                    Belarus Standard Time, Russian Standard Time, E. Africa
                    Standard Time, Iran Standard Time, Arabian Standard Time,
                    Azerbaijan Standard Time, Russia Time Zone 3, Mauritius
                    Standard Time, Georgian Standard Time, Caucasus Standard
                    Time, Afghanistan Standard Time, West Asia Standard Time,
                    Ekaterinburg Standard Time, Pakistan Standard Time, India
                    Standard Time, Sri Lanka Standard Time, Nepal Standard Time,
                    Central Asia Standard Time, Bangladesh Standard Time, N.
                    Central Asia Standard Time, Myanmar Standard Time, SE Asia
                    Standard Time, North Asia Standard Time, China Standard
                    Time, North Asia East Standard Time, Singapore Standard
                    Time, W. Australia Standard Time, Taipei Standard Time,
                    Ulaanbaatar Standard Time, Tokyo Standard Time, Korea
                    Standard Time, Yakutsk Standard Time, Cen. Australia
                    Standard Time, AUS Central Standard Time, E. Australia
                    Standard Time, AUS Eastern Standard Time, West Pacific
                    Standard Time, Tasmania Standard Time, Magadan Standard
                    Time, Vladivostok Standard Time, Russia Time Zone 10,
                    Central Pacific Standard Time, Russia Time Zone 11, New
                    Zealand Standard Time, UTC+12, Fiji Standard Time, Kamchatka
                    Standard Time, Tonga Standard Time, Samoa Standard Time,
                    Line Islands Standard Time
                required: true
                type: str
              days:
                description:
                  - >-
                    the collection of days that the profile takes effect on.
                    Possible values are Sunday through Saturday.
                required: true
                type: list
              hours:
                description:
                  - >-
                    A collection of hours that the profile takes effect on.
                    Values supported are 0 to 23 on the 24-hour clock (AM/PM
                    times are not supported).
                required: true
                type: list
              minutes:
                description:
                  - >-
                    A collection of minutes at which the profile takes effect
                    at.
                required: true
                type: list
  notifications:
    description:
      - the collection of notifications.
    type: list
    suboptions:
      operation:
        description:
          - >-
            the operation associated with the notification and its value must be
            "scale"
        required: true
        type: constant
      email:
        description:
          - the email notification.
        type: dict
        suboptions:
          send_to_subscription_administrator:
            description:
              - >-
                a value indicating whether to send email to subscription
                administrator.
            type: bool
          send_to_subscription_co_administrators:
            description:
              - >-
                a value indicating whether to send email to subscription
                co-administrators.
            type: bool
          custom_emails:
            description:
              - >-
                the custom e-mails list. This value can be null or empty, in
                which case this attribute will be ignored.
            type: list
      webhooks:
        description:
          - the collection of webhook notifications.
        type: list
        suboptions:
          service_uri:
            description:
              - the service address to receive the notification.
            type: str
          properties:
            description:
              - a property bag of settings. This value can be empty.
            type: dictionary
  enabled:
    description:
      - >-
        the enabled flag. Specifies whether automatic scaling is enabled for the
        resource. The default value is 'true'.
    type: bool
  name:
    description:
      - the name of the autoscale setting.
    type: str
  target_resource_uri:
    description:
      - >-
        the resource identifier of the resource that the autoscale setting
        should be added to.
    type: str
  state:
    description:
      - Assert the state of the AutoscaleSetting.
      - >-
        Use C(present) to create or update an AutoscaleSetting and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Create or update an autoscale setting
      azure_rm_autoscalesetting: 
        autoscale_setting_name: MySetting
        resource_group_name: TestingMetricsScaleSet
        location: West US
        properties:
          enabled: true
          notifications:
            - email:
                custom_emails:
                  - gu@ms.com
                  - ge@ns.net
                send_to_subscription_administrator: true
                send_to_subscription_co_administrators: true
              operation: Scale
              webhooks:
                - properties: {}
                  service_uri: 'http://myservice.com'
          profiles:
            - name: adios
              capacity:
                default: '1'
                maximum: '10'
                minimum: '1'
              fixed_date:
                end: '2015-03-05T14:30:00Z'
                start: '2015-03-05T14:00:00Z'
                time_zone: UTC
              rules:
                - metric_trigger:
                    metric_name: Percentage CPU
                    metric_resource_uri: >-
                      /subscriptions/b67f7fec-69fc-4974-9099-a26bd6ffeda3/resourceGroups/TestingMetricsScaleSet/providers/Microsoft.Compute/virtualMachineScaleSets/testingsc
                    operator: GreaterThan
                    statistic: Average
                    threshold: 10
                    time_aggregation: Average
                    time_grain: PT1M
                    time_window: PT5M
                  scale_action:
                    type: ChangeCount
                    cooldown: PT5M
                    direction: Increase
                    value: '1'
                - metric_trigger:
                    metric_name: Percentage CPU
                    metric_resource_uri: >-
                      /subscriptions/b67f7fec-69fc-4974-9099-a26bd6ffeda3/resourceGroups/TestingMetricsScaleSet/providers/Microsoft.Compute/virtualMachineScaleSets/testingsc
                    operator: GreaterThan
                    statistic: Average
                    threshold: 15
                    time_aggregation: Average
                    time_grain: PT2M
                    time_window: PT5M
                  scale_action:
                    type: ChangeCount
                    cooldown: PT6M
                    direction: Decrease
                    value: '2'
            - name: saludos
              capacity:
                default: '1'
                maximum: '10'
                minimum: '1'
              recurrence:
                frequency: Week
                schedule:
                  days:
                    - '1'
                  hours:
                    - 5
                  minutes:
                    - 15
                  time_zone: UTC
              rules:
                - metric_trigger:
                    metric_name: Percentage CPU
                    metric_resource_uri: >-
                      /subscriptions/b67f7fec-69fc-4974-9099-a26bd6ffeda3/resourceGroups/TestingMetricsScaleSet/providers/Microsoft.Compute/virtualMachineScaleSets/testingsc
                    operator: GreaterThan
                    statistic: Average
                    threshold: 10
                    time_aggregation: Average
                    time_grain: PT1M
                    time_window: PT5M
                  scale_action:
                    type: ChangeCount
                    cooldown: PT5M
                    direction: Increase
                    value: '1'
                - metric_trigger:
                    metric_name: Percentage CPU
                    metric_resource_uri: >-
                      /subscriptions/b67f7fec-69fc-4974-9099-a26bd6ffeda3/resourceGroups/TestingMetricsScaleSet/providers/Microsoft.Compute/virtualMachineScaleSets/testingsc
                    operator: GreaterThan
                    statistic: Average
                    threshold: 15
                    time_aggregation: Average
                    time_grain: PT2M
                    time_window: PT5M
                  scale_action:
                    type: ChangeCount
                    cooldown: PT6M
                    direction: Decrease
                    value: '2'
          target_resource_uri: >-
            /subscriptions/b67f7fec-69fc-4974-9099-a26bd6ffeda3/resourceGroups/TestingMetricsScaleSet/providers/Microsoft.Compute/virtualMachineScaleSets/testingsc
        tags: {}
        

    - name: Delete an autoscale setting
      azure_rm_autoscalesetting: 
        autoscale_setting_name: MySetting
        resource_group_name: TestingMetricsScaleSet
        

    - name: Patch an autoscale setting
      azure_rm_autoscalesetting: 
        autoscale_setting_name: MySetting
        resource_group_name: TestingMetricsScaleSet
        

'''

RETURN = '''
id:
  description:
    - Azure resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Azure resource name
  returned: always
  type: str
  sample: null
type:
  description:
    - Azure resource type
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags
  returned: always
  type: dictionary
  sample: null
profiles:
  description:
    - >-
      the collection of automatic scaling profiles that specify different
      scaling parameters for different time periods. A maximum of 20 profiles
      can be specified.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - the name of the profile.
      returned: always
      type: str
      sample: null
    capacity:
      description:
        - the number of instances that can be used during this profile.
      returned: always
      type: dict
      sample: null
      contains:
        minimum:
          description:
            - the minimum number of instances for the resource.
          returned: always
          type: str
          sample: null
        maximum:
          description:
            - >-
              the maximum number of instances for the resource. The actual
              maximum number of instances is limited by the cores that are
              available in the subscription.
          returned: always
          type: str
          sample: null
        default:
          description:
            - >-
              the number of instances that will be set if metrics are not
              available for evaluation. The default is only used if the current
              instance count is lower than the default.
          returned: always
          type: str
          sample: null
    rules:
      description:
        - >-
          the collection of rules that provide the triggers and parameters for
          the scaling action. A maximum of 10 rules can be specified.
      returned: always
      type: list
      sample: null
      contains:
        metric_trigger:
          description:
            - the trigger that results in a scaling action.
          returned: always
          type: dict
          sample: null
          contains:
            metric_name:
              description:
                - the name of the metric that defines what the rule monitors.
              returned: always
              type: str
              sample: null
            metric_namespace:
              description:
                - >-
                  the namespace of the metric that defines what the rule
                  monitors.
              returned: always
              type: str
              sample: null
            metric_resource_uri:
              description:
                - the resource identifier of the resource the rule monitors.
              returned: always
              type: str
              sample: null
            time_grain:
              description:
                - >-
                  the granularity of metrics the rule monitors. Must be one of
                  the predefined values returned from metric definitions for the
                  metric. Must be between 12 hours and 1 minute.
              returned: always
              type: duration
              sample: null
            statistic:
              description:
                - >-
                  the metric statistic type. How the metrics from multiple
                  instances are combined.
              returned: always
              type: sealed-choice
              sample: null
            time_window:
              description:
                - >-
                  the range of time in which instance data is collected. This
                  value must be greater than the delay in metric collection,
                  which can vary from resource-to-resource. Must be between 12
                  hours and 5 minutes.
              returned: always
              type: duration
              sample: null
            time_aggregation:
              description:
                - >-
                  time aggregation type. How the data that is collected should
                  be combined over time. The default value is Average.
              returned: always
              type: sealed-choice
              sample: null
            operator:
              description:
                - >-
                  the operator that is used to compare the metric data and the
                  threshold.
              returned: always
              type: sealed-choice
              sample: null
            threshold:
              description:
                - the threshold of the metric that triggers the scale action.
              returned: always
              type: number
              sample: null
            dimensions:
              description:
                - >-
                  List of dimension conditions. For example:
                  [{"DimensionName":"AppName","Operator":"Equals","Values":["App1"]},{"DimensionName":"Deployment","Operator":"Equals","Values":["default"]}].
              returned: always
              type: list
              sample: null
              contains:
                dimension_name:
                  description:
                    - Name of the dimension.
                  returned: always
                  type: str
                  sample: null
                operator:
                  description:
                    - >-
                      the dimension operator. Only 'Equals' and 'NotEquals' are
                      supported. 'Equals' being equal to any of the values.
                      'NotEquals' being not equal to all of the values
                  returned: always
                  type: str
                  sample: null
                values:
                  description:
                    - 'list of dimension values. For example: ["App1","App2"].'
                  returned: always
                  type: list
                  sample: null
        scale_action:
          description:
            - the parameters for the scaling action.
          returned: always
          type: dict
          sample: null
          contains:
            direction:
              description:
                - >-
                  the scale direction. Whether the scaling action increases or
                  decreases the number of instances.
              returned: always
              type: sealed-choice
              sample: null
            type:
              description:
                - >-
                  the type of action that should occur when the scale rule
                  fires.
              returned: always
              type: sealed-choice
              sample: null
            value:
              description:
                - >-
                  the number of instances that are involved in the scaling
                  action. This value must be 1 or greater. The default value is
                  1.
              returned: always
              type: str
              sample: null
            cooldown:
              description:
                - >-
                  the amount of time to wait since the last scaling action
                  before this action occurs. It must be between 1 week and 1
                  minute in ISO 8601 format.
              returned: always
              type: duration
              sample: null
    fixed_date:
      description:
        - >-
          the specific date-time for the profile. This element is not used if
          the Recurrence element is used.
      returned: always
      type: dict
      sample: null
      contains:
        time_zone:
          description:
            - >-
              the timezone of the start and end times for the profile. Some
              examples of valid time zones are: Dateline Standard Time, UTC-11,
              Hawaiian Standard Time, Alaskan Standard Time, Pacific Standard
              Time (Mexico), Pacific Standard Time, US Mountain Standard Time,
              Mountain Standard Time (Mexico), Mountain Standard Time, Central
              America Standard Time, Central Standard Time, Central Standard
              Time (Mexico), Canada Central Standard Time, SA Pacific Standard
              Time, Eastern Standard Time, US Eastern Standard Time, Venezuela
              Standard Time, Paraguay Standard Time, Atlantic Standard Time,
              Central Brazilian Standard Time, SA Western Standard Time, Pacific
              SA Standard Time, Newfoundland Standard Time, E. South America
              Standard Time, Argentina Standard Time, SA Eastern Standard Time,
              Greenland Standard Time, Montevideo Standard Time, Bahia Standard
              Time, UTC-02, Mid-Atlantic Standard Time, Azores Standard Time,
              Cape Verde Standard Time, Morocco Standard Time, UTC, GMT Standard
              Time, Greenwich Standard Time, W. Europe Standard Time, Central
              Europe Standard Time, Romance Standard Time, Central European
              Standard Time, W. Central Africa Standard Time, Namibia Standard
              Time, Jordan Standard Time, GTB Standard Time, Middle East
              Standard Time, Egypt Standard Time, Syria Standard Time, E. Europe
              Standard Time, South Africa Standard Time, FLE Standard Time,
              Turkey Standard Time, Israel Standard Time, Kaliningrad Standard
              Time, Libya Standard Time, Arabic Standard Time, Arab Standard
              Time, Belarus Standard Time, Russian Standard Time, E. Africa
              Standard Time, Iran Standard Time, Arabian Standard Time,
              Azerbaijan Standard Time, Russia Time Zone 3, Mauritius Standard
              Time, Georgian Standard Time, Caucasus Standard Time, Afghanistan
              Standard Time, West Asia Standard Time, Ekaterinburg Standard
              Time, Pakistan Standard Time, India Standard Time, Sri Lanka
              Standard Time, Nepal Standard Time, Central Asia Standard Time,
              Bangladesh Standard Time, N. Central Asia Standard Time, Myanmar
              Standard Time, SE Asia Standard Time, North Asia Standard Time,
              China Standard Time, North Asia East Standard Time, Singapore
              Standard Time, W. Australia Standard Time, Taipei Standard Time,
              Ulaanbaatar Standard Time, Tokyo Standard Time, Korea Standard
              Time, Yakutsk Standard Time, Cen. Australia Standard Time, AUS
              Central Standard Time, E. Australia Standard Time, AUS Eastern
              Standard Time, West Pacific Standard Time, Tasmania Standard Time,
              Magadan Standard Time, Vladivostok Standard Time, Russia Time Zone
              10, Central Pacific Standard Time, Russia Time Zone 11, New
              Zealand Standard Time, UTC+12, Fiji Standard Time, Kamchatka
              Standard Time, Tonga Standard Time, Samoa Standard Time, Line
              Islands Standard Time
          returned: always
          type: str
          sample: null
        start:
          description:
            - the start time for the profile in ISO 8601 format.
          returned: always
          type: str
          sample: null
        end:
          description:
            - the end time for the profile in ISO 8601 format.
          returned: always
          type: str
          sample: null
    recurrence:
      description:
        - >-
          the repeating times at which this profile begins. This element is not
          used if the FixedDate element is used.
      returned: always
      type: dict
      sample: null
      contains:
        frequency:
          description:
            - >-
              the recurrence frequency. How often the schedule profile should
              take effect. This value must be Week, meaning each week will have
              the same set of profiles. For example, to set a daily schedule,
              set **schedule** to every day of the week. The frequency property
              specifies that the schedule is repeated weekly.
          returned: always
          type: sealed-choice
          sample: null
        schedule:
          description:
            - the scheduling constraints for when the profile begins.
          returned: always
          type: dict
          sample: null
          contains:
            time_zone:
              description:
                - >-
                  the timezone for the hours of the profile. Some examples of
                  valid time zones are: Dateline Standard Time, UTC-11, Hawaiian
                  Standard Time, Alaskan Standard Time, Pacific Standard Time
                  (Mexico), Pacific Standard Time, US Mountain Standard Time,
                  Mountain Standard Time (Mexico), Mountain Standard Time,
                  Central America Standard Time, Central Standard Time, Central
                  Standard Time (Mexico), Canada Central Standard Time, SA
                  Pacific Standard Time, Eastern Standard Time, US Eastern
                  Standard Time, Venezuela Standard Time, Paraguay Standard
                  Time, Atlantic Standard Time, Central Brazilian Standard Time,
                  SA Western Standard Time, Pacific SA Standard Time,
                  Newfoundland Standard Time, E. South America Standard Time,
                  Argentina Standard Time, SA Eastern Standard Time, Greenland
                  Standard Time, Montevideo Standard Time, Bahia Standard Time,
                  UTC-02, Mid-Atlantic Standard Time, Azores Standard Time, Cape
                  Verde Standard Time, Morocco Standard Time, UTC, GMT Standard
                  Time, Greenwich Standard Time, W. Europe Standard Time,
                  Central Europe Standard Time, Romance Standard Time, Central
                  European Standard Time, W. Central Africa Standard Time,
                  Namibia Standard Time, Jordan Standard Time, GTB Standard
                  Time, Middle East Standard Time, Egypt Standard Time, Syria
                  Standard Time, E. Europe Standard Time, South Africa Standard
                  Time, FLE Standard Time, Turkey Standard Time, Israel Standard
                  Time, Kaliningrad Standard Time, Libya Standard Time, Arabic
                  Standard Time, Arab Standard Time, Belarus Standard Time,
                  Russian Standard Time, E. Africa Standard Time, Iran Standard
                  Time, Arabian Standard Time, Azerbaijan Standard Time, Russia
                  Time Zone 3, Mauritius Standard Time, Georgian Standard Time,
                  Caucasus Standard Time, Afghanistan Standard Time, West Asia
                  Standard Time, Ekaterinburg Standard Time, Pakistan Standard
                  Time, India Standard Time, Sri Lanka Standard Time, Nepal
                  Standard Time, Central Asia Standard Time, Bangladesh Standard
                  Time, N. Central Asia Standard Time, Myanmar Standard Time, SE
                  Asia Standard Time, North Asia Standard Time, China Standard
                  Time, North Asia East Standard Time, Singapore Standard Time,
                  W. Australia Standard Time, Taipei Standard Time, Ulaanbaatar
                  Standard Time, Tokyo Standard Time, Korea Standard Time,
                  Yakutsk Standard Time, Cen. Australia Standard Time, AUS
                  Central Standard Time, E. Australia Standard Time, AUS Eastern
                  Standard Time, West Pacific Standard Time, Tasmania Standard
                  Time, Magadan Standard Time, Vladivostok Standard Time, Russia
                  Time Zone 10, Central Pacific Standard Time, Russia Time Zone
                  11, New Zealand Standard Time, UTC+12, Fiji Standard Time,
                  Kamchatka Standard Time, Tonga Standard Time, Samoa Standard
                  Time, Line Islands Standard Time
              returned: always
              type: str
              sample: null
            days:
              description:
                - >-
                  the collection of days that the profile takes effect on.
                  Possible values are Sunday through Saturday.
              returned: always
              type: list
              sample: null
            hours:
              description:
                - >-
                  A collection of hours that the profile takes effect on. Values
                  supported are 0 to 23 on the 24-hour clock (AM/PM times are
                  not supported).
              returned: always
              type: list
              sample: null
            minutes:
              description:
                - A collection of minutes at which the profile takes effect at.
              returned: always
              type: list
              sample: null
notifications:
  description:
    - the collection of notifications.
  returned: always
  type: list
  sample: null
  contains:
    operation:
      description:
        - >-
          the operation associated with the notification and its value must be
          "scale"
      returned: always
      type: constant
      sample: null
    email:
      description:
        - the email notification.
      returned: always
      type: dict
      sample: null
      contains:
        send_to_subscription_administrator:
          description:
            - >-
              a value indicating whether to send email to subscription
              administrator.
          returned: always
          type: bool
          sample: null
        send_to_subscription_co_administrators:
          description:
            - >-
              a value indicating whether to send email to subscription
              co-administrators.
          returned: always
          type: bool
          sample: null
        custom_emails:
          description:
            - >-
              the custom e-mails list. This value can be null or empty, in which
              case this attribute will be ignored.
          returned: always
          type: list
          sample: null
    webhooks:
      description:
        - the collection of webhook notifications.
      returned: always
      type: list
      sample: null
      contains:
        service_uri:
          description:
            - the service address to receive the notification.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - a property bag of settings. This value can be empty.
          returned: always
          type: dictionary
          sample: null
enabled:
  description:
    - >-
      the enabled flag. Specifies whether automatic scaling is enabled for the
      resource. The default value is 'true'.
  returned: always
  type: bool
  sample: null
name_properties_name:
  description:
    - the name of the autoscale setting.
  returned: always
  type: str
  sample: null
target_resource_uri:
  description:
    - >-
      the resource identifier of the resource that the autoscale setting should
      be added to.
  returned: always
  type: str
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.monitor import MonitorClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMAutoscaleSetting(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            autoscale_setting_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            profiles=dict(
                type='list',
                disposition='/profiles',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    capacity=dict(
                        type='dict',
                        disposition='capacity',
                        required=True,
                        options=dict(
                            minimum=dict(
                                type='str',
                                disposition='minimum',
                                required=True
                            ),
                            maximum=dict(
                                type='str',
                                disposition='maximum',
                                required=True
                            ),
                            default=dict(
                                type='str',
                                disposition='default',
                                required=True
                            )
                        )
                    ),
                    rules=dict(
                        type='list',
                        disposition='rules',
                        required=True,
                        elements='dict',
                        options=dict(
                            metric_trigger=dict(
                                type='dict',
                                disposition='metric_trigger',
                                required=True,
                                options=dict(
                                    metric_name=dict(
                                        type='str',
                                        disposition='metric_name',
                                        required=True
                                    ),
                                    metric_namespace=dict(
                                        type='str',
                                        disposition='metric_namespace'
                                    ),
                                    metric_resource_uri=dict(
                                        type='str',
                                        disposition='metric_resource_uri',
                                        required=True
                                    ),
                                    time_grain=dict(
                                        type='duration',
                                        disposition='time_grain',
                                        required=True
                                    ),
                                    statistic=dict(
                                        type='sealed-choice',
                                        disposition='statistic',
                                        required=True
                                    ),
                                    time_window=dict(
                                        type='duration',
                                        disposition='time_window',
                                        required=True
                                    ),
                                    time_aggregation=dict(
                                        type='sealed-choice',
                                        disposition='time_aggregation',
                                        required=True
                                    ),
                                    operator=dict(
                                        type='sealed-choice',
                                        disposition='operator',
                                        required=True
                                    ),
                                    threshold=dict(
                                        type='number',
                                        disposition='threshold',
                                        required=True
                                    ),
                                    dimensions=dict(
                                        type='list',
                                        disposition='dimensions',
                                        elements='dict',
                                        options=dict(
                                            dimension_name=dict(
                                                type='str',
                                                disposition='dimension_name',
                                                required=True
                                            ),
                                            operator=dict(
                                                type='str',
                                                disposition='operator',
                                                choices=['Equals',
                                                         'NotEquals'],
                                                required=True
                                            ),
                                            values=dict(
                                                type='list',
                                                disposition='values',
                                                required=True,
                                                elements='str'
                                            )
                                        )
                                    )
                                )
                            ),
                            scale_action=dict(
                                type='dict',
                                disposition='scale_action',
                                required=True,
                                options=dict(
                                    direction=dict(
                                        type='sealed-choice',
                                        disposition='direction',
                                        required=True
                                    ),
                                    type=dict(
                                        type='sealed-choice',
                                        disposition='type',
                                        required=True
                                    ),
                                    value=dict(
                                        type='str',
                                        disposition='value'
                                    ),
                                    cooldown=dict(
                                        type='duration',
                                        disposition='cooldown',
                                        required=True
                                    )
                                )
                            )
                        )
                    ),
                    fixed_date=dict(
                        type='dict',
                        disposition='fixed_date',
                        options=dict(
                            time_zone=dict(
                                type='str',
                                disposition='time_zone'
                            ),
                            start=dict(
                                type='str',
                                disposition='start',
                                required=True
                            ),
                            end=dict(
                                type='str',
                                disposition='end',
                                required=True
                            )
                        )
                    ),
                    recurrence=dict(
                        type='dict',
                        disposition='recurrence',
                        options=dict(
                            frequency=dict(
                                type='sealed-choice',
                                disposition='frequency',
                                required=True
                            ),
                            schedule=dict(
                                type='dict',
                                disposition='schedule',
                                required=True,
                                options=dict(
                                    time_zone=dict(
                                        type='str',
                                        disposition='time_zone',
                                        required=True
                                    ),
                                    days=dict(
                                        type='list',
                                        disposition='days',
                                        required=True,
                                        elements='str'
                                    ),
                                    hours=dict(
                                        type='list',
                                        disposition='hours',
                                        required=True,
                                        elements='integer'
                                    ),
                                    minutes=dict(
                                        type='list',
                                        disposition='minutes',
                                        required=True,
                                        elements='integer'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            notifications=dict(
                type='list',
                disposition='/notifications',
                elements='dict',
                options=dict(
                    operation=dict(
                        type='constant',
                        disposition='operation',
                        required=True
                    ),
                    email=dict(
                        type='dict',
                        disposition='email',
                        options=dict(
                            send_to_subscription_administrator=dict(
                                type='bool',
                                disposition='send_to_subscription_administrator'
                            ),
                            send_to_subscription_co_administrators=dict(
                                type='bool',
                                disposition='send_to_subscription_co_administrators'
                            ),
                            custom_emails=dict(
                                type='list',
                                disposition='custom_emails',
                                elements='str'
                            )
                        )
                    ),
                    webhooks=dict(
                        type='list',
                        disposition='webhooks',
                        elements='dict',
                        options=dict(
                            service_uri=dict(
                                type='str',
                                disposition='service_uri'
                            ),
                            properties=dict(
                                type='dictionary',
                                disposition='properties'
                            )
                        )
                    )
                )
            ),
            enabled=dict(
                type='bool',
                disposition='/enabled'
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            target_resource_uri=dict(
                type='str',
                disposition='/target_resource_uri'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.autoscale_setting_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAutoscaleSetting, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                      supports_check_mode=True,
                                                      supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-04-01')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.autoscale_settings.create_or_update(resource_group_name=self.resource_group_name,
                                                                            autoscale_setting_name=self.autoscale_setting_name,
                                                                            parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the AutoscaleSetting instance.')
            self.fail('Error creating the AutoscaleSetting instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.autoscale_settings.delete(resource_group_name=self.resource_group_name,
                                                                  autoscale_setting_name=self.autoscale_setting_name)
        except CloudError as e:
            self.log('Error attempting to delete the AutoscaleSetting instance.')
            self.fail('Error deleting the AutoscaleSetting instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.autoscale_settings.get(resource_group_name=self.resource_group_name,
                                                               autoscale_setting_name=self.autoscale_setting_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAutoscaleSetting()


if __name__ == '__main__':
    main()
