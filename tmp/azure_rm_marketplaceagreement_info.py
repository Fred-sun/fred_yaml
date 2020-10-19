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
module: azure_rm_marketplaceagreement_info
version_added: '2.9'
short_description: Get MarketplaceAgreement info.
description:
  - Get info of MarketplaceAgreement.
options:
  offer_type:
    description:
      - 'Offer Type, currently only virtualmachine type is supported.'
    type: str
    choices:
      - virtualmachine
  publisher_id:
    description:
      - Publisher identifier string of image being deployed.
    type: str
  offer_id:
    description:
      - Offer identifier string of image being deployed.
    type: str
  plan_id:
    description:
      - Plan identifier string of image being deployed.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetMarketplaceTerms
      azure_rm_marketplaceagreement_info: 
        offer_id: offid
        offer_type: virtualmachine
        plan_id: planid
        publisher_id: pubid
        

    - name: SetMarketplaceTerms
      azure_rm_marketplaceagreement_info: 
        offer_id: offid
        plan_id: planid
        publisher_id: pubid
        

'''

RETURN = '''
marketplace_agreements:
  description: >-
    A list of dict results where the key is the name of the MarketplaceAgreement
    and the values are the facts for that MarketplaceAgreement.
  returned: always
  type: complex
  contains:
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.marketplace import MarketplaceOrdering.Agreements
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMMarketplaceAgreementInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            offer_type=dict(
                type='str',
                choices=['virtualmachine']
            ),
            publisher_id=dict(
                type='str'
            ),
            offer_id=dict(
                type='str'
            ),
            plan_id=dict(
                type='str'
            )
        )

        self.offer_type = None
        self.publisher_id = None
        self.offer_id = None
        self.plan_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2015-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMMarketplaceAgreementInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MarketplaceOrdering.Agreements,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-06-01')

        if (self.offer_type is not None and
            self.publisher_id is not None and
            self.offer_id is not None and
            self.plan_id is not None):
            self.results['marketplace_agreements'] = self.format_item(self.get())
        elif (self.publisher_id is not None and
              self.offer_id is not None and
              self.plan_id is not None):
            self.results['marketplace_agreements'] = self.format_item(self.getagreement())
        else:
            self.results['marketplace_agreements'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.marketplace_agreements.get(offer_type=self.offer_type,
                                                                   publisher_id=self.publisher_id,
                                                                   offer_id=self.offer_id,
                                                                   plan_id=self.plan_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getagreement(self):
        response = None

        try:
            response = self.mgmt_client.marketplace_agreements.get_agreement(publisher_id=self.publisher_id,
                                                                             offer_id=self.offer_id,
                                                                             plan_id=self.plan_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.marketplace_agreements.list()
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
    AzureRMMarketplaceAgreementInfo()


if __name__ == '__main__':
    main()
