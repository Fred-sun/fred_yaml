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
module: azure_rm_recordset
version_added: '2.9'
short_description: Manage Azure RecordSet instance.
description:
  - 'Create, update and delete instance of Azure RecordSet.'
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
      - >-
        The type of DNS record in this record set. Record sets of type SOA can
        be updated but not created (they are created when the Private DNS zone
        is created).
      - >-
        The type of DNS record in this record set. Record sets of type SOA
        cannot be deleted (they are deleted when the Private DNS zone is
        deleted).
    required: true
    type: sealed-choice
  relative_record_set_name:
    description:
      - 'The name of the record set, relative to the name of the zone.'
    required: true
    type: str
  if_match:
    description:
      - >-
        The ETag of the record set. Omit this value to always overwrite the
        current record set. Specify the last-seen ETag value to prevent
        accidentally overwriting any concurrent changes.
      - >-
        The ETag of the record set. Omit this value to always overwrite the
        current record set. Specify the last-seen ETag value to prevent
        accidentally overwriting concurrent changes.
      - >-
        The ETag of the record set. Omit this value to always delete the current
        record set. Specify the last-seen ETag value to prevent accidentally
        deleting any concurrent changes.
    type: str
  if_none_match:
    description:
      - >-
        Set to '*' to allow a new record set to be created, but to prevent
        updating an existing record set. Other values will be ignored.
    type: str
  etag:
    description:
      - The ETag of the record set.
    type: str
  metadata:
    description:
      - The metadata attached to the record set.
    type: dictionary
  ttl:
    description:
      - The TTL (time-to-live) of the records in the record set.
    type: integer
  a_records:
    description:
      - The list of A records in the record set.
    type: list
    suboptions:
      ipv4address:
        description:
          - The IPv4 address of this A record.
        type: str
  aaaa_records:
    description:
      - The list of AAAA records in the record set.
    type: list
    suboptions:
      ipv6address:
        description:
          - The IPv6 address of this AAAA record.
        type: str
  mx_records:
    description:
      - The list of MX records in the record set.
    type: list
    suboptions:
      preference:
        description:
          - The preference value for this MX record.
        type: integer
      exchange:
        description:
          - The domain name of the mail host for this MX record.
        type: str
  ptr_records:
    description:
      - The list of PTR records in the record set.
    type: list
    suboptions:
      ptrdname:
        description:
          - The PTR target domain name for this PTR record.
        type: str
  soa_record:
    description:
      - The SOA record in the record set.
    type: dict
    suboptions:
      host:
        description:
          - >-
            The domain name of the authoritative name server for this SOA
            record.
        type: str
      email:
        description:
          - The email contact for this SOA record.
        type: str
      serial_number:
        description:
          - The serial number for this SOA record.
        type: integer
      refresh_time:
        description:
          - The refresh value for this SOA record.
        type: integer
      retry_time:
        description:
          - The retry time for this SOA record.
        type: integer
      expire_time:
        description:
          - The expire time for this SOA record.
        type: integer
      minimum_ttl:
        description:
          - >-
            The minimum value for this SOA record. By convention this is used to
            determine the negative caching duration.
        type: integer
  srv_records:
    description:
      - The list of SRV records in the record set.
    type: list
    suboptions:
      priority:
        description:
          - The priority value for this SRV record.
        type: integer
      weight:
        description:
          - The weight value for this SRV record.
        type: integer
      port:
        description:
          - The port value for this SRV record.
        type: integer
      target:
        description:
          - The target domain name for this SRV record.
        type: str
  txt_records:
    description:
      - The list of TXT records in the record set.
    type: list
    suboptions:
      value:
        description:
          - The text value of this TXT record.
        type: list
  cname:
    description:
      - The canonical name for this CNAME record.
    type: str
  state:
    description:
      - Assert the state of the RecordSet.
      - >-
        Use C(present) to create or update an RecordSet and C(absent) to delete
        it.
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
    - name: PUT Private DNS Zone A Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: A
        relative_record_set_name: recordA
        resource_group_name: resourceGroup1
        properties:
          a_records:
            - ipv4address: 1.2.3.4
          metadata:
            key1: value1
          ttl: 3600
        

    - name: PUT Private DNS Zone AAAA Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: AAAA
        relative_record_set_name: recordAAAA
        resource_group_name: resourceGroup1
        properties:
          aaaa_records:
            - ipv6address: '::1'
          metadata:
            key1: value1
          ttl: 3600
        

    - name: PUT Private DNS Zone CNAME Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: CNAME
        relative_record_set_name: recordCNAME
        resource_group_name: resourceGroup1
        properties:
          cname_record:
            cname: contoso.com
          metadata:
            key1: value1
          ttl: 3600
        

    - name: PUT Private DNS Zone MX Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: MX
        relative_record_set_name: recordMX
        resource_group_name: resourceGroup1
        properties:
          metadata:
            key1: value1
          mx_records:
            - exchange: mail.privatezone1.com
              preference: 0
          ttl: 3600
        

    - name: PUT Private DNS Zone PTR Record Set
      azure_rm_recordset: 
        private_zone_name: 0.0.127.in-addr.arpa
        record_type: PTR
        relative_record_set_name: '1'
        resource_group_name: resourceGroup1
        properties:
          metadata:
            key1: value1
          ptr_records:
            - ptrdname: localhost
          ttl: 3600
        

    - name: PUT Private DNS Zone SOA Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: SOA
        relative_record_set_name: '@'
        resource_group_name: resourceGroup1
        properties:
          metadata:
            key1: value1
          soa_record:
            email: azureprivatedns-hostmaster.microsoft.com
            expire_time: 2419200
            host: azureprivatedns.net
            minimum_ttl: 300
            refresh_time: 3600
            retry_time: 300
            serial_number: 1
          ttl: 3600
        

    - name: PUT Private DNS Zone SRV Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: SRV
        relative_record_set_name: recordSRV
        resource_group_name: resourceGroup1
        properties:
          metadata:
            key1: value1
          srv_records:
            - port: 80
              priority: 0
              target: contoso.com
              weight: 10
          ttl: 3600
        

    - name: PUT Private DNS Zone TXT Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: TXT
        relative_record_set_name: recordTXT
        resource_group_name: resourceGroup1
        properties:
          metadata:
            key1: value1
          ttl: 3600
          txt_records:
            - value:
                - string1
                - string2
        

    - name: PATCH Private DNS Zone A Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: A
        relative_record_set_name: recordA
        resource_group_name: resourceGroup1
        properties:
          metadata:
            key2: value2
        

    - name: PATCH Private DNS Zone AAAA Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: AAAA
        relative_record_set_name: recordAAAA
        resource_group_name: resourceGroup1
        properties:
          metadata:
            key2: value2
        

    - name: PATCH Private DNS Zone CNAME Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: CNAME
        relative_record_set_name: recordCNAME
        resource_group_name: resourceGroup1
        properties:
          metadata:
            key2: value2
        

    - name: PATCH Private DNS Zone MX Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: MX
        relative_record_set_name: recordMX
        resource_group_name: resourceGroup1
        properties:
          metadata:
            key2: value2
        

    - name: PATCH Private DNS Zone PTR Record Set
      azure_rm_recordset: 
        private_zone_name: 0.0.127.in-addr.arpa
        record_type: PTR
        relative_record_set_name: '1'
        resource_group_name: resourceGroup1
        properties:
          metadata:
            key2: value2
        

    - name: PATCH Private DNS Zone SOA Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: SOA
        relative_record_set_name: '@'
        resource_group_name: resourceGroup1
        properties:
          metadata:
            key2: value2
        

    - name: PATCH Private DNS Zone SRV Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: SRV
        relative_record_set_name: recordSRV
        resource_group_name: resourceGroup1
        properties:
          metadata:
            key2: value2
        

    - name: PATCH Private DNS Zone TXT Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: TXT
        relative_record_set_name: recordTXT
        resource_group_name: resourceGroup1
        properties:
          metadata:
            key2: value2
        

    - name: DELETE Private DNS Zone A Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: A
        relative_record_set_name: recordA
        resource_group_name: resourceGroup1
        

    - name: DELETE Private DNS Zone AAAA Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: AAAA
        relative_record_set_name: recordAAAA
        resource_group_name: resourceGroup1
        

    - name: DELETE Private DNS Zone CNAME Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: CNAME
        relative_record_set_name: recordCNAME
        resource_group_name: resourceGroup1
        

    - name: DELETE Private DNS Zone MX Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: MX
        relative_record_set_name: recordMX
        resource_group_name: resourceGroup1
        

    - name: DELETE Private DNS Zone PTR Record Set
      azure_rm_recordset: 
        private_zone_name: 0.0.127.in-addr.arpa
        record_type: PTR
        relative_record_set_name: '1'
        resource_group_name: resourceGroup1
        

    - name: DELETE Private DNS Zone SRV Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: SRV
        relative_record_set_name: recordSRV
        resource_group_name: resourceGroup1
        

    - name: DELETE Private DNS Zone TXT Record Set
      azure_rm_recordset: 
        private_zone_name: privatezone1.com
        record_type: TXT
        relative_record_set_name: recordTXT
        resource_group_name: resourceGroup1
        

