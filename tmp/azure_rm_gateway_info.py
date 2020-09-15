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
module: azure_rm_gateway_info
version_added: '2.9'
short_description: Get Gateway info.
description:
  - Get info of Gateway.
options:
  resource_group_name:
    description:
      - Azure resource group name
    type: str
  gateway_resource_name:
    description:
      - The identity of the gateway.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetGateway
      azure_rm_gateway_info: 
        gateway_resource_name: sampleGateway
        resource_group_name: sbz_demo
        

    - name: ListGatewaysByResourceGroup
      azure_rm_gateway_info: 
        resource_group_name: sbz_demo
        

    - name: ListGatewaysBySubscriptionId
      azure_rm_gateway_info: 
        {}
        

'''

RETURN = '''
gateway:
  description: >-
    A list of dict results where the key is the name of the Gateway and the
    values are the facts for that Gateway.
  returned: always
  type: complex
  contains:
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
                  Route information to use for routing. Routes are processed in
                  the order they are specified. Specify routes that are more
                  specific before routes that can handle general cases.
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
    value:
      description:
        - One page of the list.
      returned: always
      type: list
      sample: null
      contains:
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
                  Specifies the port at which the service endpoint below needs
                  to be exposed.
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
                  Specifies the port at which the service endpoint below needs
                  to be exposed.
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
                      Route information to use for routing. Routes are processed
                      in the order they are specified. Specify routes that are
                      more specific before routes that can handle general cases.
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
                                - >-
                                  replacement string for matched part of the
                                  Uri.
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
            - >-
              Gives additional information about the current status of the
              gateway.
          returned: always
          type: str
          sample: null
        ip_address:
          description:
            - >-
              IP address of the gateway. This is populated in the response and
              is ignored for incoming requests.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - URI to fetch the next page of the list.
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
    from azure.mgmt.service import ServiceFabricMeshManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMGatewayInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            gateway_resource_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.gateway_resource_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-09-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMGatewayInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceFabricMeshManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

        if (self.resource_group_name is not None and
            self.gateway_resource_name is not None):
            self.results['gateway'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['gateway'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['gateway'] = self.format_item(self.listbysubscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.gateway.get(resource_group_name=self.resource_group_name,
                                                    gateway_resource_name=self.gateway_resource_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.gateway.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscription(self):
        response = None

        try:
            response = self.mgmt_client.gateway.list_by_subscription()
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
    AzureRMGatewayInfo()


if __name__ == '__main__':
    main()
