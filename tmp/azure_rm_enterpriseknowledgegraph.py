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
module: azure_rm_enterpriseknowledgegraph
version_added: '2.9'
short_description: Manage Azure EnterpriseKnowledgeGraph instance.
description:
  - 'Create, update and delete instance of Azure EnterpriseKnowledgeGraph.'
options:
  resource_group_name:
    description:
      - >-
        The name of the EnterpriseKnowledgeGraph resource group in the user
        subscription.
    required: true
    type: str
  resource_name:
    description:
      - The name of the EnterpriseKnowledgeGraph resource.
    required: true
    type: str
  location:
    description:
      - Specifies the location of the resource.
    type: str
  name:
    description:
      - The sku name
    type: str
    choices:
      - F0
      - S1
  description:
    description:
      - The description of the EnterpriseKnowledgeGraph
    type: str
  metadata:
    description:
      - Specifies the metadata  of the resource.
    type: any
  provisioning_state:
    description:
      - The state of EnterpriseKnowledgeGraph provisioning
    type: str
    choices:
      - Creating
      - Deleting
      - Failed
      - Succeeded
  state:
    description:
      - Assert the state of the EnterpriseKnowledgeGraph.
      - >-
        Use C(present) to create or update an EnterpriseKnowledgeGraph and
        C(absent) to delete it.
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
    - name: Create EnterpriseKnowledgeGraph
      azure_rm_enterpriseknowledgegraph: 
        resource_group_name: OneResourceGroupName
        resource_name: sampleekgname
        location: West US
        properties: {}
        tags:
          tag1: value1
          tag2: value2
        

    - name: Update EnterpriseKnowledgeGraph
      azure_rm_enterpriseknowledgegraph: 
        resource_group_name: OneResourceGroupName
        resource_name: sampleekgname
        location: West US
        properties: {}
        sku:
          name: S1
        tags:
          tag1: value1
          tag2: value2
        

    - name: Delete EnterpriseKnowledgeGraph
      azure_rm_enterpriseknowledgegraph: 
        resource_group_name: OneResourceGroupName
        resource_name: sampleekgname
        

'''

RETURN = '''
id:
  description:
    - Specifies the resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Specifies the name of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - Specifies the type of the resource.
  returned: always
  type: str
  sample: null
location:
  description:
    - Specifies the location of the resource.
  returned: always
  type: str
  sample: null
tags:
  description:
    - Contains resource tags defined as key/value pairs.
  returned: always
  type: dictionary
  sample: null
name_sku_name:
  description:
    - The sku name
  returned: always
  type: str
  sample: null
description:
  description:
    - The description of the EnterpriseKnowledgeGraph
  returned: always
  type: str
  sample: null
metadata:
  description:
    - Specifies the metadata  of the resource.
  returned: always
  type: any
  sample: null
provisioning_state:
  description:
    - The state of EnterpriseKnowledgeGraph provisioning
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
    from azure.mgmt.azure import Azure Enterprise Knowledge Graph Service
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMEnterpriseKnowledgeGraph(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            resource_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            name=dict(
                type='str',
                disposition='/name',
                choices=['F0',
                         'S1']
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            metadata=dict(
                type='any',
                disposition='/metadata'
            ),
            provisioning_state=dict(
                type='str',
                disposition='/provisioning_state',
                choices=['Creating',
                         'Deleting',
                         'Failed',
                         'Succeeded']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMEnterpriseKnowledgeGraph, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Azure Enterprise Knowledge Graph Service,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-12-03')

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
                response = self.mgmt_client.enterprise_knowledge_graph.create(resource_group_name=self.resource_group_name,
                                                                              resource_name=self.resource_name,
                                                                              parameters=self.body)
            else:
                response = self.mgmt_client.enterprise_knowledge_graph.update(resource_group_name=self.resource_group_name,
                                                                              resource_name=self.resource_name,
                                                                              parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the EnterpriseKnowledgeGraph instance.')
            self.fail('Error creating the EnterpriseKnowledgeGraph instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.enterprise_knowledge_graph.delete(resource_group_name=self.resource_group_name,
                                                                          resource_name=self.resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the EnterpriseKnowledgeGraph instance.')
            self.fail('Error deleting the EnterpriseKnowledgeGraph instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.enterprise_knowledge_graph.get(resource_group_name=self.resource_group_name,
                                                                       resource_name=self.resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMEnterpriseKnowledgeGraph()


if __name__ == '__main__':
    main()
