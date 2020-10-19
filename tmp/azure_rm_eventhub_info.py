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
module: azure_rm_eventhub_info
version_added: '2.9'
short_description: Get EventHub info.
description:
  - Get info of EventHub.
options:
  resource_group_name:
    description:
      - Name of the Resource group within the Azure subscription.
    required: true
    type: str
  namespace_name:
    description:
      - The namespace name
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: RulesCreateOrUpdate
      azure_rm_eventhub_info: 
        namespace_name: sdk-Namespace-3174
        resource_group_name: ArunMonocle
        

'''

RETURN = '''
event_hubs:
  description: >-
    A list of dict results where the key is the name of the EventHub and the
    values are the facts for that EventHub.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Result of the List EventHubs operation.
      returned: always
      type: list
      sample: null
      contains:
        partition_ids:
          description:
            - Current number of shards on the Event Hub.
          returned: always
          type: list
          sample: null
        created_at:
          description:
            - Exact time the Event Hub was created.
          returned: always
          type: str
          sample: null
        updated_at:
          description:
            - The exact time the message was updated.
          returned: always
          type: str
          sample: null
        message_retention_in_days:
          description:
            - >-
              Number of days to retain the events for this Event Hub, value
              should be 1 to 7 days
          returned: always
          type: integer
          sample: null
        partition_count:
          description:
            - >-
              Number of partitions created for the Event Hub, allowed values are
              from 1 to 32 partitions.
          returned: always
          type: integer
          sample: null
        status:
          description:
            - Enumerates the possible values for the status of a Event Hub.
          returned: always
          type: sealed-choice
          sample: null
        capture_description:
          description:
            - Properties of capture description
          returned: always
          type: dict
          sample: null
          contains:
            enabled:
              description:
                - >-
                  A value that indicates whether capture description is
                  enabled. 
              returned: always
              type: bool
              sample: null
            encoding:
              description:
                - >-
                  Enumerates the possible values for the encoding format of
                  capture description.
              returned: always
              type: sealed-choice
              sample: null
            interval_in_seconds:
              description:
                - >-
                  The time window allows you to set the frequency with which the
                  capture to Azure Blobs will happen, value should between 60 to
                  900 seconds
              returned: always
              type: integer
              sample: null
            size_limit_in_bytes:
              description:
                - >-
                  The size window defines the amount of data built up in your
                  Event Hub before an capture operation, value should be between
                  10485760 and 524288000 bytes
              returned: always
              type: integer
              sample: null
            destination:
              description:
                - >-
                  Properties of Destination where capture will be stored.
                  (Storage Account, Blob Names)
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - Name for capture destination
                  returned: always
                  type: str
                  sample: null
                storage_account_resource_id:
                  description:
                    - >-
                      Resource id of the storage account to be used to create
                      the blobs
                  returned: always
                  type: str
                  sample: null
                blob_container:
                  description:
                    - Blob container Name
                  returned: always
                  type: str
                  sample: null
                archive_name_format:
                  description:
                    - >-
                      Blob naming convention for archive, e.g.
                      {Namespace}/{EventHub}/{PartitionId}/{Year}/{Month}/{Day}/{Hour}/{Minute}/{Second}.
                      Here all the parameters (Namespace,EventHub .. etc) are
                      mandatory irrespective of order
                  returned: always
                  type: str
                  sample: null
    next_link:
      description:
        - >-
          Link to the next set of results. Not empty if Value contains
          incomplete list of EventHubs.
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
    from azure.mgmt.service import ServiceBusManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMEventHubInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            namespace_name=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.namespace_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMEventHubInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ServiceBusManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01')

        if (self.resource_group_name is not None and
            self.namespace_name is not None):
            self.results['event_hubs'] = self.format_item(self.listbynamespace())
        return self.results

    def listbynamespace(self):
        response = None

        try:
            response = self.mgmt_client.event_hubs.list_by_namespace(resource_group_name=self.resource_group_name,
                                                                     namespace_name=self.namespace_name)
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
    AzureRMEventHubInfo()


if __name__ == '__main__':
    main()
