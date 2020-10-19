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
module: azure_rm_share_info
version_added: '2.9'
short_description: Get Share info.
description:
  - Get info of Share.
options:
  device_name:
    description:
      - The device name.
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name.
    required: true
    type: str
  name:
    description:
      - The share name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ShareGetAllInDevice
      azure_rm_share_info: 
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        

    - name: ShareGet
      azure_rm_share_info: 
        name: smbshare
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        

'''

RETURN = '''
shares:
  description: >-
    A list of dict results where the key is the name of the Share and the values
    are the facts for that Share.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of shares.
      returned: always
      type: list
      sample: null
      contains:
        description:
          description:
            - Description for the share.
          returned: always
          type: str
          sample: null
        share_status:
          description:
            - Current status of the share.
          returned: always
          type: str
          sample: null
        monitoring_status:
          description:
            - Current monitoring status of the share.
          returned: always
          type: str
          sample: null
        azure_container_info:
          description:
            - Azure container mapping for the share.
          returned: always
          type: dict
          sample: null
          contains:
            storage_account_credential_id:
              description:
                - ID of the storage account credential used to access storage.
              returned: always
              type: str
              sample: null
            container_name:
              description:
                - >-
                  Container name (Based on the data format specified, this
                  represents the name of Azure Files/Page blob/Block blob).
              returned: always
              type: str
              sample: null
            data_format:
              description:
                - Storage format used for the file represented by the share.
              returned: always
              type: str
              sample: null
        access_protocol:
          description:
            - Access protocol to be used by the share.
          returned: always
          type: str
          sample: null
        user_access_rights:
          description:
            - >-
              Mapping of users and corresponding access rights on the share
              (required for SMB protocol).
          returned: always
          type: list
          sample: null
          contains:
            user_id:
              description:
                - User ID (already existing in the device).
              returned: always
              type: str
              sample: null
            access_type:
              description:
                - Type of access to be allowed for the user.
              returned: always
              type: str
              sample: null
        client_access_rights:
          description:
            - >-
              List of IP addresses and corresponding access rights on the
              share(required for NFS protocol).
          returned: always
          type: list
          sample: null
          contains:
            client:
              description:
                - IP of the client.
              returned: always
              type: str
              sample: null
            access_permission:
              description:
                - Type of access to be allowed for the client.
              returned: always
              type: str
              sample: null
        refresh_details:
          description:
            - Details of the refresh job on this share.
          returned: always
          type: dict
          sample: null
          contains:
            in_progress_refresh_job_id:
              description:
                - >-
                  If a refresh job is currently in progress on this share or
                  container, this field indicates the ARM resource ID of that
                  job. The field is empty if no job is in progress.
              returned: always
              type: str
              sample: null
            last_completed_refresh_job_time_in_utc:
              description:
                - >-
                  Indicates the completed time for the last refresh job on this
                  particular share or container, if any.This could be a failed
                  job or a successful job.
              returned: always
              type: str
              sample: null
            error_manifest_file:
              description:
                - >-
                  Indicates the relative path of the error xml for the last
                  refresh job on this particular share or container, if any.
                  This could be a failed job or a successful job.
              returned: always
              type: str
              sample: null
            last_job:
              description:
                - >-
                  Indicates the id of the last refresh job on this particular
                  share or container,if any. This could be a failed job or a
                  successful job.
              returned: always
              type: str
              sample: null
        share_mappings:
          description:
            - Share mount point to the role.
          returned: always
          type: list
          sample: null
          contains:
            share_id:
              description:
                - ID of the share mounted to the role VM.
              returned: always
              type: str
              sample: null
            role_id:
              description:
                - ID of the role to which share is mounted.
              returned: always
              type: str
              sample: null
            mount_point:
              description:
                - Mount point for the share.
              returned: always
              type: str
              sample: null
            role_type:
              description:
                - Role type.
              returned: always
              type: str
              sample: null
        data_policy:
          description:
            - Data policy of the share.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - Link to the next set of results.
      returned: always
      type: str
      sample: null
    id:
      description:
        - The path ID that uniquely identifies the object.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The object name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The hierarchical type of the object.
      returned: always
      type: str
      sample: null
    description:
      description:
        - Description for the share.
      returned: always
      type: str
      sample: null
    share_status:
      description:
        - Current status of the share.
      returned: always
      type: str
      sample: null
    monitoring_status:
      description:
        - Current monitoring status of the share.
      returned: always
      type: str
      sample: null
    azure_container_info:
      description:
        - Azure container mapping for the share.
      returned: always
      type: dict
      sample: null
      contains:
        storage_account_credential_id:
          description:
            - ID of the storage account credential used to access storage.
          returned: always
          type: str
          sample: null
        container_name:
          description:
            - >-
              Container name (Based on the data format specified, this
              represents the name of Azure Files/Page blob/Block blob).
          returned: always
          type: str
          sample: null
        data_format:
          description:
            - Storage format used for the file represented by the share.
          returned: always
          type: str
          sample: null
    access_protocol:
      description:
        - Access protocol to be used by the share.
      returned: always
      type: str
      sample: null
    user_access_rights:
      description:
        - >-
          Mapping of users and corresponding access rights on the share
          (required for SMB protocol).
      returned: always
      type: list
      sample: null
      contains:
        user_id:
          description:
            - User ID (already existing in the device).
          returned: always
          type: str
          sample: null
        access_type:
          description:
            - Type of access to be allowed for the user.
          returned: always
          type: str
          sample: null
    client_access_rights:
      description:
        - >-
          List of IP addresses and corresponding access rights on the
          share(required for NFS protocol).
      returned: always
      type: list
      sample: null
      contains:
        client:
          description:
            - IP of the client.
          returned: always
          type: str
          sample: null
        access_permission:
          description:
            - Type of access to be allowed for the client.
          returned: always
          type: str
          sample: null
    refresh_details:
      description:
        - Details of the refresh job on this share.
      returned: always
      type: dict
      sample: null
      contains:
        in_progress_refresh_job_id:
          description:
            - >-
              If a refresh job is currently in progress on this share or
              container, this field indicates the ARM resource ID of that job.
              The field is empty if no job is in progress.
          returned: always
          type: str
          sample: null
        last_completed_refresh_job_time_in_utc:
          description:
            - >-
              Indicates the completed time for the last refresh job on this
              particular share or container, if any.This could be a failed job
              or a successful job.
          returned: always
          type: str
          sample: null
        error_manifest_file:
          description:
            - >-
              Indicates the relative path of the error xml for the last refresh
              job on this particular share or container, if any. This could be a
              failed job or a successful job.
          returned: always
          type: str
          sample: null
        last_job:
          description:
            - >-
              Indicates the id of the last refresh job on this particular share
              or container,if any. This could be a failed job or a successful
              job.
          returned: always
          type: str
          sample: null
    share_mappings:
      description:
        - Share mount point to the role.
      returned: always
      type: list
      sample: null
      contains:
        share_id:
          description:
            - ID of the share mounted to the role VM.
          returned: always
          type: str
          sample: null
        role_id:
          description:
            - ID of the role to which share is mounted.
          returned: always
          type: str
          sample: null
        mount_point:
          description:
            - Mount point for the share.
          returned: always
          type: str
          sample: null
        role_type:
          description:
            - Role type.
          returned: always
          type: str
          sample: null
    data_policy:
      description:
        - Data policy of the share.
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
    from azure.mgmt.data import DataBoxEdgeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMShareInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str'
            )
        )

        self.device_name = None
        self.resource_group_name = None
        self.name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-08-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMShareInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DataBoxEdgeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-08-01')

        if (self.device_name is not None and
            self.name is not None and
            self.resource_group_name is not None):
            self.results['shares'] = self.format_item(self.get())
        elif (self.device_name is not None and
              self.resource_group_name is not None):
            self.results['shares'] = self.format_item(self.listbydataboxedgedevice())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.shares.get(device_name=self.device_name,
                                                   name=self.name,
                                                   resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydataboxedgedevice(self):
        response = None

        try:
            response = self.mgmt_client.shares.list_by_data_box_edge_device(device_name=self.device_name,
                                                                            resource_group_name=self.resource_group_name)
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
    AzureRMShareInfo()


if __name__ == '__main__':
    main()
