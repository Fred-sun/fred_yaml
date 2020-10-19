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
module: azure_rm_event_info
version_added: '2.9'
short_description: Get Event info.
description:
  - Get info of Event.
options:
  resource_group_name:
    description:
      - Name of the Azure Resource Group that migrate project is part of.
    required: true
    type: str
  migrate_project_name:
    description:
      - Name of the Azure Migrate project.
    required: true
    type: str
  continuation_token:
    description:
      - The continuation token.
    type: str
  page_size:
    description:
      - >-
        The number of items to be returned in a single page. This value is
        honored only if it is less than the 100.
    type: integer
  acceptlanguage:
    description:
      - >-
        Standard request header. Used by service to respond to client in
        appropriate language.
    type: str
  event_name:
    description:
      - Unique name of an event within a migrate project.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: MigrateEvents_List
      azure_rm_event_info: 
        migrate_project_name: project01
        resource_group_name: myResourceGroup
        

    - name: MigrateEvents_Get
      azure_rm_event_info: 
        event_name: MigrateEvent01
        migrate_project_name: project01
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
events:
  description: >-
    A list of dict results where the key is the name of the Event and the values
    are the facts for that Event.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Gets or sets the machines.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Gets or sets the relative URL to get to this REST resource.
          returned: always
          type: str
          sample: null
        name:
          description:
            - Gets or sets the name of this REST resource.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Gets the type of this REST resource.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Gets or sets the properties of the event.
          returned: always
          type: dict
          sample: null
          contains:
            instance_type:
              description:
                - Gets the Instance type.
              returned: always
              type: str
              sample: null
            error_code:
              description:
                - Gets or sets the error code.
              returned: always
              type: str
              sample: null
            error_message:
              description:
                - Gets or sets the error message.
              returned: always
              type: str
              sample: null
            recommendation:
              description:
                - Gets or sets the recommendation for the error.
              returned: always
              type: str
              sample: null
            possible_causes:
              description:
                - Gets or sets the possible causes for the error.
              returned: always
              type: str
              sample: null
            solution:
              description:
                - >-
                  Gets or sets the solution for which the error is being
                  reported.
              returned: always
              type: str
              sample: null
            client_request_id:
              description:
                - >-
                  Gets or sets the client request Id of the payload for which
                  the event is being reported.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - Gets or sets the value of nextLink.
      returned: always
      type: str
      sample: null
    id:
      description:
        - Gets or sets the relative URL to get to this REST resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Gets or sets the name of this REST resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Gets the type of this REST resource.
      returned: always
      type: str
      sample: null
    properties:
      description:
        - Gets or sets the properties of the event.
      returned: always
      type: dict
      sample: null
      contains:
        instance_type:
          description:
            - Gets the Instance type.
          returned: always
          type: str
          sample: null
        error_code:
          description:
            - Gets or sets the error code.
          returned: always
          type: str
          sample: null
        error_message:
          description:
            - Gets or sets the error message.
          returned: always
          type: str
          sample: null
        recommendation:
          description:
            - Gets or sets the recommendation for the error.
          returned: always
          type: str
          sample: null
        possible_causes:
          description:
            - Gets or sets the possible causes for the error.
          returned: always
          type: str
          sample: null
        solution:
          description:
            - Gets or sets the solution for which the error is being reported.
          returned: always
          type: str
          sample: null
        client_request_id:
          description:
            - >-
              Gets or sets the client request Id of the payload for which the
              event is being reported.
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
    from azure.mgmt.azure import Azure Migrate Hub
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMEventInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            migrate_project_name=dict(
                type='str',
                required=True
            ),
            continuation_token=dict(
                type='str'
            ),
            page_size=dict(
                type='integer'
            ),
            acceptlanguage=dict(
                type='str'
            ),
            event_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.migrate_project_name = None
        self.continuation_token = None
        self.page_size = None
        self.acceptlanguage = None
        self.event_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-09-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMEventInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Migrate Hub,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

        if (self.resource_group_name is not None and
            self.migrate_project_name is not None and
            self.event_name is not None):
            self.results['events'] = self.format_item(self.getevent())
        elif (self.resource_group_name is not None and
              self.migrate_project_name is not None):
            self.results['events'] = self.format_item(self.enumerateevent())
        return self.results

    def getevent(self):
        response = None

        try:
            response = self.mgmt_client.events.get_event(resource_group_name=self.resource_group_name,
                                                         migrate_project_name=self.migrate_project_name,
                                                         event_name=self.event_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def enumerateevent(self):
        response = None

        try:
            response = self.mgmt_client.events.enumerate_event(resource_group_name=self.resource_group_name,
                                                               migrate_project_name=self.migrate_project_name,
                                                               continuation_token=self.continuation_token,
                                                               page_size=self.page_size,
                                                               acceptlanguage=self.acceptlanguage)
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
    AzureRMEventInfo()


if __name__ == '__main__':
    main()
