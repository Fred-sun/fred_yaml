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
module: azure_rm_association_info
version_added: '2.9'
short_description: Get Association info.
description:
  - Get info of Association.
options:
  scope:
    description:
      - The scope of the association.
    required: true
    type: str
  association_name:
    description:
      - The name of the association.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get an association
      azure_rm_association_info: 
        association_name: associationName
        scope: scope
        

    - name: Get all associations
      azure_rm_association_info: 
        scope: scope
        

'''

RETURN = '''
associations:
  description: >-
    A list of dict results where the key is the name of the Association and the
    values are the facts for that Association.
  returned: always
  type: complex
  contains:
    id:
      description:
        - The association id.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The association name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - The association type.
      returned: always
      type: str
      sample: null
    target_resource_id:
      description:
        - >-
          The REST resource instance of the target resource for this
          association.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the association.
      returned: always
      type: str
      sample: null
    value:
      description:
        - The array of associations.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - The association id.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The association name.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The association type.
          returned: always
          type: str
          sample: null
        target_resource_id:
          description:
            - >-
              The REST resource instance of the target resource for this
              association.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - The provisioning state of the association.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The URL to use for getting the next set of results.
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
    from azure.mgmt.customproviders import customproviders
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAssociationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            scope=dict(
                type='str',
                required=True
            ),
            association_name=dict(
                type='str'
            )
        )

        self.scope = None
        self.association_name = None

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
        super(AzureRMAssociationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(customproviders,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

        if (self.scope is not None and
            self.association_name is not None):
            self.results['associations'] = self.format_item(self.get())
        elif (self.scope is not None):
            self.results['associations'] = self.format_item(self.listall())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.associations.get(scope=self.scope,
                                                         association_name=self.association_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listall(self):
        response = None

        try:
            response = self.mgmt_client.associations.list_all(scope=self.scope)
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
    AzureRMAssociationInfo()


if __name__ == '__main__':
    main()
