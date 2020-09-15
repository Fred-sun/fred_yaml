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
module: azure_rm_incidentcomment_info
version_added: '2.9'
short_description: Get IncidentComment info.
description:
  - Get info of IncidentComment.
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
  incident_id:
    description:
      - Incident ID
    required: true
    type: str
  filter:
    description:
      - 'Filters the results, based on a Boolean condition. Optional.'
    type: str
  orderby:
    description:
      - Sorts the results. Optional.
    type: str
  top:
    description:
      - Returns only the first n results. Optional.
    type: integer
  skip_token:
    description:
      - >-
        Skiptoken is only used if a previous operation returned a partial
        result. If a previous response contains a nextLink element, the value of
        the nextLink element will include a skiptoken parameter that specifies a
        starting point to use for subsequent calls. Optional.
    type: str
  incident_comment_id:
    description:
      - Incident comment ID
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get all incident comments.
      azure_rm_incidentcomment_info: 
        incident_id: 73e01a99-5cd7-4139-a149-9f2736ff2ab5
        resource_group_name: myRg
        workspace_name: myWorkspace
        

    - name: Get an incident comment.
      azure_rm_incidentcomment_info: 
        incident_comment_id: 4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014
        incident_id: 73e01a99-5cd7-4139-a149-9f2736ff2ab5
        resource_group_name: myRg
        workspace_name: myWorkspace
        

'''

RETURN = '''
incident_comments:
  description: >-
    A list of dict results where the key is the name of the IncidentComment and
    the values are the facts for that IncidentComment.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - URL to fetch the next set of comments.
      returned: always
      type: str
      sample: null
    value:
      description:
        - Array of comments.
      returned: always
      type: list
      sample: null
      contains:
        created_time_utc:
          description:
            - The time the comment was created
          returned: always
          type: str
          sample: null
        message:
          description:
            - The comment message
          returned: always
          type: str
          sample: null
        author:
          description:
            - Describes the client that created the comment
          returned: always
          type: dict
          sample: null
          contains:
            email:
              description:
                - The email of the client.
              returned: always
              type: str
              sample: null
            name:
              description:
                - The name of the client.
              returned: always
              type: str
              sample: null
            object_id:
              description:
                - The object id of the client.
              returned: always
              type: uuid
              sample: null
            user_principal_name:
              description:
                - The user principal name of the client.
              returned: always
              type: str
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
    created_time_utc:
      description:
        - The time the comment was created
      returned: always
      type: str
      sample: null
    message:
      description:
        - The comment message
      returned: always
      type: str
      sample: null
    author:
      description:
        - Describes the client that created the comment
      returned: always
      type: dict
      sample: null
      contains:
        email:
          description:
            - The email of the client.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name of the client.
          returned: always
          type: str
          sample: null
        object_id:
          description:
            - The object id of the client.
          returned: always
          type: uuid
          sample: null
        user_principal_name:
          description:
            - The user principal name of the client.
          returned: always
          type: str
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


class AzureRMIncidentCommentInfo(AzureRMModuleBase):
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
            incident_id=dict(
                type='str',
                required=True
            ),
            filter=dict(
                type='str'
            ),
            orderby=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            skip_token=dict(
                type='str'
            ),
            incident_comment_id=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.workspace_name = None
        self.incident_id = None
        self.filter = None
        self.orderby = None
        self.top = None
        self.skip_token = None
        self.incident_comment_id = None

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
        super(AzureRMIncidentCommentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Security Insights,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01')

        if (self.resource_group_name is not None and
            self.workspace_name is not None and
            self.incident_id is not None and
            self.incident_comment_id is not None):
            self.results['incident_comments'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.workspace_name is not None and
              self.incident_id is not None):
            self.results['incident_comments'] = self.format_item(self.listbyincident())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.incident_comments.get(resource_group_name=self.resource_group_name,
                                                              workspace_name=self.workspace_name,
                                                              incident_id=self.incident_id,
                                                              incident_comment_id=self.incident_comment_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyincident(self):
        response = None

        try:
            response = self.mgmt_client.incident_comments.list_by_incident(resource_group_name=self.resource_group_name,
                                                                           workspace_name=self.workspace_name,
                                                                           incident_id=self.incident_id,
                                                                           filter=self.filter,
                                                                           orderby=self.orderby,
                                                                           top=self.top,
                                                                           skip_token=self.skip_token)
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
    AzureRMIncidentCommentInfo()


if __name__ == '__main__':
    main()
