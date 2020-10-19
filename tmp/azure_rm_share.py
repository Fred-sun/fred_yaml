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
module: azure_rm_share
version_added: '2.9'
short_description: Manage Azure Share instance.
description:
  - 'Create, update and delete instance of Azure Share.'
options:
  device_name:
    description:
      - The device name.
    required: true
    type: str
  name:
    description:
      - The share name.
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name.
    required: true
    type: str
  description:
    description:
      - Description for the share.
    type: str
  share_status:
    description:
      - Current status of the share.
    type: str
    choices:
      - Offline
      - Unknown
      - OK
      - Updating
      - NeedsAttention
  monitoring_status:
    description:
      - Current monitoring status of the share.
    type: str
    choices:
      - Enabled
      - Disabled
  azure_container_info:
    description:
      - Azure container mapping for the share.
    type: dict
    suboptions:
      storage_account_credential_id:
        description:
          - ID of the storage account credential used to access storage.
        required: true
        type: str
      container_name:
        description:
          - >-
            Container name (Based on the data format specified, this represents
            the name of Azure Files/Page blob/Block blob).
        required: true
        type: str
      data_format:
        description:
          - Storage format used for the file represented by the share.
        required: true
        type: str
        choices:
          - BlockBlob
          - PageBlob
          - AzureFile
  access_protocol:
    description:
      - Access protocol to be used by the share.
    type: str
    choices:
      - SMB
      - NFS
  user_access_rights:
    description:
      - >-
        Mapping of users and corresponding access rights on the share (required
        for SMB protocol).
    type: list
    suboptions:
      user_id:
        description:
          - User ID (already existing in the device).
        required: true
        type: str
      access_type:
        description:
          - Type of access to be allowed for the user.
        required: true
        type: str
        choices:
          - Change
          - Read
          - Custom
  client_access_rights:
    description:
      - >-
        List of IP addresses and corresponding access rights on the
        share(required for NFS protocol).
    type: list
    suboptions:
      client:
        description:
          - IP of the client.
        required: true
        type: str
      access_permission:
        description:
          - Type of access to be allowed for the client.
        required: true
        type: str
        choices:
          - NoAccess
          - ReadOnly
          - ReadWrite
  refresh_details:
    description:
      - Details of the refresh job on this share.
    type: dict
    suboptions:
      in_progress_refresh_job_id:
        description:
          - >-
            If a refresh job is currently in progress on this share or
            container, this field indicates the ARM resource ID of that job. The
            field is empty if no job is in progress.
        type: str
      last_completed_refresh_job_time_in_utc:
        description:
          - >-
            Indicates the completed time for the last refresh job on this
            particular share or container, if any.This could be a failed job or
            a successful job.
        type: str
      error_manifest_file:
        description:
          - >-
            Indicates the relative path of the error xml for the last refresh
            job on this particular share or container, if any. This could be a
            failed job or a successful job.
        type: str
      last_job:
        description:
          - >-
            Indicates the id of the last refresh job on this particular share or
            container,if any. This could be a failed job or a successful job.
        type: str
  data_policy:
    description:
      - Data policy of the share.
    type: str
    choices:
      - Cloud
      - Local
  state:
    description:
      - Assert the state of the Share.
      - Use C(present) to create or update an Share and C(absent) to delete it.
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
    - name: SharePut
      azure_rm_share: 
        name: smbshare
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        properties:
          description: ''
          access_protocol: SMB
          azure_container_info:
            container_name: testContainerSMB
            data_format: BlockBlob
            storage_account_credential_id: >-
              /subscriptions/4385cf00-2d3a-425a-832f-f4285b1c9dce/resourceGroups/GroupForEdgeAutomation/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/testedgedevice/storageAccountCredentials/sac1
          data_policy: Cloud
          monitoring_status: Enabled
          share_status: Online
          user_access_rights:
            - access_type: Change
              user_id: >-
                /subscriptions/4385cf00-2d3a-425a-832f-f4285b1c9dce/resourceGroups/GroupForEdgeAutomation/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/testedgedevice/users/user2
        

    - name: ShareDelete
      azure_rm_share: 
        name: smbshare
        device_name: testedgedevice
        resource_group_name: GroupForEdgeAutomation
        

