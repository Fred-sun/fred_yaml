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
module: azure_rm_iotdpsresource_info
version_added: '2.9'
short_description: Get IotDpsResource info.
description:
  - Get info of IotDpsResource.
options:
  provisioning_service_name:
    description:
      - Name of the provisioning service to retrieve.
      - Name of provisioning service that the operation is running on.
      - Name of provisioning service.
    type: str
  resource_group_name:
    description:
      - Resource group name.
      - Resource group identifier.
      - Name of resource group.
      - The name of the resource group that contains the provisioning service.
    type: str
  operation_id:
    description:
      - >-
        Operation id corresponding to long running operation. Use this to poll
        for the status.
    type: str
  asyncinfo:
    description:
      - >-
        Async header used to poll on the status of the operation, obtained while
        creating the long running operation.
    type: str
  resource_name:
    description:
      - The name of the provisioning service.
    type: str
  group_id:
    description:
      - The name of the private link resource
    type: str
  private_endpoint_connection_name:
    description:
      - The name of the private endpoint connection
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: DPSGet
      azure_rm_iotdpsresource_info: 
        provisioning_service_name: myFirstProvisioningService
        resource_group_name: myResourceGroup
        

    - name: DPSListBySubscription
      azure_rm_iotdpsresource_info: 
        {}
        

    - name: DPSListByResourceGroup
      azure_rm_iotdpsresource_info: 
        resource_group_name: myResourceGroup
        

    - name: DPSGetOperationResult
      azure_rm_iotdpsresource_info: 
        operation_id: MTY5OTNmZDctODI5Yy00N2E2LTkxNDQtMDU1NGIyYzY1ZjRl
        asyncinfo: '1508265712453'
        provisioning_service_name: myFirstProvisioningService
        resource_group_name: myResourceGroup
        

    - name: DPSGetValidSku
      azure_rm_iotdpsresource_info: 
        provisioning_service_name: myFirstProvisioningService
        resource_group_name: myResourceGroup
        

    - name: PrivateLinkResources_List
      azure_rm_iotdpsresource_info: 
        resource_group_name: myResourceGroup
        resource_name: myFirstProvisioningService
        

    - name: PrivateEndpointConnections_List
      azure_rm_iotdpsresource_info: 
        resource_group_name: myResourceGroup
        resource_name: myFirstProvisioningService
        

    - name: PrivateEndpointConnection_Get
      azure_rm_iotdpsresource_info: 
        private_endpoint_connection_name: myPrivateEndpointConnection
        resource_group_name: myResourceGroup
        resource_name: myFirstProvisioningService
        

