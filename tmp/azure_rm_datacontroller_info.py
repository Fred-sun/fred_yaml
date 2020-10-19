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
module: azure_rm_datacontroller_info
version_added: '2.9'
short_description: Get DataController info.
description:
  - Get info of DataController.
options:
  resource_group_name:
    description:
      - The name of the Azure resource group
    type: str
  data_controller_name:
    description:
      - undefined
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets all dataControllers in a subscription.
      azure_rm_datacontroller_info: 
        {}
        

    - name: Gets all dataControllers in a resource group.
      azure_rm_datacontroller_info: 
        resource_group_name: testrg
        

    - name: Get a data controller.
      azure_rm_datacontroller_info: 
        data_controller_name: testdataController
        resource_group_name: testrg
        

'''

RETURN = '''
data_controllers:
  description: >-
    A list of dict results where the key is the name of the DataController and
    the values are the facts for that DataController.
  returned: always
  type: complex
  contains:
    value:
      description:
        - ''
      returned: always
      type: list
      sample: null
      contains:
        on_premise_property:
          description:
            - Properties from the on premise data controller
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - >-
                  A globally unique ID identifying the associated on premise
                  cluster
              returned: always
              type: uuid
              sample: null
            public_signing_key:
              description:
                - >-
                  Certificate that contains the on premise cluster public key
                  used to verify signing
              returned: always
              type: str
              sample: null
            signing_certificate_thumbprint:
              description:
                - >-
                  Unique thumbprint returned to customer to verify the
                  certificate being uploaded
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    location:
      description:
        - The geo-location where the resource lives
      returned: always
      type: str
      sample: null
    system_data:
      description:
        - Read only system data
      returned: always
      type: dict
      sample: null
      contains:
        created_by:
          description:
            - An identifier for the identity that created the resource
          returned: always
          type: str
          sample: null
        created_by_type:
          description:
            - The type of identity that created the resource
          returned: always
          type: str
          sample: null
        created_at:
          description:
            - The timestamp of resource creation (UTC)
          returned: always
          type: str
          sample: null
        last_modified_by:
          description:
            - An identifier for the identity that last modified the resource
          returned: always
          type: str
          sample: null
        last_modified_by_type:
          description:
            - The type of identity that last modified the resource
          returned: always
          type: str
          sample: null
        last_modified_at:
          description:
            - The timestamp of resource last modification (UTC)
          returned: always
          type: str
          sample: null
    on_premise_property:
      description:
        - Properties from the on premise data controller
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - A globally unique ID identifying the associated on premise cluster
          returned: always
          type: uuid
          sample: null
        public_signing_key:
          description:
            - >-
              Certificate that contains the on premise cluster public key used
              to verify signing
          returned: always
          type: str
          sample: null
        signing_certificate_thumbprint:
          description:
            - >-
              Unique thumbprint returned to customer to verify the certificate
              being uploaded
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
    from azure.mgmt.azure import AzureDataManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDataControllerInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            data_controller_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.data_controller_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-07-24-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDataControllerInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AzureDataManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-07-24-preview')

        if (self.resource_group_name is not None and
            self.data_controller_name is not None):
            self.results['data_controllers'] = self.format_item(self.getdatacontroller())
        elif (self.resource_group_name is not None):
            self.results['data_controllers'] = self.format_item(self.listingroup())
        else:
            self.results['data_controllers'] = self.format_item(self.listinsubscription())
        return self.results

    def getdatacontroller(self):
        response = None

        try:
            response = self.mgmt_client.data_controllers.get_data_controller(resource_group_name=self.resource_group_name,
                                                                             data_controller_name=self.data_controller_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listingroup(self):
        response = None

        try:
            response = self.mgmt_client.data_controllers.list_in_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listinsubscription(self):
        response = None

        try:
            response = self.mgmt_client.data_controllers.list_in_subscription()
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
    AzureRMDataControllerInfo()


if __name__ == '__main__':
    main()
