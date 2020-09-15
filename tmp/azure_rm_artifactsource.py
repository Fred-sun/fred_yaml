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
module: azure_rm_artifactsource
version_added: '2.9'
short_description: Manage Azure ArtifactSource instance.
description:
  - 'Create, update and delete instance of Azure ArtifactSource.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  lab_name:
    description:
      - The name of the lab.
    required: true
    type: str
  name:
    description:
      - The name of the artifact source.
    required: true
    type: str
  expand:
    description:
      - 'Specify the $expand query. Example: ''properties($select=displayName)'''
    type: str
  location:
    description:
      - The location of the resource.
    type: str
  display_name:
    description:
      - The artifact source's display name.
    type: str
  uri:
    description:
      - The artifact source's URI.
    type: str
  source_type:
    description:
      - The artifact source's type.
    type: str
    choices:
      - VsoGit
      - GitHub
  folder_path:
    description:
      - The folder containing artifacts.
    type: str
  arm_template_folder_path:
    description:
      - The folder containing Azure Resource Manager templates.
    type: str
  branch_ref:
    description:
      - The artifact source's branch reference.
    type: str
  security_token:
    description:
      - The security token to authenticate to the artifact source.
    type: str
  status:
    description:
      - 'Indicates if the artifact source is enabled (values: Enabled, Disabled).'
    type: str
    choices:
      - Enabled
      - Disabled
  state:
    description:
      - Assert the state of the ArtifactSource.
      - >-
        Use C(present) to create or update an ArtifactSource and C(absent) to
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
'''

RETURN = '''
id:
  description:
    - The identifier of the resource.
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
    - The location of the resource.
  returned: always
  type: str
  sample: null
tags:
  description:
    - The tags of the resource.
  returned: always
  type: dictionary
  sample: null
display_name:
  description:
    - The artifact source's display name.
  returned: always
  type: str
  sample: null
uri:
  description:
    - The artifact source's URI.
  returned: always
  type: str
  sample: null
source_type:
  description:
    - The artifact source's type.
  returned: always
  type: str
  sample: null
folder_path:
  description:
    - The folder containing artifacts.
  returned: always
  type: str
  sample: null
arm_template_folder_path:
  description:
    - The folder containing Azure Resource Manager templates.
  returned: always
  type: str
  sample: null
branch_ref:
  description:
    - The artifact source's branch reference.
  returned: always
  type: str
  sample: null
security_token:
  description:
    - The security token to authenticate to the artifact source.
  returned: always
  type: str
  sample: null
status:
  description:
    - 'Indicates if the artifact source is enabled (values: Enabled, Disabled).'
  returned: always
  type: str
  sample: null
created_date:
  description:
    - The artifact source's creation date.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning status of the resource.
  returned: always
  type: str
  sample: null
unique_identifier:
  description:
    - The unique immutable identifier of a resource (Guid).
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
    from azure.mgmt.dev import DevTestLabsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMArtifactSource(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            lab_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            display_name=dict(
                type='str',
                disposition='/display_name'
            ),
            uri=dict(
                type='str',
                disposition='/uri'
            ),
            source_type=dict(
                type='str',
                disposition='/source_type',
                choices=['VsoGit',
                         'GitHub']
            ),
            folder_path=dict(
                type='str',
                disposition='/folder_path'
            ),
            arm_template_folder_path=dict(
                type='str',
                disposition='/arm_template_folder_path'
            ),
            branch_ref=dict(
                type='str',
                disposition='/branch_ref'
            ),
            security_token=dict(
                type='str',
                disposition='/security_token'
            ),
            status=dict(
                type='str',
                disposition='/status',
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
        self.lab_name = None
        self.name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMArtifactSource, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DevTestLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-15')

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
            response = self.mgmt_client.artifact_sources.create_or_update(resource_group_name=self.resource_group_name,
                                                                          lab_name=self.lab_name,
                                                                          name=self.name,
                                                                          artifact_source=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ArtifactSource instance.')
            self.fail('Error creating the ArtifactSource instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.artifact_sources.delete(resource_group_name=self.resource_group_name,
                                                                lab_name=self.lab_name,
                                                                name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the ArtifactSource instance.')
            self.fail('Error deleting the ArtifactSource instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.artifact_sources.get(resource_group_name=self.resource_group_name,
                                                             lab_name=self.lab_name,
                                                             name=self.name,
                                                             expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMArtifactSource()


if __name__ == '__main__':
    main()
