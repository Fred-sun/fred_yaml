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
module: azure_rm_order_info
version_added: '2.9'
short_description: Get Order info.
description:
  - Get info of Order.
options:
  device_name:
    description:
      - The device name.
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: OrderGetAllInDevice
      azure_rm_order_info: 
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        

    - name: OrderGet
      azure_rm_order_info: 
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        

'''

RETURN = '''
orders:
  description: >-
    A list of dict results where the key is the name of the Order and the values
    are the facts for that Order.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of orders.
      returned: always
      type: list
      sample: null
      contains:
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
              Tracking information for the package delivered to the customer
              whether it has an original or a replacement device.
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
              Tracking information for the package returned from the customer
              whether it has an original or a replacement device.
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
    next_link:
      description:
        - Link to the next set of results.
      returned: always
      type: str
      sample: null
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
          Tracking information for the package delivered to the customer whether
          it has an original or a replacement device.
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
          Tracking information for the package returned from the customer
          whether it has an original or a replacement device.
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.data import DataBoxEdgeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMOrderInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            )
        )

        self.device_name = None
        self.resource_group_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-08-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMOrderInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DataBoxEdgeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-08-01')

        if (self.device_name is not None and
            self.resource_group_name is not None):
            self.results['orders'] = self.format_item(self.listbydataboxedgedevice())
        elif (self.device_name is not None and
              self.resource_group_name is not None):
            self.results['orders'] = self.format_item(self.get())
        return self.results

    def listbydataboxedgedevice(self):
        response = None

        try:
            response = self.mgmt_client.orders.list_by_data_box_edge_device(device_name=self.device_name,
                                                                            resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.orders.get(device_name=self.device_name,
                                                   resource_group_name=self.resource_group_name)
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
    AzureRMOrderInfo()


if __name__ == '__main__':
    main()
