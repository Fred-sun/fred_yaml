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
module: azure_rm_iotdpsresource
version_added: '2.9'
short_description: Manage Azure IotDpsResource instance.
description:
  - 'Create, update and delete instance of Azure IotDpsResource.'
options:
  provisioning_service_name:
    description:
      - Name of the provisioning service to retrieve.
      - Name of provisioning service to create or update.
      - Name of provisioning service to delete.
    required: true
    type: str
  resource_group_name:
    description:
      - Resource group name.
      - Resource group identifier.
    required: true
    type: str
  location:
    description:
      - The resource location.
    type: str
  etag:
    description:
      - >-
        The Etag field is *not* required. If it is provided in the response
        body, it must also be provided as a header per the normal ETag
        convention.
    type: str
  sku:
    description:
      - Sku info for a provisioning Service.
    type: dict
    suboptions:
      name:
        description:
          - Sku name.
        type: str
        choices:
          - S1
      tier:
        description:
          - Pricing tier name of the provisioning service.
        type: str
      capacity:
        description:
          - The number of units to provision
        type: integer
  state:
    description:
      - Assert the state of the IotDpsResource.
      - >-
        Use C(present) to create or update an IotDpsResource and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
  encryption:
    description:
      - The encryption properties for the IoT DPS instance.
    type: dict
    suboptions:
      key_source:
        description:
          - The source of the key.
        type: str
      key_vault_properties:
        description:
          - The properties of the KeyVault key.
        type: list
        suboptions:
          key_identifier:
            description:
              - The identifier of the key.
            type: str
  public_network_access:
    description:
      - Whether requests from Public Network are allowed
    type: str
    choices:
      - Enabled
      - Disabled
  ip_filter_rules:
    description:
      - The IP filter rules.
    type: list
    suboptions:
      filter_name:
        description:
          - The name of the IP filter rule.
        required: true
        type: str
      action:
        description:
          - The desired action for requests captured by this rule.
        required: true
        type: sealed-choice
      ip_mask:
        description:
          - >-
            A string that contains the IP address range in CIDR notation for the
            rule.
        required: true
        type: str
      target:
        description:
          - Target for requests captured by this rule.
        type: sealed-choice
  private_endpoint_connections:
    description:
      - Private endpoint connections created on this IotHub
    type: list
    suboptions:
      id:
        description:
          - The resource identifier.
        type: str
      name:
        description:
          - The resource name.
        type: str
      type:
        description:
          - The resource type.
        type: str
      private_endpoint:
        description:
          - The private endpoint property of a private endpoint connection
        type: dict
        suboptions:
          id:
            description:
              - The resource identifier.
            type: str
      private_link_service_connection_state:
        description:
          - The current state of a private endpoint connection
        required: true
        type: dict
        suboptions:
          status:
            description:
              - The status of a private endpoint connection
            required: true
            type: str
            choices:
              - Pending
              - Approved
              - Rejected
              - Disconnected
          description:
            description:
              - >-
                The description for the current state of a private endpoint
                connection
            required: true
            type: str
          actions_required:
            description:
              - Actions required for a private endpoint connection
            type: str
  provisioning_state:
    description:
      - The ARM provisioning state of the provisioning service.
    type: str
  iot_hubs:
    description:
      - List of IoT hubs associated with this provisioning service.
    type: list
    suboptions:
      apply_allocation_policy:
        description:
          - flag for applying allocationPolicy or not for a given iot hub.
        type: bool
      allocation_weight:
        description:
          - weight to apply for a given iot h.
        type: integer
      name:
        description:
          - Host name of the IoT hub.
        type: str
      connection_string:
        description:
          - Connection string of the IoT hub.
        required: true
        type: str
      location:
        description:
          - ARM region of the IoT hub.
        required: true
        type: str
  allocation_policy:
    description:
      - Allocation policy to be used by this provisioning service.
    type: str
    choices:
      - Hashed
      - GeoLatency
      - Static
  authorization_policies:
    description:
      - List of authorization keys for a provisioning service.
    type: list
    suboptions:
      key_name:
        description:
          - Name of the key.
        required: true
        type: str
      primary_key:
        description:
          - Primary SAS key value.
        type: str
      secondary_key:
        description:
          - Secondary SAS key value.
        type: str
      rights:
        description:
          - Rights that this key has.
        required: true
        type: str
        choices:
          - ServiceConfig
          - EnrollmentRead
          - EnrollmentWrite
          - DeviceConnect
          - RegistrationStatusRead
          - RegistrationStatusWrite
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: DPSCreate
      azure_rm_iotdpsresource: 
        provisioning_service_name: myFirstProvisioningService
        resource_group_name: myResourceGroup
        

    - name: DPSPatch
      azure_rm_iotdpsresource: 
        provisioning_service_name: myFirstProvisioningService
        resource_group_name: myResourceGroup
        

    - name: DPSDelete
      azure_rm_iotdpsresource: 
        provisioning_service_name: myFirstProvisioningService
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
id:
  description:
    - The resource identifier.
  returned: always
  type: str
  sample: null
