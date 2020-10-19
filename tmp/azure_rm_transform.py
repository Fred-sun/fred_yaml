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
module: azure_rm_transform
version_added: '2.9'
short_description: Manage Azure Transform instance.
description:
  - 'Create, update and delete instance of Azure Transform.'
options:
  resource_group_name:
    description:
      - The name of the resource group within the Azure subscription.
    required: true
    type: str
  account_name:
    description:
      - The Media Services account name.
    required: true
    type: str
  transform_name:
    description:
      - The Transform name.
    required: true
    type: str
  description:
    description:
      - An optional verbose description of the Transform.
    type: str
  outputs:
    description:
      - >-
        An array of one or more TransformOutputs that the Transform should
        generate.
    type: list
    suboptions:
      on_error:
        description:
          - >-
            A Transform can define more than one outputs. This property defines
            what the service should do when one output fails - either continue
            to produce other outputs, or, stop the other outputs. The overall
            Job state will not reflect failures of outputs that are specified
            with 'ContinueJob'. The default is 'StopProcessingJob'.
        type: str
        choices:
          - StopProcessingJob
          - ContinueJob
      relative_priority:
        description:
          - >-
            Sets the relative priority of the TransformOutputs within a
            Transform. This sets the priority that the service uses for
            processing TransformOutputs. The default priority is Normal.
        type: str
        choices:
          - Low
          - Normal
          - High
      preset:
        description:
          - >-
            Preset that describes the operations that will be used to modify,
            transcode, or extract insights from the source file to generate the
            output.
        required: true
        type: dict
        suboptions:
          odata_type:
            description:
              - The discriminator for derived types.
            required: true
            type: str
  state:
    description:
      - Assert the state of the Transform.
      - >-
        Use C(present) to create or update an Transform and C(absent) to delete
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
    - name: Create or update a Transform
      azure_rm_transform: 
        account_name: contosomedia
        resource_group_name: contosoresources
        transform_name: createdTransform
        properties:
          description: Example Transform to illustrate create and update.
          outputs:
            - preset:
                '@odata.type': '#Microsoft.Media.BuiltInStandardEncoderPreset'
                preset_name: AdaptiveStreaming
        

    - name: Delete a Transform
      azure_rm_transform: 
        account_name: contosomedia
        resource_group_name: contosoresources
        transform_name: sampleTransform
        

    - name: Update a Transform.
      azure_rm_transform: 
        account_name: contosomedia
        resource_group_name: contosoresources
        transform_name: transformToUpdate
        properties:
          description: Example transform to illustrate update.
          outputs:
            - preset:
                '@odata.type': '#Microsoft.Media.BuiltInStandardEncoderPreset'
                preset_name: H264MultipleBitrate720p
              relative_priority: High
        

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
created:
  description:
    - >-
      The UTC date and time when the Transform was created, in
      'YYYY-MM-DDThh:mm:ssZ' format.
  returned: always
  type: str
  sample: null
description:
  description:
    - An optional verbose description of the Transform.
  returned: always
  type: str
  sample: null
last_modified:
  description:
    - >-
      The UTC date and time when the Transform was last updated, in
      'YYYY-MM-DDThh:mm:ssZ' format.
  returned: always
  type: str
  sample: null
outputs:
  description:
    - >-
      An array of one or more TransformOutputs that the Transform should
      generate.
  returned: always
  type: list
  sample: null
  contains:
    on_error:
      description:
        - >-
          A Transform can define more than one outputs. This property defines
          what the service should do when one output fails - either continue to
          produce other outputs, or, stop the other outputs. The overall Job
          state will not reflect failures of outputs that are specified with
          'ContinueJob'. The default is 'StopProcessingJob'.
      returned: always
      type: str
      sample: null
    relative_priority:
      description:
        - >-
          Sets the relative priority of the TransformOutputs within a Transform.
          This sets the priority that the service uses for processing
          TransformOutputs. The default priority is Normal.
      returned: always
      type: str
      sample: null
    preset:
      description:
        - >-
          Preset that describes the operations that will be used to modify,
          transcode, or extract insights from the source file to generate the
          output.
      returned: always
      type: dict
      sample: null
      contains:
        odata_type:
          description:
            - The discriminator for derived types.
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
    from azure.mgmt.azure import Azure Media Services
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMTransform(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            transform_name=dict(
                type='str',
                required=True
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            outputs=dict(
                type='list',
                disposition='/outputs',
                elements='dict',
                options=dict(
                    on_error=dict(
                        type='str',
                        disposition='on_error',
                        choices=['StopProcessingJob',
                                 'ContinueJob']
                    ),
                    relative_priority=dict(
                        type='str',
                        disposition='relative_priority',
                        choices=['Low',
                                 'Normal',
                                 'High']
                    ),
                    preset=dict(
                        type='dict',
                        disposition='preset',
                        required=True,
                        options=dict(
                            odata_type=dict(
                                type='str',
                                disposition='odata_type',
                                required=True
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
        self.account_name = None
        self.transform_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMTransform, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Azure Media Services,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

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
            response = self.mgmt_client.transforms.create_or_update(resource_group_name=self.resource_group_name,
                                                                    account_name=self.account_name,
                                                                    transform_name=self.transform_name,
                                                                    parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Transform instance.')
            self.fail('Error creating the Transform instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.transforms.delete(resource_group_name=self.resource_group_name,
                                                          account_name=self.account_name,
                                                          transform_name=self.transform_name)
        except CloudError as e:
            self.log('Error attempting to delete the Transform instance.')
            self.fail('Error deleting the Transform instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.transforms.get(resource_group_name=self.resource_group_name,
                                                       account_name=self.account_name,
                                                       transform_name=self.transform_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMTransform()


if __name__ == '__main__':
    main()
