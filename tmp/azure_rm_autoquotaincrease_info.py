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
module: azure_rm_autoquotaincrease_info
version_added: '2.9'
short_description: Get AutoQuotaIncrease info.
description:
  - Get info of AutoQuotaIncrease.
options: {}
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetAutoQuotaIncreaseSettings
      azure_rm_autoquotaincrease_info: 
        {}
        

'''

RETURN = '''
auto_quota_increase:
  description: >-
    A list of dict results where the key is the name of the AutoQuotaIncrease
    and the values are the facts for that AutoQuotaIncrease.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The subscription Id.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the auto quota increase.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of the resource
      returned: always
      type: str
      sample: null
    support_ticket_action:
      description:
        - The support ticket action.
      returned: always
      type: dict
      sample: null
      contains:
        severity:
          description:
            - The support request severity.
          returned: always
          type: str
          sample: null
        first_name:
          description:
            - The first name of the recipient.
          returned: always
          type: str
          sample: null
        last_name:
          description:
            - The last name of the recipient.
          returned: always
          type: str
          sample: null
        country:
          description:
            - The country of the recipient.
          returned: always
          type: str
          sample: null
        phone_number:
          description:
            - The phone number of the recipient.
          returned: always
          type: str
          sample: null
        primary_email_address:
          description:
            - The primary email addresses of the recipients.
          returned: always
          type: str
          sample: null
        support_language:
          description:
            - The support language.
          returned: always
          type: str
          sample: null
        preferred_contact_method:
          description:
            - The preferred communication channel.
          returned: always
          type: str
          sample: null
        alternate_email_addresses:
          description:
            - The alternate email address of the recipient.
          returned: always
          type: list
          sample: null
    email_actions_properties_on_success_email_actions:
      description:
        - The email actions for auto quota increase.
      returned: always
      type: dict
      sample: null
      contains:
        email_addresses:
          description:
            - The list of email actions.
          returned: always
          type: list
          sample: null
          contains:
            email_address:
              description:
                - The email address for the action.
              returned: always
              type: str
              sample: null
    email_actions_properties_on_failure_email_actions:
      description:
        - The email actions for auto quota increase.
      returned: always
      type: dict
      sample: null
      contains:
        email_addresses:
          description:
            - The list of email actions.
          returned: always
          type: list
          sample: null
          contains:
            email_address:
              description:
                - The email address for the action.
              returned: always
              type: str
              sample: null
    auto_quota_increase_state:
      description:
        - If the subscription has enabled automatic quota increase.
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
    from azure.mgmt.azure import Azure Reservation API
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAutoQuotaIncreaseInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )


        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-07-19-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMAutoQuotaIncreaseInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Reservation API,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-19-preview')

        else:
            self.results['auto_quota_increase'] = self.format_item(self.getproperty())
        return self.results

    def getproperty(self):
        response = None

        try:
            response = self.mgmt_client.auto_quota_increase.get_property()
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
    AzureRMAutoQuotaIncreaseInfo()


if __name__ == '__main__':
    main()
