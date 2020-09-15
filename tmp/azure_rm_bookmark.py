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
module: azure_rm_bookmark
version_added: '2.9'
short_description: Manage Azure Bookmark instance.
description:
  - 'Create, update and delete instance of Azure Bookmark.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group within the user's subscription. The name
        is case insensitive.
    required: true
    type: str
  workspace_name:
    description:
      - The name of the workspace.
    required: true
    type: str
  bookmark_id:
    description:
      - Bookmark ID
    required: true
    type: str
  etag:
    description:
      - Etag of the azure resource
    type: str
  created:
    description:
      - The time the bookmark was created
    type: str
  display_name:
    description:
      - The display name of the bookmark
    type: str
  labels:
    description:
      - List of labels relevant to this bookmark
    type: list
  notes:
    description:
      - The notes of the bookmark
    type: str
  query:
    description:
      - The query of the bookmark.
    type: str
  query_result:
    description:
      - The query result of the bookmark.
    type: str
  updated:
    description:
      - The last time the bookmark was updated
    type: str
  incident_info:
    description:
      - Describes an incident that relates to bookmark
    type: dict
    suboptions:
      incident_id:
        description:
          - Incident Id
        required: true
        type: str
      severity:
        description:
          - The severity of the incident
        required: true
        type: str
        choices:
          - Critical
          - High
          - Medium
          - Low
          - Informational
      title:
        description:
          - The title of the incident
        required: true
        type: str
      relation_name:
        description:
          - Relation Name
        required: true
        type: str
  object_id:
    description:
      - The object id of the user.
    type: uuid
  user_info_object_id:
    description:
      - The object id of the user.
    type: uuid
  state:
    description:
      - Assert the state of the Bookmark.
      - >-
        Use C(present) to create or update an Bookmark and C(absent) to delete
        it.
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
    - name: Creates or updates a bookmark.
      azure_rm_bookmark: 
        bookmark_id: 73e01a99-5cd7-4139-a149-9f2736ff2ab5
        resource_group_name: myRg
        workspace_name: myWorkspace
        etag: '"0300bf09-0000-0000-0000-5c37296e0000"'
        properties:
          created: '2019-01-01T13:15:30Z'
          created_by:
            object_id: 2046feea-040d-4a46-9e2b-91c2941bfa70
          display_name: My bookmark
          labels:
            - Tag1
            - Tag2
          notes: Found a suspicious activity
          query: SecurityEvent | where TimeGenerated > ago(1d) and TimeGenerated < ago(2d)
          query_result: Security Event query result
          updated: '2019-01-01T13:15:30Z'
          updated_by:
            object_id: 2046feea-040d-4a46-9e2b-91c2941bfa70
        

    - name: Delete a bookmark.
      azure_rm_bookmark: 
        bookmark_id: 73e01a99-5cd7-4139-a149-9f2736ff2ab5
        resource_group_name: myRg
        workspace_name: myWorkspace
        

'''

RETURN = '''
id:
  description:
    - Azure resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Azure resource name
  returned: always
  type: str
  sample: null
type:
  description:
    - Azure resource type
  returned: always
  type: str
  sample: null
etag:
  description:
    - Etag of the azure resource
  returned: always
  type: str
  sample: null
created:
  description:
    - The time the bookmark was created
  returned: always
  type: str
  sample: null
display_name:
  description:
    - The display name of the bookmark
  returned: always
  type: str
  sample: null
labels:
  description:
    - List of labels relevant to this bookmark
  returned: always
  type: list
  sample: null
notes:
  description:
    - The notes of the bookmark
  returned: always
  type: str
  sample: null
query:
  description:
    - The query of the bookmark.
  returned: always
  type: str
  sample: null
query_result:
  description:
    - The query result of the bookmark.
  returned: always
  type: str
  sample: null
updated:
  description:
    - The last time the bookmark was updated
  returned: always
  type: str
  sample: null
incident_info:
  description:
    - Describes an incident that relates to bookmark
  returned: always
  type: dict
  sample: null
  contains:
    incident_id:
      description:
        - Incident Id
      returned: always
      type: str
      sample: null
    severity:
      description:
        - The severity of the incident
      returned: always
      type: str
      sample: null
    title:
      description:
        - The title of the incident
      returned: always
      type: str
      sample: null
    relation_name:
      description:
        - Relation Name
      returned: always
      type: str
      sample: null
email_properties_updated_by_email:
  description:
    - The email of the user.
  returned: always
  type: str
  sample: null
name_properties_updated_by_name:
  description:
    - The name of the user.
  returned: always
  type: str
  sample: null
object_id_properties_updated_by_object_id:
  description:
    - The object id of the user.
  returned: always
  type: uuid
  sample: null
email_properties_created_by_email:
  description:
    - The email of the user.
  returned: always
  type: str
  sample: null
name_properties_created_by_name:
  description:
    - The name of the user.
  returned: always
  type: str
  sample: null
object_id_properties_created_by_object_id:
  description:
    - The object id of the user.
  returned: always
  type: uuid
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.security import Security Insights
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMBookmark(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            workspace_name=dict(
                type='str',
                required=True
            ),
            bookmark_id=dict(
                type='str',
                required=True
            ),
            etag=dict(
                type='str',
                disposition='/etag'
            ),
            created=dict(
                type='str',
                disposition='/created'
            ),
            display_name=dict(
                type='str',
                disposition='/display_name'
            ),
            labels=dict(
                type='list',
                disposition='/labels',
                elements='str'
            ),
            notes=dict(
                type='str',
                disposition='/notes'
            ),
            query=dict(
                type='str',
                disposition='/query'
            ),
            query_result=dict(
                type='str',
                disposition='/query_result'
            ),
            updated=dict(
                type='str',
                disposition='/updated'
            ),
            incident_info=dict(
                type='dict',
                disposition='/incident_info',
                options=dict(
                    incident_id=dict(
                        type='str',
                        disposition='incident_id',
                        required=True
                    ),
                    severity=dict(
                        type='str',
                        disposition='severity',
                        choices=['Critical',
                                 'High',
                                 'Medium',
                                 'Low',
                                 'Informational'],
                        required=True
                    ),
                    title=dict(
                        type='str',
                        disposition='title',
                        required=True
                    ),
                    relation_name=dict(
                        type='str',
                        disposition='relation_name',
                        required=True
                    )
                )
            ),
            object_id=dict(
                type='uuid',
                disposition='/object_id'
            ),
            user_info_object_id=dict(
                type='uuid',
                disposition='/user_info_object_id'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.workspace_name = None
        self.bookmark_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMBookmark, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Security Insights,
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
            response = self.mgmt_client.bookmarks.create_or_update(resource_group_name=self.resource_group_name,
                                                                   workspace_name=self.workspace_name,
                                                                   bookmark_id=self.bookmark_id,
                                                                   bookmark=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Bookmark instance.')
            self.fail('Error creating the Bookmark instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.bookmarks.delete(resource_group_name=self.resource_group_name,
                                                         workspace_name=self.workspace_name,
                                                         bookmark_id=self.bookmark_id)
        except CloudError as e:
            self.log('Error attempting to delete the Bookmark instance.')
            self.fail('Error deleting the Bookmark instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.bookmarks.get(resource_group_name=self.resource_group_name,
                                                      workspace_name=self.workspace_name,
                                                      bookmark_id=self.bookmark_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMBookmark()


if __name__ == '__main__':
    main()
