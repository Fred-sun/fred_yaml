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
module: azure_rm_domaintopic_info
version_added: '2.9'
short_description: Get DomainTopic info.
description:
  - Get info of DomainTopic.
options:
  resource_group_name:
    description:
      - The name of the resource group within the user's subscription.
    required: true
    type: str
  domain_name:
    description:
      - Name of the domain.
      - Domain name.
    required: true
    type: str
  domain_topic_name:
    description:
      - Name of the topic.
    type: str
  filter:
    description:
      - >-
        The query used to filter the search results using OData syntax.
        Filtering is permitted on the 'name' property only and with limited
        number of OData operations. These operations are: the 'contains'
        function as well as the following logical operations: not, and, or, eq
        (for equal), and ne (for not equal). No arithmetic operations are
        supported. The following is a valid filter example:
        $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following
        is not a valid filter example: $filter=location eq 'westus'.
    type: str
  top:
    description:
      - >-
        The number of results to return per page for the list operation. Valid
        range for top parameter is 1 to 100. If not specified, the default
        number of results to be returned is 20 items per page.
    type: integer
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: DomainTopics_Get
      azure_rm_domaintopic_info: 
        domain_name: exampledomain2
        domain_topic_name: topic1
        resource_group_name: examplerg
        

    - name: DomainTopics_ListByDomain
      azure_rm_domaintopic_info: 
        domain_name: exampledomain2
        resource_group_name: examplerg
        

'''

RETURN = '''
domain_topics:
  description: >-
    A list of dict results where the key is the name of the DomainTopic and the
    values are the facts for that DomainTopic.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Fully qualified identifier of the resource.
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
        - Type of the resource.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Provisioning state of the domain topic.
      returned: always
      type: str
      sample: null
    value:
      description:
        - A collection of Domain Topics.
      returned: always
      type: list
      sample: null
      contains:
        provisioning_state:
          description:
            - Provisioning state of the domain topic.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - A link for the next page of domain topics.
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
    from azure.mgmt.event import EventGridManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMDomainTopicInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            domain_name=dict(
                type='str',
                required=True
            ),
            domain_topic_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            )
        )

        self.resource_group_name = None
        self.domain_name = None
        self.domain_topic_name = None
        self.filter = None
        self.top = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDomainTopicInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(EventGridManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.domain_name is not None and
            self.domain_topic_name is not None):
            self.results['domain_topics'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.domain_name is not None):
            self.results['domain_topics'] = self.format_item(self.listbydomain())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.domain_topics.get(resource_group_name=self.resource_group_name,
                                                          domain_name=self.domain_name,
                                                          domain_topic_name=self.domain_topic_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbydomain(self):
        response = None

        try:
            response = self.mgmt_client.domain_topics.list_by_domain(resource_group_name=self.resource_group_name,
                                                                     domain_name=self.domain_name,
                                                                     filter=self.filter,
                                                                     top=self.top)
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
    AzureRMDomainTopicInfo()


if __name__ == '__main__':
    main()
