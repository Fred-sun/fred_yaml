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
module: azure_rm_recommendationmetadata
version_added: '2.9'
short_description: Manage Azure RecommendationMetadata instance.
description:
  - 'Create, update and delete instance of Azure RecommendationMetadata.'
options:
  name:
    description:
      - Name of metadata entity.
    required: true
    type: str
  state:
    description:
      - Assert the state of the RecommendationMetadata.
      - >-
        Use C(present) to create or update an RecommendationMetadata and
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
'''

RETURN = '''
id:
  description:
    - The resource Id of the metadata entity.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the metadata entity.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the metadata entity.
  returned: always
  type: str
  sample: null
display_name:
  description:
    - The display name.
  returned: always
  type: str
  sample: null
depends_on:
  description:
    - The list of keys on which this entity depends on.
  returned: always
  type: list
  sample: null
applicable_scenarios:
  description:
    - The list of scenarios applicable to this metadata entity.
  returned: always
  type: list
  sample: null
supported_values:
  description:
    - The list of supported values.
  returned: always
  type: list
  sample: null
  contains:
    id:
      description:
        - The id.
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - The display name.
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


class AzureRMRecommendationMetadata(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            name=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRecommendationMetadata, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.recommendation_metadata.create()
            else:
                response = self.mgmt_client.recommendation_metadata.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the RecommendationMetadata instance.')
            self.fail('Error creating the RecommendationMetadata instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.recommendation_metadata.delete()
        except CloudError as e:
            self.log('Error attempting to delete the RecommendationMetadata instance.')
            self.fail('Error deleting the RecommendationMetadata instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.recommendation_metadata.get(name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRecommendationMetadata()


if __name__ == '__main__':
    main()
