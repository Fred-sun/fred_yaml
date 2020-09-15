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
module: azure_rm_experiment_info
version_added: '2.9'
short_description: Get Experiment info.
description:
  - Get info of Experiment.
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  profile_name:
    description:
      - The Profile identifier associated with the Tenant and Partner
    required: true
    type: str
  experiment_name:
    description:
      - The Experiment identifier associated with the Experiment
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets a list of Experiments
      azure_rm_experiment_info: 
        profile_name: MyProfile
        resource_group_name: MyResourceGroup
        

    - name: Gets an Experiment by ExperimentName
      azure_rm_experiment_info: 
        experiment_name: MyExperiment
        profile_name: MyProfile
        resource_group_name: MyResourceGroup
        

'''

RETURN = '''
experiments:
  description: >-
    A list of dict results where the key is the name of the Experiment and the
    values are the facts for that Experiment.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of Experiments within a resource group.
      returned: always
      type: list
      sample: null
      contains:
        description:
          description:
            - The description of the details or intents of the Experiment
          returned: always
          type: str
          sample: null
        endpoint_a:
          description:
            - The endpoint A of an experiment
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - The name of the endpoint
              returned: always
              type: str
              sample: null
            endpoint:
              description:
                - The endpoint URL
              returned: always
              type: str
              sample: null
        endpoint_b:
          description:
            - The endpoint B of an experiment
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - The name of the endpoint
              returned: always
              type: str
              sample: null
            endpoint:
              description:
                - The endpoint URL
              returned: always
              type: str
              sample: null
        enabled_state:
          description:
            - The state of the Experiment
          returned: always
          type: str
          sample: null
        resource_state:
          description:
            - Resource status.
          returned: always
          type: str
          sample: null
        status:
          description:
            - The description of Experiment status from the server side
          returned: always
          type: str
          sample: null
        script_file_uri:
          description:
            - The uri to the Script used in the Experiment
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - URL to get the next set of Experiment objects if there are any.
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
    description:
      description:
        - The description of the details or intents of the Experiment
      returned: always
      type: str
      sample: null
    endpoint_a:
      description:
        - The endpoint A of an experiment
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - The name of the endpoint
          returned: always
          type: str
          sample: null
        endpoint:
          description:
            - The endpoint URL
          returned: always
          type: str
          sample: null
    endpoint_b:
      description:
        - The endpoint B of an experiment
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - The name of the endpoint
          returned: always
          type: str
          sample: null
        endpoint:
          description:
            - The endpoint URL
          returned: always
          type: str
          sample: null
    enabled_state:
      description:
        - The state of the Experiment
      returned: always
      type: str
      sample: null
    resource_state:
      description:
        - Resource status.
      returned: always
      type: str
      sample: null
    status:
      description:
        - The description of Experiment status from the server side
      returned: always
      type: str
      sample: null
    script_file_uri:
      description:
        - The uri to the Script used in the Experiment
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


class AzureRMExperimentInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            profile_name=dict(
                type='str',
                required=True
            ),
            experiment_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.profile_name = None
        self.experiment_name = None

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
        super(AzureRMExperimentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(FrontDoorManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-11-01')

        if (self.resource_group_name is not None and
            self.profile_name is not None and
            self.experiment_name is not None):
            self.results['experiments'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.profile_name is not None):
            self.results['experiments'] = self.format_item(self.listbyprofile())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.experiments.get(resource_group_name=self.resource_group_name,
                                                        profile_name=self.profile_name,
                                                        experiment_name=self.experiment_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyprofile(self):
        response = None

        try:
            response = self.mgmt_client.experiments.list_by_profile(resource_group_name=self.resource_group_name,
                                                                    profile_name=self.profile_name)
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
    AzureRMExperimentInfo()


if __name__ == '__main__':
    main()
