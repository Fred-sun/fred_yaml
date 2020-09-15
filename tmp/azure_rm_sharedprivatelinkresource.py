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
module: azure_rm_sharedprivatelinkresource
version_added: '2.9'
short_description: Manage Azure SharedPrivateLinkResource instance.
description:
  - 'Create, update and delete instance of Azure SharedPrivateLinkResource.'
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
    required: true
    type: str
  clientrequestid:
    description:
      - >-
        A client-generated GUID value that identifies this request. If
        specified, this will be included in response information as a way to
        track the request.
    type: uuid
  properties:
    description:
      - >-
        Describes the properties of a Shared Private Link Resource managed by
        the Azure Cognitive Search service.
    type: dict
    suboptions:
      private_link_resource_id:
        description:
          - >-
            The resource id of the resource the shared private link resource is
            for.
        type: str
      group_id:
        description:
          - >-
            The group id from the provider of resource the shared private link
            resource is for.
        type: str
      request_message:
        description:
          - >-
            The request message for requesting approval of the shared private
            link resource.
        type: str
      resource_region:
        description:
          - >-
            Optional. Can be used to specify the Azure Resource Manager location
            of the resource to which a shared private link is to be created.
            This is only required for those resources whose DNS configuration
            are regional (such as Azure Kubernetes Service).
        type: str
      status:
        description:
          - >-
            Status of the shared private link resource. Can be Pending,
            Approved, Rejected or Disconnected.
        type: sealed-choice
      provisioning_state:
        description:
          - >-
            The provisioning state of the shared private link resource. Can be
            Updating, Deleting, Failed, Succeeded or Incomplete.
        type: sealed-choice
  search_management_request_options:
    description:
      - Parameter group
    type: group
    suboptions:
      client_request_id:
        description:
          - >-
            A client-generated GUID value that identifies this request. If
            specified, this will be included in response information as a way to
            track the request.
        type: uuid
  client_request_id:
    description:
      - >-
        A client-generated GUID value that identifies this request. If
        specified, this will be included in response information as a way to
        track the request.
    type: uuid
  state:
    description:
      - Assert the state of the SharedPrivateLinkResource.
      - >-
        Use C(present) to create or update an SharedPrivateLinkResource and
        C(absent) to delete it.
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
    - name: SharedPrivateLinkResourceCreateOrUpdate
      azure_rm_sharedprivatelinkresource: 
        resource_group_name: rg1
        search_service_name: mysearchservice
        shared_private_link_resource_name: testResource
        

    - name: SharedPrivateLinkResourceDelete
      azure_rm_sharedprivatelinkresource: 
        resource_group_name: rg1
        search_service_name: mysearchservice
        shared_private_link_resource_name: testResource
        

'''

RETURN = '''
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
      Describes the properties of a Shared Private Link Resource managed by the
      Azure Cognitive Search service.
  returned: always
  type: dict
  sample: null
  contains:
    private_link_resource_id:
      description:
        - >-
          The resource id of the resource the shared private link resource is
          for.
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
          The request message for requesting approval of the shared private link
          resource.
      returned: always
      type: str
      sample: null
    resource_region:
      description:
        - >-
          Optional. Can be used to specify the Azure Resource Manager location
          of the resource to which a shared private link is to be created. This
          is only required for those resources whose DNS configuration are
          regional (such as Azure Kubernetes Service).
      returned: always
      type: str
      sample: null
    status:
      description:
        - >-
          Status of the shared private link resource. Can be Pending, Approved,
          Rejected or Disconnected.
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

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.search import SearchManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSharedPrivateLinkResource(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            clientrequestid=dict(
                type='uuid'
            ),
            properties=dict(
                type='dict',
                disposition='/properties',
                options=dict(
                    private_link_resource_id=dict(
                        type='str',
                        disposition='private_link_resource_id'
                    ),
                    group_id=dict(
                        type='str',
                        disposition='group_id'
                    ),
                    request_message=dict(
                        type='str',
                        disposition='request_message'
                    ),
                    resource_region=dict(
                        type='str',
                        disposition='resource_region'
                    ),
                    status=dict(
                        type='sealed-choice',
                        disposition='status'
                    ),
                    provisioning_state=dict(
                        type='sealed-choice',
                        disposition='provisioning_state'
                    )
                )
            ),
            search_management_request_options=dict(
                type='group',
                disposition='/search_management_request_options',
                options=dict(
                    client_request_id=dict(
                        type='uuid',
                        disposition='client_request_id'
                    )
                )
            ),
            client_request_id=dict(
                type='uuid'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.search_service_name = None
        self.shared_private_link_resource_name = None
        self.clientrequestid = None
        self.client_request_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSharedPrivateLinkResource, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SearchManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-08-01')

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
            response = self.mgmt_client.shared_private_link_resources.create_or_update(resource_group_name=self.resource_group_name,
                                                                                       search_service_name=self.search_service_name,
                                                                                       shared_private_link_resource_name=self.shared_private_link_resource_name,
                                                                                       clientrequestid=self.clientrequestid,
                                                                                       shared_private_link_resource=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SharedPrivateLinkResource instance.')
            self.fail('Error creating the SharedPrivateLinkResource instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.shared_private_link_resources.delete(resource_group_name=self.resource_group_name,
                                                                             search_service_name=self.search_service_name,
                                                                             shared_private_link_resource_name=self.shared_private_link_resource_name,
                                                                             clientrequestid=self.clientrequestid,
                                                                             parameters=self.body)
        except CloudError as e:
            self.log('Error attempting to delete the SharedPrivateLinkResource instance.')
            self.fail('Error deleting the SharedPrivateLinkResource instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.shared_private_link_resources.get(resource_group_name=self.resource_group_name,
                                                                          search_service_name=self.search_service_name,
                                                                          shared_private_link_resource_name=self.shared_private_link_resource_name,
                                                                          clientrequestid=self.clientrequestid,
                                                                          parameters=self.body)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSharedPrivateLinkResource()


if __name__ == '__main__':
    main()