'''

RETURN = '''
iot_dps_resource:
  description: >-
    A list of dict results where the key is the name of the IotDpsResource and
    the values are the facts for that IotDpsResource.
  returned: always
  type: complex
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
          The Etag field is *not* required. If it is provided in the response
          body, it must also be provided as a header per the normal ETag
          convention.
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
              A string that contains the IP address range in CIDR notation for
              the rule.
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
    value:
      description:
        - >-
          List of provisioning service descriptions.

          The list of SKUs

          The list of available private link resources for a provisioning
          service
      returned: always
      type: list
      sample: null
      contains:
        etag:
          description:
            - >-
              The Etag field is *not* required. If it is provided in the
              response body, it must also be provided as a header per the normal
              ETag convention.
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
                  A string that contains the IP address range in CIDR notation
                  for the rule.
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
                      The description for the current state of a private
                      endpoint connection
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
    next_link:
      description:
        - |-
          the next link
          The next link.
      returned: always
      type: str
      sample: null
    status:
      description:
        - current status of a long running operation.
      returned: always
      type: str
      sample: null
    error:
      description:
        - 'Error message containing code, description and details'
      returned: always
      type: dict
      sample: null
      contains:
        code:
          description:
            - standard error code
          returned: always
          type: str
          sample: null
        message:
          description:
            - standard error description
          returned: always
          type: str
          sample: null
        details:
          description:
            - detailed summary of error
          returned: always
          type: str
          sample: null
    properties:
      description:
        - The properties for a group information object
      returned: always
      type: dict
      sample: null
      contains:
        group_id:
          description:
            - The group id
          returned: always
          type: str
          sample: null
        required_members:
          description:
            - The required members for a specific group id
          returned: always
          type: list
          sample: null
        required_zone_names:
          description:
            - The required DNS zones for a specific group id
          returned: always
          type: list
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

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.iot import iotDpsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMIotDpsResourceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            provisioning_service_name=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str'
            ),
            operation_id=dict(
                type='str'
            ),
            asyncinfo=dict(
                type='str'
            ),
            resource_name=dict(
                type='str'
            ),
            group_id=dict(
                type='str'
            ),
            private_endpoint_connection_name=dict(
                type='str'
            )
        )

        self.provisioning_service_name = None
        self.resource_group_name = None
        self.operation_id = None
        self.asyncinfo = None
        self.resource_name = None
        self.group_id = None
        self.private_endpoint_connection_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-09-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMIotDpsResourceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(iotDpsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-09-01-preview')

        if (self.operation_id is not None and
            self.resource_group_name is not None and
            self.provisioning_service_name is not None and
            self.asyncinfo is not None):
            self.results['iot_dps_resource'] = self.format_item(self.getoperationresult())
        elif (self.resource_group_name is not None and
              self.resource_name is not None and
              self.group_id is not None):
            self.results['iot_dps_resource'] = self.format_item(self.getprivatelinkresource())
        elif (self.resource_group_name is not None and
              self.resource_name is not None and
              self.private_endpoint_connection_name is not None):
            self.results['iot_dps_resource'] = self.format_item(self.getprivateendpointconnection())
        elif (self.provisioning_service_name is not None and
              self.resource_group_name is not None):
            self.results['iot_dps_resource'] = self.format_item(self.get())
        elif (self.provisioning_service_name is not None and
              self.resource_group_name is not None):
            self.results['iot_dps_resource'] = self.format_item(self.listvalidsku())
        elif (self.resource_group_name is not None and
              self.resource_name is not None):
            self.results['iot_dps_resource'] = self.format_item(self.listprivatelinkresource())
        elif (self.resource_group_name is not None and
              self.resource_name is not None):
            self.results['iot_dps_resource'] = self.format_item(self.listprivateendpointconnection())
        elif (self.resource_group_name is not None):
            self.results['iot_dps_resource'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['iot_dps_resource'] = self.format_item(self.listbysubscription())
        return self.results

    def getoperationresult(self):
        response = None

        try:
            response = self.mgmt_client.iot_dps_resource.get_operation_result(operation_id=self.operation_id,
                                                                              resource_group_name=self.resource_group_name,
                                                                              provisioning_service_name=self.provisioning_service_name,
                                                                              asyncinfo=self.asyncinfo)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getprivatelinkresource(self):
        response = None

        try:
            response = self.mgmt_client.iot_dps_resource.get_private_link_resource(resource_group_name=self.resource_group_name,
                                                                                   resource_name=self.resource_name,
                                                                                   group_id=self.group_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getprivateendpointconnection(self):
        response = None

        try:
            response = self.mgmt_client.iot_dps_resource.get_private_endpoint_connection(resource_group_name=self.resource_group_name,
                                                                                         resource_name=self.resource_name,
                                                                                         private_endpoint_connection_name=self.private_endpoint_connection_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.iot_dps_resource.get(provisioning_service_name=self.provisioning_service_name,
                                                             resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listvalidsku(self):
        response = None

        try:
            response = self.mgmt_client.iot_dps_resource.list_valid_sku(provisioning_service_name=self.provisioning_service_name,
                                                                        resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listprivatelinkresource(self):
        response = None

        try:
            response = self.mgmt_client.iot_dps_resource.list_private_link_resource(resource_group_name=self.resource_group_name,
                                                                                    resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listprivateendpointconnection(self):
        response = None

        try:
            response = self.mgmt_client.iot_dps_resource.list_private_endpoint_connection(resource_group_name=self.resource_group_name,
                                                                                          resource_name=self.resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.iot_dps_resource.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.iot_dps_resource.list_by_subscription()
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
    AzureRMIotDpsResourceInfo()


if __name__ == '__main__':
    main()
