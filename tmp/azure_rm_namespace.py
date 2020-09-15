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
module: azure_rm_namespace
version_added: '2.9'
short_description: Manage Azure Namespace instance.
description:
  - 'Create, update and delete instance of Azure Namespace.'
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  namespace_name:
    description:
      - The namespace name.
    required: true
    type: str
  location:
    description:
      - The Geo-location where the resource lives
      - Resource location
    type: str
  sku:
    description:
      - Properties of SKU
    type: dict
    suboptions:
      name:
        description:
          - Name of this SKU.
        required: true
        type: sealed-choice
      tier:
        description:
          - The billing tier of this particular SKU.
        type: sealed-choice
      capacity:
        description:
          - >-
            The specified messaging units for the tier. For Premium tier,
            capacity are 1,2 and 4.
        type: integer
  zone_redundant:
    description:
      - >-
        Enabling this property creates a Premium Service Bus Namespace in
        regions supported availability zones.
    type: bool
  key_vault_properties:
    description:
      - Properties of KeyVault
    type: dict
    suboptions:
      key_name:
        description:
          - Name of the Key from KeyVault
        type: str
      key_vault_uri:
        description:
          - Uri of KeyVault
        type: str
  keysource:
    description:
      - Enumerates the possible value of keySource for Encryption
    type: constant
  identity:
    description:
      - Properties of BYOK Identity description
    type: dict
    suboptions:
      principal_id:
        description:
          - ObjectId from the KeyVault
        type: str
      tenant_id:
        description:
          - TenantId from the KeyVault
        type: str
      type:
        description:
          - >-
            Enumerates the possible value Identity type, which currently
            supports only 'SystemAssigned'
        type: constant
  state:
    description:
      - Assert the state of the Namespace.
      - >-
        Use C(present) to create or update an Namespace and C(absent) to delete
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
    - name: NameSpaceCreate
      azure_rm_namespace: 
        namespace_name: sdk-Namespace2924
        resource_group_name: ArunMonocle
        location: South Central US
        sku:
          name: Standard
          tier: Standard
        tags:
          tag1: value1
          tag2: value2
        

    - name: NameSpaceDelete
      azure_rm_namespace: 
        namespace_name: sdk-Namespace-3285
        resource_group_name: ArunMonocle
        

    - name: NameSpaceUpdate
      azure_rm_namespace: 
        namespace_name: sdk-Namespace-3285
        resource_group_name: ArunMonocle
        location: South Central US
        tags:
          tag3: value3
          tag4: value4
        

'''

RETURN = '''
location:
  description:
    - The Geo-location where the resource lives
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags
  returned: always
  type: dictionary
  sample: null
sku:
  description:
    - Properties of SKU
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - Name of this SKU.
      returned: always
      type: sealed-choice
      sample: null
    tier:
      description:
        - The billing tier of this particular SKU.
      returned: always
      type: sealed-choice
      sample: null
    capacity:
      description:
        - >-
          The specified messaging units for the tier. For Premium tier, capacity
          are 1,2 and 4.
      returned: always
      type: integer
      sample: null
provisioning_state:
  description:
    - Provisioning state of the namespace.
  returned: always
  type: str
  sample: null
created_at:
  description:
    - The time the namespace was created
  returned: always
  type: str
  sample: null
updated_at:
  description:
    - The time the namespace was updated.
  returned: always
  type: str
  sample: null
service_bus_endpoint:
  description:
    - Endpoint you can use to perform Service Bus operations.
  returned: always
  type: str
  sample: null
metric_id:
  description:
    - Identifier for Azure Insights metrics
  returned: always
  type: str
  sample: null
zone_redundant:
  description:
    - >-
      Enabling this property creates a Premium Service Bus Namespace in regions
      supported availability zones.
  returned: always
  type: bool
  sample: null
key_vault_properties:
  description:
    - Properties of KeyVault
  returned: always
  type: dict
  sample: null
  contains:
    key_name:
      description:
        - Name of the Key from KeyVault
      returned: always
      type: str
      sample: null
    key_vault_uri:
      description:
        - Uri of KeyVault
      returned: always
      type: str
      sample: null
key_source:
  description:
    - Enumerates the possible value of keySource for Encryption
  returned: always
  type: constant
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.service import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMNamespace(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            namespace_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='sealed-choice',
                        disposition='name',
                        required=True
                    ),
                    tier=dict(
                        type='sealed-choice',
                        disposition='tier'
                    ),
                    capacity=dict(
                        type='integer',
                        disposition='capacity'
                    )
                )
            ),
            zone_redundant=dict(
                type='bool',
                disposition='/zone_redundant'
            ),
            key_vault_properties=dict(
                type='dict',
                disposition='/key_vault_properties',
                options=dict(
                    key_name=dict(
                        type='str',
                        disposition='key_name'
                    ),
                    key_vault_uri=dict(
                        type='str',
                        disposition='key_vault_uri'
                    )
                )
            ),
            keysource=dict(
                type='constant',
                disposition='/keysource'
            ),
            identity=dict(
                type='dict',
                disposition='/identity',
                options=dict(
                    principal_id=dict(
                        type='str',
                        disposition='principal_id'
                    ),
                    tenant_id=dict(
                        type='str',
                        disposition='tenant_id'
                    ),
                    type=dict(
                        type='constant',
                        disposition='type'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.namespace_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMNamespace, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-01-01-preview')

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
            response = self.mgmt_client.namespaces.create_or_update(resource_group_name=self.resource_group_name,
                                                                    namespace_name=self.namespace_name,
                                                                    parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Namespace instance.')
            self.fail('Error creating the Namespace instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.namespaces.delete(resource_group_name=self.resource_group_name,
                                                          namespace_name=self.namespace_name)
        except CloudError as e:
            self.log('Error attempting to delete the Namespace instance.')
            self.fail('Error deleting the Namespace instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.namespaces.get(resource_group_name=self.resource_group_name,
                                                       namespace_name=self.namespace_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMNamespace()


if __name__ == '__main__':
    main()
