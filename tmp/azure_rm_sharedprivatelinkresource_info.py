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
module: azure_rm_sharedprivatelinkresource_info
version_added: '2.9'
short_description: Get SharedPrivateLinkResource info.
description:
  - Get info of SharedPrivateLinkResource.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group within the current subscription. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  search_service_name:
    description:
      - >-
        The name of the Azure Cognitive Search service associated with the
        specified resource group.
    required: true
    type: str
  shared_private_link_resource_name:
    description:
      - >-
        The name of the shared private link resource managed by the Azure
        Cognitive Search service within the specified resource group.
    type: str
  clientrequestid:
    description:
      - >-
        A client-generated GUID value that identifies this request. If
        specified, this will be included in response information as a way to
        track the request.
    required: true
    type: uuid
  search_management_request_options:
    description:
      - Parameter group
    required: true
    type: group
    suboptions:
      client_request_id:
        description:
          - >-
            A client-generated GUID value that identifies this request. If
            specified, this will be included in response information as a way to
            track the request.
        type: uuid
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: SharedPrivateLinkResourceGet
      azure_rm_sharedprivatelinkresource_info: 
        resource_group_name: rg1
        search_service_name: mysearchservice
        shared_private_link_resource_name: testResource
        

    - name: ListSharedPrivateLinkResourcesByService
      azure_rm_sharedprivatelinkresource_info: 
        resource_group_name: rg1
        search_service_name: mysearchservice
        

'''

RETURN = '''
shared_private_link_resources:
  description: >-
    A list of dict results where the key is the name of the
    SharedPrivateLinkResource and the values are the facts for that
    SharedPrivateLinkResource.
  returned: always
  type: complex
  contains:
    id:
      description:
        - >-
          Fully qualified resource Id for the resource. Ex -
          /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource
      returned: always
      type: str
      sample: null
    type:
      description:
        - >-
          The type of the resource. Ex- Microsoft.Compute/virtualMachines or
          Microsoft.Storage/storageAccounts.
      returned: always
      type: str
      sample: null
    properties:
      description:
        - >-
          Describes the properties of a Shared Private Link Resource managed by
          the Azure Cognitive Search service.
      returned: always
      type: dict
      sample: null
      contains:
        private_link_resource_id:
          description:
            - >-
              The resource id of the resource the shared private link resource
              is for.
          returned: always
          type: str
          sample: null
        group_id:
          description:
            - >-
              The group id from the provider of resource the shared private link
              resource is for.
          returned: always
          type: str
          sample: null
        request_message:
          description:
            - >-
              The request message for requesting approval of the shared private
              link resource.
          returned: always
          type: str
          sample: null
        resource_region:
          description:
            - >-
              Optional. Can be used to specify the Azure Resource Manager
              location of the resource to which a shared private link is to be
              created. This is only required for those resources whose DNS
              configuration are regional (such as Azure Kubernetes Service).
          returned: always
          type: str
          sample: null
        status:
          description:
            - >-
              Status of the shared private link resource. Can be Pending,
              Approved, Rejected or Disconnected.
          returned: always
          type: sealed-choice
          sample: null
        provisioning_state:
          description:
            - >-
              The provisioning state of the shared private link resource. Can be
              Updating, Deleting, Failed, Succeeded or Incomplete.
          returned: always
          type: sealed-choice
          sample: null
    value:
      description:
        - The list of Shared Private Link Resources.
      returned: always
      type: list
      sample: null
      contains:
        properties:
          description:
            - >-
              Describes the properties of a Shared Private Link Resource managed
              by the Azure Cognitive Search service.
          returned: always
          type: dict
          sample: null
          contains:
            private_link_resource_id:
              description:
                - >-
                  The resource id of the resource the shared private link
                  resource is for.
              returned: always
              type: str
              sample: null
            group_id:
              description:
                - >-
                  The group id from the provider of resource the shared private
                  link resource is for.
              returned: always
              type: str
              sample: null
            request_message:
              description:
                - >-
                  The request message for requesting approval of the shared
                  private link resource.
              returned: always
              type: str
              sample: null
            resource_region:
              description:
                - >-
                  Optional. Can be used to specify the Azure Resource Manager
                  location of the resource to which a shared private link is to
                  be created. This is only required for those resources whose
                  DNS configuration are regional (such as Azure Kubernetes
                  Service).
              returned: always
              type: str
              sample: null
            status:
              description:
                - >-
                  Status of the shared private link resource. Can be Pending,
                  Approved, Rejected or Disconnected.
              returned: always
              type: sealed-choice
              sample: null
            provisioning_state:
              description:
                - >-
                  The provisioning state of the shared private link resource.
                  Can be Updating, Deleting, Failed, Succeeded or Incomplete.
              returned: always
              type: sealed-choice
              sample: null
    next_link:
      description:
        - >-
          The URL to get the next set of shared private link resources, if there
          are any.
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
    from azure.mgmt.search import SearchManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSharedPrivateLinkResourceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            search_service_name=dict(
                type='str',
                required=True
            ),
            shared_private_link_resource_name=dict(
                type='str'
            ),
            clientrequestid=dict(
                type='uuid',
                required=True
            ),
            search_management_request_options=dict(
                type='group',
                required=True,
                options=dict(
                    client_request_id=dict(
                        type='uuid'
                    )
                )
            )
        )

        self.resource_group_name = None
        self.search_service_name = None
        self.shared_private_link_resource_name = None
        self.clientrequestid = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-08-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSharedPrivateLinkResourceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SearchManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-08-01')

        if (self.resource_group_name is not None and
            self.search_service_name is not None and
            self.shared_private_link_resource_name is not None):
            self.results['shared_private_link_resources'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.search_service_name is not None):
            self.results['shared_private_link_resources'] = self.format_item(self.listbyservice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.shared_private_link_resources.get(resource_group_name=self.resource_group_name,
                                                                          search_service_name=self.search_service_name,
                                                                          shared_private_link_resource_name=self.shared_private_link_resource_name,
                                                                          clientrequestid=self.clientrequestid,
                                                                          parameters=self.body)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyservice(self):
        response = None

        try:
            response = self.mgmt_client.shared_private_link_resources.list_by_service(clientrequestid=self.clientrequestid,
                                                                                      resource_group_name=self.resource_group_name,
                                                                                      search_service_name=self.search_service_name,
                                                                                      parameters=self.body)
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
    AzureRMSharedPrivateLinkResourceInfo()


if __name__ == '__main__':
    main()
