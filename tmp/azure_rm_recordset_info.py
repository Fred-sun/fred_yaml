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
module: azure_rm_recordset_info
version_added: '2.9'
short_description: Get RecordSet info.
description:
  - Get info of RecordSet.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  private_zone_name:
    description:
      - The name of the Private DNS zone (without a terminating dot).
    required: true
    type: str
  record_type:
    description:
      - The type of DNS record in this record set.
      - The type of record sets to enumerate.
    type: sealed-choice
  relative_record_set_name:
    description:
      - 'The name of the record set, relative to the name of the zone.'
    type: str
  top:
    description:
      - >-
        The maximum number of record sets to return. If not specified, returns
        up to 100 record sets.
    type: integer
  recordsetnamesuffix:
    description:
      - >-
        The suffix label of the record set name to be used to filter the record
        set enumeration. If this parameter is specified, the returned
        enumeration will only contain records that end with
        ".<recordsetnamesuffix>".
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GET Private DNS Zone A Record Set
      azure_rm_recordset_info: 
        private_zone_name: privatezone1.com
        record_type: A
        relative_record_set_name: recordA
        resource_group_name: resourceGroup1
        

    - name: GET Private DNS Zone AAAA Record Set
      azure_rm_recordset_info: 
        private_zone_name: privatezone1.com
        record_type: AAAA
        relative_record_set_name: recordAAAA
        resource_group_name: resourceGroup1
        

    - name: GET Private DNS Zone CNAME Record Set
      azure_rm_recordset_info: 
        private_zone_name: privatezone1.com
        record_type: CNAME
        relative_record_set_name: recordCNAME
        resource_group_name: resourceGroup1
        

    - name: GET Private DNS Zone MX Record Set
      azure_rm_recordset_info: 
        private_zone_name: privatezone1.com
        record_type: MX
        relative_record_set_name: recordMX
        resource_group_name: resourceGroup1
        

    - name: GET Private DNS Zone PTR Record Set
      azure_rm_recordset_info: 
        private_zone_name: 0.0.127.in-addr.arpa
        record_type: PTR
        relative_record_set_name: '1'
        resource_group_name: resourceGroup1
        

    - name: GET Private DNS Zone SOA Record Set
      azure_rm_recordset_info: 
        private_zone_name: privatezone1.com
        record_type: SOA
        relative_record_set_name: '@'
        resource_group_name: resourceGroup1
        

    - name: GET Private DNS Zone SRV Record Set
      azure_rm_recordset_info: 
        private_zone_name: privatezone1.com
        record_type: SRV
        relative_record_set_name: recordSRV
        resource_group_name: resourceGroup1
        

    - name: GET Private DNS Zone TXT Record Set
      azure_rm_recordset_info: 
        private_zone_name: privatezone1.com
        record_type: TXT
        relative_record_set_name: recordTXT
        resource_group_name: resourceGroup1
        

    - name: GET Private DNS Zone A Record Sets
      azure_rm_recordset_info: 
        private_zone_name: privatezone1.com
        record_type: A
        resource_group_name: resourceGroup1
        

    - name: GET Private DNS Zone AAAA Record Sets
      azure_rm_recordset_info: 
        private_zone_name: privatezone1.com
        record_type: AAAA
        resource_group_name: resourceGroup1
        

    - name: GET Private DNS Zone CNAME Record Sets
      azure_rm_recordset_info: 
        private_zone_name: privatezone1.com
        record_type: CNAME
        resource_group_name: resourceGroup1
        

    - name: GET Private DNS Zone MX Record Sets
      azure_rm_recordset_info: 
        private_zone_name: privatezone1.com
        record_type: MX
        resource_group_name: resourceGroup1
        

    - name: GET Private DNS Zone PTR Record Sets
      azure_rm_recordset_info: 
        private_zone_name: 0.0.127.in-addr.arpa
        record_type: PTR
        resource_group_name: resourceGroup1
        

    - name: GET Private DNS Zone SOA Record Sets
      azure_rm_recordset_info: 
        private_zone_name: privatezone1.com
        record_type: SOA
        resource_group_name: resourceGroup1
        

    - name: GET Private DNS Zone SRV Record Sets
      azure_rm_recordset_info: 
        private_zone_name: privatezone1.com
        record_type: SRV
        resource_group_name: resourceGroup1
        

    - name: GET Private DNS Zone TXT Record Sets
      azure_rm_recordset_info: 
        private_zone_name: privatezone1.com
        record_type: TXT
        resource_group_name: resourceGroup1
        

    - name: GET Private DNS Zone ALL Record Sets
      azure_rm_recordset_info: 
        private_zone_name: privatezone1.com
        resource_group_name: resourceGroup1
        

