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
module: azure_rm_privateendpoint
version_added: '2.9'
short_description: Manage Azure PrivateEndpoint instance.
description:
  - 'Create, update and delete instance of Azure PrivateEndpoint.'
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  cluster_name:
    description:
      - The name of the cluster.
    required: true
    type: str
  private_endpoint_name:
    description:
      - The name of the private endpoint.
    required: true
    type: str
  if_match:
    description:
      - >-
        The ETag of the resource. Omit this value to always overwrite the
        current record set. Specify the last-seen ETag value to prevent
        accidentally overwriting concurrent changes.
    type: str
  if_none_match:
    description:
      - >-
        Set to '*' to allow a new resource to be created, but to prevent
        updating an existing record set. Other values will result in a 412
        Pre-condition Failed response.
    type: str
  manual_private_link_service_connections:
    description:
      - A list of connections to the remote resource. Immutable after it is set.
    type: list
    suboptions:
      private_link_service_id:
        description:
          - >-
            The resource id of the private link service. Required on PUT
            (CreateOrUpdate) requests.
        type: str
      group_ids:
        description:
          - >-
            The ID(s) of the group(s) obtained from the remote resource that
            this private endpoint should connect to. Required on PUT
            (CreateOrUpdate) requests.
        type: list
      request_message:
        description:
          - >-
            A message passed to the owner of the remote resource with this
            connection request. Restricted to 140 chars.
        type: str
      private_link_service_connection_state:
        description:
          - >-
            A collection of read-only information about the state of the
            connection to the private remote resource.
        type: dict
        suboptions:
          status:
            description:
              - >-
                Indicates whether the connection has been
                Approved/Rejected/Removed by the owner of the remote
                resource/service.
            type: str
          description:
            description:
              - The reason for approval/rejection of the connection.
            type: str
          actions_required:
            description:
              - >-
                A message indicating if changes on the service provider require
                any updates on the consumer.
            type: str
  state:
    description:
      - Assert the state of the PrivateEndpoint.
      - >-
        Use C(present) to create or update an PrivateEndpoint and C(absent) to
        delete it.
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
    - name: Create a private endpoint
      azure_rm_privateendpoint: 
        cluster_name: testcluster
        private_endpoint_name: testpe
        resource_group_name: sjrg
        

    - name: Delete a private endpoint
      azure_rm_privateendpoint: 
        cluster_name: testcluster
        private_endpoint_name: testpe
        resource_group_name: sjrg
        

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
etag:
  description:
    - >-
      Unique opaque string (generally a GUID) that represents the metadata state
      of the resource (private endpoint) and changes whenever the resource is
      updated. Required on PUT (CreateOrUpdate) requests.
  returned: always
  type: str
  sample: null
created_date:
  description:
    - The date when this private endpoint was created.
  returned: always
  type: str
  sample: null
manual_private_link_service_connections:
  description:
    - A list of connections to the remote resource. Immutable after it is set.
  returned: always
  type: list
  sample: null
  contains:
    private_link_service_id:
      description:
        - >-
          The resource id of the private link service. Required on PUT
          (CreateOrUpdate) requests.
      returned: always
      type: str
      sample: null
    group_ids:
      description:
        - >-
          The ID(s) of the group(s) obtained from the remote resource that this
          private endpoint should connect to. Required on PUT (CreateOrUpdate)
          requests.
      returned: always
      type: list
      sample: null
    request_message:
      description:
        - >-
          A message passed to the owner of the remote resource with this
          connection request. Restricted to 140 chars.
      returned: always
      type: str
      sample: null
    private_link_service_connection_state:
      description:
        - >-
          A collection of read-only information about the state of the
          connection to the private remote resource.
      returned: always
      type: dict
      sample: null
      contains:
        status:
          description:
            - >-
              Indicates whether the connection has been
              Approved/Rejected/Removed by the owner of the remote
              resource/service.
          returned: always
          type: str
          sample: null
        description:
          description:
            - The reason for approval/rejection of the connection.
          returned: always
          type: str
          sample: null
        actions_required:
          description:
            - >-
              A message indicating if changes on the service provider require
              any updates on the consumer.
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
    from azure.mgmt.stream import Stream Analytics Management Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMPrivateEndpoint(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            cluster_name=dict(
                type='str',
                required=True
            ),
            private_endpoint_name=dict(
                type='str',
                required=True
            ),
            if_match=dict(
                type='str'
            ),
            if_none_match=dict(
                type='str'
            ),
            manual_private_link_service_connections=dict(
                type='list',
                disposition='/manual_private_link_service_connections',
                elements='dict',
                options=dict(
                    private_link_service_id=dict(
                        type='str',
                        disposition='private_link_service_id'
                    ),
                    group_ids=dict(
                        type='list',
                        disposition='group_ids',
                        elements='str'
                    ),
                    request_message=dict(
                        type='str',
                        disposition='request_message'
                    ),
                    private_link_service_connection_state=dict(
                        type='dict',
                        disposition='private_link_service_connection_state',
                        options=dict(
                            status=dict(
                                type='str',
                                updatable=False,
                                disposition='status'
                            ),
                            description=dict(
                                type='str',
                                updatable=False,
                                disposition='description'
                            ),
                            actions_required=dict(
                                type='str',
                                updatable=False,
                                disposition='actions_required'
                            )
                        )
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
        self.cluster_name = None
        self.private_endpoint_name = None
        self.if_match = None
        self.if_none_match = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPrivateEndpoint, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Stream Analytics Management Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-03-01-preview')

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
            response = self.mgmt_client.private_endpoints.create_or_update(resource_group_name=self.resource_group_name,
                                                                           cluster_name=self.cluster_name,
                                                                           private_endpoint_name=self.private_endpoint_name,
                                                                           if_match=self.if_match,
                                                                           if_none_match=self.if_none_match,
                                                                           private_endpoint=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the PrivateEndpoint instance.')
            self.fail('Error creating the PrivateEndpoint instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.private_endpoints.delete(resource_group_name=self.resource_group_name,
                                                                 cluster_name=self.cluster_name,
                                                                 private_endpoint_name=self.private_endpoint_name)
        except CloudError as e:
            self.log('Error attempting to delete the PrivateEndpoint instance.')
            self.fail('Error deleting the PrivateEndpoint instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.private_endpoints.get(resource_group_name=self.resource_group_name,
                                                              cluster_name=self.cluster_name,
                                                              private_endpoint_name=self.private_endpoint_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPrivateEndpoint()


if __name__ == '__main__':
    main()
