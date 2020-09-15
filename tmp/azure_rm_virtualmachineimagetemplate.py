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
module: azure_rm_virtualmachineimagetemplate
version_added: '2.9'
short_description: Manage Azure VirtualMachineImageTemplate instance.
description:
  - 'Create, update and delete instance of Azure VirtualMachineImageTemplate.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  image_template_name:
    description:
      - The name of the image Template
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  type:
    description:
      - >-
        The type of identity used for the image template. The type 'None' will
        remove any identities from the image template.
    type: sealed-choice
  user_assigned_identities:
    description:
      - >-
        The list of user identities associated with the image template. The user
        identity dictionary key references will be ARM resource ids in the form:
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
    type: dictionary
  source:
    description:
      - Specifies the properties used to describe the source image.
    type: dict
    suboptions:
      type:
        description:
          - Specifies the type of source image you want to start with.
        required: true
        type: str
  customize:
    description:
      - >-
        Specifies the properties used to describe the customization steps of the
        image, like Image source etc
    type: list
    suboptions:
      type:
        description:
          - >-
            The type of customization tool you want to use on the Image. For
            example, "Shell" can be shell customizer
        required: true
        type: str
      name:
        description:
          - >-
            Friendly Name to provide context on what this customization step
            does
        type: str
  distribute:
    description:
      - The distribution targets where the image output needs to go to.
    type: list
    suboptions:
      type:
        description:
          - Type of distribution.
        required: true
        type: str
      run_output_name:
        description:
          - The name to be used for the associated RunOutput.
        required: true
        type: str
      artifact_tags:
        description:
          - >-
            Tags that will be applied to the artifact once it has been
            created/updated by the distributor.
        type: dictionary
  build_timeout_in_minutes:
    description:
      - >-
        Maximum duration to wait while building the image template. Omit or
        specify 0 to use the default (4 hours).
    type: integer
  vm_size:
    description:
      - >-
        Size of the virtual machine used to build, customize and capture images.
        Omit or specify empty string to use the default (Standard_D1_v2).
    type: str
  os_disk_size_gb:
    description:
      - >-
        Size of the OS disk in GB. Omit or specify 0 to use Azure's default OS
        disk size.
    type: integer
  vnet_config:
    description:
      - >-
        Optional configuration of the virtual network to use to deploy the build
        virtual machine in. Omit if no specific virtual network needs to be
        used.
    type: dict
    suboptions:
      subnet_id:
        description:
          - Resource id of a pre-existing subnet.
        type: str
  state:
    description:
      - Assert the state of the VirtualMachineImageTemplate.
      - >-
        Use C(present) to create or update an VirtualMachineImageTemplate and
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
    - name: Create an Image Template for Linux.
      azure_rm_virtualmachineimagetemplate: 
        image_template_name: myImageTemplate
        resource_group_name: myResourceGroup
        identity:
          type: UserAssigned
          user_assigned_identities:
            /subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/rg1/providers/microsoft.managed_identity/user_assigned_identities/identity_1: {}
        location: westus
        properties:
          customize:
            - name: Shell Customizer Example
              type: Shell
              script_uri: 'https://example.com/path/to/script.sh'
          distribute:
            - type: ManagedImage
              artifact_tags:
                tag_name: value
              image_id: >-
                /subscriptions/{subscription-id}/resourceGroups/rg1/providers/Microsoft.Compute/images/image_it_1
              location: 1_location
              run_output_name: image_it_pir_1
          source:
            type: ManagedImage
            image_id: >-
              /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.Compute/images/source_image
          vm_profile:
            os_disk_size_gb: 64
            vm_size: Standard_D2s_v3
            vnet_config:
              subnet_id: >-
                /subscriptions/{subscription-id}/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/vnet_name/subnets/subnet_name
        tags:
          imagetemplate_tag1: IT_T1
          imagetemplate_tag2: IT_T2
        

    - name: Create an Image Template for Windows.
      azure_rm_virtualmachineimagetemplate: 
        image_template_name: myImageTemplate
        resource_group_name: myResourceGroup
        identity:
          type: UserAssigned
          user_assigned_identities:
            /subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/rg1/providers/microsoft.managed_identity/user_assigned_identities/identity_1: {}
        location: westus
        properties:
          customize:
            - name: PowerShell (inline) Customizer Example
              type: PowerShell
              inline:
                - Powershell command-1
                - Powershell command-2
                - Powershell command-3
            - name: PowerShell (script) Customizer Example
              type: PowerShell
              script_uri: 'https://example.com/path/to/script.ps1'
              valid_exit_codes:
                - 0
                - 1
            - name: Restart Customizer Example
              type: WindowsRestart
              restart_check_command: 'powershell -command "& {Write-Output ''restarted.''}"'
              restart_command: shutdown /f /r /t 0 /c "packer restart"
              restart_timeout: 10m
            - name: Windows Update Customizer Example
              type: WindowsUpdate
              filters:
                - $_.BrowseOnly
              search_criteria: BrowseOnly=0 and IsInstalled=0
              update_limit: 100
          distribute:
            - type: ManagedImage
              artifact_tags:
                tag_name: value
              image_id: >-
                /subscriptions/{subscription-id}/resourceGroups/rg1/providers/Microsoft.Compute/images/image_it_1
              location: 1_location
              run_output_name: image_it_pir_1
          source:
            type: ManagedImage
            image_id: >-
              /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.Compute/images/source_image
          vm_profile:
            os_disk_size_gb: 64
            vm_size: Standard_D2s_v3
            vnet_config:
              subnet_id: >-
                /subscriptions/{subscription-id}/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/vnet_name/subnets/subnet_name
        tags:
          imagetemplate_tag1: IT_T1
          imagetemplate_tag2: IT_T2
        

    - name: Remove identities for an Image Template.
      azure_rm_virtualmachineimagetemplate: 
        image_template_name: myImageTemplate
        resource_group_name: myResourceGroup
        identity:
          type: None
        

    - name: Update the tags for an Image Template.
      azure_rm_virtualmachineimagetemplate: 
        image_template_name: myImageTemplate
        resource_group_name: myResourceGroup
        tags:
          new-tag: new-value
        

    - name: Delete an Image Template.
      azure_rm_virtualmachineimagetemplate: 
        image_template_name: myImageTemplate
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
id:
  description:
    - Resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags
  returned: always
  type: dictionary
  sample: null
