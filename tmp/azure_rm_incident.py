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
module: azure_rm_incident
version_added: '2.9'
short_description: Manage Azure Incident instance.
description:
  - 'Create, update and delete instance of Azure Incident.'
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
  etag:
    description:
      - Etag of the azure resource
    type: str
  classification:
    description:
      - The reason the incident was closed
    type: str
    choices:
      - Undetermined
      - TruePositive
      - BenignPositive
      - FalsePositive
  classification_comment:
    description:
      - Describes the reason the incident was closed
    type: str
  classification_reason:
    description:
      - The classification reason the incident was closed with
    type: str
    choices:
      - SuspiciousActivity
      - SuspiciousButExpected
      - IncorrectAlertLogic
      - InaccurateData
  description:
    description:
      - The description of the incident
    type: str
  first_activity_time_utc:
    description:
      - The time of the first activity in the incident
    type: str
  labels:
    description:
      - List of labels relevant to this incident
    type: list
    suboptions:
      label_name:
        description:
          - The name of the label
        required: true
        type: str
      label_type:
        description:
          - The type of the label
        type: str
        choices:
          - User
          - System
  last_activity_time_utc:
    description:
      - The time of the last activity in the incident
    type: str
  owner:
    description:
      - Describes a user that the incident is assigned to
    type: dict
    suboptions:
      email:
        description:
          - The email of the user the incident is assigned to.
        type: str
      assigned_to:
        description:
          - The name of the user the incident is assigned to.
        type: str
      object_id:
        description:
          - The object id of the user the incident is assigned to.
        type: uuid
      user_principal_name:
        description:
          - The user principal name of the user the incident is assigned to.
        type: str
  severity:
    description:
      - The severity of the incident
    type: str
    choices:
      - High
      - Medium
      - Low
      - Informational
  status:
    description:
      - The status of the incident
    type: str
    choices:
      - New
      - Active
      - Closed
  title:
    description:
      - The title of the incident
    type: str
  state:
    description:
      - Assert the state of the Incident.
      - >-
        Use C(present) to create or update an Incident and C(absent) to delete
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
    - name: Creates or updates an incident.
      azure_rm_incident: 
        incident_id: 73e01a99-5cd7-4139-a149-9f2736ff2ab5
        resource_group_name: myRg
        workspace_name: myWorkspace
        etag: '"0300bf09-0000-0000-0000-5c37296e0000"'
        properties:
          description: This is a demo incident
          classification: FalsePositive
          classification_comment: Not a malicious activity
          classification_reason: IncorrectAlertLogic
          first_activity_time_utc: '2019-01-01T13:00:30Z'
          last_activity_time_utc: '2019-01-01T13:05:30Z'
          owner:
            object_id: 2046feea-040d-4a46-9e2b-91c2941bfa70
          severity: High
          status: Closed
          title: My incident
        

    - name: Delete an incident.
      azure_rm_incident: 
        incident_id: 73e01a99-5cd7-4139-a149-9f2736ff2ab5
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


class AzureRMIncident(AzureRMModuleBaseExt):
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
            etag=dict(
                type='str',
                disposition='/etag'
            ),
            classification=dict(
                type='str',
                disposition='/classification',
                choices=['Undetermined',
                         'TruePositive',
                         'BenignPositive',
                         'FalsePositive']
            ),
            classification_comment=dict(
                type='str',
                disposition='/classification_comment'
            ),
            classification_reason=dict(
                type='str',
                disposition='/classification_reason',
                choices=['SuspiciousActivity',
                         'SuspiciousButExpected',
                         'IncorrectAlertLogic',
                         'InaccurateData']
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            first_activity_time_utc=dict(
                type='str',
                disposition='/first_activity_time_utc'
            ),
            labels=dict(
                type='list',
                disposition='/labels',
                elements='dict',
                options=dict(
                    label_name=dict(
                        type='str',
                        disposition='label_name',
                        required=True
                    ),
                    label_type=dict(
                        type='str',
                        updatable=False,
                        disposition='label_type',
                        choices=['User',
                                 'System']
                    )
                )
            ),
            last_activity_time_utc=dict(
                type='str',
                disposition='/last_activity_time_utc'
            ),
            owner=dict(
                type='dict',
                disposition='/owner',
                options=dict(
                    email=dict(
                        type='str',
                        disposition='email'
                    ),
                    assigned_to=dict(
                        type='str',
                        disposition='assigned_to'
                    ),
                    object_id=dict(
                        type='uuid',
                        disposition='object_id'
                    ),
                    user_principal_name=dict(
                        type='str',
                        disposition='user_principal_name'
                    )
                )
            ),
            severity=dict(
                type='str',
                disposition='/severity',
                choices=['High',
                         'Medium',
                         'Low',
                         'Informational']
            ),
            status=dict(
                type='str',
                disposition='/status',
                choices=['New',
                         'Active',
                         'Closed']
            ),
            title=dict(
                type='str',
                disposition='/title'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.workspace_name = None
        self.incident_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMIncident, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.incidents.create_or_update(resource_group_name=self.resource_group_name,
                                                                   workspace_name=self.workspace_name,
                                                                   incident_id=self.incident_id,
                                                                   incident=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Incident instance.')
            self.fail('Error creating the Incident instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.incidents.delete(resource_group_name=self.resource_group_name,
                                                         workspace_name=self.workspace_name,
                                                         incident_id=self.incident_id)
        except CloudError as e:
            self.log('Error attempting to delete the Incident instance.')
            self.fail('Error deleting the Incident instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.incidents.get(resource_group_name=self.resource_group_name,
                                                      workspace_name=self.workspace_name,
                                                      incident_id=self.incident_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMIncident()


if __name__ == '__main__':
    main()
