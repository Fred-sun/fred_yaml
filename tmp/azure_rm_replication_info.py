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
module: azure_rm_replication_info
version_added: '2.9'
short_description: Get Replication info.
description:
  - Get info of Replication.
options:
  resource_group_name:
    description:
      - The name of the resource group to which the container registry belongs.
    required: true
    type: str
  registry_name:
    description:
      - The name of the container registry.
    required: true
    type: str
  replication_name:
    description:
      - The name of the replication.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ReplicationGet
      azure_rm_replication_info: 
        registry_name: myRegistry
        replication_name: myReplication
        resource_group_name: myResourceGroup
        

    - name: ReplicationList
      azure_rm_replication_info: 
        registry_name: myRegistry
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
replications:
  description: >-
    A list of dict results where the key is the name of the Replication and the
    values are the facts for that Replication.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of the resource.
      returned: always
      type: str
      sample: null
    location:
      description:
        - >-
          The location of the resource. This cannot be changed after the
          resource is created.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - The tags of the resource.
      returned: always
      type: dictionary
      sample: null
    provisioning_state:
      description:
        - >-
          The provisioning state of the replication at the time the operation
          was called.
      returned: always
      type: str
      sample: null
    status:
      description:
        - The status of the replication at the time the operation was called.
      returned: always
      type: dict
      sample: null
      contains:
        display_status:
          description:
            - The short label for the status.
          returned: always
          type: str
          sample: null
        message:
          description:
            - >-
              The detailed message for the status, including alerts and error
              messages.
          returned: always
          type: str
          sample: null
        timestamp:
          description:
            - The timestamp when the status was changed to the current value.
          returned: always
          type: str
          sample: null
    region_endpoint_enabled:
      description:
        - >-
          Specifies whether the replication's regional endpoint is enabled.
          Requests will not be routed to a replication whose regional endpoint
          is disabled, however its data will continue to be synced with other
          replications.
      returned: always
      type: bool
      sample: null
    value:
      description:
        - >-
          The list of replications. Since this list may be incomplete, the
          nextLink field should be used to request the next list of
          replications.
      returned: always
      type: list
      sample: null
      contains:
        provisioning_state:
          description:
            - >-
              The provisioning state of the replication at the time the
              operation was called.
          returned: always
          type: str
          sample: null
        status:
          description:
            - >-
              The status of the replication at the time the operation was
              called.
          returned: always
          type: dict
          sample: null
          contains:
            display_status:
              description:
                - The short label for the status.
              returned: always
              type: str
              sample: null
            message:
              description:
                - >-
                  The detailed message for the status, including alerts and
                  error messages.
              returned: always
              type: str
              sample: null
            timestamp:
              description:
                - >-
                  The timestamp when the status was changed to the current
                  value.
              returned: always
              type: str
              sample: null
        region_endpoint_enabled:
          description:
            - >-
              Specifies whether the replication's regional endpoint is enabled.
              Requests will not be routed to a replication whose regional
              endpoint is disabled, however its data will continue to be synced
              with other replications.
          returned: always
          type: bool
          sample: null
    next_link:
      description:
        - The URI that can be used to request the next list of replications.
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
    from azure.mgmt.container import ContainerRegistryManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMReplicationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            registry_name=dict(
                type='str',
                required=True
            ),
            replication_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.registry_name = None
        self.replication_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-12-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMReplicationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ContainerRegistryManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-01-preview')

        if (self.resource_group_name is not None and
            self.registry_name is not None and
            self.replication_name is not None):
            self.results['replications'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.registry_name is not None):
            self.results['replications'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.replications.get(resource_group_name=self.resource_group_name,
                                                         registry_name=self.registry_name,
                                                         replication_name=self.replication_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.replications.list(resource_group_name=self.resource_group_name,
                                                          registry_name=self.registry_name)
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
    AzureRMReplicationInfo()


if __name__ == '__main__':
    main()
