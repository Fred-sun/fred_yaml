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
module: azure_rm_emergingissue
version_added: '2.9'
short_description: Manage Azure EmergingIssue instance.
description:
  - 'Create, update and delete instance of Azure EmergingIssue.'
options:
  issuename:
    description:
      - The name of the emerging issue.
    required: true
    type: constant
  state:
    description:
      - Assert the state of the EmergingIssue.
      - >-
        Use C(present) to create or update an EmergingIssue and C(absent) to
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
'''

RETURN = '''
id:
  description:
    - >-
      Fully qualified resource Id for the resource. Ex -
      /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the resource
  returned: always
  type: str
  sample: null
type:
  description:
    - >-
      The type of the resource. Ex- Microsoft.Compute/virtualMachines or
      Microsoft.Storage/storageAccounts.
  returned: always
  type: str
  sample: null
refresh_timestamp:
  description:
    - Timestamp for when last time refreshed for ongoing emerging issue.
  returned: always
  type: str
  sample: null
status_banners:
  description:
    - The list of emerging issues of banner type.
  returned: always
  type: list
  sample: null
  contains:
    title:
      description:
        - The banner title.
      returned: always
      type: str
      sample: null
    message:
      description:
        - The details of banner.
      returned: always
      type: str
      sample: null
    cloud:
      description:
        - The cloud type of this banner.
      returned: always
      type: str
      sample: null
    last_modified_time:
      description:
        - The last time modified on this banner.
      returned: always
      type: str
      sample: null
status_active_events:
  description:
    - The list of emerging issues of active event type.
  returned: always
  type: list
  sample: null
  contains:
    title:
      description:
        - The active event title.
      returned: always
      type: str
      sample: null
    description:
      description:
        - The details of active event.
      returned: always
      type: str
      sample: null
    tracking_id:
      description:
        - The tracking id of this active event.
      returned: always
      type: str
      sample: null
    start_time:
      description:
        - The impact start time on this active event.
      returned: always
      type: str
      sample: null
    cloud:
      description:
        - The cloud type of this active event.
      returned: always
      type: str
      sample: null
    severity:
      description:
        - The severity level of this active event.
      returned: always
      type: str
      sample: null
    stage:
      description:
        - The stage of this active event.
      returned: always
      type: str
      sample: null
    published:
      description:
        - The boolean value of this active event if published or not.
      returned: always
      type: bool
      sample: null
    last_modified_time:
      description:
        - The last time modified on this banner.
      returned: always
      type: str
      sample: null
    impacts:
      description:
        - The list of emerging issues impacts.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - The impacted service id.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The impacted service name.
          returned: always
          type: str
          sample: null
        regions:
          description:
            - The list of impacted regions for corresponding emerging issues.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - The impacted region id.
              returned: always
              type: str
              sample: null
            name:
              description:
                - The impacted region name.
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
    from azure.mgmt.microsoft.resource import Microsoft.ResourceHealth
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMEmergingIssue(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            issuename=dict(
                type='constant',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.issuename = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMEmergingIssue, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Microsoft.ResourceHealth,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-07-01')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.emerging_issues.create()
            else:
                response = self.mgmt_client.emerging_issues.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the EmergingIssue instance.')
            self.fail('Error creating the EmergingIssue instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.emerging_issues.delete()
        except CloudError as e:
            self.log('Error attempting to delete the EmergingIssue instance.')
            self.fail('Error deleting the EmergingIssue instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.emerging_issues.get(issuename=self.issuename)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMEmergingIssue()


if __name__ == '__main__':
    main()
