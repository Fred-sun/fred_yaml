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
module: azure_rm_virtualmachineimagetemplate_info
version_added: '2.9'
short_description: Get VirtualMachineImageTemplate info.
description:
  - Get info of VirtualMachineImageTemplate.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  image_template_name:
    description:
      - The name of the image Template
    type: str
  run_output_name:
    description:
      - The name of the run output
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List images by subscription.
      azure_rm_virtualmachineimagetemplate_info: 
        {}
        

    - name: List images by resource group
      azure_rm_virtualmachineimagetemplate_info: 
        resource_group_name: myResourceGroup
        

    - name: Retrieve an Image Template.
      azure_rm_virtualmachineimagetemplate_info: 
        image_template_name: myImageTemplate
        resource_group_name: myResourceGroup
        

    - name: Retrieve a list of all outputs created by the last run of an Image Template
      azure_rm_virtualmachineimagetemplate_info: 
        image_template_name: myImageTemplate
        resource_group_name: myResourceGroup
        

    - name: Retrieve single runOutput
      azure_rm_virtualmachineimagetemplate_info: 
        image_template_name: myImageTemplate
        resource_group_name: myResourceGroup
        run_output_name: myManagedImageOutput
        

'''

RETURN = '''
virtual_machine_image_templates:
  description: >-
    A list of dict results where the key is the name of the
    VirtualMachineImageTemplate and the values are the facts for that
    VirtualMachineImageTemplate.
  returned: always
  type: complex
  contains:
    value:
      description:
        - |-
          An array of image templates
          An array of run outputs
      returned: always
      type: list
      sample: null
      contains:
        type_identity_type:
          description:
            - >-
              The type of identity used for the image template. The type 'None'
              will remove any identities from the image template.
          returned: always
          type: sealed-choice
          sample: null
        user_assigned_identities:
          description:
            - >-
              The list of user identities associated with the image template.
              The user identity dictionary key references will be ARM resource
              ids in the form:
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
              Specifies the properties used to describe the customization steps
              of the image, like Image source etc
          returned: always
          type: list
          sample: null
          contains:
            type:
              description:
                - >-
                  The type of customization tool you want to use on the Image.
                  For example, "Shell" can be shell customizer
              returned: always
              type: str
              sample: null
            name:
              description:
                - >-
                  Friendly Name to provide context on what this customization
                  step does
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
              Maximum duration to wait while building the image template. Omit
              or specify 0 to use the default (4 hours).
          returned: always
          type: integer
          sample: null
        vm_size:
          description:
            - >-
              Size of the virtual machine used to build, customize and capture
              images. Omit or specify empty string to use the default
              (Standard_D1_v2).
          returned: always
          type: str
          sample: null
        os_disk_size_gb:
          description:
            - >-
              Size of the OS disk in GB. Omit or specify 0 to use Azure's
              default OS disk size.
          returned: always
          type: integer
          sample: null
        vnet_config:
          description:
            - >-
              Optional configuration of the virtual network to use to deploy the
              build virtual machine in. Omit if no specific virtual network
              needs to be used.
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
    next_link:
      description:
        - The continuation token.
      returned: always
      type: str
      sample: null
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
          The list of user identities associated with the image template. The
          user identity dictionary key references will be ARM resource ids in
          the form:
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
          Specifies the properties used to describe the customization steps of
          the image, like Image source etc
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
            - >-
              Friendly Name to provide context on what this customization step
              does
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
          Size of the virtual machine used to build, customize and capture
          images. Omit or specify empty string to use the default
          (Standard_D1_v2).
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
          Optional configuration of the virtual network to use to deploy the
          build virtual machine in. Omit if no specific virtual network needs to
          be used.
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
    artifact_id:
      description:
        - The resource id of the artifact.
      returned: always
      type: str
      sample: null
    artifact_uri:
      description:
        - The location URI of the artifact.
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
    from azure.mgmt.image import ImageBuilderClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMVirtualMachineImageTemplateInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            image_template_name=dict(
                type='str'
            ),
            run_output_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.image_template_name = None
        self.run_output_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-02-14'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVirtualMachineImageTemplateInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ImageBuilderClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-02-14')

        if (self.resource_group_name is not None and
            self.image_template_name is not None and
            self.run_output_name is not None):
            self.results['virtual_machine_image_templates'] = self.format_item(self.getrunoutput())
        elif (self.resource_group_name is not None and
              self.image_template_name is not None):
            self.results['virtual_machine_image_templates'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.image_template_name is not None):
            self.results['virtual_machine_image_templates'] = self.format_item(self.listrunoutput())
        elif (self.resource_group_name is not None):
            self.results['virtual_machine_image_templates'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['virtual_machine_image_templates'] = self.format_item(self.list())
        return self.results

    def getrunoutput(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_image_templates.get_run_output(resource_group_name=self.resource_group_name,
                                                                                       image_template_name=self.image_template_name,
                                                                                       run_output_name=self.run_output_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_image_templates.get(resource_group_name=self.resource_group_name,
                                                                            image_template_name=self.image_template_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listrunoutput(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_image_templates.list_run_output(resource_group_name=self.resource_group_name,
                                                                                        image_template_name=self.image_template_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_image_templates.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_image_templates.list()
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
    AzureRMVirtualMachineImageTemplateInfo()


if __name__ == '__main__':
    main()
