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
module: azure_rm_autoscalesetting_info
version_added: '2.9'
short_description: Get AutoscaleSetting info.
description:
  - Get info of AutoscaleSetting.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  autoscale_setting_name:
    description:
      - The autoscale setting name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List autoscale settings
      azure_rm_autoscalesetting_info: 
        resource_group_name: TestingMetricsScaleSet
        

    - name: Get an autoscale setting
      azure_rm_autoscalesetting_info: 
        autoscale_setting_name: MySetting
        resource_group_name: TestingMetricsScaleSet
        

'''

RETURN = '''
autoscale_settings:
  description: >-
    A list of dict results where the key is the name of the AutoscaleSetting and
    the values are the facts for that AutoscaleSetting.
  returned: always
  type: complex
  contains:
    value:
      description:
        - the values for the autoscale setting resources.
      returned: always
      type: list
      sample: null
      contains:
        profiles:
          description:
            - >-
              the collection of automatic scaling profiles that specify
              different scaling parameters for different time periods. A maximum
              of 20 profiles can be specified.
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
                      the maximum number of instances for the resource. The
                      actual maximum number of instances is limited by the cores
                      that are available in the subscription.
                  returned: always
                  type: str
                  sample: null
                default:
                  description:
                    - >-
                      the number of instances that will be set if metrics are
                      not available for evaluation. The default is only used if
                      the current instance count is lower than the default.
                  returned: always
                  type: str
                  sample: null
            rules:
              description:
                - >-
                  the collection of rules that provide the triggers and
                  parameters for the scaling action. A maximum of 10 rules can
                  be specified.
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
                        - >-
                          the name of the metric that defines what the rule
                          monitors.
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
                        - >-
                          the resource identifier of the resource the rule
                          monitors.
                      returned: always
                      type: str
                      sample: null
                    time_grain:
                      description:
                        - >-
                          the granularity of metrics the rule monitors. Must be
                          one of the predefined values returned from metric
                          definitions for the metric. Must be between 12 hours
                          and 1 minute.
                      returned: always
                      type: duration
                      sample: null
                    statistic:
                      description:
                        - >-
                          the metric statistic type. How the metrics from
                          multiple instances are combined.
                      returned: always
                      type: sealed-choice
                      sample: null
                    time_window:
                      description:
                        - >-
                          the range of time in which instance data is collected.
                          This value must be greater than the delay in metric
                          collection, which can vary from resource-to-resource.
                          Must be between 12 hours and 5 minutes.
                      returned: always
                      type: duration
                      sample: null
                    time_aggregation:
                      description:
                        - >-
                          time aggregation type. How the data that is collected
                          should be combined over time. The default value is
                          Average.
                      returned: always
                      type: sealed-choice
                      sample: null
                    operator:
                      description:
                        - >-
                          the operator that is used to compare the metric data
                          and the threshold.
                      returned: always
                      type: sealed-choice
                      sample: null
                    threshold:
                      description:
                        - >-
                          the threshold of the metric that triggers the scale
                          action.
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
                              the dimension operator. Only 'Equals' and
                              'NotEquals' are supported. 'Equals' being equal to
                              any of the values. 'NotEquals' being not equal to
                              all of the values
                          returned: always
                          type: str
                          sample: null
                        values:
                          description:
                            - >-
                              list of dimension values. For example:
                              ["App1","App2"].
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
                          the scale direction. Whether the scaling action
                          increases or decreases the number of instances.
                      returned: always
                      type: sealed-choice
                      sample: null
                    type:
                      description:
                        - >-
                          the type of action that should occur when the scale
                          rule fires.
                      returned: always
                      type: sealed-choice
                      sample: null
                    value:
                      description:
                        - >-
                          the number of instances that are involved in the
                          scaling action. This value must be 1 or greater. The
                          default value is 1.
                      returned: always
                      type: str
                      sample: null
                    cooldown:
                      description:
                        - >-
                          the amount of time to wait since the last scaling
                          action before this action occurs. It must be between 1
                          week and 1 minute in ISO 8601 format.
                      returned: always
                      type: duration
                      sample: null
            fixed_date:
              description:
                - >-
                  the specific date-time for the profile. This element is not
                  used if the Recurrence element is used.
              returned: always
              type: dict
              sample: null
              contains:
                time_zone:
                  description:
                    - >-
                      the timezone of the start and end times for the profile.
                      Some examples of valid time zones are: Dateline Standard
                      Time, UTC-11, Hawaiian Standard Time, Alaskan Standard
                      Time, Pacific Standard Time (Mexico), Pacific Standard
                      Time, US Mountain Standard Time, Mountain Standard Time
                      (Mexico), Mountain Standard Time, Central America Standard
                      Time, Central Standard Time, Central Standard Time
                      (Mexico), Canada Central Standard Time, SA Pacific
                      Standard Time, Eastern Standard Time, US Eastern Standard
                      Time, Venezuela Standard Time, Paraguay Standard Time,
                      Atlantic Standard Time, Central Brazilian Standard Time,
                      SA Western Standard Time, Pacific SA Standard Time,
                      Newfoundland Standard Time, E. South America Standard
                      Time, Argentina Standard Time, SA Eastern Standard Time,
                      Greenland Standard Time, Montevideo Standard Time, Bahia
                      Standard Time, UTC-02, Mid-Atlantic Standard Time, Azores
                      Standard Time, Cape Verde Standard Time, Morocco Standard
                      Time, UTC, GMT Standard Time, Greenwich Standard Time, W.
                      Europe Standard Time, Central Europe Standard Time,
                      Romance Standard Time, Central European Standard Time, W.
                      Central Africa Standard Time, Namibia Standard Time,
                      Jordan Standard Time, GTB Standard Time, Middle East
                      Standard Time, Egypt Standard Time, Syria Standard Time,
                      E. Europe Standard Time, South Africa Standard Time, FLE
                      Standard Time, Turkey Standard Time, Israel Standard Time,
                      Kaliningrad Standard Time, Libya Standard Time, Arabic
                      Standard Time, Arab Standard Time, Belarus Standard Time,
                      Russian Standard Time, E. Africa Standard Time, Iran
                      Standard Time, Arabian Standard Time, Azerbaijan Standard
                      Time, Russia Time Zone 3, Mauritius Standard Time,
                      Georgian Standard Time, Caucasus Standard Time,
                      Afghanistan Standard Time, West Asia Standard Time,
                      Ekaterinburg Standard Time, Pakistan Standard Time, India
                      Standard Time, Sri Lanka Standard Time, Nepal Standard
                      Time, Central Asia Standard Time, Bangladesh Standard
                      Time, N. Central Asia Standard Time, Myanmar Standard
                      Time, SE Asia Standard Time, North Asia Standard Time,
                      China Standard Time, North Asia East Standard Time,
                      Singapore Standard Time, W. Australia Standard Time,
                      Taipei Standard Time, Ulaanbaatar Standard Time, Tokyo
                      Standard Time, Korea Standard Time, Yakutsk Standard Time,
                      Cen. Australia Standard Time, AUS Central Standard Time,
                      E. Australia Standard Time, AUS Eastern Standard Time,
                      West Pacific Standard Time, Tasmania Standard Time,
                      Magadan Standard Time, Vladivostok Standard Time, Russia
                      Time Zone 10, Central Pacific Standard Time, Russia Time
                      Zone 11, New Zealand Standard Time, UTC+12, Fiji Standard
                      Time, Kamchatka Standard Time, Tonga Standard Time, Samoa
                      Standard Time, Line Islands Standard Time
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
                  the repeating times at which this profile begins. This element
                  is not used if the FixedDate element is used.
              returned: always
              type: dict
              sample: null
              contains:
                frequency:
                  description:
                    - >-
                      the recurrence frequency. How often the schedule profile
                      should take effect. This value must be Week, meaning each
                      week will have the same set of profiles. For example, to
                      set a daily schedule, set **schedule** to every day of the
                      week. The frequency property specifies that the schedule
                      is repeated weekly.
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
                          the timezone for the hours of the profile. Some
                          examples of valid time zones are: Dateline Standard
                          Time, UTC-11, Hawaiian Standard Time, Alaskan Standard
                          Time, Pacific Standard Time (Mexico), Pacific Standard
                          Time, US Mountain Standard Time, Mountain Standard
                          Time (Mexico), Mountain Standard Time, Central America
                          Standard Time, Central Standard Time, Central Standard
                          Time (Mexico), Canada Central Standard Time, SA
                          Pacific Standard Time, Eastern Standard Time, US
                          Eastern Standard Time, Venezuela Standard Time,
                          Paraguay Standard Time, Atlantic Standard Time,
                          Central Brazilian Standard Time, SA Western Standard
                          Time, Pacific SA Standard Time, Newfoundland Standard
                          Time, E. South America Standard Time, Argentina
                          Standard Time, SA Eastern Standard Time, Greenland
                          Standard Time, Montevideo Standard Time, Bahia
                          Standard Time, UTC-02, Mid-Atlantic Standard Time,
                          Azores Standard Time, Cape Verde Standard Time,
                          Morocco Standard Time, UTC, GMT Standard Time,
                          Greenwich Standard Time, W. Europe Standard Time,
                          Central Europe Standard Time, Romance Standard Time,
                          Central European Standard Time, W. Central Africa
                          Standard Time, Namibia Standard Time, Jordan Standard
                          Time, GTB Standard Time, Middle East Standard Time,
                          Egypt Standard Time, Syria Standard Time, E. Europe
                          Standard Time, South Africa Standard Time, FLE
                          Standard Time, Turkey Standard Time, Israel Standard
                          Time, Kaliningrad Standard Time, Libya Standard Time,
                          Arabic Standard Time, Arab Standard Time, Belarus
                          Standard Time, Russian Standard Time, E. Africa
                          Standard Time, Iran Standard Time, Arabian Standard
                          Time, Azerbaijan Standard Time, Russia Time Zone 3,
                          Mauritius Standard Time, Georgian Standard Time,
                          Caucasus Standard Time, Afghanistan Standard Time,
                          West Asia Standard Time, Ekaterinburg Standard Time,
                          Pakistan Standard Time, India Standard Time, Sri Lanka
                          Standard Time, Nepal Standard Time, Central Asia
                          Standard Time, Bangladesh Standard Time, N. Central
                          Asia Standard Time, Myanmar Standard Time, SE Asia
                          Standard Time, North Asia Standard Time, China
                          Standard Time, North Asia East Standard Time,
                          Singapore Standard Time, W. Australia Standard Time,
                          Taipei Standard Time, Ulaanbaatar Standard Time, Tokyo
                          Standard Time, Korea Standard Time, Yakutsk Standard
                          Time, Cen. Australia Standard Time, AUS Central
                          Standard Time, E. Australia Standard Time, AUS Eastern
                          Standard Time, West Pacific Standard Time, Tasmania
                          Standard Time, Magadan Standard Time, Vladivostok
                          Standard Time, Russia Time Zone 10, Central Pacific
                          Standard Time, Russia Time Zone 11, New Zealand
                          Standard Time, UTC+12, Fiji Standard Time, Kamchatka
                          Standard Time, Tonga Standard Time, Samoa Standard
                          Time, Line Islands Standard Time
                      returned: always
                      type: str
                      sample: null
                    days:
                      description:
                        - >-
                          the collection of days that the profile takes effect
                          on. Possible values are Sunday through Saturday.
                      returned: always
                      type: list
                      sample: null
                    hours:
                      description:
                        - >-
                          A collection of hours that the profile takes effect
                          on. Values supported are 0 to 23 on the 24-hour clock
                          (AM/PM times are not supported).
                      returned: always
                      type: list
                      sample: null
                    minutes:
                      description:
                        - >-
                          A collection of minutes at which the profile takes
                          effect at.
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
                  the operation associated with the notification and its value
                  must be "scale"
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
                      the custom e-mails list. This value can be null or empty,
                      in which case this attribute will be ignored.
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
              the enabled flag. Specifies whether automatic scaling is enabled
              for the resource. The default value is 'true'.
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
              the resource identifier of the resource that the autoscale setting
              should be added to.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - URL to get the next set of results.
      returned: always
      type: str
      sample: null
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
          scaling parameters for different time periods. A maximum of 20
          profiles can be specified.
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
                  available for evaluation. The default is only used if the
                  current instance count is lower than the default.
              returned: always
              type: str
              sample: null
        rules:
          description:
            - >-
              the collection of rules that provide the triggers and parameters
              for the scaling action. A maximum of 10 rules can be specified.
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
                    - >-
                      the name of the metric that defines what the rule
                      monitors.
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
                      the granularity of metrics the rule monitors. Must be one
                      of the predefined values returned from metric definitions
                      for the metric. Must be between 12 hours and 1 minute.
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
                      the range of time in which instance data is collected.
                      This value must be greater than the delay in metric
                      collection, which can vary from resource-to-resource. Must
                      be between 12 hours and 5 minutes.
                  returned: always
                  type: duration
                  sample: null
                time_aggregation:
                  description:
                    - >-
                      time aggregation type. How the data that is collected
                      should be combined over time. The default value is
                      Average.
                  returned: always
                  type: sealed-choice
                  sample: null
                operator:
                  description:
                    - >-
                      the operator that is used to compare the metric data and
                      the threshold.
                  returned: always
                  type: sealed-choice
                  sample: null
                threshold:
                  description:
                    - >-
                      the threshold of the metric that triggers the scale
                      action.
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
                          the dimension operator. Only 'Equals' and 'NotEquals'
                          are supported. 'Equals' being equal to any of the
                          values. 'NotEquals' being not equal to all of the
                          values
                      returned: always
                      type: str
                      sample: null
                    values:
                      description:
                        - >-
                          list of dimension values. For example:
                          ["App1","App2"].
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
                      the scale direction. Whether the scaling action increases
                      or decreases the number of instances.
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
                      action. This value must be 1 or greater. The default value
                      is 1.
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
              the specific date-time for the profile. This element is not used
              if the Recurrence element is used.
          returned: always
          type: dict
          sample: null
          contains:
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
                  Standard Time, Cape Verde Standard Time, Morocco Standard
                  Time, UTC, GMT Standard Time, Greenwich Standard Time, W.
                  Europe Standard Time, Central Europe Standard Time, Romance
                  Standard Time, Central European Standard Time, W. Central
                  Africa Standard Time, Namibia Standard Time, Jordan Standard
                  Time, GTB Standard Time, Middle East Standard Time, Egypt
                  Standard Time, Syria Standard Time, E. Europe Standard Time,
                  South Africa Standard Time, FLE Standard Time, Turkey Standard
                  Time, Israel Standard Time, Kaliningrad Standard Time, Libya
                  Standard Time, Arabic Standard Time, Arab Standard Time,
                  Belarus Standard Time, Russian Standard Time, E. Africa
                  Standard Time, Iran Standard Time, Arabian Standard Time,
                  Azerbaijan Standard Time, Russia Time Zone 3, Mauritius
                  Standard Time, Georgian Standard Time, Caucasus Standard Time,
                  Afghanistan Standard Time, West Asia Standard Time,
                  Ekaterinburg Standard Time, Pakistan Standard Time, India
                  Standard Time, Sri Lanka Standard Time, Nepal Standard Time,
                  Central Asia Standard Time, Bangladesh Standard Time, N.
                  Central Asia Standard Time, Myanmar Standard Time, SE Asia
                  Standard Time, North Asia Standard Time, China Standard Time,
                  North Asia East Standard Time, Singapore Standard Time, W.
                  Australia Standard Time, Taipei Standard Time, Ulaanbaatar
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
              the repeating times at which this profile begins. This element is
              not used if the FixedDate element is used.
          returned: always
          type: dict
          sample: null
          contains:
            frequency:
              description:
                - >-
                  the recurrence frequency. How often the schedule profile
                  should take effect. This value must be Week, meaning each week
                  will have the same set of profiles. For example, to set a
                  daily schedule, set **schedule** to every day of the week. The
                  frequency property specifies that the schedule is repeated
                  weekly.
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
                      the timezone for the hours of the profile. Some examples
                      of valid time zones are: Dateline Standard Time, UTC-11,
                      Hawaiian Standard Time, Alaskan Standard Time, Pacific
                      Standard Time (Mexico), Pacific Standard Time, US Mountain
                      Standard Time, Mountain Standard Time (Mexico), Mountain
                      Standard Time, Central America Standard Time, Central
                      Standard Time, Central Standard Time (Mexico), Canada
                      Central Standard Time, SA Pacific Standard Time, Eastern
                      Standard Time, US Eastern Standard Time, Venezuela
                      Standard Time, Paraguay Standard Time, Atlantic Standard
                      Time, Central Brazilian Standard Time, SA Western Standard
                      Time, Pacific SA Standard Time, Newfoundland Standard
                      Time, E. South America Standard Time, Argentina Standard
                      Time, SA Eastern Standard Time, Greenland Standard Time,
                      Montevideo Standard Time, Bahia Standard Time, UTC-02,
                      Mid-Atlantic Standard Time, Azores Standard Time, Cape
                      Verde Standard Time, Morocco Standard Time, UTC, GMT
                      Standard Time, Greenwich Standard Time, W. Europe Standard
                      Time, Central Europe Standard Time, Romance Standard Time,
                      Central European Standard Time, W. Central Africa Standard
                      Time, Namibia Standard Time, Jordan Standard Time, GTB
                      Standard Time, Middle East Standard Time, Egypt Standard
                      Time, Syria Standard Time, E. Europe Standard Time, South
                      Africa Standard Time, FLE Standard Time, Turkey Standard
                      Time, Israel Standard Time, Kaliningrad Standard Time,
                      Libya Standard Time, Arabic Standard Time, Arab Standard
                      Time, Belarus Standard Time, Russian Standard Time, E.
                      Africa Standard Time, Iran Standard Time, Arabian Standard
                      Time, Azerbaijan Standard Time, Russia Time Zone 3,
                      Mauritius Standard Time, Georgian Standard Time, Caucasus
                      Standard Time, Afghanistan Standard Time, West Asia
                      Standard Time, Ekaterinburg Standard Time, Pakistan
                      Standard Time, India Standard Time, Sri Lanka Standard
                      Time, Nepal Standard Time, Central Asia Standard Time,
                      Bangladesh Standard Time, N. Central Asia Standard Time,
                      Myanmar Standard Time, SE Asia Standard Time, North Asia
                      Standard Time, China Standard Time, North Asia East
                      Standard Time, Singapore Standard Time, W. Australia
                      Standard Time, Taipei Standard Time, Ulaanbaatar Standard
                      Time, Tokyo Standard Time, Korea Standard Time, Yakutsk
                      Standard Time, Cen. Australia Standard Time, AUS Central
                      Standard Time, E. Australia Standard Time, AUS Eastern
                      Standard Time, West Pacific Standard Time, Tasmania
                      Standard Time, Magadan Standard Time, Vladivostok Standard
                      Time, Russia Time Zone 10, Central Pacific Standard Time,
                      Russia Time Zone 11, New Zealand Standard Time, UTC+12,
                      Fiji Standard Time, Kamchatka Standard Time, Tonga
                      Standard Time, Samoa Standard Time, Line Islands Standard
                      Time
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
                      A collection of hours that the profile takes effect on.
                      Values supported are 0 to 23 on the 24-hour clock (AM/PM
                      times are not supported).
                  returned: always
                  type: list
                  sample: null
                minutes:
                  description:
                    - >-
                      A collection of minutes at which the profile takes effect
                      at.
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
              the operation associated with the notification and its value must
              be "scale"
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
                  the custom e-mails list. This value can be null or empty, in
                  which case this attribute will be ignored.
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
          the enabled flag. Specifies whether automatic scaling is enabled for
          the resource. The default value is 'true'.
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
          the resource identifier of the resource that the autoscale setting
          should be added to.
      returned: always
      type: str
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.monitor import MonitorClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAutoscaleSettingInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            autoscale_setting_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.autoscale_setting_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2015-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMAutoscaleSettingInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-04-01')

        if (self.resource_group_name is not None and
            self.autoscale_setting_name is not None):
            self.results['autoscale_settings'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['autoscale_settings'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['autoscale_settings'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.autoscale_settings.get(resource_group_name=self.resource_group_name,
                                                               autoscale_setting_name=self.autoscale_setting_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.autoscale_settings.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.autoscale_settings.list_by_subscription()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def format_item(self, item):
        if hasattr(item, 'as_dict'):
            return [item.as_dict()]
        else:
            result = []
            items = list(item)
            for tmp in items:
               result.append(tmp.as_dict())
            return result


def main():
    AzureRMAutoscaleSettingInfo()


if __name__ == '__main__':
    main()
