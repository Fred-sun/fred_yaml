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
module: azure_rm_transparentdataencryptionactivity_info
version_added: '2.9'
short_description: Get TransparentDataEncryptionActivity info.
description:
  - Get info of TransparentDataEncryptionActivity.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  server_name:
    description:
      - The name of the server.
    required: true
    type: str
  database_name:
    description:
      - >-
        The name of the database for which the transparent data encryption
        applies.
    required: true
    type: str
  transparent_data_encryption_name:
    description:
      - The name of the transparent data encryption configuration.
    required: true
    type: str
    choices:
      - current
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List a database's transparent data encryption activities
      azure_rm_transparentdataencryptionactivity_info: 
        database_name: sqlcrudtest-9187
        resource_group_name: sqlcrudtest-6852
        server_name: sqlcrudtest-2080
        transparent_data_encryption_name: current
        

'''

RETURN = '''
transparent_data_encryption_activities:
  description: >-
    A list of dict results where the key is the name of the
    TransparentDataEncryptionActivity and the values are the facts for that
    TransparentDataEncryptionActivity.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of database transparent data encryption activities.
      returned: always
      type: list
      sample: null
      contains:
        location:
          description:
            - Resource location.
          returned: always
          type: str
          sample: null
        status:
          description:
            - The status of the database.
          returned: always
          type: str
          sample: null
        percent_complete:
          description:
            - >-
              The percent complete of the transparent data encryption scan for a
              database.
          returned: always
          type: number
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMTransparentDataEncryptionActivityInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            database_name=dict(
                type='str',
                required=True
            ),
            transparent_data_encryption_name=dict(
                type='str',
                choices=['current'],
                required=True
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.transparent_data_encryption_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2014-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMTransparentDataEncryptionActivityInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.database_name is not None and
            self.transparent_data_encryption_name is not None):
            self.results['transparent_data_encryption_activities'] = self.format_item(self.listbyconfiguration())
        return self.results

    def listbyconfiguration(self):
        response = None

        try:
            response = self.mgmt_client.transparent_data_encryption_activities.list_by_configuration(resource_group_name=self.resource_group_name,
                                                                                                     server_name=self.server_name,
                                                                                                     database_name=self.database_name,
                                                                                                     transparent_data_encryption_name=self.transparent_data_encryption_name)
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
    AzureRMTransparentDataEncryptionActivityInfo()


if __name__ == '__main__':
    main()
