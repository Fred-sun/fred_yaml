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
module: azure_rm_guestconfigurationassignmentreport
version_added: '2.9'
short_description: Manage Azure GuestConfigurationAssignmentReport instance.
description:
  - >-
    Create, update and delete instance of Azure
    GuestConfigurationAssignmentReport.
options:
  resource_group_name:
    description:
      - The resource group name.
    required: true
    type: str
  guest_configuration_assignment_name:
    description:
      - The guest configuration assignment name.
    required: true
    type: str
  report_id:
    description:
      - The GUID for the guest configuration assignment report.
    required: true
    type: str
  vm_name:
    description:
      - The name of the virtual machine.
    required: true
    type: str
  state:
    description:
      - Assert the state of the GuestConfigurationAssignmentReport.
      - >-
        Use C(present) to create or update an GuestConfigurationAssignmentReport
        and C(absent) to delete it.
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
    - ARM resource id of the report for the guest configuration assignment.
  returned: always
  type: str
  sample: null
name:
  description:
    - >-
      GUID that identifies the guest configuration assignment report under a
      subscription, resource group.
  returned: always
  type: str
  sample: null
properties:
  description:
    - Properties of the guest configuration report.
  returned: always
  type: dict
  sample: null
  contains:
    compliance_status:
      description:
        - >-
          A value indicating compliance status of the machine for the assigned
          guest configuration.
      returned: always
      type: str
      sample: null
    report_id:
      description:
        - >-
          GUID that identifies the guest configuration assignment report under a
          subscription, resource group.
      returned: always
      type: str
      sample: null
    assignment:
      description:
        - Configuration details of the guest configuration assignment.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - Name of the guest configuration assignment.
          returned: always
          type: str
          sample: null
        configuration:
          description:
            - Information about the configuration.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Name of the configuration.
              returned: always
              type: str
              sample: null
            version:
              description:
                - Version of the configuration.
              returned: always
              type: str
              sample: null
    vm:
      description:
        - Information about the VM.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - Azure resource Id of the VM.
          returned: always
          type: str
          sample: null
        uuid:
          description:
            - UUID(Universally Unique Identifier) of the VM.
          returned: always
          type: str
          sample: null
    start_time:
      description:
        - >-
          Start date and time of the guest configuration assignment compliance
          status check.
      returned: always
      type: str
      sample: null
    end_time:
      description:
        - >-
          End date and time of the guest configuration assignment compliance
          status check.
      returned: always
      type: str
      sample: null
    details:
      description:
        - Details of the assignment report.
      returned: always
      type: dict
      sample: null
      contains:
        compliance_status:
          description:
            - >-
              A value indicating compliance status of the machine for the
              assigned guest configuration.
          returned: always
          type: str
          sample: null
        start_time:
          description:
            - >-
              Start date and time of the guest configuration assignment
              compliance status check.
          returned: always
          type: str
          sample: null
        end_time:
          description:
            - >-
              End date and time of the guest configuration assignment compliance
              status check.
          returned: always
          type: str
          sample: null
        job_id:
          description:
            - GUID of the report.
          returned: always
          type: str
          sample: null
        operation_type:
          description:
            - 'Type of report, Consistency or Initial'
          returned: always
          type: str
          sample: null
        resources:
          description:
            - >-
              The list of resources for which guest configuration assignment
              compliance is checked.
          returned: always
          type: list
          sample: null
          contains:
            compliance_status:
              description:
                - >-
                  A value indicating compliance status of the machine for the
                  assigned guest configuration.
              returned: always
              type: str
              sample: null
            resource_id:
              description:
                - Name of the guest configuration assignment resource setting.
              returned: always
              type: str
              sample: null
            reasons:
              description:
                - Compliance reason and reason code for a resource.
              returned: always
              type: list
              sample: null
              contains:
                phrase:
                  description:
                    - >-
                      Reason for the compliance of the guest configuration
                      assignment resource.
                  returned: always
                  type: str
                  sample: null
                code:
                  description:
                    - >-
                      Code for the compliance of the guest configuration
                      assignment resource.
                  returned: always
                  type: str
                  sample: null
            properties:
              description:
                - Properties of a guest configuration assignment resource.
              returned: always
              type: any
              sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.guest import GuestConfigurationClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMGuestConfigurationAssignmentReport(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            guest_configuration_assignment_name=dict(
                type='str',
                required=True
            ),
            report_id=dict(
                type='str',
                required=True
            ),
            vm_name=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.guest_configuration_assignment_name = None
        self.report_id = None
        self.vm_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGuestConfigurationAssignmentReport, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(GuestConfigurationClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-25')

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
                response = self.mgmt_client.guest_configuration_assignment_reports.create()
            else:
                response = self.mgmt_client.guest_configuration_assignment_reports.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the GuestConfigurationAssignmentReport instance.')
            self.fail('Error creating the GuestConfigurationAssignmentReport instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.guest_configuration_assignment_reports.delete()
        except CloudError as e:
            self.log('Error attempting to delete the GuestConfigurationAssignmentReport instance.')
            self.fail('Error deleting the GuestConfigurationAssignmentReport instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.guest_configuration_assignment_reports.get(resource_group_name=self.resource_group_name,
                                                                                   guest_configuration_assignment_name=self.guest_configuration_assignment_name,
                                                                                   report_id=self.report_id,
                                                                                   vm_name=self.vm_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGuestConfigurationAssignmentReport()


if __name__ == '__main__':
    main()
