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
module: azure_rm_marketplaceagreement
version_added: '2.9'
short_description: Manage Azure MarketplaceAgreement instance.
description:
  - 'Create, update and delete instance of Azure MarketplaceAgreement.'
options:
  offer_type:
    description:
      - 'Offer Type, currently only virtualmachine type is supported.'
    required: true
    type: str
    choices:
      - virtualmachine
  publisher_id:
    description:
      - Publisher identifier string of image being deployed.
    required: true
    type: str
  offer_id:
    description:
      - Offer identifier string of image being deployed.
    required: true
    type: str
  plan_id:
    description:
      - Plan identifier string of image being deployed.
    required: true
    type: str
  publisher:
    description:
      - Publisher identifier string of image being deployed.
    type: str
  product:
    description:
      - Offer identifier string of image being deployed.
    type: str
  plan:
    description:
      - Plan identifier string of image being deployed.
    type: str
  license_text_link:
    description:
      - Link to HTML with Microsoft and Publisher terms.
    type: str
  privacy_policy_link:
    description:
      - Link to the privacy policy of the publisher.
    type: str
  retrieve_datetime:
    description:
      - >-
        Date and time in UTC of when the terms were accepted. This is empty if
        Accepted is false.
    type: str
  signature:
    description:
      - Terms signature.
    type: str
  accepted:
    description:
      - 'If any version of the terms have been accepted, otherwise false.'
    type: bool
  state:
    description:
      - Assert the state of the MarketplaceAgreement.
      - >-
        Use C(present) to create or update an MarketplaceAgreement and C(absent)
        to delete it.
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
    - name: SetMarketplaceTerms
      azure_rm_marketplaceagreement: 
        offer_id: offid
        offer_type: virtualmachine
        plan_id: planid
        publisher_id: pubid
        name: planid
        type: Microsoft.MarketplaceOrdering/offertypes
        id: id
        properties:
          accepted: false
          license_text_link: test.licenseLink
          plan: planid
          privacy_policy_link: test.privacyPolicyLink
          product: offid
          publisher: pubid
          retrieve_datetime: '2017-08-15T11:33:07.12132Z'
          signature: ASDFSDAFWEFASDGWERLWER
        

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
publisher:
  description:
    - Publisher identifier string of image being deployed.
  returned: always
  type: str
  sample: null
product:
  description:
    - Offer identifier string of image being deployed.
  returned: always
  type: str
  sample: null
plan:
  description:
    - Plan identifier string of image being deployed.
  returned: always
  type: str
  sample: null
license_text_link:
  description:
    - Link to HTML with Microsoft and Publisher terms.
  returned: always
  type: str
  sample: null
privacy_policy_link:
  description:
    - Link to the privacy policy of the publisher.
  returned: always
  type: str
  sample: null
retrieve_datetime:
  description:
    - >-
      Date and time in UTC of when the terms were accepted. This is empty if
      Accepted is false.
  returned: always
  type: str
  sample: null
signature:
  description:
    - Terms signature.
  returned: always
  type: str
  sample: null
accepted:
  description:
    - 'If any version of the terms have been accepted, otherwise false.'
  returned: always
  type: bool
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.marketplace import MarketplaceOrdering.Agreements
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMMarketplaceAgreement(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            offer_type=dict(
                type='str',
                choices=['virtualmachine'],
                required=True
            ),
            publisher_id=dict(
                type='str',
                required=True
            ),
            offer_id=dict(
                type='str',
                required=True
            ),
            plan_id=dict(
                type='str',
                required=True
            ),
            publisher=dict(
                type='str',
                disposition='/publisher'
            ),
            product=dict(
                type='str',
                disposition='/product'
            ),
            plan=dict(
                type='str',
                disposition='/plan'
            ),
            license_text_link=dict(
                type='str',
                disposition='/license_text_link'
            ),
            privacy_policy_link=dict(
                type='str',
                disposition='/privacy_policy_link'
            ),
            retrieve_datetime=dict(
                type='str',
                disposition='/retrieve_datetime'
            ),
            signature=dict(
                type='str',
                disposition='/signature'
            ),
            accepted=dict(
                type='bool',
                disposition='/accepted'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.offer_type = None
        self.publisher_id = None
        self.offer_id = None
        self.plan_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMMarketplaceAgreement, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(MarketplaceOrdering.Agreements,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-06-01')

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
                response = self.mgmt_client.marketplace_agreements.create(offer_type=self.offer_type,
                                                                          publisher_id=self.publisher_id,
                                                                          offer_id=self.offer_id,
                                                                          plan_id=self.plan_id,
                                                                          parameters=self.body)
            else:
                response = self.mgmt_client.marketplace_agreements.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the MarketplaceAgreement instance.')
            self.fail('Error creating the MarketplaceAgreement instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.marketplace_agreements.delete()
        except CloudError as e:
            self.log('Error attempting to delete the MarketplaceAgreement instance.')
            self.fail('Error deleting the MarketplaceAgreement instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.marketplace_agreements.get(offer_type=self.offer_type,
                                                                   publisher_id=self.publisher_id,
                                                                   offer_id=self.offer_id,
                                                                   plan_id=self.plan_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMMarketplaceAgreement()


if __name__ == '__main__':
    main()
