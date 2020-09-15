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
module: azure_rm_accountbackup_info
version_added: '2.9'
short_description: Get AccountBackup info.
description:
  - Get info of AccountBackup.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  account_name:
    description:
      - The name of the NetApp account
    required: true
    type: str
  backup_name:
    description:
      - The name of the backup
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: AccountBackups_List
      azure_rm_accountbackup_info: 
        account_name: account1
        resource_group_name: myRG
        

    - name: AccountBackups_Get
      azure_rm_accountbackup_info: 
        account_name: account1
        backup_name: backup1
        resource_group_name: myRG
        

'''

RETURN = '''
account_backups:
  description: >-
    A list of dict results where the key is the name of the AccountBackup and
    the values are the facts for that AccountBackup.
  returned: always
  type: complex
  contains:
    value:
      description:
        - A list of Backups
      returned: always
      type: list
      sample: null
      contains:
        location:
          description:
            - Resource location
          returned: always
          type: str
          sample: null
        id:
          description:
            - Resource Id
          returned: always
          type: str
          sample: null
        name:
          description:
            - Resource name
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type
          returned: always
          type: str
          sample: null
        creation_date:
          description:
            - The creation date of the backup
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - Azure lifecycle management
          returned: always
          type: str
          sample: null
        size:
          description:
            - Size of backup
          returned: always
          type: integer
          sample: null
        label:
          description:
            - Label for backup
          returned: always
          type: str
          sample: null
        backup_type:
          description:
            - Type of backup adhoc or scheduled
          returned: always
          type: str
          sample: null
    location:
      description:
        - Resource location
      returned: always
      type: str
      sample: null
    id:
      description:
        - Resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type
      returned: always
      type: str
      sample: null
    creation_date:
      description:
        - The creation date of the backup
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Azure lifecycle management
      returned: always
      type: str
      sample: null
    size:
      description:
        - Size of backup
      returned: always
      type: integer
      sample: null
    label:
      description:
        - Label for backup
      returned: always
      type: str
      sample: null
    backup_type:
      description:
        - Type of backup adhoc or scheduled
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
    from azure.mgmt.net import NetAppManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAccountBackupInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            backup_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.backup_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMAccountBackupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetAppManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.backup_name is not None):
            self.results['account_backups'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['account_backups'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.account_backups.get(resource_group_name=self.resource_group_name,
                                                            account_name=self.account_name,
                                                            backup_name=self.backup_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.account_backups.list(resource_group_name=self.resource_group_name,
                                                             account_name=self.account_name)
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
    AzureRMAccountBackupInfo()


if __name__ == '__main__':
    main()
