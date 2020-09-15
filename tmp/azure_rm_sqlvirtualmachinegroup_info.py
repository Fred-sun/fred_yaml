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
module: azure_rm_sqlvirtualmachinegroup_info
version_added: '2.9'
short_description: Get SqlVirtualMachineGroup info.
description:
  - Get info of SqlVirtualMachineGroup.
options:
  resource_group_name:
    description:
      - >-
        Name of the resource group that contains the resource. You can obtain
        this value from the Azure Resource Manager API or the portal.
    type: str
  sqlvirtual_machine_group_name:
    description:
      - Name of the SQL virtual machine group.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Gets a SQL virtual machine group.
      azure_rm_sqlvirtualmachinegroup_info: 
        resource_group_name: testrg
        

    - name: Gets all SQL virtual machine groups in a resource group.
      azure_rm_sqlvirtualmachinegroup_info: 
        resource_group_name: testrg
        

    - name: Gets all SQL virtual machine groups in a subscription.
      azure_rm_sqlvirtualmachinegroup_info: 
        {}
        

'''

RETURN = '''
sql_virtual_machine_groups:
  description: >-
    A list of dict results where the key is the name of the
    SqlVirtualMachineGroup and the values are the facts for that
    SqlVirtualMachineGroup.
  returned: always
  type: complex
  contains:
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
          Type of cluster manager: Windows Server Failover Cluster (WSFC),
          implied by the scale type of the group and the OS type.
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
              Account name used for creating cluster (at minimum needs
              permissions to 'Create Computer Objects' in domain).
          returned: always
          type: str
          sample: null
        cluster_operator_account:
          description:
            - >-
              Account name used for operating cluster i.e. will be part of
              administrators group on all the participating virtual machines in
              the cluster.
          returned: always
          type: str
          sample: null
        sqlservice_account:
          description:
            - >-
              Account name under which SQL service will run on all participating
              SQL virtual machines in the cluster.
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
    value:
      description:
        - Array of results.
      returned: always
      type: list
      sample: null
      contains:
        provisioning_state:
          description:
            - Provisioning state to track the async operation status.
          returned: always
          type: str
          sample: null
        sqlimage_offer:
          description:
            - >-
              SQL image offer. Examples may include SQL2016-WS2016,
              SQL2017-WS2016.
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
              Type of cluster manager: Windows Server Failover Cluster (WSFC),
              implied by the scale type of the group and the OS type.
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
                  Organizational Unit path in which the nodes and cluster will
                  be present.
              returned: always
              type: str
              sample: null
            cluster_bootstrap_account:
              description:
                - >-
                  Account name used for creating cluster (at minimum needs
                  permissions to 'Create Computer Objects' in domain).
              returned: always
              type: str
              sample: null
            cluster_operator_account:
              description:
                - >-
                  Account name used for operating cluster i.e. will be part of
                  administrators group on all the participating virtual machines
                  in the cluster.
              returned: always
              type: str
              sample: null
            sqlservice_account:
              description:
                - >-
                  Account name under which SQL service will run on all
                  participating SQL virtual machines in the cluster.
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
                - >-
                  Fully qualified ARM resource id of the witness storage
                  account.
              returned: always
              type: str
              sample: null
            storage_account_primary_key:
              description:
                - Primary key of the witness storage account.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - Link to retrieve next page of results.
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
    from azure.mgmt.sql import SqlVirtualMachineManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSqlVirtualMachineGroupInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            sqlvirtual_machine_group_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.sqlvirtual_machine_group_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-03-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSqlVirtualMachineGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(SqlVirtualMachineManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-03-01-preview')

        if (self.resource_group_name is not None and
            self.sqlvirtual_machine_group_name is not None):
            self.results['sql_virtual_machine_groups'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['sql_virtual_machine_groups'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['sql_virtual_machine_groups'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.sql_virtual_machine_groups.get(resource_group_name=self.resource_group_name,
                                                                       sqlvirtual_machine_group_name=self.sqlvirtual_machine_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.sql_virtual_machine_groups.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.sql_virtual_machine_groups.list()
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
    AzureRMSqlVirtualMachineGroupInfo()


if __name__ == '__main__':
    main()
