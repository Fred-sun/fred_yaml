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
module: azure_rm_replicationlink_info
version_added: '2.9'
short_description: Get ReplicationLink info.
description:
  - Get info of ReplicationLink.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group that contains the resource. You can
        obtain this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  server_name:
    description:
      - The name of the server.
    required: true
    type: str
  database_name:
    description:
      - The name of the database to get the link for.
      - The name of the database to retrieve links for.
    required: true
    type: str
  link_id:
    description:
      - The replication link ID to be retrieved.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a replication link
      azure_rm_replicationlink_info: 
        database_name: testdb
        link_id: f0550bf5-07ce-4270-8e4b-71737975973a
        resource_group_name: sqlcrudtest-8931
        server_name: sqlcrudtest-2137
        

    - name: List Replication links
      azure_rm_replicationlink_info: 
        database_name: testdb
        resource_group_name: sqlcrudtest-4799
        server_name: sqlcrudtest-6440
        

'''

RETURN = '''
replication_links:
  description: >-
    A list of dict results where the key is the name of the ReplicationLink and
    the values are the facts for that ReplicationLink.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Location of the server that contains this firewall rule.
      returned: always
      type: str
      sample: null
    is_termination_allowed:
      description:
        - >-
          Legacy value indicating whether termination is allowed.  Currently
          always returns true.
      returned: always
      type: bool
      sample: null
    replication_mode:
      description:
        - Replication mode of this replication link.
      returned: always
      type: str
      sample: null
    partner_server:
      description:
        - The name of the server hosting the partner database.
      returned: always
      type: str
      sample: null
    partner_database:
      description:
        - The name of the partner database.
      returned: always
      type: str
      sample: null
    partner_location:
      description:
        - The Azure Region of the partner database.
      returned: always
      type: str
      sample: null
    role:
      description:
        - The role of the database in the replication link.
      returned: always
      type: sealed-choice
      sample: null
    partner_role:
      description:
        - The role of the partner database in the replication link.
      returned: always
      type: sealed-choice
      sample: null
    start_time:
      description:
        - The start time for the replication link.
      returned: always
      type: str
      sample: null
    percent_complete:
      description:
        - The percentage of seeding complete for the replication link.
      returned: always
      type: integer
      sample: null
    replication_state:
      description:
        - The replication state for the replication link.
      returned: always
      type: str
      sample: null
    value:
      description:
        - The list of database replication links housed in the database.
      returned: always
      type: list
      sample: null
      contains:
        location:
          description:
            - Location of the server that contains this firewall rule.
          returned: always
          type: str
          sample: null
        is_termination_allowed:
          description:
            - >-
              Legacy value indicating whether termination is allowed.  Currently
              always returns true.
          returned: always
          type: bool
          sample: null
        replication_mode:
          description:
            - Replication mode of this replication link.
          returned: always
          type: str
          sample: null
        partner_server:
          description:
            - The name of the server hosting the partner database.
          returned: always
          type: str
          sample: null
        partner_database:
          description:
            - The name of the partner database.
          returned: always
          type: str
          sample: null
        partner_location:
          description:
            - The Azure Region of the partner database.
          returned: always
          type: str
          sample: null
        role:
          description:
            - The role of the database in the replication link.
          returned: always
          type: sealed-choice
          sample: null
        partner_role:
          description:
            - The role of the partner database in the replication link.
          returned: always
          type: sealed-choice
          sample: null
        start_time:
          description:
            - The start time for the replication link.
          returned: always
          type: str
          sample: null
        percent_complete:
          description:
            - The percentage of seeding complete for the replication link.
          returned: always
          type: integer
          sample: null
        replication_state:
          description:
            - The replication state for the replication link.
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
    from azure.mgmt.sql import SqlManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMReplicationLinkInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            server_name=dict(
                type='str',
                required=True
            ),
            database_name=dict(
                type='str',
                required=True
            ),
            link_id=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.server_name = None
        self.database_name = None
        self.link_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2014-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMReplicationLinkInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2014-04-01')

        if (self.resource_group_name is not None and
            self.server_name is not None and
            self.database_name is not None and
            self.link_id is not None):
            self.results['replication_links'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.server_name is not None and
              self.database_name is not None):
            self.results['replication_links'] = self.format_item(self.listbydatabase())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.replication_links.get(resource_group_name=self.resource_group_name,
                                                              server_name=self.server_name,
                                                              database_name=self.database_name,
                                                              link_id=self.link_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydatabase(self):
        response = None

        try:
            response = self.mgmt_client.replication_links.list_by_database(resource_group_name=self.resource_group_name,
                                                                           server_name=self.server_name,
                                                                           database_name=self.database_name)
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
    AzureRMReplicationLinkInfo()


if __name__ == '__main__':
    main()
