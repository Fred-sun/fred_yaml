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
module: azure_rm_gateway
version_added: '2.9'
short_description: Manage Azure Gateway instance.
description:
  - 'Create, update and delete instance of Azure Gateway.'
options:
  resource_group_name:
    description:
      - Azure resource group name
    required: true
    type: str
  gateway_resource_name:
    description:
      - The identity of the gateway.
    required: true
    type: str
  location:
    description:
      - The geo-location where the resource lives
    type: str
  description:
    description:
      - User readable description of the gateway.
    type: str
  source_network:
    description:
      - Network the gateway should listen on for requests.
    type: dict
    suboptions:
      name:
        description:
          - Name of the network
        type: str
      endpoint_refs:
        description:
          - A list of endpoints that are exposed on this network.
        type: list
        suboptions:
          name:
            description:
              - Name of the endpoint.
            type: str
  destination_network:
    description:
      - Network that the Application is using.
    type: dict
    suboptions:
      name:
        description:
          - Name of the network
        type: str
      endpoint_refs:
        description:
          - A list of endpoints that are exposed on this network.
        type: list
        suboptions:
          name:
            description:
              - Name of the endpoint.
            type: str
  tcp:
    description:
      - Configuration for tcp connectivity for this gateway.
    type: list
    suboptions:
      name:
        description:
          - tcp gateway config name.
        required: true
        type: str
      port:
        description:
          - >-
            Specifies the port at which the service endpoint below needs to be
            exposed.
        required: true
        type: integer
      destination:
        description:
          - Describes destination endpoint for routing traffic.
        required: true
        type: dict
        suboptions:
          application_name:
            description:
              - Name of the service fabric Mesh application.
            required: true
            type: str
          service_name:
            description:
              - service that contains the endpoint.
            required: true
            type: str
          endpoint_name:
            description:
              - name of the endpoint in the service.
            required: true
            type: str
  http:
    description:
      - Configuration for http connectivity for this gateway.
    type: list
    suboptions:
      name:
        description:
          - http gateway config name.
        required: true
        type: str
      port:
        description:
          - >-
            Specifies the port at which the service endpoint below needs to be
            exposed.
        required: true
        type: integer
      hosts:
        description:
          - description for routing.
        required: true
        type: list
        suboptions:
          name:
            description:
              - http hostname config name.
            required: true
            type: str
          routes:
            description:
              - >-
                Route information to use for routing. Routes are processed in
                the order they are specified. Specify routes that are more
                specific before routes that can handle general cases.
            required: true
            type: list
            suboptions:
              name:
                description:
                  - http route name.
                required: true
                type: str
              match:
                description:
                  - Describes a rule for http route matching.
                required: true
                type: dict
                suboptions:
                  path:
                    description:
                      - Path to match for routing.
                    required: true
                    type: dict
                    suboptions:
                      value:
                        description:
                          - Uri path to match for request.
                        required: true
                        type: str
                      rewrite:
                        description:
                          - replacement string for matched part of the Uri.
                        type: str
                      type:
                        description:
                          - how to match value in the Uri
                        required: true
                        type: str
                        choices:
                          - prefix
                  headers:
                    description:
                      - headers and their values to match in request.
                    type: list
                    suboptions:
                      name:
                        description:
                          - Name of header to match in request.
                        required: true
                        type: str
                      value:
                        description:
                          - Value of header to match in request.
                        type: str
                      type:
                        description:
                          - how to match header value
                        type: str
                        choices:
                          - exact
              destination:
                description:
                  - Describes destination endpoint for routing traffic.
                required: true
                type: dict
                suboptions:
                  application_name:
                    description:
                      - Name of the service fabric Mesh application.
                    required: true
                    type: str
                  service_name:
                    description:
                      - service that contains the endpoint.
                    required: true
                    type: str
                  endpoint_name:
                    description:
                      - name of the endpoint in the service.
                    required: true
                    type: str
  state:
    description:
      - Assert the state of the Gateway.
      - >-
        Use C(present) to create or update an Gateway and C(absent) to delete
        it.
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
    - name: CreateOrUpdateGateway
      azure_rm_gateway: 
        gateway_resource_name: sampleGateway
        resource_group_name: sbz_demo
        

    - name: DeleteGateway
      azure_rm_gateway: 
        gateway_resource_name: sampleGateway
        resource_group_name: sbz_demo
        

