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
module: azure_rm_availabilitygrouplistener_info
version_added: '2.9'
short_description: Get AvailabilityGroupListener info.
description:
  - Get info of AvailabilityGroupListener.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets an availability group listener.
      azure_rm_availabilitygrouplistener_info: 
        availability_group_listener_name: agl-test
        resource_group_name: testrg
        

    - name: Lists all availability group listeners in a SQL virtual machine group.
      azure_rm_availabilitygrouplistener_info: 
        resource_group_name: testrg
        

'''

RETURN = '''
availability_group_listeners:
  description: >-
    A list of dict results where the key is the name of the
    AvailabilityGroupListener and the values are the facts for that
    AvailabilityGroupListener.
  returned: always
  type: complex
  contains:
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
        - >-
          List of load balancer configurations for an availability group
          listener.
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
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
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
            - >-
              List of load balancer configurations for an availability group
              listener.
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
                    - >-
                      Private IP address bound to the availability group
                      listener.
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
                  List of the SQL virtual machine instance resource id's that
                  are enrolled into the availability group listener.
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
    next_link:
      description:
        - Link to retrieve next page of results.
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
    from azure.mgmt.sql import SqlVirtualMachineManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAvailabilityGroupListenerInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.sqlvirtual_machine_group_name = None
        self.availability_group_listener_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-03-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMAvailabilityGroupListenerInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlVirtualMachineManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

        if (self.resource_group_name is not None and
            self.sqlvirtual_machine_group_name is not None and
            self.availability_group_listener_name is not None):
            self.results['availability_group_listeners'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.sqlvirtual_machine_group_name is not None):
            self.results['availability_group_listeners'] = self.format_item(self.listbygroup())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.availability_group_listeners.get(resource_group_name=self.resource_group_name,
                                                                         sqlvirtual_machine_group_name=self.sqlvirtual_machine_group_name,
                                                                         availability_group_listener_name=self.availability_group_listener_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbygroup(self):
        response = None

        try:
            response = self.mgmt_client.availability_group_listeners.list_by_group(resource_group_name=self.resource_group_name,
                                                                                   sqlvirtual_machine_group_name=self.sqlvirtual_machine_group_name)
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
    AzureRMAvailabilityGroupListenerInfo()


if __name__ == '__main__':
    main()