type_identity_type:
  description:
    - >-
      The type of identity used for the image template. The type 'None' will
      remove any identities from the image template.
  returned: always
  type: sealed-choice
  sample: null
user_assigned_identities:
  description:
    - >-
      The list of user identities associated with the image template. The user
      identity dictionary key references will be ARM resource ids in the form:
      '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
  returned: always
  type: dictionary
  sample: null
source:
  description:
    - Specifies the properties used to describe the source image.
  returned: always
  type: dict
  sample: null
  contains:
    type:
      description:
        - Specifies the type of source image you want to start with.
      returned: always
      type: str
      sample: null
customize:
  description:
    - >-
      Specifies the properties used to describe the customization steps of the
      image, like Image source etc
  returned: always
  type: list
  sample: null
  contains:
    type:
      description:
        - >-
          The type of customization tool you want to use on the Image. For
          example, "Shell" can be shell customizer
      returned: always
      type: str
      sample: null
    name:
      description:
        - Friendly Name to provide context on what this customization step does
      returned: always
      type: str
      sample: null
distribute:
  description:
    - The distribution targets where the image output needs to go to.
  returned: always
  type: list
  sample: null
  contains:
    type:
      description:
        - Type of distribution.
      returned: always
      type: str
      sample: null
    run_output_name:
      description:
        - The name to be used for the associated RunOutput.
      returned: always
      type: str
      sample: null
    artifact_tags:
      description:
        - >-
          Tags that will be applied to the artifact once it has been
          created/updated by the distributor.
      returned: always
      type: dictionary
      sample: null
provisioning_state:
  description:
    - Provisioning state of the resource
  returned: always
  type: sealed-choice
  sample: null
