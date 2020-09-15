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
module: azure_rm_cloudmanifestfile_info
version_added: '2.9'
short_description: Get CloudManifestFile info.
description:
  - Get info of CloudManifestFile.
options:
  verification_version:
    description:
      - Signing verification key version.
    type: str
  version_creation_date:
    description:
      - Signing verification key version creation date.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Returns the properties of a cloud specific manifest file with latest version.
      azure_rm_cloudmanifestfile_info: 
        {}
        

    - name: Returns the properties of a cloud specific manifest file.
      azure_rm_cloudmanifestfile_info: 
        verification_version: latest
        

'''

RETURN = '''
cloud_manifest_file:
  description: >-
    A list of dict results where the key is the name of the CloudManifestFile
    and the values are the facts for that CloudManifestFile.
  returned: always
  type: complex
  contains:
    id:
      description:
        - ID of the resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Name of the resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Type of Resource.
      returned: always
      type: str
      sample: null
    etag:
      description:
        - >-
          The entity tag used for optimistic concurrency when modifying the
          resource.
      returned: always
      type: str
      sample: null
    properties:
      description:
        - Cloud specific manifest data.
      returned: always
      type: dict
      sample: null
      contains:
        deployment_data:
          description:
            - Cloud specific manifest data.
          returned: always
          type: dict
          sample: null
          contains:
            external_dsms_certificates:
              description:
                - Dsms external certificates.
              returned: always
              type: str
              sample: null
            custom_cloud_verification_key:
              description:
                - Signing verification public key.
              returned: always
              type: str
              sample: null
            custom_cloud_arm_endpoint:
              description:
                - ARM endpoint.
              returned: always
              type: str
              sample: null
            external_dsms_endpoint:
              description:
                - Dsms endpoint.
              returned: always
              type: str
              sample: null
        signature:
          description:
            - Signature of the cloud specific manifest data.
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
    from azure.mgmt.azure import AzureStackManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMCloudManifestFileInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            verification_version=dict(
                type='str'
            ),
            version_creation_date=dict(
                type='str'
            )
        )

        self.verification_version = None
        self.version_creation_date = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMCloudManifestFileInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AzureStackManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-06-01')

        if (self.verification_version is not None):
            self.results['cloud_manifest_file'] = self.format_item(self.get())
        else:
            self.results['cloud_manifest_file'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.cloud_manifest_file.get(verification_version=self.verification_version,
                                                                version_creation_date=self.version_creation_date)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.cloud_manifest_file.list()
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
    AzureRMCloudManifestFileInfo()


if __name__ == '__main__':
    main()
