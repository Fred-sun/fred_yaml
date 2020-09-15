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
module: azure_rm_environmentsetting_info
version_added: '2.9'
short_description: Get EnvironmentSetting info.
description:
  - Get info of EnvironmentSetting.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  lab_account_name:
    description:
      - The name of the lab Account.
    required: true
    type: str
  lab_name:
    description:
      - The name of the lab.
    required: true
    type: str
  expand:
    description:
      - >-
        Specify the $expand query. Example:
        'properties($select=publishingState)'
    required: true
    type: str
  filter:
    description:
      - The filter to apply to the operation.
    type: str
  top:
    description:
      - The maximum number of resources to return from the operation.
    type: integer
  orderby:
    description:
      - 'The ordering expression for the results, using OData notation.'
    type: str
  environment_setting_name:
    description:
      - The name of the environment Setting.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
environment_settings:
  description: >-
    A list of dict results where the key is the name of the EnvironmentSetting
    and the values are the facts for that EnvironmentSetting.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Results of the list operation.
      returned: always
      type: list
      sample: null
      contains:
        publishing_state:
          description:
            - Describes the readiness of this environment setting
          returned: always
          type: str
          sample: null
        configuration_state:
          description:
            - >-
              Describes the user's progress in configuring their environment
              setting
          returned: always
          type: str
          sample: null
        description:
          description:
            - Describes the environment and its resource settings
          returned: always
          type: str
          sample: null
        title:
          description:
            - Brief title describing the environment and its resource settings
          returned: always
          type: str
          sample: null
        last_changed:
          description:
            - Time when the template VM was last changed.
          returned: always
          type: str
          sample: null
        last_published:
          description:
            - Time when the template VM was last sent for publishing.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - The provisioning status of the resource.
          returned: always
          type: str
          sample: null
        unique_identifier:
          description:
            - The unique immutable identifier of a resource (Guid).
          returned: always
          type: str
          sample: null
        latest_operation_result:
          description:
            - 'The details of the latest operation. ex: status, error'
          returned: always
          type: dict
          sample: null
          contains:
            status:
              description:
                - The current status of the operation.
              returned: always
              type: str
              sample: null
            error_code:
              description:
                - Error code on failure.
              returned: always
              type: str
              sample: null
            error_message:
              description:
                - The error message.
              returned: always
              type: str
              sample: null
            request_uri:
              description:
                - Request URI of the operation.
              returned: always
              type: str
              sample: null
            http_method:
              description:
                - The HttpMethod - PUT/POST/DELETE for the operation.
              returned: always
              type: str
              sample: null
            operation_url:
              description:
                - The URL to use to check long-running operation status
              returned: always
              type: str
              sample: null
        id_properties_resource_settings_id:
          description:
            - The unique id of the resource setting
          returned: always
          type: str
          sample: null
        gallery_image_resource_id:
          description:
            - >-
              The resource id of the gallery image used for creating the virtual
              machine
          returned: always
          type: str
          sample: null
        image_name:
          description:
            - The name of the image used to created the environment setting
          returned: always
          type: str
          sample: null
        size:
          description:
            - The size of the virtual machine
          returned: always
          type: str
          sample: null
        cores:
          description:
            - The translated compute cores of the virtual machine
          returned: always
          type: integer
          sample: null
        reference_vm:
          description:
            - Details specific to Reference Vm
          returned: always
          type: dict
          sample: null
          contains:
            user_name:
              description:
                - The username of the virtual machine
              returned: always
              type: str
              sample: null
            password:
              description:
                - >-
                  The password of the virtual machine. This will be set to null
                  in GET resource API
              returned: always
              type: str
              sample: null
            vm_state_details:
              description:
                - The state details for the reference virtual machine.
              returned: always
              type: dict
              sample: null
              contains:
                rdp_authority:
                  description:
                    - >-
                      The RdpAuthority property is a server DNS host name or IP
                      address followed by the service port number for RDP
                      (Remote Desktop Protocol).
                  returned: always
                  type: str
                  sample: null
                ssh_authority:
                  description:
                    - >-
                      The SshAuthority property is a server DNS host name or IP
                      address followed by the service port number for SSH.
                  returned: always
                  type: str
                  sample: null
                power_state:
                  description:
                    - The power state of the reference virtual machine.
                  returned: always
                  type: str
                  sample: null
                last_known_power_state:
                  description:
                    - Last known compute power state captured in DTL
                  returned: always
                  type: str
                  sample: null
            vm_resource_id:
              description:
                - VM resource Id for the environment
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - Link for next set of results.
      returned: always
      type: str
      sample: null
    id:
      description:
        - The identifier of the resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The type of the resource.
      returned: always
      type: str
      sample: null
    location:
      description:
        - The location of the resource.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - The tags of the resource.
      returned: always
      type: dictionary
      sample: null
    publishing_state:
      description:
        - Describes the readiness of this environment setting
      returned: always
      type: str
      sample: null
    configuration_state:
      description:
        - Describes the user's progress in configuring their environment setting
      returned: always
      type: str
      sample: null
    description:
      description:
        - Describes the environment and its resource settings
      returned: always
      type: str
      sample: null
    title:
      description:
        - Brief title describing the environment and its resource settings
      returned: always
      type: str
      sample: null
    last_changed:
      description:
        - Time when the template VM was last changed.
      returned: always
      type: str
      sample: null
    last_published:
      description:
        - Time when the template VM was last sent for publishing.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning status of the resource.
      returned: always
      type: str
      sample: null
    unique_identifier:
      description:
        - The unique immutable identifier of a resource (Guid).
      returned: always
      type: str
      sample: null
    latest_operation_result:
      description:
        - 'The details of the latest operation. ex: status, error'
      returned: always
      type: dict
      sample: null
      contains:
        status:
          description:
            - The current status of the operation.
          returned: always
          type: str
          sample: null
        error_code:
          description:
            - Error code on failure.
          returned: always
          type: str
          sample: null
        error_message:
          description:
            - The error message.
          returned: always
          type: str
          sample: null
        request_uri:
          description:
            - Request URI of the operation.
          returned: always
          type: str
          sample: null
        http_method:
          description:
            - The HttpMethod - PUT/POST/DELETE for the operation.
          returned: always
          type: str
          sample: null
        operation_url:
          description:
            - The URL to use to check long-running operation status
          returned: always
          type: str
          sample: null
    id_properties_resource_settings_id:
      description:
        - The unique id of the resource setting
      returned: always
      type: str
      sample: null
    gallery_image_resource_id:
      description:
        - >-
          The resource id of the gallery image used for creating the virtual
          machine
      returned: always
      type: str
      sample: null
    image_name:
      description:
        - The name of the image used to created the environment setting
      returned: always
      type: str
      sample: null
    size:
      description:
        - The size of the virtual machine
      returned: always
      type: str
      sample: null
    cores:
      description:
        - The translated compute cores of the virtual machine
      returned: always
      type: integer
      sample: null
    reference_vm:
      description:
        - Details specific to Reference Vm
      returned: always
      type: dict
      sample: null
      contains:
        user_name:
          description:
            - The username of the virtual machine
          returned: always
          type: str
          sample: null
        password:
          description:
            - >-
              The password of the virtual machine. This will be set to null in
              GET resource API
          returned: always
          type: str
          sample: null
        vm_state_details:
          description:
            - The state details for the reference virtual machine.
          returned: always
          type: dict
          sample: null
          contains:
            rdp_authority:
              description:
                - >-
                  The RdpAuthority property is a server DNS host name or IP
                  address followed by the service port number for RDP (Remote
                  Desktop Protocol).
              returned: always
              type: str
              sample: null
            ssh_authority:
              description:
                - >-
                  The SshAuthority property is a server DNS host name or IP
                  address followed by the service port number for SSH.
              returned: always
              type: str
              sample: null
            power_state:
              description:
                - The power state of the reference virtual machine.
              returned: always
              type: str
              sample: null
            last_known_power_state:
              description:
                - Last known compute power state captured in DTL
              returned: always
              type: str
              sample: null
        vm_resource_id:
          description:
            - VM resource Id for the environment
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
    from azure.mgmt.managed import ManagedLabsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMEnvironmentSettingInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            lab_account_name=dict(
                type='str',
                required=True
            ),
            lab_name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str',
                required=True
            ),
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            orderby=dict(
                type='str'
            ),
            environment_setting_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.lab_account_name = None
        self.lab_name = None
        self.expand = None
        self.filter = None
        self.top = None
        self.orderby = None
        self.environment_setting_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-10-15'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMEnvironmentSettingInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ManagedLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-10-15')

        if (self.resource_group_name is not None and
            self.lab_account_name is not None and
            self.lab_name is not None and
            self.environment_setting_name is not None):
            self.results['environment_settings'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.lab_account_name is not None and
              self.lab_name is not None):
            self.results['environment_settings'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.environment_settings.get(resource_group_name=self.resource_group_name,
                                                                 lab_account_name=self.lab_account_name,
                                                                 lab_name=self.lab_name,
                                                                 environment_setting_name=self.environment_setting_name,
                                                                 expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.environment_settings.list(resource_group_name=self.resource_group_name,
                                                                  lab_account_name=self.lab_account_name,
                                                                  lab_name=self.lab_name,
                                                                  expand=self.expand,
                                                                  filter=self.filter,
                                                                  top=self.top,
                                                                  orderby=self.orderby)
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
    AzureRMEnvironmentSettingInfo()


if __name__ == '__main__':
    main()
