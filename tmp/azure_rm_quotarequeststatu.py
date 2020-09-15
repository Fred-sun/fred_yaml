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
module: azure_rm_quotarequeststatu
version_added: '2.9'
short_description: Manage Azure QuotaRequestStatu instance.
description:
  - 'Create, update and delete instance of Azure QuotaRequestStatu.'
options:
  provider_id:
    description:
      - Azure resource provider id.
    required: true
    type: str
  location:
    description:
      - Azure region.
    required: true
    type: str
  id:
    description:
      - Quota Request id.
    required: true
    type: str
  state:
    description:
      - Assert the state of the QuotaRequestStatu.
      - >-
        Use C(present) to create or update an QuotaRequestStatu and C(absent) to
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
    - The quota request Id.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the quota request.
  returned: always
  type: str
  sample: null
type:
  description:
    - Type of resource. "Microsoft.Capacity/ServiceLimits"
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The quota request status.
  returned: always
  type: str
  sample: null
message:
  description:
    - User friendly status message.
  returned: always
  type: str
  sample: null
request_submit_time:
  description:
    - >-
      The quota request submit time. The date conforms to the following format:
      yyyy-MM-ddTHH:mm:ssZ as specified by the ISO 8601 standard.
  returned: always
  type: str
  sample: null
value:
  description:
    - The quotaRequests.
  returned: always
  type: list
  sample: null
  contains:
    limit:
      description:
        - The Resource limit.
      returned: always
      type: integer
      sample: null
    name:
      description:
        - The Resource name.
      returned: always
      type: dict
      sample: null
      contains:
        value:
          description:
            - Resource name.
          returned: always
          type: str
          sample: null
        localized_value:
          description:
            - Resource display name.
          returned: always
          type: str
          sample: null
    resource_type:
      description:
        - Resource type for which the quota check was made.
      returned: always
      type: str
      sample: null
    unit:
      description:
        - ' The units of the limit, such as - Count, Bytes, etc. Use the unit field provided in the Get quota response.'
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The quota request status.
      returned: always
      type: str
      sample: null
    message:
      description:
        - User friendly status message.
      returned: always
      type: str
      sample: null
    sub_request_id:
      description:
        - Sub request id for individual request.
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
    from azure.mgmt.azure import Azure Reservation API
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMQuotaRequestStatu(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            provider_id=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                required=True
            ),
            id=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.provider_id = None
        self.location = None
        self.id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMQuotaRequestStatu, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Azure Reservation API,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-19-preview')

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
                response = self.mgmt_client.quota_request_status.create()
            else:
                response = self.mgmt_client.quota_request_status.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the QuotaRequestStatu instance.')
            self.fail('Error creating the QuotaRequestStatu instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.quota_request_status.delete()
        except CloudError as e:
            self.log('Error attempting to delete the QuotaRequestStatu instance.')
            self.fail('Error deleting the QuotaRequestStatu instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.quota_request_status.get(provider_id=self.provider_id,
                                                                 location=self.location,
                                                                 id=self.id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMQuotaRequestStatu()


if __name__ == '__main__':
    main()
