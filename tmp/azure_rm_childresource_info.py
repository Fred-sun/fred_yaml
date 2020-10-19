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
module: azure_rm_childresource_info
version_added: '2.9'
short_description: Get ChildResource info.
description:
  - Get info of ChildResource.
options:
  resource_uri:
    description:
      - >-
        The fully qualified ID of the resource, including the resource name and
        resource type. Currently the API only support not nested parent resource
        type:
        /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name}
    required: true
    type: str
  filter:
    description:
      - >-
        The filter to apply on the operation. For more information please see
        https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
    required: true
    type: str
  expand:
    description:
      - >-
        Setting $expand=recommendedactions in url query expands the
        recommendedactions in the response.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetHealthHistoryByResource
      azure_rm_childresource_info: 
        resource_uri: resourceUri
        

'''

RETURN = '''
child_resources:
  description: >-
    A list of dict results where the key is the name of the ChildResource and
    the values are the facts for that ChildResource.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of availabilityStatuses.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - >-
              Azure Resource Manager Identity for the availabilityStatuses
              resource.
          returned: always
          type: str
          sample: null
        name:
          description:
            - current.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Microsoft.ResourceHealth/AvailabilityStatuses.
          returned: always
          type: str
          sample: null
        location:
          description:
            - Azure Resource Manager geo location of the resource.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Properties of availability state.
          returned: always
          type: dict
          sample: null
          contains:
            availability_state:
              description:
                - >-
                  Availability status of the resource. When it is null, this
                  availabilityStatus object represents an availability impacting
                  event
              returned: always
              type: sealed-choice
              sample: null
            summary:
              description:
                - Summary description of the availability status.
              returned: always
              type: str
              sample: null
            detailed_status:
              description:
                - Details of the availability status.
              returned: always
              type: str
              sample: null
            reason_type:
              description:
                - >-
                  When the resource's availabilityState is Unavailable, it
                  describes where the health impacting event was originated.
                  Examples are planned, unplanned, user initiated or an outage
                  etc.
              returned: always
              type: str
              sample: null
            root_cause_attribution_time:
              description:
                - >-
                  When the resource's availabilityState is Unavailable, it
                  provides the Timestamp for when the health impacting event was
                  received.
              returned: always
              type: str
              sample: null
            health_event_type:
              description:
                - >-
                  In case of an availability impacting event, it describes when
                  the health impacting event was originated. Examples are
                  Lifecycle, Downtime, Fault Analysis etc.
              returned: always
              type: str
              sample: null
            health_event_cause:
              description:
                - >-
                  In case of an availability impacting event, it describes where
                  the health impacting event was originated. Examples are
                  PlatformInitiated, UserInitiated etc.
              returned: always
              type: str
              sample: null
            health_event_category:
              description:
                - >-
                  In case of an availability impacting event, it describes the
                  category of a PlatformInitiated health impacting event.
                  Examples are Planned, Unplanned etc.
              returned: always
              type: str
              sample: null
            health_event_id:
              description:
                - It is a unique Id that identifies the event
              returned: always
              type: str
              sample: null
            resolution_eta:
              description:
                - >-
                  When the resource's availabilityState is Unavailable and the
                  reasonType is not User Initiated, it provides the date and
                  time for when the issue is expected to be resolved.
              returned: always
              type: str
              sample: null
            occured_time:
              description:
                - Timestamp for when last change in health status occurred.
              returned: always
              type: str
              sample: null
            reason_chronicity:
              description:
                - Chronicity of the availability transition.
              returned: always
              type: sealed-choice
              sample: null
            reported_time:
              description:
                - 'Timestamp for when the health was last checked. '
              returned: always
              type: str
              sample: null
            recently_resolved_state:
              description:
                - >-
                  An annotation describing a change in the availabilityState to
                  Available from Unavailable with a reasonType of type Unplanned
              returned: always
              type: dict
              sample: null
              contains:
                unavailable_occurred_time:
                  description:
                    - >-
                      Timestamp for when the availabilityState changed to
                      Unavailable
                  returned: always
                  type: str
                  sample: null
                resolved_time:
                  description:
                    - Timestamp when the availabilityState changes to Available.
                  returned: always
                  type: str
                  sample: null
                unavailability_summary:
                  description:
                    - >-
                      Brief description of cause of the resource becoming
                      unavailable.
                  returned: always
                  type: str
                  sample: null
            recommended_actions:
              description:
                - >-
                  Lists actions the user can take based on the current
                  availabilityState of the resource.
              returned: always
              type: list
              sample: null
              contains:
                action:
                  description:
                    - Recommended action.
                  returned: always
                  type: str
                  sample: null
                action_url:
                  description:
                    - Link to the action
                  returned: always
                  type: str
                  sample: null
                action_url_text:
                  description:
                    - >-
                      Substring of action, it describes which text should host
                      the action url.
                  returned: always
                  type: str
                  sample: null
            service_impacting_events:
              description:
                - >-
                  Lists the service impacting events that may be affecting the
                  health of the resource.
              returned: always
              type: list
              sample: null
              contains:
                event_start_time:
                  description:
                    - Timestamp for when the event started.
                  returned: always
                  type: str
                  sample: null
                event_status_last_modified_time:
                  description:
                    - Timestamp for when event was submitted/detected.
                  returned: always
                  type: str
                  sample: null
                correlation_id:
                  description:
                    - Correlation id for the event
                  returned: always
                  type: str
                  sample: null
                status:
                  description:
                    - Status of the service impacting event.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    value:
                      description:
                        - Current status of the event
                      returned: always
                      type: str
                      sample: null
                incident_properties:
                  description:
                    - Properties of the service impacting event.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    title:
                      description:
                        - Title of the incident.
                      returned: always
                      type: str
                      sample: null
                    service:
                      description:
                        - Service impacted by the event.
                      returned: always
                      type: str
                      sample: null
                    region:
                      description:
                        - Region impacted by the event.
                      returned: always
                      type: str
                      sample: null
                    incident_type:
                      description:
                        - Type of Event.
                      returned: always
                      type: str
                      sample: null
    next_link:
      description:
        - >-
          The URI to fetch the next page of availabilityStatuses. Call
          ListNext() with this URI to fetch the next page of
          availabilityStatuses.
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
    from azure.mgmt.microsoft.resource import Microsoft.ResourceHealth
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMChildResourceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_uri=dict(
                type='str',
                required=True
            ),
            filter=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str',
                required=True
            )
        )

        self.resource_uri = None
        self.filter = None
        self.expand = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-07-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMChildResourceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Microsoft.ResourceHealth,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-07-01')

        if (self.resource_uri is not None):
            self.results['child_resources'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.child_resources.list(resource_uri=self.resource_uri,
                                                             filter=self.filter,
                                                             expand=self.expand)
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
    AzureRMChildResourceInfo()


if __name__ == '__main__':
    main()
