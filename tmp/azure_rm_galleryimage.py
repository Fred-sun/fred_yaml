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
module: azure_rm_galleryimage
version_added: '2.9'
short_description: Manage Azure GalleryImage instance.
description:
  - 'Create, update and delete instance of Azure GalleryImage.'
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
  gallery_image_name:
    description:
      - The name of the gallery Image.
    required: true
    type: str
  expand:
    description:
      - 'Specify the $expand query. Example: ''properties($select=author)'''
    type: str
  location:
    description:
      - The location of the resource.
    type: str
  is_enabled:
    description:
      - Indicates whether this gallery image is enabled.
    type: bool
  is_override:
    description:
      - Indicates whether this gallery has been overridden for this lab account
    type: bool
  is_plan_authorized:
    description:
      - Indicates if the plan has been authorized for programmatic deployment.
    type: bool
  provisioning_state:
    description:
      - The provisioning status of the resource.
    type: str
  unique_identifier:
    description:
      - The unique immutable identifier of a resource (Guid).
    type: str
  state:
    description:
      - Assert the state of the GalleryImage.
      - >-
        Use C(present) to create or update an GalleryImage and C(absent) to
        delete it.
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
'''

RETURN = '''
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
    - Indicates whether this gallery has been overridden for this lab account
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.managed import ManagedLabsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMGalleryImage(AzureRMModuleBaseExt):
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
            gallery_image_name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            is_enabled=dict(
                type='bool',
                disposition='/is_enabled'
            ),
            is_override=dict(
                type='bool',
                disposition='/is_override'
            ),
            is_plan_authorized=dict(
                type='bool',
                disposition='/is_plan_authorized'
            ),
            provisioning_state=dict(
                type='str',
                disposition='/provisioning_state'
            ),
            unique_identifier=dict(
                type='str',
                disposition='/unique_identifier'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.lab_account_name = None
        self.gallery_image_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGalleryImage, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ManagedLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-10-15')

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
            response = self.mgmt_client.gallery_images.create_or_update(resource_group_name=self.resource_group_name,
                                                                        lab_account_name=self.lab_account_name,
                                                                        gallery_image_name=self.gallery_image_name,
                                                                        gallery_image=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the GalleryImage instance.')
            self.fail('Error creating the GalleryImage instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.gallery_images.delete(resource_group_name=self.resource_group_name,
                                                              lab_account_name=self.lab_account_name,
                                                              gallery_image_name=self.gallery_image_name)
        except CloudError as e:
            self.log('Error attempting to delete the GalleryImage instance.')
            self.fail('Error deleting the GalleryImage instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.gallery_images.get(resource_group_name=self.resource_group_name,
                                                           lab_account_name=self.lab_account_name,
                                                           gallery_image_name=self.gallery_image_name,
                                                           expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGalleryImage()


if __name__ == '__main__':
    main()
