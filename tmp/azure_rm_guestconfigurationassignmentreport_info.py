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
module: azure_rm_guestconfigurationassignmentreport_info
version_added: '2.9'
short_description: Get GuestConfigurationAssignmentReport info.
description:
  - Get info of GuestConfigurationAssignmentReport.
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
  vm_name:
    description:
      - The name of the virtual machine.
    required: true
    type: str
  report_id:
    description:
      - The GUID for the guest configuration assignment report.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List all guest configuration assignments for a virtual machine
      azure_rm_guestconfigurationassignmentreport_info: 
        guest_configuration_assignment_name: AuditSecureProtocol
        resource_group_name: myResourceGroupName
        vm_name: myVMName
        

    - name: Get a guest configuration assignment report by Id for a virtual machine
      azure_rm_guestconfigurationassignmentreport_info: 
        guest_configuration_assignment_name: AuditSecureProtocol
        report_id: 7367cbb8-ae99-47d0-a33b-a283564d2cb1
        resource_group_name: myResourceGroupName
        vm_name: myvm
        

'''

RETURN = '''
guest_configuration_assignment_reports:
  description: >-
    A list of dict results where the key is the name of the
    GuestConfigurationAssignmentReport and the values are the facts for that
    GuestConfigurationAssignmentReport.
  returned: always
  type: complex
  contains:
    value:
      description:
        - >-
          List of reports for the guest configuration. Report contains
          information such as compliance status, reason and more.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - >-
              ARM resource id of the report for the guest configuration
              assignment.
          returned: always
          type: str
          sample: null
        name:
          description:
            - >-
              GUID that identifies the guest configuration assignment report
              under a subscription, resource group.
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
                  A value indicating compliance status of the machine for the
                  assigned guest configuration.
              returned: always
              type: str
              sample: null
            report_id:
              description:
                - >-
                  GUID that identifies the guest configuration assignment report
                  under a subscription, resource group.
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
                  Start date and time of the guest configuration assignment
                  compliance status check.
              returned: always
              type: str
              sample: null
            end_time:
              description:
                - >-
                  End date and time of the guest configuration assignment
                  compliance status check.
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
                      A value indicating compliance status of the machine for
                      the assigned guest configuration.
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
                      End date and time of the guest configuration assignment
                      compliance status check.
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
                      The list of resources for which guest configuration
                      assignment compliance is checked.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    compliance_status:
                      description:
                        - >-
                          A value indicating compliance status of the machine
                          for the assigned guest configuration.
                      returned: always
                      type: str
                      sample: null
                    resource_id:
                      description:
                        - >-
                          Name of the guest configuration assignment resource
                          setting.
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
                              Reason for the compliance of the guest
                              configuration assignment resource.
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
                        - >-
                          Properties of a guest configuration assignment
                          resource.
                      returned: always
                      type: any
                      sample: null
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
              A value indicating compliance status of the machine for the
              assigned guest configuration.
          returned: always
          type: str
          sample: null
        report_id:
          description:
            - >-
              GUID that identifies the guest configuration assignment report
              under a subscription, resource group.
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
                  End date and time of the guest configuration assignment
                  compliance status check.
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
                      A value indicating compliance status of the machine for
                      the assigned guest configuration.
                  returned: always
                  type: str
                  sample: null
                resource_id:
                  description:
                    - >-
                      Name of the guest configuration assignment resource
                      setting.
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.guest import GuestConfigurationClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMGuestConfigurationAssignmentReportInfo(AzureRMModuleBase):
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
            vm_name=dict(
                type='str',
                required=True
            ),
            report_id=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.guest_configuration_assignment_name = None
        self.vm_name = None
        self.report_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-25'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMGuestConfigurationAssignmentReportInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GuestConfigurationClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-25')

        if (self.resource_group_name is not None and
            self.guest_configuration_assignment_name is not None and
            self.report_id is not None and
            self.vm_name is not None):
            self.results['guest_configuration_assignment_reports'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.guest_configuration_assignment_name is not None and
              self.vm_name is not None):
            self.results['guest_configuration_assignment_reports'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.guest_configuration_assignment_reports.get(resource_group_name=self.resource_group_name,
                                                                                   guest_configuration_assignment_name=self.guest_configuration_assignment_name,
                                                                                   report_id=self.report_id,
                                                                                   vm_name=self.vm_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.guest_configuration_assignment_reports.list(resource_group_name=self.resource_group_name,
                                                                                    guest_configuration_assignment_name=self.guest_configuration_assignment_name,
                                                                                    vm_name=self.vm_name)
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
    AzureRMGuestConfigurationAssignmentReportInfo()


if __name__ == '__main__':
    main()
