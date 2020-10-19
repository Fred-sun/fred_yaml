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
module: azure_rm_bookmark_info
version_added: '2.9'
short_description: Get Bookmark info.
description:
  - Get info of Bookmark.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get all bookmarks.
      azure_rm_bookmark_info: 
        resource_group_name: myRg
        workspace_name: myWorkspace
        

    - name: Get a bookmark.
      azure_rm_bookmark_info: 
        bookmark_id: 73e01a99-5cd7-4139-a149-9f2736ff2ab5
        resource_group_name: myRg
        workspace_name: myWorkspace
        

'''

RETURN = '''
bookmarks:
  description: >-
    A list of dict results where the key is the name of the Bookmark and the
    values are the facts for that Bookmark.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - URL to fetch the next set of cases.
      returned: always
      type: str
      sample: null
    value:
      description:
        - Array of bookmarks.
      returned: always
      type: list
      sample: null
      contains:
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.security import Security Insights
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMBookmarkInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.workspace_name = None
        self.bookmark_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMBookmarkInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Security Insights,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01')

        if (self.resource_group_name is not None and
            self.workspace_name is not None and
            self.bookmark_id is not None):
            self.results['bookmarks'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.workspace_name is not None):
            self.results['bookmarks'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.bookmarks.get(resource_group_name=self.resource_group_name,
                                                      workspace_name=self.workspace_name,
                                                      bookmark_id=self.bookmark_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.bookmarks.list(resource_group_name=self.resource_group_name,
                                                       workspace_name=self.workspace_name)
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
    AzureRMBookmarkInfo()


if __name__ == '__main__':
    main()
