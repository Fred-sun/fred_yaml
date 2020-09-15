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
module: azure_rm_availabilitygrouplistener
version_added: '2.9'
short_description: Manage Azure AvailabilityGroupListener instance.
description:
  - 'Create, update and delete instance of Azure AvailabilityGroupListener.'
options:
  resource_group_name:
    description:
      - >-
        Name of the resource group that contains the resource. You can obtain
        this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  sqlvirtual_machine_group_name:
    description:
      - Name of the SQL virtual machine group.
    required: true
    type: str
  availability_group_listener_name:
    description:
      - Name of the availability group listener.
    required: true
    type: str
  availability_group_name:
    description:
      - Name of the availability group.
    type: str
  load_balancer_configurations:
    description:
      - List of load balancer configurations for an availability group listener.
    type: list
    suboptions:
      private_ip_address:
        description:
          - Private IP address.
        type: dict
        suboptions:
          ip_address:
            description:
              - Private IP address bound to the availability group listener.
            type: str
          subnet_resource_id:
            description:
              - Subnet used to include private IP.
            type: str
      public_ip_address_resource_id:
        description:
          - Resource id of the public IP.
        type: str
      load_balancer_resource_id:
        description:
          - Resource id of the load balancer.
        type: str
      probe_port:
        description:
          - Probe port.
        type: integer
      sqlvirtual_machine_instances:
        description:
          - >-
            List of the SQL virtual machine instance resource id's that are
            enrolled into the availability group listener.
        type: list
  create_default_availability_group_if_not_exist:
    description:
      - Create a default availability group if it does not exist.
    type: bool
  port:
    description:
      - Listener port.
    type: integer
  state:
    description:
      - Assert the state of the AvailabilityGroupListener.
      - >-
        Use C(present) to create or update an AvailabilityGroupListener and
        C(absent) to delete it.
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
    - name: Creates or updates an availability group listener.
      azure_rm_availabilitygrouplistener: 
        availability_group_listener_name: agl-test
        resource_group_name: testrg
        properties:
          availability_group_name: ag-test
          load_balancer_configurations:
            - load_balancer_resource_id: >-
                /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.Network/loadBalancers/lb-test
              private_ip_address:
                ip_address: 10.1.0.112
                subnet_resource_id: >-
                  /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.Network/virtualNetworks/test-vnet/subnets/default
              probe_port: 59983
              sql_virtual_machine_instances:
                - >-
                  /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.SqlVirtualMachine/sqlVirtualMachines/testvm2
                - >-
                  /subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/testrg/providers/Microsoft.SqlVirtualMachine/sqlVirtualMachines/testvm3
          port: 1433
        

    - name: Deletes an availability group listener.
      azure_rm_availabilitygrouplistener: 
        availability_group_listener_name: agl-test
        resource_group_name: testrg
        

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - Provisioning state to track the async operation status.
  returned: always
  type: str
  sample: null
availability_group_name:
  description:
    - Name of the availability group.
  returned: always
  type: str
  sample: null
load_balancer_configurations:
  description:
    - List of load balancer configurations for an availability group listener.
  returned: always
  type: list
  sample: null
  contains:
    private_ip_address:
      description:
        - Private IP address.
      returned: always
      type: dict
      sample: null
      contains:
        ip_address:
          description:
            - Private IP address bound to the availability group listener.
          returned: always
          type: str
          sample: null
        subnet_resource_id:
          description:
            - Subnet used to include private IP.
          returned: always
          type: str
          sample: null
    public_ip_address_resource_id:
      description:
        - Resource id of the public IP.
      returned: always
      type: str
      sample: null
    load_balancer_resource_id:
      description:
        - Resource id of the load balancer.
      returned: always
      type: str
      sample: null
    probe_port:
      description:
        - Probe port.
      returned: always
      type: integer
      sample: null
    sqlvirtual_machine_instances:
      description:
        - >-
          List of the SQL virtual machine instance resource id's that are
          enrolled into the availability group listener.
      returned: always
      type: list
      sample: null
create_default_availability_group_if_not_exist:
  description:
    - Create a default availability group if it does not exist.
  returned: always
  type: bool
  sample: null
port:
  description:
    - Listener port.
  returned: always
  type: integer
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlVirtualMachineManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMAvailabilityGroupListener(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            sqlvirtual_machine_group_name=dict(
                type='str',
                required=True
            ),
            availability_group_listener_name=dict(
                type='str',
                required=True
            ),
            availability_group_name=dict(
                type='str',
                disposition='/availability_group_name'
            ),
            load_balancer_configurations=dict(
                type='list',
                disposition='/load_balancer_configurations',
                elements='dict',
                options=dict(
                    private_ip_address=dict(
                        type='dict',
                        disposition='private_ip_address',
                        options=dict(
                            ip_address=dict(
                                type='str',
                                disposition='ip_address'
                            ),
                            subnet_resource_id=dict(
                                type='str',
                                disposition='subnet_resource_id'
                            )
                        )
                    ),
                    public_ip_address_resource_id=dict(
                        type='str',
                        disposition='public_ip_address_resource_id'
                    ),
                    load_balancer_resource_id=dict(
                        type='str',
                        disposition='load_balancer_resource_id'
                    ),
                    probe_port=dict(
                        type='integer',
                        disposition='probe_port'
                    ),
                    sqlvirtual_machine_instances=dict(
                        type='list',
                        disposition='sqlvirtual_machine_instances',
                        elements='str'
                    )
                )
            ),
            create_default_availability_group_if_not_exist=dict(
                type='bool',
                disposition='/create_default_availability_group_if_not_exist'
            ),
            port=dict(
                type='integer',
                disposition='/port'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.sqlvirtual_machine_group_name = None
        self.availability_group_listener_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAvailabilityGroupListener, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SqlVirtualMachineManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

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
            response = self.mgmt_client.availability_group_listeners.create_or_update(resource_group_name=self.resource_group_name,
                                                                                      sqlvirtual_machine_group_name=self.sqlvirtual_machine_group_name,
                                                                                      availability_group_listener_name=self.availability_group_listener_name,
                                                                                      parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the AvailabilityGroupListener instance.')
            self.fail('Error creating the AvailabilityGroupListener instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.availability_group_listeners.delete(resource_group_name=self.resource_group_name,
                                                                            sqlvirtual_machine_group_name=self.sqlvirtual_machine_group_name,
                                                                            availability_group_listener_name=self.availability_group_listener_name)
        except CloudError as e:
            self.log('Error attempting to delete the AvailabilityGroupListener instance.')
            self.fail('Error deleting the AvailabilityGroupListener instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.availability_group_listeners.get(resource_group_name=self.resource_group_name,
                                                                         sqlvirtual_machine_group_name=self.sqlvirtual_machine_group_name,
                                                                         availability_group_listener_name=self.availability_group_listener_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAvailabilityGroupListener()


if __name__ == '__main__':
    main()
