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
module: azure_rm_recommendation
version_added: '2.9'
short_description: Manage Azure Recommendation instance.
description:
  - 'Create, update and delete instance of Azure Recommendation.'
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
  state:
    description:
      - Assert the state of the Recommendation.
      - >-
        Use C(present) to create or update an Recommendation and C(absent) to
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
category:
  description:
    - The category of the recommendation.
  returned: always
  type: str
  sample: null
impact:
  description:
    - The business impact of the recommendation.
  returned: always
  type: str
  sample: null
impacted_field:
  description:
    - The resource type identified by Advisor.
  returned: always
  type: str
  sample: null
impacted_value:
  description:
    - The resource identified by Advisor.
  returned: always
  type: str
  sample: null
last_updated:
  description:
    - >-
      The most recent time that Advisor checked the validity of the
      recommendation.
  returned: always
  type: str
  sample: null
metadata:
  description:
    - The recommendation metadata.
  returned: always
  type: dictionary
  sample: null
recommendation_type_id:
  description:
    - The recommendation-type GUID.
  returned: always
  type: str
  sample: null
risk:
  description:
    - The potential risk of not implementing the recommendation.
  returned: always
  type: str
  sample: null
short_description:
  description:
    - A summary of the recommendation.
  returned: always
  type: dict
  sample: null
  contains:
    problem:
      description:
        - The issue or opportunity identified by the recommendation.
      returned: always
      type: str
      sample: null
    solution:
      description:
        - The remediation action suggested by the recommendation.
      returned: always
      type: str
      sample: null
suppression_ids:
  description:
    - The list of snoozed and dismissed rules for the recommendation.
  returned: always
  type: list
  sample: null
extended_properties:
  description:
    - Extended properties
  returned: always
  type: dictionary
  sample: null
resource_metadata:
  description:
    - Metadata of resource that was assessed
  returned: always
  type: dict
  sample: null
  contains:
    resource_id:
      description:
        - Azure resource Id of the assessed resource
      returned: always
      type: str
      sample: null
    source:
      description:
        - Source from which recommendation is generated
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


class AzureRMRecommendation(AzureRMModuleBaseExt):
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
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_uri = None
        self.recommendation_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRecommendation, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.recommendations.create()
            else:
                response = self.mgmt_client.recommendations.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Recommendation instance.')
            self.fail('Error creating the Recommendation instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.recommendations.delete()
        except CloudError as e:
            self.log('Error attempting to delete the Recommendation instance.')
            self.fail('Error deleting the Recommendation instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.recommendations.get(resource_uri=self.resource_uri,
                                                            recommendation_id=self.recommendation_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRecommendation()


if __name__ == '__main__':
    main()
