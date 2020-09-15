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
module: azure_rm_storagetarget
version_added: '2.9'
short_description: Manage Azure StorageTarget instance.
description:
  - 'Create, update and delete instance of Azure StorageTarget.'
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
      - Name of Storage Target.
      - >-
        Name of the Storage Target. Length of name must be not greater than 80
        and chars must be in list of [-0-9a-zA-Z_] char class.
    required: true
    type: str
  junctions:
    description:
      - List of Cache namespace junctions to target for namespace associations.
    type: list
    suboptions:
      namespace_path:
        description:
          - Namespace path on a Cache for a Storage Target.
        type: str
      target_path:
        description:
          - Path in Storage Target to which namespacePath points.
        type: str
      nfs_export:
        description:
          - NFS export where targetPath exists.
        type: str
  target_type:
    description:
      - Type of the Storage Target.
    type: str
    choices:
      - nfs3
      - clfs
      - unknown
  provisioning_state:
    description:
      - >-
        ARM provisioning state, see
        https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property
    type: str
    choices:
      - Succeeded
      - Failed
      - Cancelled
      - Creating
      - Deleting
      - Updating
  nfs3:
    description:
      - Properties when targetType is nfs3.
    type: dict
    suboptions:
      target:
        description:
          - 'IP address or host name of an NFSv3 host (e.g., 10.0.44.44).'
        type: str
      usage_model:
        description:
          - >-
            Identifies the primary usage model to be used for this Storage
            Target. Get choices from .../usageModels
        type: str
  clfs:
    description:
      - Properties when targetType is clfs.
    type: dict
    suboptions:
      target:
        description:
          - Resource ID of storage container.
        type: str
  unknown:
    description:
      - Properties when targetType is unknown.
    type: dict
    suboptions:
      unknown_map:
        description:
          - >-
            Dictionary of string->string pairs containing information about the
            Storage Target.
        type: dictionary
  state:
    description:
      - Assert the state of the StorageTarget.
      - >-
        Use C(present) to create or update an StorageTarget and C(absent) to
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
    - name: StorageTargets_Delete
      azure_rm_storagetarget: 
        cache_name: sc1
        resource_group_name: scgroup
        storage_target_name: st1
        

    - name: StorageTargets_CreateOrUpdate
      azure_rm_storagetarget: 
        cache_name: sc1
        resource_group_name: scgroup
        storage_target_name: st1
        properties:
          junctions:
            - namespace_path: /path/on/cache
              nfs_export: exp1
              target_path: /path/on/exp1
            - namespace_path: /path2/on/cache
              nfs_export: exp2
              target_path: /path2/on/exp2
          nfs3:
            target: 10.0.44.44
            usage_model: READ_HEAVY_INFREQ
          target_type: nfs3
        

'''

RETURN = '''
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
    - List of Cache namespace junctions to target for namespace associations.
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
          Identifies the primary usage model to be used for this Storage Target.
          Get choices from .../usageModels
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
          Dictionary of string->string pairs containing information about the
          Storage Target.
      returned: always
      type: dictionary
      sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.storage import StorageCacheManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMStorageTarget(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            junctions=dict(
                type='list',
                disposition='/junctions',
                elements='dict',
                options=dict(
                    namespace_path=dict(
                        type='str',
                        disposition='namespace_path'
                    ),
                    target_path=dict(
                        type='str',
                        disposition='target_path'
                    ),
                    nfs_export=dict(
                        type='str',
                        disposition='nfs_export'
                    )
                )
            ),
            target_type=dict(
                type='str',
                disposition='/target_type',
                choices=['nfs3',
                         'clfs',
                         'unknown']
            ),
            provisioning_state=dict(
                type='str',
                disposition='/provisioning_state',
                choices=['Succeeded',
                         'Failed',
                         'Cancelled',
                         'Creating',
                         'Deleting',
                         'Updating']
            ),
            nfs3=dict(
                type='dict',
                disposition='/nfs3',
                options=dict(
                    target=dict(
                        type='str',
                        disposition='target'
                    ),
                    usage_model=dict(
                        type='str',
                        disposition='usage_model'
                    )
                )
            ),
            clfs=dict(
                type='dict',
                disposition='/clfs',
                options=dict(
                    target=dict(
                        type='str',
                        disposition='target'
                    )
                )
            ),
            unknown=dict(
                type='dict',
                disposition='/unknown',
                options=dict(
                    unknown_map=dict(
                        type='dictionary',
                        disposition='unknown_map'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.cache_name = None
        self.storage_target_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMStorageTarget, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(StorageCacheManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01')

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
            response = self.mgmt_client.storage_targets.create_or_update(resource_group_name=self.resource_group_name,
                                                                         cache_name=self.cache_name,
                                                                         storage_target_name=self.storage_target_name,
                                                                         storagetarget=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the StorageTarget instance.')
            self.fail('Error creating the StorageTarget instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.storage_targets.delete(resource_group_name=self.resource_group_name,
                                                               cache_name=self.cache_name,
                                                               storage_target_name=self.storage_target_name)
        except CloudError as e:
            self.log('Error attempting to delete the StorageTarget instance.')
            self.fail('Error deleting the StorageTarget instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.storage_targets.get(resource_group_name=self.resource_group_name,
                                                            cache_name=self.cache_name,
                                                            storage_target_name=self.storage_target_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMStorageTarget()


if __name__ == '__main__':
    main()