'''

RETURN = '''
record_sets:
  description: >-
    A list of dict results where the key is the name of the RecordSet and the
    values are the facts for that RecordSet.
  returned: always
  type: complex
  contains:
    id:
      description:
        - >-
          Fully qualified resource Id for the resource. Example -
          '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateDnsZoneName}'.
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource
      returned: always
      type: str
      sample: null
    type:
      description:
        - >-
          The type of the resource. Example -
          'Microsoft.Network/privateDnsZones'.
      returned: always
      type: str
      sample: null
    etag:
      description:
        - The ETag of the record set.
      returned: always
      type: str
      sample: null
    metadata:
      description:
        - The metadata attached to the record set.
      returned: always
      type: dictionary
      sample: null
    ttl:
      description:
        - The TTL (time-to-live) of the records in the record set.
      returned: always
      type: integer
      sample: null
    fqdn:
      description:
        - Fully qualified domain name of the record set.
      returned: always
      type: str
      sample: null
    is_auto_registered:
      description:
        - >-
          Is the record set auto-registered in the Private DNS zone through a
          virtual network link?
      returned: always
      type: bool
      sample: null
    a_records:
      description:
        - The list of A records in the record set.
      returned: always
      type: list
      sample: null
      contains:
        ipv4address:
          description:
            - The IPv4 address of this A record.
          returned: always
          type: str
          sample: null
    aaaa_records:
      description:
        - The list of AAAA records in the record set.
      returned: always
      type: list
      sample: null
      contains:
        ipv6address:
          description:
            - The IPv6 address of this AAAA record.
          returned: always
          type: str
          sample: null
    mx_records:
      description:
        - The list of MX records in the record set.
      returned: always
      type: list
      sample: null
      contains:
        preference:
          description:
            - The preference value for this MX record.
          returned: always
          type: integer
          sample: null
        exchange:
          description:
            - The domain name of the mail host for this MX record.
          returned: always
          type: str
          sample: null
    ptr_records:
      description:
        - The list of PTR records in the record set.
      returned: always
      type: list
      sample: null
      contains:
        ptrdname:
          description:
            - The PTR target domain name for this PTR record.
          returned: always
          type: str
          sample: null
    soa_record:
      description:
        - The SOA record in the record set.
      returned: always
      type: dict
      sample: null
      contains:
        host:
          description:
            - >-
              The domain name of the authoritative name server for this SOA
              record.
          returned: always
          type: str
          sample: null
        email:
          description:
            - The email contact for this SOA record.
          returned: always
          type: str
          sample: null
        serial_number:
          description:
            - The serial number for this SOA record.
          returned: always
          type: integer
          sample: null
        refresh_time:
          description:
            - The refresh value for this SOA record.
          returned: always
          type: integer
          sample: null
        retry_time:
          description:
            - The retry time for this SOA record.
          returned: always
          type: integer
          sample: null
        expire_time:
          description:
            - The expire time for this SOA record.
          returned: always
          type: integer
          sample: null
        minimum_ttl:
          description:
            - >-
              The minimum value for this SOA record. By convention this is used
              to determine the negative caching duration.
          returned: always
          type: integer
          sample: null
    srv_records:
      description:
        - The list of SRV records in the record set.
      returned: always
      type: list
      sample: null
      contains:
        priority:
          description:
            - The priority value for this SRV record.
          returned: always
          type: integer
          sample: null
        weight:
          description:
            - The weight value for this SRV record.
          returned: always
          type: integer
          sample: null
        port:
          description:
            - The port value for this SRV record.
          returned: always
          type: integer
          sample: null
        target:
          description:
            - The target domain name for this SRV record.
          returned: always
          type: str
          sample: null
    txt_records:
      description:
        - The list of TXT records in the record set.
      returned: always
      type: list
      sample: null
      contains:
        value:
          description:
            - The text value of this TXT record.
          returned: always
          type: list
          sample: null
    cname:
      description:
        - The canonical name for this CNAME record.
      returned: always
      type: str
      sample: null
    value:
      description:
        - Information about the record sets in the response.
      returned: always
      type: list
      sample: null
      contains:
        etag:
          description:
            - The ETag of the record set.
          returned: always
          type: str
          sample: null
        metadata:
          description:
            - The metadata attached to the record set.
          returned: always
          type: dictionary
          sample: null
        ttl:
          description:
            - The TTL (time-to-live) of the records in the record set.
          returned: always
          type: integer
          sample: null
        fqdn:
          description:
            - Fully qualified domain name of the record set.
          returned: always
          type: str
          sample: null
        is_auto_registered:
          description:
            - >-
              Is the record set auto-registered in the Private DNS zone through
              a virtual network link?
          returned: always
          type: bool
          sample: null
        a_records:
          description:
            - The list of A records in the record set.
          returned: always
          type: list
          sample: null
          contains:
            ipv4address:
              description:
                - The IPv4 address of this A record.
              returned: always
              type: str
              sample: null
        aaaa_records:
          description:
            - The list of AAAA records in the record set.
          returned: always
          type: list
          sample: null
          contains:
            ipv6address:
              description:
                - The IPv6 address of this AAAA record.
              returned: always
              type: str
              sample: null
        mx_records:
          description:
            - The list of MX records in the record set.
          returned: always
          type: list
          sample: null
          contains:
            preference:
              description:
                - The preference value for this MX record.
              returned: always
              type: integer
              sample: null
            exchange:
              description:
                - The domain name of the mail host for this MX record.
              returned: always
              type: str
              sample: null
        ptr_records:
          description:
            - The list of PTR records in the record set.
          returned: always
          type: list
          sample: null
          contains:
            ptrdname:
              description:
                - The PTR target domain name for this PTR record.
              returned: always
              type: str
              sample: null
        soa_record:
          description:
            - The SOA record in the record set.
          returned: always
          type: dict
          sample: null
          contains:
            host:
              description:
                - >-
                  The domain name of the authoritative name server for this SOA
                  record.
              returned: always
              type: str
              sample: null
            email:
              description:
                - The email contact for this SOA record.
              returned: always
              type: str
              sample: null
            serial_number:
              description:
                - The serial number for this SOA record.
              returned: always
              type: integer
              sample: null
            refresh_time:
              description:
                - The refresh value for this SOA record.
              returned: always
              type: integer
              sample: null
            retry_time:
              description:
                - The retry time for this SOA record.
              returned: always
              type: integer
              sample: null
            expire_time:
              description:
                - The expire time for this SOA record.
              returned: always
              type: integer
              sample: null
            minimum_ttl:
              description:
                - >-
                  The minimum value for this SOA record. By convention this is
                  used to determine the negative caching duration.
              returned: always
              type: integer
              sample: null
        srv_records:
          description:
            - The list of SRV records in the record set.
          returned: always
          type: list
          sample: null
          contains:
            priority:
              description:
                - The priority value for this SRV record.
              returned: always
              type: integer
              sample: null
            weight:
              description:
                - The weight value for this SRV record.
              returned: always
              type: integer
              sample: null
            port:
              description:
                - The port value for this SRV record.
              returned: always
              type: integer
              sample: null
            target:
              description:
                - The target domain name for this SRV record.
              returned: always
              type: str
              sample: null
        txt_records:
          description:
            - The list of TXT records in the record set.
          returned: always
          type: list
          sample: null
          contains:
            value:
              description:
                - The text value of this TXT record.
              returned: always
              type: list
              sample: null
        cname:
          description:
            - The canonical name for this CNAME record.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The continuation token for the next page of results.
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
    from azure.mgmt.private import PrivateDnsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMRecordSetInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            private_zone_name=dict(
                type='str',
                required=True
            ),
            record_type=dict(
                type='sealed-choice'
            ),
            relative_record_set_name=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            recordsetnamesuffix=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.private_zone_name = None
        self.record_type = None
        self.relative_record_set_name = None
        self.top = None
        self.recordsetnamesuffix = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-09-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMRecordSetInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(PrivateDnsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01')

        if (self.resource_group_name is not None and
            self.private_zone_name is not None and
            self.record_type is not None and
            self.relative_record_set_name is not None):
            self.results['record_sets'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.private_zone_name is not None and
              self.record_type is not None):
            self.results['record_sets'] = self.format_item(self.listbytype())
        elif (self.resource_group_name is not None and
              self.private_zone_name is not None):
            self.results['record_sets'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.record_sets.get(resource_group_name=self.resource_group_name,
                                                        private_zone_name=self.private_zone_name,
                                                        record_type=self.record_type,
                                                        relative_record_set_name=self.relative_record_set_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbytype(self):
        response = None

        try:
            response = self.mgmt_client.record_sets.list_by_type(resource_group_name=self.resource_group_name,
                                                                 private_zone_name=self.private_zone_name,
                                                                 record_type=self.record_type,
                                                                 top=self.top,
                                                                 recordsetnamesuffix=self.recordsetnamesuffix)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.record_sets.list(resource_group_name=self.resource_group_name,
                                                         private_zone_name=self.private_zone_name,
                                                         top=self.top,
                                                         recordsetnamesuffix=self.recordsetnamesuffix)
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
    AzureRMRecordSetInfo()


if __name__ == '__main__':
    main()
