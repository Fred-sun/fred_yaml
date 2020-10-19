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
module: azure_rm_availableprovideroperation_info
version_added: '2.9'
short_description: Get AvailableProviderOperation info.
description:
  - Get info of AvailableProviderOperation.
options: {}
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: OperationsList
      azure_rm_availableprovideroperation_info: 
        {}
        

'''

RETURN = '''
available_provider_operations:
  description: >-
    A list of dict results where the key is the name of the
    AvailableProviderOperation and the values are the facts for that
    AvailableProviderOperation.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The value.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - "Gets or sets the name of the operation being performed on this particular object\r\nReturn value format: \"{resourceProviderNamespace}/{resourceType}/{read|write|deletion|action}\"\r\nEg: Microsoft.StorSimple/managers/devices/fileServers/read\r\n    Microsoft.StorSimple/managers/devices/alerts/clearAlerts/action"
          returned: always
          type: str
          sample: null
        display:
          description:
            - "Gets or sets Display information\r\nContains the localized display information for this particular operation/action"
          returned: always
          type: dict
          sample: null
          contains:
            provider:
              description:
                - "Gets or sets Provider\r\nThe localized friendly form of the resource provider name – it is expected to also include the publisher/company responsible. \r\nIt should use Title Casing and begin with “Microsoft” for 1st party services."
              returned: always
              type: str
              sample: null
            resource:
              description:
                - "Gets or sets Resource\r\nThe localized friendly form of the resource type related to this action/operation – it should match the public documentation for the resource provider. \r\nIt should use Title Casing – for examples, please refer to the “name” section."
              returned: always
              type: str
              sample: null
            operation:
              description:
                - "Gets or sets Operation\r\nThe localized friendly name for the operation, as it should be shown to the user. \r\nIt should be concise (to fit in drop downs) but clear (i.e. self-documenting). It should use Title Casing and include the entity/resource to which it applies."
              returned: always
              type: str
              sample: null
            description:
              description:
                - "Gets or sets Description\r\nThe localized friendly description for the operation, as it should be shown to the user. \r\nIt should be thorough, yet concise – it will be used in tool tips and detailed views."
              returned: always
              type: str
              sample: null
        origin:
          description:
            - "Gets or sets Origin\r\nThe intended executor of the operation; governs the display of the operation in the RBAC UX and the audit logs UX.\r\nDefault value is “user,system”"
          returned: always
          type: str
          sample: null
        properties:
          description:
            - "Gets or sets Properties\r\nReserved for future use"
          returned: always
          type: any
          sample: null
    next_link:
      description:
        - The NextLink.
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
    from azure.mgmt.stor import StorSimpleManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAvailableProviderOperationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )


        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2016-10-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMAvailableProviderOperationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimpleManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2016-10-01')

        else:
            self.results['available_provider_operations'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.available_provider_operations.list()
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
    AzureRMAvailableProviderOperationInfo()


if __name__ == '__main__':
    main()
