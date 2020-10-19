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
module: azure_rm_sqlvirtualmachinegroup
version_added: '2.9'
short_description: Manage Azure SqlVirtualMachineGroup instance.
description:
  - 'Create, update and delete instance of Azure SqlVirtualMachineGroup.'
options:
  resource_group_name:
    description:
      - >-
        Name of the resource group that contains the resource. You can obtain
        this value from the Azure Resource Manager API or the portal.
    required: true
    type: str
  sqlvirtual_machine_group_name:
    description:
      - Name of the SQL virtual machine group.
    required: true
    type: str
  location:
    description:
      - Resource location.
    type: str
  sqlimage_offer:
    description:
      - 'SQL image offer. Examples may include SQL2016-WS2016, SQL2017-WS2016.'
    type: str
  sqlimage_sku:
    description:
      - SQL image sku.
    type: str
    choices:
      - Developer
      - Enterprise
  wsfc_domain_profile:
    description:
      - Cluster Active Directory domain profile.
    type: dict
    suboptions:
      domain_fqdn:
        description:
          - Fully qualified name of the domain.
        type: str
      ou_path:
        description:
          - >-
            Organizational Unit path in which the nodes and cluster will be
            present.
        type: str
      cluster_bootstrap_account:
        description:
          - >-
            Account name used for creating cluster (at minimum needs permissions
            to 'Create Computer Objects' in domain).
        type: str
      cluster_operator_account:
        description:
          - >-
            Account name used for operating cluster i.e. will be part of
            administrators group on all the participating virtual machines in
            the cluster.
        type: str
      sqlservice_account:
        description:
          - >-
            Account name under which SQL service will run on all participating
            SQL virtual machines in the cluster.
        type: str
      file_share_witness_path:
        description:
          - Optional path for fileshare witness.
        type: str
      storage_account_url:
        description:
          - Fully qualified ARM resource id of the witness storage account.
        type: str
      storage_account_primary_key:
        description:
          - Primary key of the witness storage account.
        type: str
  state:
    description:
      - Assert the state of the SqlVirtualMachineGroup.
      - >-
        Use C(present) to create or update an SqlVirtualMachineGroup and
        C(absent) to delete it.
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
    - name: Creates or updates a SQL virtual machine group.
      azure_rm_sqlvirtualmachinegroup: 
        resource_group_name: testrg
        location: northeurope
        properties:
          sql_image_offer: SQL2016-WS2016
          sql_image_sku: Enterprise
          wsfc_domain_profile:
            cluster_bootstrap_account: testrpadmin
            cluster_operator_account: testrp@testdomain.com
            domain_fqdn: testdomain.com
            ou_path: 'OU=WSCluster,DC=testdomain,DC=com'
            sql_service_account: sqlservice@testdomain.com
            storage_account_primary_key: <primary storage access key>
            storage_account_url: 'https://storgact.blob.core.windows.net/'
        tags:
          mytag: myval
        

    - name: Deletes a SQL virtual machine group.
      azure_rm_sqlvirtualmachinegroup: 
        resource_group_name: testrg
        

    - name: Updates a SQL virtual machine group tags.
      azure_rm_sqlvirtualmachinegroup: 
        resource_group_name: testrg
        tags:
          mytag: myval
        

'''

RETURN = '''
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
provisioning_state:
  description:
    - Provisioning state to track the async operation status.
  returned: always
  type: str
  sample: null
sqlimage_offer:
  description:
    - 'SQL image offer. Examples may include SQL2016-WS2016, SQL2017-WS2016.'
  returned: always
  type: str
  sample: null
sqlimage_sku:
  description:
    - SQL image sku.
  returned: always
  type: str
  sample: null
scale_type:
  description:
    - Scale type.
  returned: always
  type: str
  sample: null
cluster_manager_type:
  description:
    - >-
      Type of cluster manager: Windows Server Failover Cluster (WSFC), implied
      by the scale type of the group and the OS type.
  returned: always
  type: str
  sample: null
cluster_configuration:
  description:
    - Cluster type.
  returned: always
  type: str
  sample: null
wsfc_domain_profile:
  description:
    - Cluster Active Directory domain profile.
  returned: always
  type: dict
  sample: null
  contains:
    domain_fqdn:
      description:
        - Fully qualified name of the domain.
      returned: always
      type: str
      sample: null
    ou_path:
      description:
        - >-
          Organizational Unit path in which the nodes and cluster will be
          present.
      returned: always
      type: str
      sample: null
    cluster_bootstrap_account:
      description:
        - >-
          Account name used for creating cluster (at minimum needs permissions
          to 'Create Computer Objects' in domain).
      returned: always
      type: str
      sample: null
    cluster_operator_account:
      description:
        - >-
          Account name used for operating cluster i.e. will be part of
          administrators group on all the participating virtual machines in the
          cluster.
      returned: always
      type: str
      sample: null
    sqlservice_account:
      description:
        - >-
          Account name under which SQL service will run on all participating SQL
          virtual machines in the cluster.
      returned: always
      type: str
      sample: null
    file_share_witness_path:
      description:
        - Optional path for fileshare witness.
      returned: always
      type: str
      sample: null
    storage_account_url:
      description:
        - Fully qualified ARM resource id of the witness storage account.
      returned: always
      type: str
      sample: null
    storage_account_primary_key:
      description:
        - Primary key of the witness storage account.
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
    from azure.mgmt.sql import SqlVirtualMachineManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSqlVirtualMachineGroup(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            sqlvirtual_machine_group_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            sqlimage_offer=dict(
                type='str',
                disposition='/sqlimage_offer'
            ),
            sqlimage_sku=dict(
                type='str',
                disposition='/sqlimage_sku',
                choices=['Developer',
                         'Enterprise']
            ),
            wsfc_domain_profile=dict(
                type='dict',
                disposition='/wsfc_domain_profile',
                options=dict(
                    domain_fqdn=dict(
                        type='str',
                        disposition='domain_fqdn'
                    ),
                    ou_path=dict(
                        type='str',
                        disposition='ou_path'
                    ),
                    cluster_bootstrap_account=dict(
                        type='str',
                        disposition='cluster_bootstrap_account'
                    ),
                    cluster_operator_account=dict(
                        type='str',
                        disposition='cluster_operator_account'
                    ),
                    sqlservice_account=dict(
                        type='str',
                        disposition='sqlservice_account'
                    ),
                    file_share_witness_path=dict(
                        type='str',
                        disposition='file_share_witness_path'
                    ),
                    storage_account_url=dict(
                        type='str',
                        disposition='storage_account_url'
                    ),
                    storage_account_primary_key=dict(
                        type='str',
                        disposition='storage_account_primary_key'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.sqlvirtual_machine_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSqlVirtualMachineGroup, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(SqlVirtualMachineManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

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
            response = self.mgmt_client.sql_virtual_machine_groups.create_or_update(resource_group_name=self.resource_group_name,
                                                                                    sqlvirtual_machine_group_name=self.sqlvirtual_machine_group_name,
                                                                                    parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SqlVirtualMachineGroup instance.')
            self.fail('Error creating the SqlVirtualMachineGroup instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.sql_virtual_machine_groups.delete(resource_group_name=self.resource_group_name,
                                                                          sqlvirtual_machine_group_name=self.sqlvirtual_machine_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the SqlVirtualMachineGroup instance.')
            self.fail('Error deleting the SqlVirtualMachineGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.sql_virtual_machine_groups.get(resource_group_name=self.resource_group_name,
                                                                       sqlvirtual_machine_group_name=self.sqlvirtual_machine_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSqlVirtualMachineGroup()


if __name__ == '__main__':
    main()
