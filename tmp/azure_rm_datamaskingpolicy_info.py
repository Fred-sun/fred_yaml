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
module: azure_rm_datamaskingpolicy_info
version_added: '2.9'
short_description: Get DataMaskingPolicy info.
description:
  - Get info of DataMaskingPolicy.
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
      - The name of the database.
    required: true
    type: str
  datamaskingpolicyname:
    description:
      - The name of the database for which the data masking rule applies.
    required: true
    type: constant
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get data masking policy
      azure_rm_datamaskingpolicy_info: 
        database_name: sqlcrudtest-331
        resource_group_name: sqlcrudtest-6852
        server_name: sqlcrudtest-2080
        

'''

RETURN = '''
data_masking_policies:
  description: >-
    A list of dict results where the key is the name of the DataMaskingPolicy
    and the values are the facts for that DataMaskingPolicy.
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
    location:
      description:
        - The location of the data masking policy.
      returned: always
      type: str
      sample: null
    kind:
      description:
        - 'The kind of data masking policy. Metadata, used for Azure portal.'
      returned: always
      type: str
      sample: null
    data_masking_state:
      description:
        - The state of the data masking policy.
      returned: always
      type: sealed-choice
      sample: null
    exempt_principals:
      description:
        - >-
          The list of the exempt principals. Specifies the semicolon-separated
          list of database users for which the data masking policy does not
          apply. The specified users receive data results without masking for
          all of the database queries.
      returned: always
      type: str
      sample: null
    application_principals:
      description:
        - >-
          The list of the application principals. This is a legacy parameter and
          is no longer used.
      returned: always
      type: str
      sample: null
    masking_level:
      description:
        - The masking level. This is a legacy parameter and is no longer used.
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDataMaskingPolicyInfo(AzureRMModuleBase):
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
            datamaskingpolicyname=dict(
                type='constant',
                required=True
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.datamaskingpolicyname = None

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
        super(AzureRMDataMaskingPolicyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.database_name is not None and
            self.datamaskingpolicyname is not None):
            self.results['data_masking_policies'] = self.format_item(self.get())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.data_masking_policies.get(resource_group_name=self.resource_group_name,
                                                                  server_name=self.server_name,
                                                                  database_name=self.database_name,
                                                                  datamaskingpolicyname=self.datamaskingpolicyname)
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
    AzureRMDataMaskingPolicyInfo()


if __name__ == '__main__':
    main()
