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
module: azure_rm_association
version_added: '2.9'
short_description: Manage Azure Association instance.
description:
  - 'Create, update and delete instance of Azure Association.'
options:
  scope:
    description:
      - >-
        The scope of the association. The scope can be any valid REST resource
        instance. For example, use
        '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/Microsoft.Compute/virtualMachines/{vm-name}'
        for a virtual machine resource.
    required: true
    type: str
  association_name:
    description:
      - The name of the association.
    required: true
    type: str
  target_resource_id:
    description:
      - The REST resource instance of the target resource for this association.
    type: str
  state:
    description:
      - Assert the state of the Association.
      - >-
        Use C(present) to create or update an Association and C(absent) to
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
    - name: Create or update an association
      azure_rm_association: 
        association_name: associationName
        scope: scope
        properties:
          target_resource_id: >-
            /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/appRG/providers/Microsoft.Solutions/applications/applicationName
        

    - name: Delete an association
      azure_rm_association: 
        association_name: associationName
        scope: scope
        

'''

RETURN = '''
id:
  description:
    - The association id.
  returned: always
  type: str
  sample: null
name:
  description:
    - The association name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The association type.
  returned: always
  type: str
  sample: null
target_resource_id:
  description:
    - The REST resource instance of the target resource for this association.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning state of the association.
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
    from azure.mgmt.customproviders import customproviders
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMAssociation(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            scope=dict(
                type='str',
                required=True
            ),
            association_name=dict(
                type='str',
                required=True
            ),
            target_resource_id=dict(
                type='str',
                disposition='/target_resource_id'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.scope = None
        self.association_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAssociation, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(customproviders,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

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
            response = self.mgmt_client.associations.create_or_update(scope=self.scope,
                                                                      association_name=self.association_name,
                                                                      association=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Association instance.')
            self.fail('Error creating the Association instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.associations.delete(scope=self.scope,
                                                            association_name=self.association_name)
        except CloudError as e:
            self.log('Error attempting to delete the Association instance.')
            self.fail('Error deleting the Association instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.associations.get(scope=self.scope,
                                                         association_name=self.association_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAssociation()


if __name__ == '__main__':
    main()
