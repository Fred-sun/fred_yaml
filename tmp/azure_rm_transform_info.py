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
module: azure_rm_transform_info
version_added: '2.9'
short_description: Get Transform info.
description:
  - Get info of Transform.
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
  filter:
    description:
      - Restricts the set of items returned.
    type: str
  orderby:
    description:
      - Specifies the key by which the result collection should be ordered.
    type: str
  transform_name:
    description:
      - The Transform name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Lists the Transforms
      azure_rm_transform_info: 
        account_name: contosomedia
        resource_group_name: contosoresources
        

    - name: Lists the Transforms filter by created
      azure_rm_transform_info: 
        account_name: contosomedia
        resource_group_name: contosoresources
        

    - name: Lists the Transforms filter by lastmodified
      azure_rm_transform_info: 
        account_name: contosomedia
        resource_group_name: contosoresources
        

    - name: Lists the Transforms filter by name
      azure_rm_transform_info: 
        account_name: contosomedia
        resource_group_name: contosoresources
        

    - name: Get a Transform by name
      azure_rm_transform_info: 
        account_name: contosomedia
        resource_group_name: contosoresources
        transform_name: sampleTransform
        

'''

RETURN = '''
transforms:
  description: >-
    A list of dict results where the key is the name of the Transform and the
    values are the facts for that Transform.
  returned: always
  type: complex
  contains:
    value:
      description:
        - A collection of Transform items.
      returned: always
      type: list
      sample: null
      contains:
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
                  A Transform can define more than one outputs. This property
                  defines what the service should do when one output fails -
                  either continue to produce other outputs, or, stop the other
                  outputs. The overall Job state will not reflect failures of
                  outputs that are specified with 'ContinueJob'. The default is
                  'StopProcessingJob'.
              returned: always
              type: str
              sample: null
            relative_priority:
              description:
                - >-
                  Sets the relative priority of the TransformOutputs within a
                  Transform. This sets the priority that the service uses for
                  processing TransformOutputs. The default priority is Normal.
              returned: always
              type: str
              sample: null
            preset:
              description:
                - >-
                  Preset that describes the operations that will be used to
                  modify, transcode, or extract insights from the source file to
                  generate the output.
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
    odata_next_link:
      description:
        - >-
          A link to the next page of the collection (when the collection
          contains too many results to return in one response).
      returned: always
      type: str
      sample: null
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
              A Transform can define more than one outputs. This property
              defines what the service should do when one output fails - either
              continue to produce other outputs, or, stop the other outputs. The
              overall Job state will not reflect failures of outputs that are
              specified with 'ContinueJob'. The default is 'StopProcessingJob'.
          returned: always
          type: str
          sample: null
        relative_priority:
          description:
            - >-
              Sets the relative priority of the TransformOutputs within a
              Transform. This sets the priority that the service uses for
              processing TransformOutputs. The default priority is Normal.
          returned: always
          type: str
          sample: null
        preset:
          description:
            - >-
              Preset that describes the operations that will be used to modify,
              transcode, or extract insights from the source file to generate
              the output.
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.azure import Azure Media Services
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMTransformInfo(AzureRMModuleBase):
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
            filter=dict(
                type='str'
            ),
            orderby=dict(
                type='str'
            ),
            transform_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.filter = None
        self.orderby = None
        self.transform_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-05-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMTransformInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Media Services,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-05-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.transform_name is not None):
            self.results['transforms'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['transforms'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.transforms.get(resource_group_name=self.resource_group_name,
                                                       account_name=self.account_name,
                                                       transform_name=self.transform_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.transforms.list(resource_group_name=self.resource_group_name,
                                                        account_name=self.account_name,
                                                        filter=self.filter,
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
    AzureRMTransformInfo()


if __name__ == '__main__':
    main()
