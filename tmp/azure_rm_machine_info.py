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
module: azure_rm_machine_info
version_added: '2.9'
short_description: Get Machine info.
description:
  - Get info of Machine.
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
  machine_name:
    description:
      - Unique name of a machine in Azure migration hub.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Machines_List
      azure_rm_machine_info: 
        migrate_project_name: project01
        resource_group_name: myResourceGroup
        

    - name: Machines_Get
      azure_rm_machine_info: 
        machine_name: vm1
        migrate_project_name: project01
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
machines:
  description: >-
    A list of dict results where the key is the name of the Machine and the
    values are the facts for that Machine.
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
            - Gets or sets the properties of the machine.
          returned: always
          type: dict
          sample: null
          contains:
            discovery_data:
              description:
                - >-
                  Gets or sets the discovery details of the machine published by
                  various sources.
              returned: always
              type: list
              sample: null
              contains:
                os_type:
                  description:
                    - Gets or sets the OS type.
                  returned: always
                  type: str
                  sample: null
                os_name:
                  description:
                    - Gets or sets the OS name.
                  returned: always
                  type: str
                  sample: null
                os_version:
                  description:
                    - Gets or sets the OS version.
                  returned: always
                  type: str
                  sample: null
                enqueue_time:
                  description:
                    - Gets or sets the time the message was enqueued.
                  returned: always
                  type: str
                  sample: null
                solution_name:
                  description:
                    - Gets or sets the name of the solution that sent the data.
                  returned: always
                  type: str
                  sample: null
                machine_id:
                  description:
                    - Gets or sets the unique identifier of the machine.
                  returned: always
                  type: str
                  sample: null
                machine_manager_id:
                  description:
                    - >-
                      Gets or sets the unique identifier of the virtual machine
                      manager(vCenter/VMM).
                  returned: always
                  type: str
                  sample: null
                fabric_type:
                  description:
                    - Gets or sets the fabric type.
                  returned: always
                  type: str
                  sample: null
                last_updated_time:
                  description:
                    - >-
                      Gets or sets the time of the last modification of the
                      machine details.
                  returned: always
                  type: str
                  sample: null
                machine_name:
                  description:
                    - Gets or sets the name of the machine.
                  returned: always
                  type: str
                  sample: null
                ip_addresses:
                  description:
                    - >-
                      Gets or sets the list of IP addresses of the machine. IP
                      addresses could be IP V4 or IP V6.
                  returned: always
                  type: list
                  sample: null
                fqdn:
                  description:
                    - Gets or sets the FQDN of the machine.
                  returned: always
                  type: str
                  sample: null
                bios_id:
                  description:
                    - Gets or sets the BIOS ID of the machine.
                  returned: always
                  type: str
                  sample: null
                mac_addresses:
                  description:
                    - Gets or sets the list of MAC addresses of the machine.
                  returned: always
                  type: list
                  sample: null
                extended_info:
                  description:
                    - Gets or sets the ISV specific extended information.
                  returned: always
                  type: dictionary
                  sample: null
            assessment_data:
              description:
                - >-
                  Gets or sets the assessment details of the machine published
                  by various sources.
              returned: always
              type: list
              sample: null
              contains:
                assessment_id:
                  description:
                    - Gets or sets the id of the assessment done on the machine.
                  returned: always
                  type: str
                  sample: null
                target_vm_size:
                  description:
                    - Gets or sets the target VM size.
                  returned: always
                  type: str
                  sample: null
                target_vm_location:
                  description:
                    - Gets or sets the target VM location.
                  returned: always
                  type: str
                  sample: null
                target_storage_type:
                  description:
                    - Gets or sets the target storage type.
                  returned: always
                  type: dictionary
                  sample: null
                enqueue_time:
                  description:
                    - Gets or sets the time the message was enqueued.
                  returned: always
                  type: str
                  sample: null
                solution_name:
                  description:
                    - Gets or sets the name of the solution that sent the data.
                  returned: always
                  type: str
                  sample: null
                machine_id:
                  description:
                    - Gets or sets the unique identifier of the machine.
                  returned: always
                  type: str
                  sample: null
                machine_manager_id:
                  description:
                    - >-
                      Gets or sets the unique identifier of the virtual machine
                      manager(vCenter/VMM).
                  returned: always
                  type: str
                  sample: null
                fabric_type:
                  description:
                    - Gets or sets the fabric type.
                  returned: always
                  type: str
                  sample: null
                last_updated_time:
                  description:
                    - >-
                      Gets or sets the time of the last modification of the
                      machine details.
                  returned: always
                  type: str
                  sample: null
                machine_name:
                  description:
                    - Gets or sets the name of the machine.
                  returned: always
                  type: str
                  sample: null
                ip_addresses:
                  description:
                    - >-
                      Gets or sets the list of IP addresses of the machine. IP
                      addresses could be IP V4 or IP V6.
                  returned: always
                  type: list
                  sample: null
                fqdn:
                  description:
                    - Gets or sets the FQDN of the machine.
                  returned: always
                  type: str
                  sample: null
                bios_id:
                  description:
                    - Gets or sets the BIOS ID of the machine.
                  returned: always
                  type: str
                  sample: null
                mac_addresses:
                  description:
                    - Gets or sets the list of MAC addresses of the machine.
                  returned: always
                  type: list
                  sample: null
                extended_info:
                  description:
                    - Gets or sets the ISV specific extended information.
                  returned: always
                  type: dictionary
                  sample: null
            migration_data:
              description:
                - >-
                  Gets or sets the migration details of the machine published by
                  various sources.
              returned: always
              type: list
              sample: null
              contains:
                migration_phase:
                  description:
                    - Gets or sets the phase of migration of the machine.
                  returned: always
                  type: str
                  sample: null
                migration_tested:
                  description:
                    - >-
                      Gets or sets a value indicating whether migration was
                      tested on the machine.
                  returned: always
                  type: bool
                  sample: null
                replication_progress_percentage:
                  description:
                    - >-
                      Gets or sets the progress percentage of migration on the
                      machine.
                  returned: always
                  type: integer
                  sample: null
                target_vm_arm_id:
                  description:
                    - Gets or sets the ARM id the migrated VM.
                  returned: always
                  type: str
                  sample: null
                enqueue_time:
                  description:
                    - Gets or sets the time the message was enqueued.
                  returned: always
                  type: str
                  sample: null
                solution_name:
                  description:
                    - Gets or sets the name of the solution that sent the data.
                  returned: always
                  type: str
                  sample: null
                machine_id:
                  description:
                    - Gets or sets the unique identifier of the machine.
                  returned: always
                  type: str
                  sample: null
                machine_manager_id:
                  description:
                    - >-
                      Gets or sets the unique identifier of the virtual machine
                      manager(vCenter/VMM).
                  returned: always
                  type: str
                  sample: null
                fabric_type:
                  description:
                    - Gets or sets the fabric type.
                  returned: always
                  type: str
                  sample: null
                last_updated_time:
                  description:
                    - >-
                      Gets or sets the time of the last modification of the
                      machine details.
                  returned: always
                  type: str
                  sample: null
                machine_name:
                  description:
                    - Gets or sets the name of the machine.
                  returned: always
                  type: str
                  sample: null
                ip_addresses:
                  description:
                    - >-
                      Gets or sets the list of IP addresses of the machine. IP
                      addresses could be IP V4 or IP V6.
                  returned: always
                  type: list
                  sample: null
                fqdn:
                  description:
                    - Gets or sets the FQDN of the machine.
                  returned: always
                  type: str
                  sample: null
                bios_id:
                  description:
                    - Gets or sets the BIOS ID of the machine.
                  returned: always
                  type: str
                  sample: null
                mac_addresses:
                  description:
                    - Gets or sets the list of MAC addresses of the machine.
                  returned: always
                  type: list
                  sample: null
                extended_info:
                  description:
                    - Gets or sets the ISV specific extended information.
                  returned: always
                  type: dictionary
                  sample: null
            last_updated_time:
              description:
                - Gets or sets the time of the last modification of the machine.
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
        - Gets or sets the properties of the machine.
      returned: always
      type: dict
      sample: null
      contains:
        discovery_data:
          description:
            - >-
              Gets or sets the discovery details of the machine published by
              various sources.
          returned: always
          type: list
          sample: null
          contains:
            os_type:
              description:
                - Gets or sets the OS type.
              returned: always
              type: str
              sample: null
            os_name:
              description:
                - Gets or sets the OS name.
              returned: always
              type: str
              sample: null
            os_version:
              description:
                - Gets or sets the OS version.
              returned: always
              type: str
              sample: null
            enqueue_time:
              description:
                - Gets or sets the time the message was enqueued.
              returned: always
              type: str
              sample: null
            solution_name:
              description:
                - Gets or sets the name of the solution that sent the data.
              returned: always
              type: str
              sample: null
            machine_id:
              description:
                - Gets or sets the unique identifier of the machine.
              returned: always
              type: str
              sample: null
            machine_manager_id:
              description:
                - >-
                  Gets or sets the unique identifier of the virtual machine
                  manager(vCenter/VMM).
              returned: always
              type: str
              sample: null
            fabric_type:
              description:
                - Gets or sets the fabric type.
              returned: always
              type: str
              sample: null
            last_updated_time:
              description:
                - >-
                  Gets or sets the time of the last modification of the machine
                  details.
              returned: always
              type: str
              sample: null
            machine_name:
              description:
                - Gets or sets the name of the machine.
              returned: always
              type: str
              sample: null
            ip_addresses:
              description:
                - >-
                  Gets or sets the list of IP addresses of the machine. IP
                  addresses could be IP V4 or IP V6.
              returned: always
              type: list
              sample: null
            fqdn:
              description:
                - Gets or sets the FQDN of the machine.
              returned: always
              type: str
              sample: null
            bios_id:
              description:
                - Gets or sets the BIOS ID of the machine.
              returned: always
              type: str
              sample: null
            mac_addresses:
              description:
                - Gets or sets the list of MAC addresses of the machine.
              returned: always
              type: list
              sample: null
            extended_info:
              description:
                - Gets or sets the ISV specific extended information.
              returned: always
              type: dictionary
              sample: null
        assessment_data:
          description:
            - >-
              Gets or sets the assessment details of the machine published by
              various sources.
          returned: always
          type: list
          sample: null
          contains:
            assessment_id:
              description:
                - Gets or sets the id of the assessment done on the machine.
              returned: always
              type: str
              sample: null
            target_vm_size:
              description:
                - Gets or sets the target VM size.
              returned: always
              type: str
              sample: null
            target_vm_location:
              description:
                - Gets or sets the target VM location.
              returned: always
              type: str
              sample: null
            target_storage_type:
              description:
                - Gets or sets the target storage type.
              returned: always
              type: dictionary
              sample: null
            enqueue_time:
              description:
                - Gets or sets the time the message was enqueued.
              returned: always
              type: str
              sample: null
            solution_name:
              description:
                - Gets or sets the name of the solution that sent the data.
              returned: always
              type: str
              sample: null
            machine_id:
              description:
                - Gets or sets the unique identifier of the machine.
              returned: always
              type: str
              sample: null
            machine_manager_id:
              description:
                - >-
                  Gets or sets the unique identifier of the virtual machine
                  manager(vCenter/VMM).
              returned: always
              type: str
              sample: null
            fabric_type:
              description:
                - Gets or sets the fabric type.
              returned: always
              type: str
              sample: null
            last_updated_time:
              description:
                - >-
                  Gets or sets the time of the last modification of the machine
                  details.
              returned: always
              type: str
              sample: null
            machine_name:
              description:
                - Gets or sets the name of the machine.
              returned: always
              type: str
              sample: null
            ip_addresses:
              description:
                - >-
                  Gets or sets the list of IP addresses of the machine. IP
                  addresses could be IP V4 or IP V6.
              returned: always
              type: list
              sample: null
            fqdn:
              description:
                - Gets or sets the FQDN of the machine.
              returned: always
              type: str
              sample: null
            bios_id:
              description:
                - Gets or sets the BIOS ID of the machine.
              returned: always
              type: str
              sample: null
            mac_addresses:
              description:
                - Gets or sets the list of MAC addresses of the machine.
              returned: always
              type: list
              sample: null
            extended_info:
              description:
                - Gets or sets the ISV specific extended information.
              returned: always
              type: dictionary
              sample: null
        migration_data:
          description:
            - >-
              Gets or sets the migration details of the machine published by
              various sources.
          returned: always
          type: list
          sample: null
          contains:
            migration_phase:
              description:
                - Gets or sets the phase of migration of the machine.
              returned: always
              type: str
              sample: null
            migration_tested:
              description:
                - >-
                  Gets or sets a value indicating whether migration was tested
                  on the machine.
              returned: always
              type: bool
              sample: null
            replication_progress_percentage:
              description:
                - >-
                  Gets or sets the progress percentage of migration on the
                  machine.
              returned: always
              type: integer
              sample: null
            target_vm_arm_id:
              description:
                - Gets or sets the ARM id the migrated VM.
              returned: always
              type: str
              sample: null
            enqueue_time:
              description:
                - Gets or sets the time the message was enqueued.
              returned: always
              type: str
              sample: null
            solution_name:
              description:
                - Gets or sets the name of the solution that sent the data.
              returned: always
              type: str
              sample: null
            machine_id:
              description:
                - Gets or sets the unique identifier of the machine.
              returned: always
              type: str
              sample: null
            machine_manager_id:
              description:
                - >-
                  Gets or sets the unique identifier of the virtual machine
                  manager(vCenter/VMM).
              returned: always
              type: str
              sample: null
            fabric_type:
              description:
                - Gets or sets the fabric type.
              returned: always
              type: str
              sample: null
            last_updated_time:
              description:
                - >-
                  Gets or sets the time of the last modification of the machine
                  details.
              returned: always
              type: str
              sample: null
            machine_name:
              description:
                - Gets or sets the name of the machine.
              returned: always
              type: str
              sample: null
            ip_addresses:
              description:
                - >-
                  Gets or sets the list of IP addresses of the machine. IP
                  addresses could be IP V4 or IP V6.
              returned: always
              type: list
              sample: null
            fqdn:
              description:
                - Gets or sets the FQDN of the machine.
              returned: always
              type: str
              sample: null
            bios_id:
              description:
                - Gets or sets the BIOS ID of the machine.
              returned: always
              type: str
              sample: null
            mac_addresses:
              description:
                - Gets or sets the list of MAC addresses of the machine.
              returned: always
              type: list
              sample: null
            extended_info:
              description:
                - Gets or sets the ISV specific extended information.
              returned: always
              type: dictionary
              sample: null
        last_updated_time:
          description:
            - Gets or sets the time of the last modification of the machine.
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


class AzureRMMachineInfo(AzureRMModuleBase):
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
            machine_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.migrate_project_name = None
        self.continuation_token = None
        self.page_size = None
        self.machine_name = None

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
        super(AzureRMMachineInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Migrate Hub,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

        if (self.resource_group_name is not None and
            self.migrate_project_name is not None and
            self.machine_name is not None):
            self.results['machines'] = self.format_item(self.getmachine())
        elif (self.resource_group_name is not None and
              self.migrate_project_name is not None):
            self.results['machines'] = self.format_item(self.enumeratemachine())
        return self.results

    def getmachine(self):
        response = None

        try:
            response = self.mgmt_client.machines.get_machine(resource_group_name=self.resource_group_name,
                                                             migrate_project_name=self.migrate_project_name,
                                                             machine_name=self.machine_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def enumeratemachine(self):
        response = None

        try:
            response = self.mgmt_client.machines.enumerate_machine(resource_group_name=self.resource_group_name,
                                                                   migrate_project_name=self.migrate_project_name,
                                                                   continuation_token=self.continuation_token,
                                                                   page_size=self.page_size)
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
    AzureRMMachineInfo()


if __name__ == '__main__':
    main()
