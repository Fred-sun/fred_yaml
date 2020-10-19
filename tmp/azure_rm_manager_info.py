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
module: azure_rm_manager_info
version_added: '2.9'
short_description: Get Manager info.
description:
  - Get info of Manager.
options:
  resource_group_name:
    description:
      - The resource group name
    type: str
  manager_name:
    description:
      - The manager name
    type: str
  filter:
    description:
      - OData Filter options
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ManagersList
      azure_rm_manager_info: 
        {}
        

    - name: ManagersListByResourceGroup
      azure_rm_manager_info: 
        resource_group_name: ResourceGroupForSDKTest
        

    - name: ManagersGet
      azure_rm_manager_info: 
        manager_name: ManagerForSDKTest2
        resource_group_name: ResourceGroupForSDKTest
        

    - name: ManagersGetEncryptionSettings
      azure_rm_manager_info: 
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: ManagersGetExtendedInfo
      azure_rm_manager_info: 
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: ManagersListFeatureSupportStatus
      azure_rm_manager_info: 
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: ManagersListMetrics
      azure_rm_manager_info: 
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

    - name: ManagersListMetricDefinition
      azure_rm_manager_info: 
        manager_name: ManagerForSDKTest1
        resource_group_name: ResourceGroupForSDKTest
        

'''

RETURN = '''
managers:
  description: >-
    A list of dict results where the key is the name of the Manager and the
    values are the facts for that Manager.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          The list of StorSimple managers.
          The value.
          The list of metric definitions.
      returned: always
      type: list
      sample: null
      contains:
        etag:
          description:
            - The etag of the manager.
          returned: always
          type: str
          sample: null
        cis_intrinsic_settings:
          description:
            - Represents the type of StorSimple Manager.
          returned: always
          type: dict
          sample: null
          contains:
            type:
              description:
                - The type of StorSimple Manager.
              returned: always
              type: sealed-choice
              sample: null
        sku:
          description:
            - Specifies the Sku.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Refers to the sku name which should be "Standard"
              returned: always
              type: constant
              sample: null
        provisioning_state:
          description:
            - >-
              Specifies the state of the resource as it is getting provisioned.
              Value of "Succeeded" means the Manager was successfully created.
          returned: always
          type: str
          sample: null
    id:
      description:
        - |-
          The resource ID.
          The path ID that uniquely identifies the object.
      returned: always
      type: str
      sample: null
    name:
      description:
        - |-
          The resource name.
          The name of the object.
      returned: always
      type: str
      sample: null
    type:
      description:
        - |-
          The resource type.
          The hierarchical type of the object.
      returned: always
      type: str
      sample: null
    location:
      description:
        - The geo location of the resource.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - The tags attached to the resource.
      returned: always
      type: dictionary
      sample: null
    etag:
      description:
        - |-
          The etag of the manager.
          The etag of the resource.
      returned: always
      type: str
      sample: null
    cis_intrinsic_settings:
      description:
        - Represents the type of StorSimple Manager.
      returned: always
      type: dict
      sample: null
      contains:
        type:
          description:
            - The type of StorSimple Manager.
          returned: always
          type: sealed-choice
          sample: null
    sku:
      description:
        - Specifies the Sku.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - Refers to the sku name which should be "Standard"
          returned: always
          type: constant
          sample: null
    provisioning_state:
      description:
        - >-
          Specifies the state of the resource as it is getting provisioned.
          Value of "Succeeded" means the Manager was successfully created.
      returned: always
      type: str
      sample: null
    kind:
      description:
        - The Kind of the object. Currently only Series8000 is supported
      returned: always
      type: constant
      sample: null
    encryption_status:
      description:
        - The encryption status to indicates if encryption is enabled or not.
      returned: always
      type: sealed-choice
      sample: null
    key_rollover_status:
      description:
        - >-
          The key rollover status to indicates if key rollover is required or
          not. If secret's encryption has been upgraded, then it requires key
          rollover.
      returned: always
      type: sealed-choice
      sample: null
    version:
      description:
        - The version of the extended info being persisted.
      returned: always
      type: str
      sample: null
    integrity_key:
      description:
        - Represents the CIK of the resource.
      returned: always
      type: str
      sample: null
    encryption_key:
      description:
        - Represents the CEK of the resource.
      returned: always
      type: str
      sample: null
    encryption_key_thumbprint:
      description:
        - Represents the Cert thumbprint that was used to encrypt the CEK.
      returned: always
      type: str
      sample: null
    portal_certificate_thumbprint:
      description:
        - >-
          Represents the portal thumbprint which can be used optionally to
          encrypt the entire data before storing it.
      returned: always
      type: str
      sample: null
    algorithm:
      description:
        - >-
          Represents the encryption algorithm used to encrypt the keys. None -
          if Key is saved in plain text format. Algorithm name - if key is
          encrypted
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
    from azure.mgmt.stor import StorSimple8000SeriesManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMManagerInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            manager_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.manager_name = None
        self.filter = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMManagerInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorSimple8000SeriesManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.resource_group_name is not None and
            self.manager_name is not None and
            self.filter is not None):
            self.results['managers'] = self.format_item(self.listmetric())
        elif (self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['managers'] = self.format_item(self.listfeaturesupportstatus())
        elif (self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['managers'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['managers'] = self.format_item(self.getencryptionsetting())
        elif (self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['managers'] = self.format_item(self.getextendedinfo())
        elif (self.resource_group_name is not None and
              self.manager_name is not None):
            self.results['managers'] = self.format_item(self.listmetricdefinition())
        elif (self.resource_group_name is not None):
            self.results['managers'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['managers'] = self.format_item(self.list())
        return self.results

    def listmetric(self):
        response = None

        try:
            response = self.mgmt_client.managers.list_metric(resource_group_name=self.resource_group_name,
                                                             manager_name=self.manager_name,
                                                             filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listfeaturesupportstatus(self):
        response = None

        try:
            response = self.mgmt_client.managers.list_feature_support_status(resource_group_name=self.resource_group_name,
                                                                             manager_name=self.manager_name,
                                                                             filter=self.filter)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.managers.get(resource_group_name=self.resource_group_name,
                                                     manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getencryptionsetting(self):
        response = None

        try:
            response = self.mgmt_client.managers.get_encryption_setting(resource_group_name=self.resource_group_name,
                                                                        manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getextendedinfo(self):
        response = None

        try:
            response = self.mgmt_client.managers.get_extended_info(resource_group_name=self.resource_group_name,
                                                                   manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listmetricdefinition(self):
        response = None

        try:
            response = self.mgmt_client.managers.list_metric_definition(resource_group_name=self.resource_group_name,
                                                                        manager_name=self.manager_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.managers.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.managers.list()
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
    AzureRMManagerInfo()


if __name__ == '__main__':
    main()