name:
  description:
    - The resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The resource type.
  returned: always
  type: str
  sample: null
location:
  description:
    - The resource location.
  returned: always
  type: str
  sample: null
tags:
  description:
    - The resource tags.
  returned: always
  type: dictionary
  sample: null
etag:
  description:
    - >-
      The Etag field is *not* required. If it is provided in the response body,
      it must also be provided as a header per the normal ETag convention.
  returned: always
  type: str
  sample: null
sku:
  description:
    - Sku info for a provisioning Service.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - Sku name.
      returned: always
      type: str
      sample: null
    tier:
      description:
        - Pricing tier name of the provisioning service.
      returned: always
      type: str
      sample: null
    capacity:
      description:
        - The number of units to provision
      returned: always
      type: integer
      sample: null
state:
  description:
    - Current state of the provisioning service.
  returned: always
  type: str
  sample: null
encryption:
  description:
    - The encryption properties for the IoT DPS instance.
  returned: always
  type: dict
  sample: null
  contains:
    key_source:
      description:
        - The source of the key.
      returned: always
      type: str
      sample: null
    key_vault_properties:
      description:
        - The properties of the KeyVault key.
      returned: always
      type: list
      sample: null
      contains:
        key_identifier:
          description:
            - The identifier of the key.
          returned: always
          type: str
          sample: null
public_network_access:
  description:
    - Whether requests from Public Network are allowed
  returned: always
  type: str
  sample: null
ip_filter_rules:
  description:
    - The IP filter rules.
  returned: always
  type: list
  sample: null
  contains:
    filter_name:
      description:
        - The name of the IP filter rule.
      returned: always
      type: str
      sample: null
    action:
      description:
        - The desired action for requests captured by this rule.
      returned: always
      type: sealed-choice
      sample: null
    ip_mask:
      description:
        - >-
          A string that contains the IP address range in CIDR notation for the
          rule.
      returned: always
      type: str
      sample: null
    target:
      description:
        - Target for requests captured by this rule.
      returned: always
      type: sealed-choice
      sample: null
private_endpoint_connections:
  description:
    - Private endpoint connections created on this IotHub
  returned: always
  type: list
  sample: null
  contains:
    id:
      description:
        - The resource identifier.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The resource type.
      returned: always
      type: str
      sample: null
    private_endpoint:
      description:
        - The private endpoint property of a private endpoint connection
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - The resource identifier.
          returned: always
          type: str
          sample: null
    private_link_service_connection_state:
      description:
        - The current state of a private endpoint connection
      returned: always
      type: dict
      sample: null
      contains:
        status:
          description:
            - The status of a private endpoint connection
          returned: always
          type: str
          sample: null
        description:
          description:
            - >-
              The description for the current state of a private endpoint
              connection
          returned: always
          type: str
          sample: null
        actions_required:
          description:
            - Actions required for a private endpoint connection
          returned: always
          type: str
          sample: null
provisioning_state:
  description:
    - The ARM provisioning state of the provisioning service.
  returned: always
  type: str
  sample: null
iot_hubs:
  description:
    - List of IoT hubs associated with this provisioning service.
  returned: always
  type: list
  sample: null
  contains:
    apply_allocation_policy:
      description:
        - flag for applying allocationPolicy or not for a given iot hub.
      returned: always
      type: bool
      sample: null
    allocation_weight:
      description:
        - weight to apply for a given iot h.
      returned: always
      type: integer
      sample: null
    name:
      description:
        - Host name of the IoT hub.
      returned: always
      type: str
      sample: null
    connection_string:
      description:
        - Connection string of the IoT hub.
      returned: always
      type: str
      sample: null
    location:
      description:
        - ARM region of the IoT hub.
      returned: always
      type: str
      sample: null
allocation_policy:
  description:
    - Allocation policy to be used by this provisioning service.
  returned: always
  type: str
  sample: null
service_operations_host_name:
  description:
    - Service endpoint for provisioning service.
  returned: always
  type: str
  sample: null
device_provisioning_host_name:
  description:
    - Device endpoint for this provisioning service.
  returned: always
  type: str
  sample: null
id_scope:
  description:
    - Unique identifier of this provisioning service.
  returned: always
  type: str
  sample: null
