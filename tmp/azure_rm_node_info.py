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
module: azure_rm_node_info
version_added: '2.9'
short_description: Get Node info.
description:
  - Get info of Node.
options:
  device_name:
    description:
      - The device name.
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: NodesGetAllInDevice
      azure_rm_node_info: 
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        

'''

RETURN = '''
nodes:
  description: >-
    A list of dict results where the key is the name of the Node and the values
    are the facts for that Node.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of Nodes.
      returned: always
      type: list
      sample: null
      contains:
        node_status:
          description:
            - The current status of the individual node
          returned: always
          type: str
          sample: null
        node_chassis_serial_number:
          description:
            - Serial number of the Chassis
          returned: always
          type: str
          sample: null
        node_serial_number:
          description:
            - Serial number of the individual node
          returned: always
          type: str
          sample: null
        node_display_name:
          description:
            - Display Name of the individual node
          returned: always
          type: str
          sample: null
        node_friendly_software_version:
          description:
            - >-
              Friendly software version name that is currently installed on the
              node
          returned: always
          type: str
          sample: null
        node_hcs_version:
          description:
            - HCS version that is currently installed on the node
          returned: always
          type: str
          sample: null
        node_instance_id:
          description:
            - Guid instance id of the node
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
    from azure.mgmt.data import DataBoxEdgeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMNodeInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            )
        )

        self.device_name = None
        self.resource_group_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-08-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMNodeInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DataBoxEdgeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-08-01')

        if (self.device_name is not None and
            self.resource_group_name is not None):
            self.results['nodes'] = self.format_item(self.listbydataboxedgedevice())
        return self.results

    def listbydataboxedgedevice(self):
        response = None

        try:
            response = self.mgmt_client.nodes.list_by_data_box_edge_device(device_name=self.device_name,
                                                                           resource_group_name=self.resource_group_name)
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
    AzureRMNodeInfo()


if __name__ == '__main__':
    main()
