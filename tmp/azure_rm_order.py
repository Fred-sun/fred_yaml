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
module: azure_rm_order
version_added: '2.9'
short_description: Manage Azure Order instance.
description:
  - 'Create, update and delete instance of Azure Order.'
options:
  device_name:
    description:
      - The device name.
      - The order details of a device.
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name.
    required: true
    type: str
  contact_information:
    description:
      - The contact details.
    type: dict
    suboptions:
      contact_person:
        description:
          - The contact person name.
        required: true
        type: str
      company_name:
        description:
          - The name of the company.
        required: true
        type: str
      phone:
        description:
          - The phone number.
        required: true
        type: str
      email_list:
        description:
          - The email list.
        required: true
        type: list
  shipping_address:
    description:
      - The shipping address.
    type: dict
    suboptions:
      address_line1:
        description:
          - The address line1.
        required: true
        type: str
      address_line2:
        description:
          - The address line2.
        type: str
      address_line3:
        description:
          - The address line3.
        type: str
      postal_code:
        description:
          - The postal code.
        required: true
        type: str
      city:
        description:
          - The city name.
        required: true
        type: str
      state:
        description:
          - The state name.
        required: true
        type: str
      country:
        description:
          - The country name.
        required: true
        type: str
  status:
    description:
      - Status of the order as per the allowed status types.
    type: str
    choices:
      - Untracked
      - AwaitingFulfilment
      - AwaitingPreparation
      - AwaitingShipment
      - Shipped
      - Arriving
      - Delivered
      - ReplacementRequested
      - LostDevice
      - Declined
      - ReturnInitiated
      - AwaitingReturnShipment
      - ShippedBack
      - CollectedAtMicrosoft
  comments:
    description:
      - Comments related to this status change.
    type: str
  state:
    description:
      - Assert the state of the Order.
      - Use C(present) to create or update an Order and C(absent) to delete it.
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
    - name: OrderPut
      azure_rm_order: 
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        properties:
          contact_information:
            company_name: Microsoft
            contact_person: John Mcclane
            email_list:
              - john@microsoft.com
            phone: (800) 426-9400
          shipping_address:
            address_line1: Microsoft Corporation
            address_line2: One Microsoft Way
            address_line3: Redmond
            city: WA
            country: USA
            postal_code: '98052'
            state: WA
        

    - name: OrderDelete
      azure_rm_order: 
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        

'''

RETURN = '''
id:
  description:
    - The path ID that uniquely identifies the object.
  returned: always
  type: str
  sample: null
name:
  description:
    - The object name.
  returned: always
  type: str
  sample: null
type:
  description:
    - The hierarchical type of the object.
  returned: always
  type: str
  sample: null
contact_information:
  description:
    - The contact details.
  returned: always
  type: dict
  sample: null
  contains:
    contact_person:
      description:
        - The contact person name.
      returned: always
      type: str
      sample: null
    company_name:
      description:
        - The name of the company.
      returned: always
      type: str
      sample: null
    phone:
      description:
        - The phone number.
      returned: always
      type: str
      sample: null
    email_list:
      description:
        - The email list.
      returned: always
      type: list
      sample: null
shipping_address:
  description:
    - The shipping address.
  returned: always
  type: dict
  sample: null
  contains:
    address_line1:
      description:
        - The address line1.
      returned: always
      type: str
      sample: null
    address_line2:
      description:
        - The address line2.
      returned: always
      type: str
      sample: null
    address_line3:
      description:
        - The address line3.
      returned: always
      type: str
      sample: null
    postal_code:
      description:
        - The postal code.
      returned: always
      type: str
      sample: null
    city:
      description:
        - The city name.
      returned: always
      type: str
      sample: null
    state:
      description:
        - The state name.
      returned: always
      type: str
      sample: null
    country:
      description:
        - The country name.
      returned: always
      type: str
      sample: null
order_history:
  description:
    - List of status changes in the order.
  returned: always
  type: list
  sample: null
  contains:
    status:
      description:
        - Status of the order as per the allowed status types.
      returned: always
      type: str
      sample: null
    update_date_time:
      description:
        - Time of status update.
      returned: always
      type: str
      sample: null
    comments:
      description:
        - Comments related to this status change.
      returned: always
      type: str
      sample: null
    additional_order_details:
      description:
        - "Dictionary to hold generic information which is not stored\r\nby the already existing properties"
      returned: always
      type: dictionary
      sample: null
