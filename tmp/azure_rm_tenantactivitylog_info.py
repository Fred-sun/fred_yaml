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
module: azure_rm_tenantactivitylog_info
version_added: '2.9'
short_description: Get TenantActivityLog info.
description:
  - Get info of TenantActivityLog.
options:
  filter:
    description:
      - >-
        Reduces the set of data collected. <br>The **$filter** is very
        restricted and allows only the following patterns.<br>- List events for
        a resource group: $filter=eventTimestamp ge '<Start Time>' and
        eventTimestamp le '<End Time>' and eventChannels eq 'Admin, Operation'
        and resourceGroupName eq '<ResourceGroupName>'.<br>- List events for
        resource: $filter=eventTimestamp ge '<Start Time>' and eventTimestamp le
        '<End Time>' and eventChannels eq 'Admin, Operation' and resourceUri eq
        '<ResourceURI>'.<br>- List events for a subscription:
        $filter=eventTimestamp ge '<Start Time>' and eventTimestamp le '<End
        Time>' and eventChannels eq 'Admin, Operation'.<br>- List events for a
        resource provider: $filter=eventTimestamp ge '<Start Time>' and
        eventTimestamp le '<End Time>' and eventChannels eq 'Admin, Operation'
        and resourceProvider eq '<ResourceProviderName>'.<br>- List events for a
        correlation Id: api-version=2014-04-01&$filter=eventTimestamp ge
        '2014-07-16T04:36:37.6407898Z' and eventTimestamp le
        '2014-07-20T04:36:37.6407898Z' and eventChannels eq 'Admin, Operation'
        and correlationId eq '<CorrelationID>'.<br>**NOTE**: No other syntax is
        allowed.
    required: true
    type: str
  select:
    description:
      - >-
        Used to fetch events with only the given properties.<br>The **$select**
        argument is a comma separated list of property names to be returned.
        Possible values are: *authorization*, *claims*, *correlationId*,
        *description*, *eventDataId*, *eventName*, *eventTimestamp*,
        *httpRequest*, *level*, *operationId*, *operationName*, *properties*,
        *resourceGroupName*, *resourceProviderName*, *resourceId*, *status*,
        *submissionTimestamp*, *subStatus*, *subscriptionId*
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get Tenant Activity Logs with filter
      azure_rm_tenantactivitylog_info: 
        {}
        

    - name: Get Tenant Activity Logs with filter and select
      azure_rm_tenantactivitylog_info: 
        {}
        

    - name: Get Tenant Activity Logs with select
      azure_rm_tenantactivitylog_info: 
        {}
        

    - name: Get Tenant Activity Logs without filter or select
      azure_rm_tenantactivitylog_info: 
        {}
        

