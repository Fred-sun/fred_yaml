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
module: azure_rm_communication_info
version_added: '2.9'
short_description: Get Communication info.
description:
  - Get info of Communication.
options:
  support_ticket_name:
    description:
      - Support ticket name.
    required: true
    type: str
  top:
    description:
      - >-
        The number of values to return in the collection. Default is 10 and max
        is 10.
    type: integer
  filter:
    description:
      - >-
        The filter to apply on the operation. You can filter by
        communicationType and createdDate properties. CommunicationType supports
        Equals ('eq') operator and createdDate supports Greater Than ('gt') and
        Greater Than or Equals ('ge') operators. You may combine the
        CommunicationType and CreatedDate filters by Logical And ('and')
        operator.
    type: str
  communication_name:
    description:
      - Communication name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List communications for a subscription support ticket
      azure_rm_communication_info: 
        support_ticket_name: testticket
        

    - name: List web communication created on or after a specific date for a subscription support ticket
      azure_rm_communication_info: 
        support_ticket_name: testticket
        

    - name: List web communications for a subscription support ticket
      azure_rm_communication_info: 
        support_ticket_name: testticket
        

    - name: Get communication details for a subscription support ticket
      azure_rm_communication_info: 
        communication_name: testmessage
        support_ticket_name: testticket
        

'''

RETURN = '''
communications:
  description: >-
    A list of dict results where the key is the name of the Communication and
    the values are the facts for that Communication.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of Communication resources.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Id of the resource.
          returned: always
          type: str
          sample: null
        name:
          description:
            - Name of the resource.
          returned: always
          type: str
          sample: null
        type:
          description:
            - Type of the resource 'Microsoft.Support/communications'.
          returned: always
          type: str
          sample: null
        communication_type:
          description:
            - Communication type.
          returned: always
          type: str
          sample: null
        communication_direction:
          description:
            - Direction of communication.
          returned: always
          type: str
          sample: null
        sender:
          description:
            - >-
              Email address of the sender. This property is required if called
              by a service principal.
          returned: always
          type: str
          sample: null
        subject:
          description:
            - Subject of the communication.
          returned: always
          type: str
          sample: null
        body:
          description:
            - Body of the communication.
          returned: always
          type: str
          sample: null
        created_date:
          description:
            - Time in UTC (ISO 8601 format) when the communication was created.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The URI to fetch the next page of Communication resources.
      returned: always
      type: str
      sample: null
    id:
      description:
        - Id of the resource.
      returned: always
      type: str
      sample: null
    name:
      description:
        - Name of the resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Type of the resource 'Microsoft.Support/communications'.
      returned: always
      type: str
      sample: null
    communication_type:
      description:
        - Communication type.
      returned: always
      type: str
      sample: null
    communication_direction:
      description:
        - Direction of communication.
      returned: always
      type: str
      sample: null
    sender:
      description:
        - >-
          Email address of the sender. This property is required if called by a
          service principal.
      returned: always
      type: str
      sample: null
    subject:
      description:
        - Subject of the communication.
      returned: always
      type: str
      sample: null
    body:
      description:
        - Body of the communication.
      returned: always
      type: str
      sample: null
    created_date:
      description:
        - Time in UTC (ISO 8601 format) when the communication was created.
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
    from azure.mgmt.microsoft.support import Microsoft.Support
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMCommunicationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            support_ticket_name=dict(
                type='str',
                required=True
            ),
            top=dict(
                type='integer'
            ),
            filter=dict(
                type='str'
            ),
            communication_name=dict(
                type='str'
            )
        )

        self.support_ticket_name = None
        self.top = None
        self.filter = None
        self.communication_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMCommunicationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Microsoft.Support,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.support_ticket_name is not None and
            self.communication_name is not None):
            self.results['communications'] = self.format_item(self.get())
        elif (self.support_ticket_name is not None):
            self.results['communications'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.communications.get(support_ticket_name=self.support_ticket_name,
                                                           communication_name=self.communication_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.communications.list(support_ticket_name=self.support_ticket_name,
                                                            top=self.top,
                                                            filter=self.filter)
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
    AzureRMCommunicationInfo()


if __name__ == '__main__':
    main()
