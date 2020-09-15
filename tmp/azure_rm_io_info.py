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
module: azure_rm_io_info
version_added: '2.9'
short_description: Get Io info.
description:
  - Get info of Io.
options:
  host_name:
    description:
      - Location hostName for the tenant
    required: true
    type: str
  filter:
    description:
      - The filter to apply on the operation.
    type: str
  top:
    description:
      - undefined
    type: integer
  select:
    description:
      - select specific fields in entity.
    type: str
  policy_name:
    description:
      - Unique name for the policy
      - policy name for the tenant
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
ios:
  description: >-
    A list of dict results where the key is the name of the Io and the values
    are the facts for that Io.
  returned: always
  type: complex
  contains:
    value:
      description:
        - ''
      returned: always
      type: list
      sample: null
      contains:
        friendly_name:
          description:
            - ''
          returned: always
          type: str
          sample: null
        description:
          description:
            - ''
          returned: always
          type: str
          sample: null
        app_sharing_from_level:
          description:
            - ''
          returned: always
          type: str
          sample: null
        app_sharing_to_level:
          description:
            - ''
          returned: always
          type: str
          sample: null
        authentication:
          description:
            - ''
          returned: always
          type: str
          sample: null
        clipboard_sharing_level:
          description:
            - ''
          returned: always
          type: str
          sample: null
        data_backup:
          description:
            - ''
          returned: always
          type: str
          sample: null
        file_sharing_save_as:
          description:
            - ''
          returned: always
          type: str
          sample: null
        pin:
          description:
            - ''
          returned: always
          type: str
          sample: null
        pin_num_retry:
          description:
            - ''
          returned: always
          type: integer
          sample: null
        device_compliance:
          description:
            - ''
          returned: always
          type: str
          sample: null
        managed_browser:
          description:
            - ''
          returned: always
          type: str
          sample: null
        access_recheck_offline_timeout:
          description:
            - ''
          returned: always
          type: duration
          sample: null
        access_recheck_online_timeout:
          description:
            - ''
          returned: always
          type: duration
          sample: null
        offline_wipe_timeout:
          description:
            - ''
          returned: always
          type: duration
          sample: null
        num_of_apps:
          description:
            - ''
          returned: always
          type: integer
          sample: null
        group_status:
          description:
            - ''
          returned: always
          type: str
          sample: null
        last_modified_time:
          description:
            - ''
          returned: always
          type: str
          sample: null
        file_encryption_level:
          description:
            - ''
          returned: always
          type: str
          sample: null
        touch_id:
          description:
            - ''
          returned: always
          type: str
          sample: null
    nextlink:
      description:
        - Gets the URL to get the next set of results.
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
    tags:
      description:
        - Resource Tags
      returned: always
      type: dictionary
      sample: null
    location:
      description:
        - Resource Location
      returned: always
      type: str
      sample: null
    friendly_name:
      description:
        - ''
      returned: always
      type: str
      sample: null
    description:
      description:
        - ''
      returned: always
      type: str
      sample: null
    app_sharing_from_level:
      description:
        - ''
      returned: always
      type: str
      sample: null
    app_sharing_to_level:
      description:
        - ''
      returned: always
      type: str
      sample: null
    authentication:
      description:
        - ''
      returned: always
      type: str
      sample: null
    clipboard_sharing_level:
      description:
        - ''
      returned: always
      type: str
      sample: null
    data_backup:
      description:
        - ''
      returned: always
      type: str
      sample: null
    file_sharing_save_as:
      description:
        - ''
      returned: always
      type: str
      sample: null
    pin:
      description:
        - ''
      returned: always
      type: str
      sample: null
    pin_num_retry:
      description:
        - ''
      returned: always
      type: integer
      sample: null
    device_compliance:
      description:
        - ''
      returned: always
      type: str
      sample: null
    managed_browser:
      description:
        - ''
      returned: always
      type: str
      sample: null
    access_recheck_offline_timeout:
      description:
        - ''
      returned: always
      type: duration
      sample: null
    access_recheck_online_timeout:
      description:
        - ''
      returned: always
      type: duration
      sample: null
    offline_wipe_timeout:
      description:
        - ''
      returned: always
      type: duration
      sample: null
    num_of_apps:
      description:
        - ''
      returned: always
      type: integer
      sample: null
    group_status:
      description:
        - ''
      returned: always
      type: str
      sample: null
    last_modified_time:
      description:
        - ''
      returned: always
      type: str
      sample: null
    file_encryption_level:
      description:
        - ''
      returned: always
      type: str
      sample: null
    touch_id:
      description:
        - ''
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
    from azure.mgmt.intune import IntuneResourceManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMIoInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            host_name=dict(
                type='str',
                required=True
            ),
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            select=dict(
                type='str'
            ),
            policy_name=dict(
                type='str'
            )
        )

        self.host_name = None
        self.filter = None
        self.top = None
        self.select = None
        self.policy_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2015-01-14-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMIoInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(IntuneResourceManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-01-14-preview')

        if (self.host_name is not None and
            self.policy_name is not None):
            self.results['ios'] = self.format_item(self.getappformampolicy())
        elif (self.host_name is not None and
              self.policy_name is not None):
            self.results['ios'] = self.format_item(self.getmampolicybyname())
        elif (self.host_name is not None and
              self.policy_name is not None):
            self.results['ios'] = self.format_item(self.getgroupformampolicy())
        elif (self.host_name is not None):
            self.results['ios'] = self.format_item(self.getmampolicy())
        return self.results

    def getappformampolicy(self):
        response = None

        try:
            response = self.mgmt_client.ios.get_app_for_mam_policy(host_name=self.host_name,
                                                                   policy_name=self.policy_name,
                                                                   filter=self.filter,
                                                                   top=self.top,
                                                                   select=self.select)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getmampolicybyname(self):
        response = None

        try:
            response = self.mgmt_client.ios.get_mam_policy_by_name(host_name=self.host_name,
                                                                   policy_name=self.policy_name,
                                                                   select=self.select)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getgroupformampolicy(self):
        response = None

        try:
            response = self.mgmt_client.ios.get_group_for_mam_policy(host_name=self.host_name,
                                                                     policy_name=self.policy_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def getmampolicy(self):
        response = None

        try:
            response = self.mgmt_client.ios.get_mam_policy(host_name=self.host_name,
                                                           filter=self.filter,
                                                           top=self.top,
                                                           select=self.select)
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
    AzureRMIoInfo()


if __name__ == '__main__':
    main()
