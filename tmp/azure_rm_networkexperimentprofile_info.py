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
module: azure_rm_networkexperimentprofile_info
version_added: '2.9'
short_description: Get NetworkExperimentProfile info.
description:
  - Get info of NetworkExperimentProfile.
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    type: str
  profile_name:
    description:
      - The Profile identifier associated with the Tenant and Partner
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List NetworkExperiment Profiles in a Resource Group
      azure_rm_networkexperimentprofile_info: 
        {}
        

    - name: Gets an NetworkExperiment Profile by Profile Id
      azure_rm_networkexperimentprofile_info: 
        profile_name: MyProfile
        resource_group_name: MyResourceGroup
        

'''

RETURN = '''
network_experiment_profiles:
  description: >-
    A list of dict results where the key is the name of the
    NetworkExperimentProfile and the values are the facts for that
    NetworkExperimentProfile.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of Profiles within a resource group.
      returned: always
      type: list
      sample: null
      contains:
        etag:
          description:
            - >-
              Gets a unique read-only string that changes whenever the resource
              is updated.
          returned: always
          type: str
          sample: null
        resource_state:
          description:
            - Resource status.
          returned: always
          type: str
          sample: null
        enabled_state:
          description:
            - The state of the Experiment
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - URL to get the next set of Profile objects if there are any.
      returned: always
      type: str
      sample: null
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
        - Resource location.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    etag:
      description:
        - >-
          Gets a unique read-only string that changes whenever the resource is
          updated.
      returned: always
      type: str
      sample: null
    resource_state:
      description:
        - Resource status.
      returned: always
      type: str
      sample: null
    enabled_state:
      description:
        - The state of the Experiment
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
    from azure.mgmt.front import FrontDoorManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMNetworkExperimentProfileInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            profile_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.profile_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-11-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMNetworkExperimentProfileInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(FrontDoorManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-11-01')

        if (self.resource_group_name is not None and
            self.profile_name is not None):
            self.results['network_experiment_profiles'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['network_experiment_profiles'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['network_experiment_profiles'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.network_experiment_profiles.get(resource_group_name=self.resource_group_name,
                                                                        profile_name=self.profile_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.network_experiment_profiles.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.network_experiment_profiles.list()
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
    AzureRMNetworkExperimentProfileInfo()


if __name__ == '__main__':
    main()
