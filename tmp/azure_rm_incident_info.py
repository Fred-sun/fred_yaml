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
module: azure_rm_incident_info
version_added: '2.9'
short_description: Get Incident info.
description:
  - Get info of Incident.
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
  incident_id:
    description:
      - Incident ID
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get all incidents.
      azure_rm_incident_info: 
        resource_group_name: myRg
        workspace_name: myWorkspace
        

    - name: Get an incident.
      azure_rm_incident_info: 
        incident_id: 73e01a99-5cd7-4139-a149-9f2736ff2ab5
        resource_group_name: myRg
        workspace_name: myWorkspace
        

'''

RETURN = '''
incidents:
  description: >-
    A list of dict results where the key is the name of the Incident and the
    values are the facts for that Incident.
  returned: always
  type: complex
  contains:
    next_link:
      description:
        - URL to fetch the next set of incidents.
      returned: always
      type: str
      sample: null
    value:
      description:
        - Array of incidents.
      returned: always
      type: list
      sample: null
      contains:
        additional_data:
          description:
            - Additional data on the incident
          returned: always
          type: dict
          sample: null
          contains:
            alerts_count:
              description:
                - The number of alerts in the incident
              returned: always
              type: integer
              sample: null
            bookmarks_count:
              description:
                - The number of bookmarks in the incident
              returned: always
              type: integer
              sample: null
            comments_count:
              description:
                - The number of comments in the incident
              returned: always
              type: integer
              sample: null
            alert_product_names:
              description:
                - List of product names of alerts in the incident
              returned: always
              type: list
              sample: null
            tactics:
              description:
                - The tactics associated with incident
              returned: always
              type: list
              sample: null
        classification:
          description:
            - The reason the incident was closed
          returned: always
          type: str
          sample: null
        classification_comment:
          description:
            - Describes the reason the incident was closed
          returned: always
          type: str
          sample: null
        classification_reason:
          description:
            - The classification reason the incident was closed with
          returned: always
          type: str
          sample: null
        created_time_utc:
          description:
            - The time the incident was created
          returned: always
          type: str
          sample: null
        description:
          description:
            - The description of the incident
          returned: always
          type: str
          sample: null
        first_activity_time_utc:
          description:
            - The time of the first activity in the incident
          returned: always
          type: str
          sample: null
        incident_url:
          description:
            - The deep-link url to the incident in Azure portal
          returned: always
          type: str
          sample: null
        incident_number:
          description:
            - A sequential number
          returned: always
          type: integer
          sample: null
        labels:
          description:
            - List of labels relevant to this incident
          returned: always
          type: list
          sample: null
          contains:
            label_name:
              description:
                - The name of the label
              returned: always
              type: str
              sample: null
            label_type:
              description:
                - The type of the label
              returned: always
              type: str
              sample: null
        last_activity_time_utc:
          description:
            - The time of the last activity in the incident
          returned: always
          type: str
          sample: null
        last_modified_time_utc:
          description:
            - The last time the incident was updated
          returned: always
          type: str
          sample: null
        owner:
          description:
            - Describes a user that the incident is assigned to
          returned: always
          type: dict
          sample: null
          contains:
            email:
              description:
                - The email of the user the incident is assigned to.
              returned: always
              type: str
              sample: null
            assigned_to:
              description:
                - The name of the user the incident is assigned to.
              returned: always
              type: str
              sample: null
            object_id:
              description:
                - The object id of the user the incident is assigned to.
              returned: always
              type: uuid
              sample: null
            user_principal_name:
              description:
                - >-
                  The user principal name of the user the incident is assigned
                  to.
              returned: always
              type: str
              sample: null
        related_analytic_rule_ids:
          description:
            - List of resource ids of Analytic rules related to the incident
          returned: always
          type: list
          sample: null
        severity:
          description:
            - The severity of the incident
          returned: always
          type: str
          sample: null
        status:
          description:
            - The status of the incident
          returned: always
          type: str
          sample: null
        title:
          description:
            - The title of the incident
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
    etag:
      description:
        - Etag of the azure resource
      returned: always
      type: str
      sample: null
    additional_data:
      description:
        - Additional data on the incident
      returned: always
      type: dict
      sample: null
      contains:
        alerts_count:
          description:
            - The number of alerts in the incident
          returned: always
          type: integer
          sample: null
        bookmarks_count:
          description:
            - The number of bookmarks in the incident
          returned: always
          type: integer
          sample: null
        comments_count:
          description:
            - The number of comments in the incident
          returned: always
          type: integer
          sample: null
        alert_product_names:
          description:
            - List of product names of alerts in the incident
          returned: always
          type: list
          sample: null
        tactics:
          description:
            - The tactics associated with incident
          returned: always
          type: list
          sample: null
    classification:
      description:
        - The reason the incident was closed
      returned: always
      type: str
      sample: null
    classification_comment:
      description:
        - Describes the reason the incident was closed
      returned: always
      type: str
      sample: null
    classification_reason:
      description:
        - The classification reason the incident was closed with
      returned: always
      type: str
      sample: null
    created_time_utc:
      description:
        - The time the incident was created
      returned: always
      type: str
      sample: null
    description:
      description:
        - The description of the incident
      returned: always
      type: str
      sample: null
    first_activity_time_utc:
      description:
        - The time of the first activity in the incident
      returned: always
      type: str
      sample: null
    incident_url:
      description:
        - The deep-link url to the incident in Azure portal
      returned: always
      type: str
      sample: null
    incident_number:
      description:
        - A sequential number
      returned: always
      type: integer
      sample: null
    labels:
      description:
        - List of labels relevant to this incident
      returned: always
      type: list
      sample: null
      contains:
        label_name:
          description:
            - The name of the label
          returned: always
          type: str
          sample: null
        label_type:
          description:
            - The type of the label
          returned: always
          type: str
          sample: null
    last_activity_time_utc:
      description:
        - The time of the last activity in the incident
      returned: always
      type: str
      sample: null
    last_modified_time_utc:
      description:
        - The last time the incident was updated
      returned: always
      type: str
      sample: null
    owner:
      description:
        - Describes a user that the incident is assigned to
      returned: always
      type: dict
      sample: null
      contains:
        email:
          description:
            - The email of the user the incident is assigned to.
          returned: always
          type: str
          sample: null
        assigned_to:
          description:
            - The name of the user the incident is assigned to.
          returned: always
          type: str
          sample: null
        object_id:
          description:
            - The object id of the user the incident is assigned to.
          returned: always
          type: uuid
          sample: null
        user_principal_name:
          description:
            - The user principal name of the user the incident is assigned to.
          returned: always
          type: str
          sample: null
    related_analytic_rule_ids:
      description:
        - List of resource ids of Analytic rules related to the incident
      returned: always
      type: list
      sample: null
    severity:
      description:
        - The severity of the incident
      returned: always
      type: str
      sample: null
    status:
      description:
        - The status of the incident
      returned: always
      type: str
      sample: null
    title:
      description:
        - The title of the incident
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


class AzureRMIncidentInfo(AzureRMModuleBase):
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
            incident_id=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.workspace_name = None
        self.filter = None
        self.orderby = None
        self.top = None
        self.skip_token = None
        self.incident_id = None

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
        super(AzureRMIncidentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Security Insights,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-01-01')

        if (self.resource_group_name is not None and
            self.workspace_name is not None and
            self.incident_id is not None):
            self.results['incidents'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.workspace_name is not None):
            self.results['incidents'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.incidents.get(resource_group_name=self.resource_group_name,
                                                      workspace_name=self.workspace_name,
                                                      incident_id=self.incident_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.incidents.list(resource_group_name=self.resource_group_name,
                                                       workspace_name=self.workspace_name,
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
    AzureRMIncidentInfo()


if __name__ == '__main__':
    main()