provisioning_error:
  description:
    - 'Provisioning error, if any'
  returned: always
  type: dict
  sample: null
  contains:
    provisioning_error_code:
      description:
        - Error code of the provisioning failure
      returned: always
      type: str
      sample: null
    message:
      description:
        - Verbose error message about the provisioning failure
      returned: always
      type: str
      sample: null
last_run_status:
  description:
    - State of 'run' that is currently executing or was last executed.
  returned: always
  type: dict
  sample: null
  contains:
    start_time:
      description:
        - Start time of the last run (UTC)
      returned: always
      type: str
      sample: null
    end_time:
      description:
        - End time of the last run (UTC)
      returned: always
      type: str
      sample: null
    run_state:
      description:
        - State of the last run
      returned: always
      type: sealed-choice
      sample: null
    run_sub_state:
      description:
        - Sub-state of the last run
      returned: always
      type: sealed-choice
      sample: null
    message:
      description:
        - Verbose information about the last run state
      returned: always
      type: str
      sample: null
build_timeout_in_minutes:
  description:
    - >-
      Maximum duration to wait while building the image template. Omit or
      specify 0 to use the default (4 hours).
  returned: always
  type: integer
  sample: null
vm_size:
  description:
    - >-
      Size of the virtual machine used to build, customize and capture images.
      Omit or specify empty string to use the default (Standard_D1_v2).
  returned: always
  type: str
  sample: null
os_disk_size_gb:
  description:
    - >-
      Size of the OS disk in GB. Omit or specify 0 to use Azure's default OS
      disk size.
  returned: always
  type: integer
  sample: null
vnet_config:
  description:
    - >-
      Optional configuration of the virtual network to use to deploy the build
      virtual machine in. Omit if no specific virtual network needs to be used.
  returned: always
  type: dict
  sample: null
  contains:
    subnet_id:
      description:
        - Resource id of a pre-existing subnet.
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
    from azure.mgmt.image import ImageBuilderClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMVirtualMachineImageTemplate(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            image_template_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            type=dict(
                type='sealed-choice',
                disposition='/type'
            ),
            user_assigned_identities=dict(
                type='dictionary',
                disposition='/user_assigned_identities'
            ),
            source=dict(
                type='dict',
                disposition='/source',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type',
                        required=True
                    )
                )
            ),
            customize=dict(
                type='list',
                disposition='/customize',
                elements='dict',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type',
                        required=True
                    ),
                    name=dict(
                        type='str',
                        disposition='name'
                    )
                )
            ),
            distribute=dict(
                type='list',
                disposition='/distribute',
                elements='dict',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type',
                        required=True
                    ),
                    run_output_name=dict(
                        type='str',
                        disposition='run_output_name',
                        required=True
                    ),
                    artifact_tags=dict(
                        type='dictionary',
                        disposition='artifact_tags'
                    )
                )
            ),
            build_timeout_in_minutes=dict(
                type='integer',
                disposition='/build_timeout_in_minutes'
            ),
            vm_size=dict(
                type='str',
                disposition='/vm_size'
            ),
            os_disk_size_gb=dict(
                type='integer',
                disposition='/os_disk_size_gb'
            ),
            vnet_config=dict(
                type='dict',
                disposition='/vnet_config',
                options=dict(
                    subnet_id=dict(
                        type='str',
                        disposition='subnet_id'
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
        self.image_template_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualMachineImageTemplate, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ImageBuilderClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-02-14')

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
            response = self.mgmt_client.virtual_machine_image_templates.create_or_update(resource_group_name=self.resource_group_name,
                                                                                         image_template_name=self.image_template_name,
                                                                                         parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualMachineImageTemplate instance.')
            self.fail('Error creating the VirtualMachineImageTemplate instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_image_templates.delete(resource_group_name=self.resource_group_name,
                                                                               image_template_name=self.image_template_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualMachineImageTemplate instance.')
            self.fail('Error deleting the VirtualMachineImageTemplate instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_image_templates.get(resource_group_name=self.resource_group_name,
                                                                            image_template_name=self.image_template_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachineImageTemplate()


if __name__ == '__main__':
    main()
