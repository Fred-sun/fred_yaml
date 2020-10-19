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
module: azure_rm_migrateproject_info
version_added: '2.9'
short_description: Get MigrateProject info.
description:
  - Get info of MigrateProject.
options:
  resource_group_name:
    description:
      - Name of the Azure Resource Group that migrate project is part of.
    required: true
    type: str
  migrate_project_name:
    description:
      - Name of the Azure Migrate project.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: MigrateProjects_Get
      azure_rm_migrateproject_info: 
        migrate_project_name: project01
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
migrate_projects:
  description: >-
    A list of dict results where the key is the name of the MigrateProject and
    the values are the facts for that MigrateProject.
  returned: always
  type: complex
  contains:
    e_tag:
      description:
        - Gets or sets the eTag for concurrency control.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Gets or sets the Azure location in which migrate project is created.
      returned: always
      type: str
      sample: null
    id:
      description:
        - Gets the relative URL to get this migrate project.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Gets the name of the migrate project.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Handled by resource provider. Type = Microsoft.Migrate/MigrateProject.
      returned: always
      type: str
      sample: null
    additional_properties:
      description:
        - ''
      returned: always
      type: str
      sample: null
    registered_tools:
      description:
        - Gets or sets the list of tools registered with the migrate project.
      returned: always
      type: list
      sample: null
    summary:
      description:
        - Gets the summary of the migrate project.
      returned: always
      type: dictionary
      sample: null
    last_summary_refreshed_time:
      description:
        - Gets the last time the project summary was refreshed.
      returned: always
      type: str
      sample: null
    refresh_summary_state:
      description:
        - Gets the refresh summary state.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Provisioning state of the migrate project.
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
    from azure.mgmt.azure import Azure Migrate Hub
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMMigrateProjectInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            migrate_project_name=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.migrate_project_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-09-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMMigrateProjectInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Migrate Hub,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

        if (self.resource_group_name is not None and
            self.migrate_project_name is not None):
            self.results['migrate_projects'] = self.format_item(self.getmigrateproject())
        return self.results

    def getmigrateproject(self):
        response = None

        try:
            response = self.mgmt_client.migrate_projects.get_migrate_project(resource_group_name=self.resource_group_name,
                                                                             migrate_project_name=self.migrate_project_name)
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
    AzureRMMigrateProjectInfo()


if __name__ == '__main__':
    main()
