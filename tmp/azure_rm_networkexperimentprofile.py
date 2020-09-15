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
module: azure_rm_networkexperimentprofile
version_added: '2.9'
short_description: Manage Azure NetworkExperimentProfile instance.
description:
  - 'Create, update and delete instance of Azure NetworkExperimentProfile.'
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  profile_name:
    description:
      - The Profile identifier associated with the Tenant and Partner
    required: true
    type: str
  location:
    description:
      - Resource location.
    type: str
  etag:
    description:
      - >-
        Gets a unique read-only string that changes whenever the resource is
        updated.
    type: str
  enabled_state:
    description:
      - The state of the Experiment
      - The enabled state of the Profile
    type: str
    choices:
      - Enabled
      - Disabled
  state:
    description:
      - Assert the state of the NetworkExperimentProfile.
      - >-
        Use C(present) to create or update an NetworkExperimentProfile and
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
    - name: Creates an NetworkExperiment Profile in a Resource Group
      azure_rm_networkexperimentprofile: 
        profile_name: MyProfile
        resource_group_name: MyResourceGroup
        location: WestUs
        properties:
          enabled_state: Enabled
        

    - name: Updates an Experiment
      azure_rm_networkexperimentprofile: 
        profile_name: MyProfile
        resource_group_name: MyResourceGroup
        properties:
          enabled_state: Enabled
        tags:
          key1: value1
          key2: value2
        

    - name: Deletes an NetworkExperiment Profile by ProfileName
      azure_rm_networkexperimentprofile: 
        profile_name: MyProfile
        resource_group_name: MyResourceGroup
        

'''

RETURN = '''
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
    - Resource location.
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
etag:
  description:
    - >-
      Gets a unique read-only string that changes whenever the resource is
      updated.
  returned: always
  type: str
  sample: null
resource_state:
  description:
    - Resource status.
  returned: always
  type: str
  sample: null
enabled_state:
  description:
    - The state of the Experiment
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
    from azure.mgmt.front import FrontDoorManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMNetworkExperimentProfile(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            profile_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            etag=dict(
                type='str',
                disposition='/etag'
            ),
            enabled_state=dict(
                type='str',
                disposition='/enabled_state',
                choices=['Enabled',
                         'Disabled']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.profile_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMNetworkExperimentProfile, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(FrontDoorManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-11-01')

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
            response = self.mgmt_client.network_experiment_profiles.create_or_update(profile_name=self.profile_name,
                                                                                     resource_group_name=self.resource_group_name,
                                                                                     parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the NetworkExperimentProfile instance.')
            self.fail('Error creating the NetworkExperimentProfile instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.network_experiment_profiles.delete(resource_group_name=self.resource_group_name,
                                                                           profile_name=self.profile_name)
        except CloudError as e:
            self.log('Error attempting to delete the NetworkExperimentProfile instance.')
            self.fail('Error deleting the NetworkExperimentProfile instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.network_experiment_profiles.get(resource_group_name=self.resource_group_name,
                                                                        profile_name=self.profile_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMNetworkExperimentProfile()


if __name__ == '__main__':
    main()