'''

RETURN = '''
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
provisioning_state:
  description:
    - State of the resource.
  returned: always
  type: str
  sample: null
description:
  description:
    - User readable description of the gateway.
  returned: always
  type: str
  sample: null
source_network:
  description:
    - Network the gateway should listen on for requests.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - Name of the network
      returned: always
      type: str
      sample: null
    endpoint_refs:
      description:
        - A list of endpoints that are exposed on this network.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - Name of the endpoint.
          returned: always
          type: str
          sample: null
destination_network:
  description:
    - Network that the Application is using.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - Name of the network
      returned: always
      type: str
      sample: null
    endpoint_refs:
      description:
        - A list of endpoints that are exposed on this network.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - Name of the endpoint.
          returned: always
          type: str
          sample: null
tcp:
  description:
    - Configuration for tcp connectivity for this gateway.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - tcp gateway config name.
      returned: always
      type: str
      sample: null
    port:
      description:
        - >-
          Specifies the port at which the service endpoint below needs to be
          exposed.
      returned: always
      type: integer
      sample: null
    destination:
      description:
        - Describes destination endpoint for routing traffic.
      returned: always
      type: dict
      sample: null
      contains:
        application_name:
          description:
            - Name of the service fabric Mesh application.
          returned: always
          type: str
          sample: null
        service_name:
          description:
            - service that contains the endpoint.
          returned: always
          type: str
          sample: null
        endpoint_name:
          description:
            - name of the endpoint in the service.
          returned: always
          type: str
          sample: null
http:
  description:
    - Configuration for http connectivity for this gateway.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - http gateway config name.
      returned: always
      type: str
      sample: null
    port:
      description:
        - >-
          Specifies the port at which the service endpoint below needs to be
          exposed.
      returned: always
      type: integer
      sample: null
    hosts:
      description:
        - description for routing.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - http hostname config name.
          returned: always
          type: str
          sample: null
        routes:
          description:
            - >-
              Route information to use for routing. Routes are processed in the
              order they are specified. Specify routes that are more specific
              before routes that can handle general cases.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - http route name.
              returned: always
              type: str
              sample: null
            match:
              description:
                - Describes a rule for http route matching.
              returned: always
              type: dict
              sample: null
              contains:
                path:
                  description:
                    - Path to match for routing.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    value:
                      description:
                        - Uri path to match for request.
                      returned: always
                      type: str
                      sample: null
                    rewrite:
                      description:
                        - replacement string for matched part of the Uri.
                      returned: always
                      type: str
                      sample: null
                    type:
                      description:
                        - how to match value in the Uri
                      returned: always
                      type: str
                      sample: null
                headers:
                  description:
                    - headers and their values to match in request.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    name:
                      description:
                        - Name of header to match in request.
                      returned: always
                      type: str
                      sample: null
                    value:
                      description:
                        - Value of header to match in request.
                      returned: always
                      type: str
                      sample: null
                    type:
                      description:
                        - how to match header value
                      returned: always
                      type: str
                      sample: null
            destination:
              description:
                - Describes destination endpoint for routing traffic.
              returned: always
              type: dict
              sample: null
              contains:
                application_name:
                  description:
                    - Name of the service fabric Mesh application.
                  returned: always
                  type: str
                  sample: null
                service_name:
                  description:
                    - service that contains the endpoint.
                  returned: always
                  type: str
                  sample: null
                endpoint_name:
                  description:
                    - name of the endpoint in the service.
                  returned: always
                  type: str
                  sample: null
status:
  description:
    - Status of the resource.
  returned: always
  type: str
  sample: null
status_details:
  description:
    - Gives additional information about the current status of the gateway.
  returned: always
  type: str
  sample: null
