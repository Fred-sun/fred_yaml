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
module: azure_rm_suppression
version_added: '2.9'
short_description: Manage Azure Suppression instance.
description:
  - 'Create, update and delete instance of Azure Suppression.'
options:
  resource_uri:
    description:
      - >-
        The fully qualified Azure Resource Manager identifier of the resource to
        which the recommendation applies.
    required: true
    type: str
  recommendation_id:
    description:
      - The recommendation ID.
    required: true
    type: str
  name:
    description:
      - The name of the suppression.
    required: true
    type: str
  suppression_id:
    description:
      - The GUID of the suppression.
    type: str
  ttl:
    description:
      - The duration for which the suppression is valid.
    type: str
  state:
    description:
      - Assert the state of the Suppression.
      - >-
        Use C(present) to create or update an Suppression and C(absent) to
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
    - name: CreateSuppression
      azure_rm_suppression: 
        name: suppressionName1
        recommendation_id: recommendationId
        resource_uri: resourceUri
        

    - name: DeleteSuppression
      azure_rm_suppression: 
        name: suppressionName1
        recommendation_id: recommendationId
        resource_uri: resourceUri
        

'''

RETURN = '''
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
suppression_id:
  description:
    - The GUID of the suppression.
  returned: always
  type: str
  sample: null
ttl:
  description:
    - The duration for which the suppression is valid.
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
    from azure.mgmt.advisor import AdvisorManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSuppression(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_uri=dict(
                type='str',
                required=True
            ),
            recommendation_id=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            suppression_id=dict(
                type='str',
                disposition='/suppression_id'
            ),
            ttl=dict(
                type='str',
                disposition='/ttl'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_uri = None
        self.recommendation_id = None
        self.name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSuppression, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(AdvisorManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.suppressions.create(resource_uri=self.resource_uri,
                                                                recommendation_id=self.recommendation_id,
                                                                name=self.name,
                                                                suppression_contract=self.body)
            else:
                response = self.mgmt_client.suppressions.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Suppression instance.')
            self.fail('Error creating the Suppression instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.suppressions.delete(resource_uri=self.resource_uri,
                                                            recommendation_id=self.recommendation_id,
                                                            name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the Suppression instance.')
            self.fail('Error deleting the Suppression instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.suppressions.get(resource_uri=self.resource_uri,
                                                         recommendation_id=self.recommendation_id,
                                                         name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSuppression()


if __name__ == '__main__':
    main()
