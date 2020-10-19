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
module: azure_rm_storagetarget_info
version_added: '2.9'
short_description: Get StorageTarget info.
description:
  - Get info of StorageTarget.
options:
  resource_group_name:
    description:
      - Target resource group.
    required: true
    type: str
  cache_name:
    description:
      - >-
        Name of Cache. Length of name must be not greater than 80 and chars must
        be in list of [-0-9a-zA-Z_] char class.
    required: true
    type: str
  storage_target_name:
    description:
      - >-
        Name of the Storage Target. Length of name must be not greater than 80
        and chars must be in list of [-0-9a-zA-Z_] char class.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: StorageTargets_List
      azure_rm_storagetarget_info: 
        cache_name: sc1
        resource_group_name: scgroup
        

    - name: StorageTargets_Get
      azure_rm_storagetarget_info: 
        cache_name: sc1
        resource_group_name: scgroup
        storage_target_name: st1
        

'''

RETURN = '''
storage_targets:
  description: >-
    A list of dict results where the key is the name of the StorageTarget and
    the values are the facts for that StorageTarget.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - The URI to fetch the next page of Storage Targets.
      returned: always
      type: str
      sample: null
    value:
      description:
        - The list of Storage Targets defined for the Cache.
      returned: always
      type: list
      sample: null
      contains:
        junctions:
          description:
            - >-
              List of Cache namespace junctions to target for namespace
              associations.
          returned: always
          type: list
          sample: null
          contains:
            namespace_path:
              description:
                - Namespace path on a Cache for a Storage Target.
              returned: always
              type: str
              sample: null
            target_path:
              description:
                - Path in Storage Target to which namespacePath points.
              returned: always
              type: str
              sample: null
            nfs_export:
              description:
                - NFS export where targetPath exists.
              returned: always
              type: str
              sample: null
        target_type:
          description:
            - Type of the Storage Target.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - >-
              ARM provisioning state, see
              https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property
          returned: always
          type: str
          sample: null
        nfs3:
          description:
            - Properties when targetType is nfs3.
          returned: always
          type: dict
          sample: null
          contains:
            target:
              description:
                - 'IP address or host name of an NFSv3 host (e.g., 10.0.44.44).'
              returned: always
              type: str
              sample: null
            usage_model:
              description:
                - >-
                  Identifies the primary usage model to be used for this Storage
                  Target. Get choices from .../usageModels
              returned: always
              type: str
              sample: null
        clfs:
          description:
            - Properties when targetType is clfs.
          returned: always
          type: dict
          sample: null
          contains:
            target:
              description:
                - Resource ID of storage container.
              returned: always
              type: str
              sample: null
        unknown:
          description:
            - Properties when targetType is unknown.
          returned: always
          type: dict
          sample: null
          contains:
            unknown_map:
              description:
                - >-
                  Dictionary of string->string pairs containing information
                  about the Storage Target.
              returned: always
              type: dictionary
              sample: null
    name:
      description:
        - Name of the Storage Target.
      returned: always
      type: str
      sample: null
    id:
      description:
        - Resource ID of the Storage Target.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Type of the Storage Target; Microsoft.StorageCache/Cache/StorageTarget
      returned: always
      type: str
      sample: null
    junctions:
      description:
        - >-
          List of Cache namespace junctions to target for namespace
          associations.
      returned: always
      type: list
      sample: null
      contains:
        namespace_path:
          description:
            - Namespace path on a Cache for a Storage Target.
          returned: always
          type: str
          sample: null
        target_path:
          description:
            - Path in Storage Target to which namespacePath points.
          returned: always
          type: str
          sample: null
        nfs_export:
          description:
            - NFS export where targetPath exists.
          returned: always
          type: str
          sample: null
    target_type:
      description:
        - Type of the Storage Target.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - >-
          ARM provisioning state, see
          https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property
      returned: always
      type: str
      sample: null
    nfs3:
      description:
        - Properties when targetType is nfs3.
      returned: always
      type: dict
      sample: null
      contains:
        target:
          description:
            - 'IP address or host name of an NFSv3 host (e.g., 10.0.44.44).'
          returned: always
          type: str
          sample: null
        usage_model:
          description:
            - >-
              Identifies the primary usage model to be used for this Storage
              Target. Get choices from .../usageModels
          returned: always
          type: str
          sample: null
    clfs:
      description:
        - Properties when targetType is clfs.
      returned: always
      type: dict
      sample: null
      contains:
        target:
          description:
            - Resource ID of storage container.
          returned: always
          type: str
          sample: null
    unknown:
      description:
        - Properties when targetType is unknown.
      returned: always
      type: dict
      sample: null
      contains:
        unknown_map:
          description:
            - >-
              Dictionary of string->string pairs containing information about
              the Storage Target.
          returned: always
          type: dictionary
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.storage import StorageCacheManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMStorageTargetInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            cache_name=dict(
                type='str',
                required=True
            ),
            storage_target_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.cache_name = None
        self.storage_target_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-03-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMStorageTargetInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageCacheManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01')

        if (self.resource_group_name is not None and
            self.cache_name is not None and
            self.storage_target_name is not None):
            self.results['storage_targets'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.cache_name is not None):
            self.results['storage_targets'] = self.format_item(self.listbycache())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.storage_targets.get(resource_group_name=self.resource_group_name,
                                                            cache_name=self.cache_name,
                                                            storage_target_name=self.storage_target_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbycache(self):
        response = None

        try:
            response = self.mgmt_client.storage_targets.list_by_cache(resource_group_name=self.resource_group_name,
                                                                      cache_name=self.cache_name)
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
    AzureRMStorageTargetInfo()


if __name__ == '__main__':
    main()