serial_number:
  description:
    - Serial number of the device.
  returned: always
  type: str
  sample: null
delivery_tracking_info:
  description:
    - >-
      Tracking information for the package delivered to the customer whether it
      has an original or a replacement device.
  returned: always
  type: list
  sample: null
  contains:
    serial_number:
      description:
        - Serial number of the device being tracked.
      returned: always
      type: str
      sample: null
    carrier_name:
      description:
        - Name of the carrier used in the delivery.
      returned: always
      type: str
      sample: null
    tracking_id:
      description:
        - Tracking ID of the shipment.
      returned: always
      type: str
      sample: null
    tracking_url:
      description:
        - Tracking URL of the shipment.
      returned: always
      type: str
      sample: null
return_tracking_info:
  description:
    - >-
      Tracking information for the package returned from the customer whether it
      has an original or a replacement device.
  returned: always
  type: list
  sample: null
  contains:
    serial_number:
      description:
        - Serial number of the device being tracked.
      returned: always
      type: str
      sample: null
    carrier_name:
      description:
        - Name of the carrier used in the delivery.
      returned: always
      type: str
      sample: null
    tracking_id:
      description:
        - Tracking ID of the shipment.
      returned: always
      type: str
      sample: null
    tracking_url:
      description:
        - Tracking URL of the shipment.
      returned: always
      type: str
      sample: null
status:
  description:
    - Status of the order as per the allowed status types.
  returned: always
  type: str
  sample: null
update_date_time:
  description:
    - Time of status update.
  returned: always
  type: str
  sample: null
comments:
  description:
    - Comments related to this status change.
  returned: always
  type: str
  sample: null
additional_order_details:
  description:
    - "Dictionary to hold generic information which is not stored\r\nby the already existing properties"
  returned: always
  type: dictionary
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.data import DataBoxEdgeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMOrder(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            contact_information=dict(
                type='dict',
                disposition='/contact_information',
                options=dict(
                    contact_person=dict(
                        type='str',
                        disposition='contact_person',
                        required=True
                    ),
                    company_name=dict(
                        type='str',
                        disposition='company_name',
                        required=True
                    ),
                    phone=dict(
                        type='str',
                        disposition='phone',
                        required=True
                    ),
                    email_list=dict(
                        type='list',
                        disposition='email_list',
                        required=True,
                        elements='str'
                    )
                )
            ),
            shipping_address=dict(
                type='dict',
                disposition='/shipping_address',
                options=dict(
                    address_line1=dict(
                        type='str',
                        disposition='address_line1',
                        required=True
                    ),
                    address_line2=dict(
                        type='str',
                        disposition='address_line2'
                    ),
                    address_line3=dict(
                        type='str',
                        disposition='address_line3'
                    ),
                    postal_code=dict(
                        type='str',
                        disposition='postal_code',
                        required=True
                    ),
                    city=dict(
                        type='str',
                        disposition='city',
                        required=True
                    ),
                    state=dict(
                        type='str',
                        disposition='state',
                        required=True
                    ),
                    country=dict(
                        type='str',
                        disposition='country',
                        required=True
                    )
                )
            ),
            status=dict(
                type='str',
                disposition='/status',
                choices=['Untracked',
                         'AwaitingFulfilment',
                         'AwaitingPreparation',
                         'AwaitingShipment',
                         'Shipped',
                         'Arriving',
                         'Delivered',
                         'ReplacementRequested',
                         'LostDevice',
                         'Declined',
                         'ReturnInitiated',
                         'AwaitingReturnShipment',
                         'ShippedBack',
                         'CollectedAtMicrosoft']
            ),
            comments=dict(
                type='str',
                disposition='/comments'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.device_name = None
        self.resource_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMOrder, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DataBoxEdgeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-08-01')

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
            response = self.mgmt_client.orders.create_or_update(device_name=self.device_name,
                                                                resource_group_name=self.resource_group_name,
                                                                order=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Order instance.')
            self.fail('Error creating the Order instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.orders.delete(device_name=self.device_name,
                                                      resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the Order instance.')
            self.fail('Error deleting the Order instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.orders.get(device_name=self.device_name,
                                                   resource_group_name=self.resource_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMOrder()


if __name__ == '__main__':
    main()
