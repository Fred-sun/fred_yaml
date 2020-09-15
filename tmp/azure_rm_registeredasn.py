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
module: azure_rm_registeredasn
version_added: '2.9'
short_description: Manage Azure RegisteredAsn instance.
description:
  - 'Create, update and delete instance of Azure RegisteredAsn.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  peering_name:
    description:
      - The name of the peering.
    required: true
    type: str
  registered_asn_name:
    description:
      - The name of the registered ASN.
      - The name of the ASN.
    required: true
    type: str
  asn:
    description:
      - The customer's ASN from which traffic originates.
    type: integer
  state:
    description:
      - Assert the state of the RegisteredAsn.
      - >-
        Use C(present) to create or update an RegisteredAsn and C(absent) to
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
    - name: Create or update a registered ASN for the peering
      azure_rm_registeredasn: 
        peering_name: peeringName
        registered_asn_name: registeredAsnName
        resource_group_name: rgName
        

    - name: Deletes a registered ASN associated with the peering
      azure_rm_registeredasn: 
        peering_name: peeringName
        registered_asn_name: registeredAsnName
        resource_group_name: rgName
        

'''

RETURN = '''
name:
  description:
    - The name of the resource.
  returned: always
  type: str
  sample: null
id:
  description:
    - The ID of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the resource.
  returned: always
  type: str
  sample: null
asn:
  description:
    - The customer's ASN from which traffic originates.
  returned: always
  type: integer
  sample: null
peering_service_prefix_key:
  description:
    - The peering service prefix key that is to be shared with the customer.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning state of the resource.
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
    from azure.mgmt.peering import PeeringManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRegisteredAsn(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            peering_name=dict(
                type='str',
                required=True
            ),
            registered_asn_name=dict(
                type='str',
                required=True
            ),
            asn=dict(
                type='integer',
                disposition='/asn'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.peering_name = None
        self.registered_asn_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRegisteredAsn, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(PeeringManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

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
            response = self.mgmt_client.registered_asns.create_or_update(resource_group_name=self.resource_group_name,
                                                                         peering_name=self.peering_name,
                                                                         registered_asn_name=self.registered_asn_name,
                                                                         registered_asn=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the RegisteredAsn instance.')
            self.fail('Error creating the RegisteredAsn instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.registered_asns.delete(resource_group_name=self.resource_group_name,
                                                               peering_name=self.peering_name,
                                                               registered_asn_name=self.registered_asn_name)
        except CloudError as e:
            self.log('Error attempting to delete the RegisteredAsn instance.')
            self.fail('Error deleting the RegisteredAsn instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.registered_asns.get(resource_group_name=self.resource_group_name,
                                                            peering_name=self.peering_name,
                                                            registered_asn_name=self.registered_asn_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRegisteredAsn()


if __name__ == '__main__':
    main()
