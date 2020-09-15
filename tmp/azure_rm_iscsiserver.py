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
module: azure_rm_iscsiserver
version_added: '2.9'
short_description: Manage Azure IscsiServer instance.
description:
  - 'Create, update and delete instance of Azure IscsiServer.'
options:
  device_name:
    description:
      - The device name.
    required: true
    type: str
  iscsi_server_name:
    description:
      - The iSCSI server name.
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name
    required: true
    type: str
  manager_name:
    description:
      - The manager name
    required: true
    type: str
  storage_domain_id:
    description:
      - The storage domain id.
    type: str
  backup_schedule_group_id:
    description:
      - The backup policy id.
    type: str
  description:
    description:
      - The description.
    type: str
  chap_id:
    description:
      - The chap id.
    type: str
  reverse_chap_id:
    description:
      - The reverse chap id.
    type: str
  state:
    description:
      - Assert the state of the IscsiServer.
      - >-
        Use C(present) to create or update an IscsiServer and C(absent) to
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
    - name: IscsiServersCreateOrUpdate
      azure_rm_iscsiserver: 
        device_name: HSDK-WSJQERQW3F
        iscsi_server_name: HSDK-WSJQERQW3F
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

    - name: IscsiServersDelete
      azure_rm_iscsiserver: 
        device_name: HSDK-UGU4PITWNI
        iscsi_server_name: HSDK-UGU4PITWNI
        manager_name: hAzureSDKOperations
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
id:
  description:
    - The identifier.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type.
  returned: always
  type: str
  sample: null
storage_domain_id:
  description:
    - The storage domain id.
  returned: always
  type: str
  sample: null
backup_schedule_group_id:
  description:
    - The backup policy id.
  returned: always
  type: str
  sample: null
description:
  description:
    - The description.
  returned: always
  type: str
  sample: null
chap_id:
  description:
    - The chap id.
  returned: always
  type: str
  sample: null
reverse_chap_id:
  description:
    - The reverse chap id.
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
    from azure.mgmt.stor import StorSimpleManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMIscsiServer(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            iscsi_server_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            manager_name=dict(
                type='str',
                required=True
            ),
            storage_domain_id=dict(
                type='str',
                disposition='/storage_domain_id'
            ),
            backup_schedule_group_id=dict(
                type='str',
                disposition='/backup_schedule_group_id'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            chap_id=dict(
                type='str',
                disposition='/chap_id'
            ),
            reverse_chap_id=dict(
                type='str',
                disposition='/reverse_chap_id'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.device_name = None
        self.iscsi_server_name = None
        self.resource_group_name = None
        self.manager_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMIscsiServer, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(StorSimpleManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-10-01')

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
            response = self.mgmt_client.iscsi_servers.create_or_update(device_name=self.device_name,
                                                                       iscsi_server_name=self.iscsi_server_name,
                                                                       resource_group_name=self.resource_group_name,
                                                                       manager_name=self.manager_name,
                                                                       iscsi_server=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the IscsiServer instance.')
            self.fail('Error creating the IscsiServer instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.iscsi_servers.delete(device_name=self.device_name,
                                                             iscsi_server_name=self.iscsi_server_name,
                                                             resource_group_name=self.resource_group_name,
                                                             manager_name=self.manager_name)
        except CloudError as e:
            self.log('Error attempting to delete the IscsiServer instance.')
            self.fail('Error deleting the IscsiServer instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.iscsi_servers.get(device_name=self.device_name,
                                                          iscsi_server_name=self.iscsi_server_name,
                                                          resource_group_name=self.resource_group_name,
                                                          manager_name=self.manager_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMIscsiServer()


if __name__ == '__main__':
    main()