ip_address:
  description:
    - >-
      IP address of the gateway. This is populated in the response and is
      ignored for incoming requests.
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
    from azure.mgmt.service import ServiceFabricMeshManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMGateway(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            gateway_resource_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            source_network=dict(
                type='dict',
                disposition='/source_network',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    endpoint_refs=dict(
                        type='list',
                        disposition='endpoint_refs',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name'
                            )
                        )
                    )
                )
            ),
            destination_network=dict(
                type='dict',
                disposition='/destination_network',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    endpoint_refs=dict(
                        type='list',
                        disposition='endpoint_refs',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name'
                            )
                        )
                    )
                )
            ),
            tcp=dict(
                type='list',
                disposition='/tcp',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    port=dict(
                        type='integer',
                        disposition='port',
                        required=True
                    ),
                    destination=dict(
                        type='dict',
                        disposition='destination',
                        required=True,
                        options=dict(
                            application_name=dict(
                                type='str',
                                disposition='application_name',
                                required=True
                            ),
                            service_name=dict(
                                type='str',
                                disposition='service_name',
                                required=True
                            ),
                            endpoint_name=dict(
                                type='str',
                                disposition='endpoint_name',
                                required=True
                            )
                        )
                    )
                )
            ),
            http=dict(
                type='list',
                disposition='/http',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    port=dict(
                        type='integer',
                        disposition='port',
                        required=True
                    ),
                    hosts=dict(
                        type='list',
                        disposition='hosts',
                        required=True,
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name',
                                required=True
                            ),
                            routes=dict(
                                type='list',
                                disposition='routes',
                                required=True,
                                elements='dict',
                                options=dict(
                                    name=dict(
                                        type='str',
                                        disposition='name',
                                        required=True
                                    ),
                                    match=dict(
                                        type='dict',
                                        disposition='match',
                                        required=True,
                                        options=dict(
                                            path=dict(
                                                type='dict',
                                                disposition='path',
                                                required=True,
                                                options=dict(
                                                    value=dict(
                                                        type='str',
                                                        disposition='value',
                                                        required=True
                                                    ),
                                                    rewrite=dict(
                                                        type='str',
                                                        disposition='rewrite'
                                                    ),
                                                    type=dict(
                                                        type='str',
                                                        disposition='type',
                                                        choices=['prefix'],
                                                        required=True
                                                    )
                                                )
                                            ),
                                            headers=dict(
                                                type='list',
                                                disposition='headers',
                                                elements='dict',
                                                options=dict(
                                                    name=dict(
                                                        type='str',
                                                        disposition='name',
                                                        required=True
                                                    ),
                                                    value=dict(
                                                        type='str',
                                                        disposition='value'
                                                    ),
                                                    type=dict(
                                                        type='str',
                                                        disposition='type',
                                                        choices=['exact']
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                    destination=dict(
                                        type='dict',
                                        disposition='destination',
                                        required=True,
                                        options=dict(
                                            application_name=dict(
                                                type='str',
                                                disposition='application_name',
                                                required=True
                                            ),
                                            service_name=dict(
                                                type='str',
                                                disposition='service_name',
                                                required=True
                                            ),
                                            endpoint_name=dict(
                                                type='str',
                                                disposition='endpoint_name',
                                                required=True
                                            )
                                        )
                                    )
                                )
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
        self.gateway_resource_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGateway, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ServiceFabricMeshManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.gateway.create(resource_group_name=self.resource_group_name,
                                                           gateway_resource_name=self.gateway_resource_name,
                                                           gateway_resource_description=self.body)
            else:
                response = self.mgmt_client.gateway.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Gateway instance.')
            self.fail('Error creating the Gateway instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.gateway.delete(resource_group_name=self.resource_group_name,
                                                       gateway_resource_name=self.gateway_resource_name)
        except CloudError as e:
            self.log('Error attempting to delete the Gateway instance.')
            self.fail('Error deleting the Gateway instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.gateway.get(resource_group_name=self.resource_group_name,
                                                    gateway_resource_name=self.gateway_resource_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGateway()


if __name__ == '__main__':
    main()
