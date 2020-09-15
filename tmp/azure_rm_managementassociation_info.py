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
module: azure_rm_managementassociation_info
version_added: '2.9'
short_description: Get ManagementAssociation info.
description:
  - Get info of ManagementAssociation.
options:
  resource_group_name:
    description:
      - The name of the resource group to get. The name is case insensitive.
    type: str
  providername:
    description:
      - Provider name for the parent resource.
    type: str
  resourcetype:
    description:
      - Resource type for the parent resource
    type: str
  resourcename:
    description:
      - Parent resource name.
    type: str
  management_association_name:
    description:
      - User ManagementAssociation Name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: SolutionList
      azure_rm_managementassociation_info: 
        {}
        

    - name: SolutionGet
      azure_rm_managementassociation_info: 
        management_association_name: managementAssociation1
        resource_group_name: rg1
        

'''

RETURN = '''
management_associations:
  description: >-
    A list of dict results where the key is the name of the
    ManagementAssociation and the values are the facts for that
    ManagementAssociation.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of Management Association properties within the subscription.
      returned: always
      type: list
      sample: null
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
        location:
          description:
            - Resource location
          returned: always
          type: str
          sample: null
        application_id:
          description:
            - The applicationId of the appliance for this association.
          returned: always
          type: str
          sample: null
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
    location:
      description:
        - Resource location
      returned: always
      type: str
      sample: null
    application_id:
      description:
        - The applicationId of the appliance for this association.
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
    from azure.mgmt.operations import OperationsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMManagementAssociationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            providername=dict(
                type='str'
            ),
            resourcetype=dict(
                type='str'
            ),
            resourcename=dict(
                type='str'
            ),
            management_association_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.providername = None
        self.resourcetype = None
        self.resourcename = None
        self.management_association_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2015-11-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMManagementAssociationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(OperationsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-11-01-preview')

        if (self.resource_group_name is not None and
            self.providername is not None and
            self.resourcetype is not None and
            self.resourcename is not None and
            self.management_association_name is not None):
            self.results['management_associations'] = self.format_item(self.get())
        else:
            self.results['management_associations'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.management_associations.get(resource_group_name=self.resource_group_name,
                                                                    providername=self.providername,
                                                                    resourcetype=self.resourcetype,
                                                                    resourcename=self.resourcename,
                                                                    management_association_name=self.management_association_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.management_associations.list_by_subscription()
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
    AzureRMManagementAssociationInfo()


if __name__ == '__main__':
    main()