'''

RETURN = '''
tenant_activity_logs:
  description: >-
    A list of dict results where the key is the name of the TenantActivityLog
    and the values are the facts for that TenantActivityLog.
  returned: always
  type: complex
  contains:
    value:
      description:
        - this list that includes the Azure audit logs.
      returned: always
      type: list
      sample: null
      contains:
        authorization:
          description:
            - The sender authorization information.
          returned: always
          type: dict
          sample: null
          contains:
            action:
              description:
                - >-
                  the permissible actions. For instance:
                  microsoft.support/supporttickets/write
              returned: always
              type: str
              sample: null
            role:
              description:
                - 'the role of the user. For instance: Subscription Admin'
              returned: always
              type: str
              sample: null
            scope:
              description:
                - the scope.
              returned: always
              type: str
              sample: null
        claims:
          description:
            - key value pairs to identify ARM permissions.
          returned: always
          type: dictionary
          sample: null
        caller:
          description:
            - >-
              the email address of the user who has performed the operation, the
              UPN claim or SPN claim based on availability.
          returned: always
          type: str
          sample: null
        description:
          description:
            - the description of the event.
          returned: always
          type: str
          sample: null
        id:
          description:
            - >-
              the Id of this event as required by ARM for RBAC. It contains the
              EventDataID and a timestamp information.
          returned: always
          type: str
          sample: null
        event_data_id:
          description:
            - the event data Id. This is a unique identifier for an event.
          returned: always
          type: str
          sample: null
        correlation_id:
          description:
            - >-
              the correlation Id, usually a GUID in the string format. The
              correlation Id is shared among the events that belong to the same
              uber operation.
          returned: always
          type: str
          sample: null
        event_name:
          description:
            - >-
              the event name. This value should not be confused with
              OperationName. For practical purposes, OperationName might be more
              appealing to end users.
          returned: always
          type: dict
          sample: null
          contains:
            value:
              description:
                - the invariant value.
              returned: always
              type: str
              sample: null
            localized_value:
              description:
                - the locale specific value.
              returned: always
              type: str
              sample: null
        category:
          description:
            - the event category.
          returned: always
          type: dict
          sample: null
          contains:
            value:
              description:
                - the invariant value.
              returned: always
              type: str
              sample: null
            localized_value:
              description:
                - the locale specific value.
              returned: always
              type: str
              sample: null
        http_request:
          description:
            - >-
              the HTTP request info. Usually includes the 'clientRequestId',
              'clientIpAddress' (IP address of the user who initiated the event)
              and 'method' (HTTP method e.g. PUT).
          returned: always
          type: dict
          sample: null
          contains:
            client_request_id:
              description:
                - the client request id.
              returned: always
              type: str
              sample: null
            client_ip_address:
              description:
                - the client Ip Address
              returned: always
              type: str
              sample: null
            method:
              description:
                - the Http request method.
              returned: always
              type: str
              sample: null
            uri:
              description:
                - the Uri.
              returned: always
              type: str
              sample: null
        level:
          description:
            - the event level
          returned: always
          type: sealed-choice
          sample: null
        resource_group_name:
          description:
            - the resource group name of the impacted resource.
          returned: always
          type: str
          sample: null
        resource_provider_name:
          description:
            - the resource provider name of the impacted resource.
          returned: always
          type: dict
          sample: null
          contains:
            value:
              description:
                - the invariant value.
              returned: always
              type: str
              sample: null
            localized_value:
              description:
                - the locale specific value.
              returned: always
              type: str
              sample: null
        resource_id:
          description:
            - >-
              the resource uri that uniquely identifies the resource that caused
              this event.
          returned: always
          type: str
          sample: null
        resource_type:
          description:
            - the resource type
          returned: always
          type: dict
          sample: null
          contains:
            value:
              description:
                - the invariant value.
              returned: always
              type: str
              sample: null
            localized_value:
              description:
                - the locale specific value.
              returned: always
              type: str
              sample: null
        operation_id:
          description:
            - >-
              It is usually a GUID shared among the events corresponding to
              single operation. This value should not be confused with
              EventName.
          returned: always
          type: str
          sample: null
        operation_name:
          description:
            - the operation name.
          returned: always
          type: dict
          sample: null
          contains:
            value:
              description:
                - the invariant value.
              returned: always
              type: str
              sample: null
            localized_value:
              description:
                - the locale specific value.
              returned: always
              type: str
              sample: null
        properties:
          description:
            - >-
              the set of <Key, Value> pairs (usually a Dictionary<String,
              String>) that includes details about the event.
          returned: always
          type: dictionary
          sample: null
        status:
          description:
            - >-
              a string describing the status of the operation. Some typical
              values are: Started, In progress, Succeeded, Failed, Resolved.
          returned: always
          type: dict
          sample: null
          contains:
            value:
              description:
                - the invariant value.
              returned: always
              type: str
              sample: null
            localized_value:
              description:
                - the locale specific value.
              returned: always
              type: str
              sample: null
        sub_status:
          description:
            - >-
              the event sub status. Most of the time, when included, this
              captures the HTTP status code of the REST call. Common values are:
              OK (HTTP Status Code: 200), Created (HTTP Status Code: 201),
              Accepted (HTTP Status Code: 202), No Content (HTTP Status Code:
              204), Bad Request(HTTP Status Code: 400), Not Found (HTTP Status
              Code: 404), Conflict (HTTP Status Code: 409), Internal Server
              Error (HTTP Status Code: 500), Service Unavailable (HTTP Status
              Code:503), Gateway Timeout (HTTP Status Code: 504)
          returned: always
          type: dict
          sample: null
          contains:
            value:
              description:
                - the invariant value.
              returned: always
              type: str
              sample: null
            localized_value:
              description:
                - the locale specific value.
              returned: always
              type: str
              sample: null
        event_timestamp:
          description:
            - >-
              the timestamp of when the event was generated by the Azure service
              processing the request corresponding the event. It in ISO 8601
              format.
          returned: always
          type: str
          sample: null
        submission_timestamp:
          description:
            - >-
              the timestamp of when the event became available for querying via
              this API. It is in ISO 8601 format. This value should not be
              confused eventTimestamp. As there might be a delay between the
              occurrence time of the event, and the time that the event is
              submitted to the Azure logging infrastructure.
          returned: always
          type: str
          sample: null
        subscription_id:
          description:
            - the Azure subscription Id usually a GUID.
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - the Azure tenant Id
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Provides the link to retrieve the next set of events.
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


class AzureRMTenantActivityLogInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            filter=dict(
                type='str',
                required=True
            ),
            select=dict(
                type='str',
                required=True
            )
        )

        self.filter = None
        self.select = None

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
        super(AzureRMTenantActivityLogInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-04-01')

        else:
            self.results['tenant_activity_logs'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.tenant_activity_logs.list(filter=self.filter,
                                                                  select=self.select)
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
    AzureRMTenantActivityLogInfo()


if __name__ == '__main__':
    main()