'''

RETURN = '''
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
    - The type of the resource. Example - 'Microsoft.Network/privateDnsZones'.
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
        - The domain name of the authoritative name server for this SOA record.
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
          The minimum value for this SOA record. By convention this is used to
          determine the negative caching duration.
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

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.private import PrivateDnsManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMRecordSet(AzureRMModuleBaseExt):
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
                type='sealed-choice',
                required=True
            ),
            relative_record_set_name=dict(
                type='str',
                required=True
            ),
            if_match=dict(
                type='str'
            ),
            if_none_match=dict(
                type='str'
            ),
            etag=dict(
                type='str',
                disposition='/etag'
            ),
            metadata=dict(
                type='dictionary',
                disposition='/metadata'
            ),
            ttl=dict(
                type='integer',
                disposition='/ttl'
            ),
            a_records=dict(
                type='list',
                disposition='/a_records',
                elements='dict',
                options=dict(
                    ipv4address=dict(
                        type='str',
                        disposition='ipv4address'
                    )
                )
            ),
            aaaa_records=dict(
                type='list',
                disposition='/aaaa_records',
                elements='dict',
                options=dict(
                    ipv6address=dict(
                        type='str',
                        disposition='ipv6address'
                    )
                )
            ),
            mx_records=dict(
                type='list',
                disposition='/mx_records',
                elements='dict',
                options=dict(
                    preference=dict(
                        type='integer',
                        disposition='preference'
                    ),
                    exchange=dict(
                        type='str',
                        disposition='exchange'
                    )
                )
            ),
            ptr_records=dict(
                type='list',
                disposition='/ptr_records',
                elements='dict',
                options=dict(
                    ptrdname=dict(
                        type='str',
                        disposition='ptrdname'
                    )
                )
            ),
            soa_record=dict(
                type='dict',
                disposition='/soa_record',
                options=dict(
                    host=dict(
                        type='str',
                        disposition='host'
                    ),
                    email=dict(
                        type='str',
                        disposition='email'
                    ),
                    serial_number=dict(
                        type='integer',
                        disposition='serial_number'
                    ),
                    refresh_time=dict(
                        type='integer',
                        disposition='refresh_time'
                    ),
                    retry_time=dict(
                        type='integer',
                        disposition='retry_time'
                    ),
                    expire_time=dict(
                        type='integer',
                        disposition='expire_time'
                    ),
                    minimum_ttl=dict(
                        type='integer',
                        disposition='minimum_ttl'
                    )
                )
            ),
            srv_records=dict(
                type='list',
                disposition='/srv_records',
                elements='dict',
                options=dict(
                    priority=dict(
                        type='integer',
                        disposition='priority'
                    ),
                    weight=dict(
                        type='integer',
                        disposition='weight'
                    ),
                    port=dict(
                        type='integer',
                        disposition='port'
                    ),
                    target=dict(
                        type='str',
                        disposition='target'
                    )
                )
            ),
            txt_records=dict(
                type='list',
                disposition='/txt_records',
                elements='dict',
                options=dict(
                    value=dict(
                        type='list',
                        disposition='value',
                        elements='str'
                    )
                )
            ),
            cname=dict(
                type='str',
                disposition='/cname'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.private_zone_name = None
        self.record_type = None
        self.relative_record_set_name = None
        self.if_match = None
        self.if_none_match = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMRecordSet, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(PrivateDnsManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01')

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
            response = self.mgmt_client.record_sets.create_or_update(resource_group_name=self.resource_group_name,
                                                                     private_zone_name=self.private_zone_name,
                                                                     record_type=self.record_type,
                                                                     relative_record_set_name=self.relative_record_set_name,
                                                                     if_match=self.if_match,
                                                                     if_none_match=self.if_none_match,
                                                                     parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the RecordSet instance.')
            self.fail('Error creating the RecordSet instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.record_sets.delete(resource_group_name=self.resource_group_name,
                                                           private_zone_name=self.private_zone_name,
                                                           record_type=self.record_type,
                                                           relative_record_set_name=self.relative_record_set_name,
                                                           if_match=self.if_match)
        except CloudError as e:
            self.log('Error attempting to delete the RecordSet instance.')
            self.fail('Error deleting the RecordSet instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.record_sets.get(resource_group_name=self.resource_group_name,
                                                        private_zone_name=self.private_zone_name,
                                                        record_type=self.record_type,
                                                        relative_record_set_name=self.relative_record_set_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMRecordSet()


if __name__ == '__main__':
    main()