authorization_policies:
  description:
    - List of authorization keys for a provisioning service.
  returned: always
  type: list
  sample: null
  contains:
    key_name:
      description:
        - Name of the key.
      returned: always
      type: str
      sample: null
    primary_key:
      description:
        - Primary SAS key value.
      returned: always
      type: str
      sample: null
    secondary_key:
      description:
        - Secondary SAS key value.
      returned: always
      type: str
      sample: null
    rights:
      description:
        - Rights that this key has.
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
    from azure.mgmt.iot import iotDpsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMIotDpsResource(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            provisioning_service_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            etag=dict(
                type='str',
                disposition='/etag'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        choices=['S1']
                    ),
                    tier=dict(
                        type='str',
                        updatable=False,
                        disposition='tier'
                    ),
                    capacity=dict(
                        type='integer',
                        disposition='capacity'
                    )
                )
            ),
            state=dict(
                type='str',
                disposition='/state',
                choices=['Activating',
                         'Active',
                         'Deleting',
                         'Deleted',
                         'ActivationFailed',
                         'DeletionFailed',
                         'Transitioning',
                         'Suspending',
                         'Suspended',
                         'Resuming',
                         'FailingOver',
                         'FailoverFailed']
            ),
            encryption=dict(
                type='dict',
                disposition='/encryption',
                options=dict(
                    key_source=dict(
                        type='str',
                        disposition='key_source'
                    ),
                    key_vault_properties=dict(
                        type='list',
                        disposition='key_vault_properties',
                        elements='dict',
                        options=dict(
                            key_identifier=dict(
                                type='str',
                                disposition='key_identifier'
                            )
                        )
                    )
                )
            ),
            public_network_access=dict(
                type='str',
                disposition='/public_network_access',
                choices=['Enabled',
                         'Disabled']
            ),
            ip_filter_rules=dict(
                type='list',
                disposition='/ip_filter_rules',
                elements='dict',
                options=dict(
                    filter_name=dict(
                        type='str',
                        disposition='filter_name',
                        required=True
                    ),
                    action=dict(
                        type='sealed-choice',
                        disposition='action',
                        required=True
                    ),
                    ip_mask=dict(
                        type='str',
                        disposition='ip_mask',
                        required=True
                    ),
                    target=dict(
                        type='sealed-choice',
                        disposition='target'
                    )
                )
            ),
            private_endpoint_connections=dict(
                type='list',
                disposition='/private_endpoint_connections',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        updatable=False,
                        disposition='id'
                    ),
                    name=dict(
                        type='str',
                        updatable=False,
                        disposition='name'
                    ),
                    type=dict(
                        type='str',
                        updatable=False,
                        disposition='type'
                    ),
                    private_endpoint=dict(
                        type='dict',
                        disposition='private_endpoint',
                        options=dict(
                            id=dict(
                                type='str',
                                updatable=False,
                                disposition='id'
                            )
                        )
                    ),
                    private_link_service_connection_state=dict(
                        type='dict',
                        disposition='private_link_service_connection_state',
                        required=True,
                        options=dict(
                            status=dict(
                                type='str',
                                disposition='status',
                                choices=['Pending',
                                         'Approved',
                                         'Rejected',
                                         'Disconnected'],
                                required=True
                            ),
                            description=dict(
                                type='str',
                                disposition='description',
                                required=True
                            ),
                            actions_required=dict(
                                type='str',
                                disposition='actions_required'
                            )
                        )
                    )
                )
            ),
            provisioning_state=dict(
                type='str',
                disposition='/provisioning_state'
            ),
            iot_hubs=dict(
                type='list',
                disposition='/iot_hubs',
                elements='dict',
                options=dict(
                    apply_allocation_policy=dict(
                        type='bool',
                        disposition='apply_allocation_policy'
                    ),
                    allocation_weight=dict(
                        type='integer',
                        disposition='allocation_weight'
                    ),
                    name=dict(
                        type='str',
                        updatable=False,
                        disposition='name'
                    ),
                    connection_string=dict(
                        type='str',
                        disposition='connection_string',
                        required=True
                    ),
                    location=dict(
                        type='str',
                        disposition='location',
                        required=True
                    )
                )
            ),
            allocation_policy=dict(
                type='str',
                disposition='/allocation_policy',
                choices=['Hashed',
                         'GeoLatency',
                         'Static']
            ),
            authorization_policies=dict(
                type='list',
                disposition='/authorization_policies',
                elements='dict',
                options=dict(
                    key_name=dict(
                        type='str',
                        disposition='key_name',
                        required=True
                    ),
                    primary_key=dict(
                        type='str',
                        disposition='primary_key'
                    ),
                    secondary_key=dict(
                        type='str',
                        disposition='secondary_key'
                    ),
                    rights=dict(
                        type='str',
                        disposition='rights',
                        choices=['ServiceConfig',
                                 'EnrollmentRead',
                                 'EnrollmentWrite',
                                 'DeviceConnect',
                                 'RegistrationStatusRead',
                                 'RegistrationStatusWrite'],
                        required=True
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.provisioning_service_name = None
        self.resource_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMIotDpsResource, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(iotDpsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-09-01-preview')

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
            response = self.mgmt_client.iot_dps_resource.create_or_update(resource_group_name=self.resource_group_name,
                                                                          provisioning_service_name=self.provisioning_service_name,
                                                                          iot_dps_description=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the IotDpsResource instance.')
            self.fail('Error creating the IotDpsResource instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.iot_dps_resource.delete(provisioning_service_name=self.provisioning_service_name,
                                                                resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the IotDpsResource instance.')
            self.fail('Error deleting the IotDpsResource instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.iot_dps_resource.get(provisioning_service_name=self.provisioning_service_name,
                                                             resource_group_name=self.resource_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMIotDpsResource()


if __name__ == '__main__':
    main()
