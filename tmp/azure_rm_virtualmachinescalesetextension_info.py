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
module: azure_rm_virtualmachinescalesetextension_info
version_added: '2.9'
short_description: Get VirtualMachineScaleSetExtension info.
description:
  - Get info of VirtualMachineScaleSetExtension.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  vm_scale_set_name:
    description:
      - The name of the VM scale set containing the extension.
    required: true
    type: str
  vmss_extension_name:
    description:
      - The name of the VM scale set extension.
    type: str
  expand:
    description:
      - The expand expression to apply on the operation.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
virtual_machine_scale_set_extensions:
  description: >-
    A list of dict results where the key is the name of the
    VirtualMachineScaleSetExtension and the values are the facts for that
    VirtualMachineScaleSetExtension.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the extension.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type
      returned: always
      type: str
      sample: null
    force_update_tag:
      description:
        - >-
          If a value is provided and is different from the previous value, the
          extension handler will be forced to update even if the extension
          configuration has not changed.
      returned: always
      type: str
      sample: null
    publisher:
      description:
        - The name of the extension handler publisher.
      returned: always
      type: str
      sample: null
    type_properties_type:
      description:
        - >-
          Specifies the type of the extension; an example is
          "CustomScriptExtension".
      returned: always
      type: str
      sample: null
    type_handler_version:
      description:
        - Specifies the version of the script handler.
      returned: always
      type: str
      sample: null
    auto_upgrade_minor_version:
      description:
        - >-
          Indicates whether the extension should use a newer minor version if
          one is available at deployment time. Once deployed, however, the
          extension will not upgrade minor versions unless redeployed, even with
          this property set to true.
      returned: always
      type: bool
      sample: null
    enable_automatic_upgrade:
      description:
        - >-
          Indicates whether the extension should be automatically upgraded by
          the platform if there is a newer version of the extension available.
      returned: always
      type: bool
      sample: null
    settings:
      description:
        - Json formatted public settings for the extension.
      returned: always
      type: any
      sample: null
    protected_settings:
      description:
        - >-
          The extension can contain either protectedSettings or
          protectedSettingsFromKeyVault or no protected settings at all.
      returned: always
      type: any
      sample: null
    provisioning_state:
      description:
        - 'The provisioning state, which only appears in the response.'
      returned: always
      type: str
      sample: null
    provision_after_extensions:
      description:
        - >-
          Collection of extension names after which this extension needs to be
          provisioned.
      returned: always
      type: list
      sample: null
    value:
      description:
        - The list of VM scale set extensions.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The name of the extension.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type
          returned: always
          type: str
          sample: null
        force_update_tag:
          description:
            - >-
              If a value is provided and is different from the previous value,
              the extension handler will be forced to update even if the
              extension configuration has not changed.
          returned: always
          type: str
          sample: null
        publisher:
          description:
            - The name of the extension handler publisher.
          returned: always
          type: str
          sample: null
        type_properties_type:
          description:
            - >-
              Specifies the type of the extension; an example is
              "CustomScriptExtension".
          returned: always
          type: str
          sample: null
        type_handler_version:
          description:
            - Specifies the version of the script handler.
          returned: always
          type: str
          sample: null
        auto_upgrade_minor_version:
          description:
            - >-
              Indicates whether the extension should use a newer minor version
              if one is available at deployment time. Once deployed, however,
              the extension will not upgrade minor versions unless redeployed,
              even with this property set to true.
          returned: always
          type: bool
          sample: null
        enable_automatic_upgrade:
          description:
            - >-
              Indicates whether the extension should be automatically upgraded
              by the platform if there is a newer version of the extension
              available.
          returned: always
          type: bool
          sample: null
        settings:
          description:
            - Json formatted public settings for the extension.
          returned: always
          type: any
          sample: null
        protected_settings:
          description:
            - >-
              The extension can contain either protectedSettings or
              protectedSettingsFromKeyVault or no protected settings at all.
          returned: always
          type: any
          sample: null
        provisioning_state:
          description:
            - 'The provisioning state, which only appears in the response.'
          returned: always
          type: str
          sample: null
        provision_after_extensions:
          description:
            - >-
              Collection of extension names after which this extension needs to
              be provisioned.
          returned: always
          type: list
          sample: null
    next_link:
      description:
        - >-
          The uri to fetch the next page of VM scale set extensions. Call
          ListNext() with this to fetch the next page of VM scale set
          extensions.
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
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMVirtualMachineScaleSetExtensionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            vm_scale_set_name=dict(
                type='str',
                required=True
            ),
            vmss_extension_name=dict(
                type='str'
            ),
            expand=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.vm_scale_set_name = None
        self.vmss_extension_name = None
        self.expand = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVirtualMachineScaleSetExtensionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.vm_scale_set_name is not None and
            self.vmss_extension_name is not None):
            self.results['virtual_machine_scale_set_extensions'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.vm_scale_set_name is not None):
            self.results['virtual_machine_scale_set_extensions'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_set_extensions.get(resource_group_name=self.resource_group_name,
                                                                                 vm_scale_set_name=self.vm_scale_set_name,
                                                                                 vmss_extension_name=self.vmss_extension_name,
                                                                                 expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_set_extensions.list(resource_group_name=self.resource_group_name,
                                                                                  vm_scale_set_name=self.vm_scale_set_name)
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
    AzureRMVirtualMachineScaleSetExtensionInfo()


if __name__ == '__main__':
    main()