'''

RETURN = '''
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
          Container name (Based on the data format specified, this represents
          the name of Azure Files/Page blob/Block blob).
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
      Mapping of users and corresponding access rights on the share (required
      for SMB protocol).
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
      List of IP addresses and corresponding access rights on the share(required
      for NFS protocol).
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
          If a refresh job is currently in progress on this share or container,
          this field indicates the ARM resource ID of that job. The field is
          empty if no job is in progress.
      returned: always
      type: str
      sample: null
    last_completed_refresh_job_time_in_utc:
      description:
        - >-
          Indicates the completed time for the last refresh job on this
          particular share or container, if any.This could be a failed job or a
          successful job.
      returned: always
      type: str
      sample: null
    error_manifest_file:
      description:
        - >-
          Indicates the relative path of the error xml for the last refresh job
          on this particular share or container, if any. This could be a failed
          job or a successful job.
      returned: always
      type: str
      sample: null
    last_job:
      description:
        - >-
          Indicates the id of the last refresh job on this particular share or
          container,if any. This could be a failed job or a successful job.
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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.data import DataBoxEdgeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMShare(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            device_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            share_status=dict(
                type='str',
                disposition='/share_status',
                choices=['Offline',
                         'Unknown',
                         'OK',
                         'Updating',
                         'NeedsAttention']
            ),
            monitoring_status=dict(
                type='str',
                disposition='/monitoring_status',
                choices=['Enabled',
                         'Disabled']
            ),
            azure_container_info=dict(
                type='dict',
                disposition='/azure_container_info',
                options=dict(
                    storage_account_credential_id=dict(
                        type='str',
                        disposition='storage_account_credential_id',
                        required=True
                    ),
                    container_name=dict(
                        type='str',
                        disposition='container_name',
                        required=True
                    ),
                    data_format=dict(
                        type='str',
                        disposition='data_format',
                        choices=['BlockBlob',
                                 'PageBlob',
                                 'AzureFile'],
                        required=True
                    )
                )
            ),
            access_protocol=dict(
                type='str',
                disposition='/access_protocol',
                choices=['SMB',
                         'NFS']
            ),
            user_access_rights=dict(
                type='list',
                disposition='/user_access_rights',
                elements='dict',
                options=dict(
                    user_id=dict(
                        type='str',
                        disposition='user_id',
                        required=True
                    ),
                    access_type=dict(
                        type='str',
                        disposition='access_type',
                        choices=['Change',
                                 'Read',
                                 'Custom'],
                        required=True
                    )
                )
            ),
            client_access_rights=dict(
                type='list',
                disposition='/client_access_rights',
                elements='dict',
                options=dict(
                    client=dict(
                        type='str',
                        disposition='client',
                        required=True
                    ),
                    access_permission=dict(
                        type='str',
                        disposition='access_permission',
                        choices=['NoAccess',
                                 'ReadOnly',
                                 'ReadWrite'],
                        required=True
                    )
                )
            ),
            refresh_details=dict(
                type='dict',
                disposition='/refresh_details',
                options=dict(
                    in_progress_refresh_job_id=dict(
                        type='str',
                        disposition='in_progress_refresh_job_id'
                    ),
                    last_completed_refresh_job_time_in_utc=dict(
                        type='str',
                        disposition='last_completed_refresh_job_time_in_utc'
                    ),
                    error_manifest_file=dict(
                        type='str',
                        disposition='error_manifest_file'
                    ),
                    last_job=dict(
                        type='str',
                        disposition='last_job'
                    )
                )
            ),
            data_policy=dict(
                type='str',
                disposition='/data_policy',
                choices=['Cloud',
                         'Local']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.device_name = None
        self.name = None
        self.resource_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMShare, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DataBoxEdgeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-08-01')

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
            response = self.mgmt_client.shares.create_or_update(device_name=self.device_name,
                                                                name=self.name,
                                                                resource_group_name=self.resource_group_name,
                                                                share=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Share instance.')
            self.fail('Error creating the Share instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.shares.delete(device_name=self.device_name,
                                                      name=self.name,
                                                      resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the Share instance.')
            self.fail('Error deleting the Share instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.shares.get(device_name=self.device_name,
                                                   name=self.name,
                                                   resource_group_name=self.resource_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMShare()


if __name__ == '__main__':
    main()
