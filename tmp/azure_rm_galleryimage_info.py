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
module: azure_rm_galleryimage_info
version_added: '2.9'
short_description: Get GalleryImage info.
description:
  - Get info of GalleryImage.
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
  expand:
    description:
      - 'Specify the $expand query. Example: ''properties($select=author)'''
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
  gallery_image_name:
    description:
      - The name of the gallery Image.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
gallery_images:
  description: >-
    A list of dict results where the key is the name of the GalleryImage and the
    values are the facts for that GalleryImage.
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
        author:
          description:
            - The author of the gallery image.
          returned: always
          type: str
          sample: null
        created_date:
          description:
            - The creation date of the gallery image.
          returned: always
          type: str
          sample: null
        description:
          description:
            - The description of the gallery image.
          returned: always
          type: str
          sample: null
        image_reference:
          description:
            - The image reference of the gallery image.
          returned: always
          type: dict
          sample: null
          contains:
            offer:
              description:
                - The offer of the gallery image.
              returned: always
              type: str
              sample: null
            publisher:
              description:
                - The publisher of the gallery image.
              returned: always
              type: str
              sample: null
            sku:
              description:
                - The SKU of the gallery image.
              returned: always
              type: str
              sample: null
            os_type:
              description:
                - The OS type of the gallery image.
              returned: always
              type: str
              sample: null
            version:
              description:
                - The version of the gallery image.
              returned: always
              type: str
              sample: null
        icon:
          description:
            - The icon of the gallery image.
          returned: always
          type: str
          sample: null
        is_enabled:
          description:
            - Indicates whether this gallery image is enabled.
          returned: always
          type: bool
          sample: null
        is_override:
          description:
            - >-
              Indicates whether this gallery has been overridden for this lab
              account
          returned: always
          type: bool
          sample: null
        plan_id:
          description:
            - The third party plan that applies to this image
          returned: always
          type: str
          sample: null
        is_plan_authorized:
          description:
            - >-
              Indicates if the plan has been authorized for programmatic
              deployment.
          returned: always
          type: bool
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
    author:
      description:
        - The author of the gallery image.
      returned: always
      type: str
      sample: null
    created_date:
      description:
        - The creation date of the gallery image.
      returned: always
      type: str
      sample: null
    description:
      description:
        - The description of the gallery image.
      returned: always
      type: str
      sample: null
    image_reference:
      description:
        - The image reference of the gallery image.
      returned: always
      type: dict
      sample: null
      contains:
        offer:
          description:
            - The offer of the gallery image.
          returned: always
          type: str
          sample: null
        publisher:
          description:
            - The publisher of the gallery image.
          returned: always
          type: str
          sample: null
        sku:
          description:
            - The SKU of the gallery image.
          returned: always
          type: str
          sample: null
        os_type:
          description:
            - The OS type of the gallery image.
          returned: always
          type: str
          sample: null
        version:
          description:
            - The version of the gallery image.
          returned: always
          type: str
          sample: null
    icon:
      description:
        - The icon of the gallery image.
      returned: always
      type: str
      sample: null
    is_enabled:
      description:
        - Indicates whether this gallery image is enabled.
      returned: always
      type: bool
      sample: null
    is_override:
      description:
        - >-
          Indicates whether this gallery has been overridden for this lab
          account
      returned: always
      type: bool
      sample: null
    plan_id:
      description:
        - The third party plan that applies to this image
      returned: always
      type: str
      sample: null
    is_plan_authorized:
      description:
        - Indicates if the plan has been authorized for programmatic deployment.
      returned: always
      type: bool
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


class AzureRMGalleryImageInfo(AzureRMModuleBase):
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
            gallery_image_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.lab_account_name = None
        self.expand = None
        self.filter = None
        self.top = None
        self.orderby = None
        self.gallery_image_name = None

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
        super(AzureRMGalleryImageInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ManagedLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-10-15')

        if (self.resource_group_name is not None and
            self.lab_account_name is not None and
            self.gallery_image_name is not None):
            self.results['gallery_images'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.lab_account_name is not None):
            self.results['gallery_images'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.gallery_images.get(resource_group_name=self.resource_group_name,
                                                           lab_account_name=self.lab_account_name,
                                                           gallery_image_name=self.gallery_image_name,
                                                           expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.gallery_images.list(resource_group_name=self.resource_group_name,
                                                            lab_account_name=self.lab_account_name,
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
    AzureRMGalleryImageInfo()


if __name__ == '__main__':
    main()
