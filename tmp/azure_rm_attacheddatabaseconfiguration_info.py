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
module: azure_rm_attacheddatabaseconfiguration_info
version_added: '2.9'
short_description: Get AttachedDatabaseConfiguration info.
description:
  - Get info of AttachedDatabaseConfiguration.
options:
  resource_group_name:
    description:
      - The name of the resource group containing the Kusto cluster.
    required: true
    type: str
  cluster_name:
    description:
      - The name of the Kusto cluster.
    required: true
    type: str
  attached_database_configuration_name:
    description:
      - The name of the attached database configuration.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: KustoAttachedDatabaseConfigurationsListByCluster
      azure_rm_attacheddatabaseconfiguration_info: 
        cluster_name: kustoclusterrptest4
        resource_group_name: kustorptest
        

    - name: AttachedDatabaseConfigurationsGet
      azure_rm_attacheddatabaseconfiguration_info: 
        attached_database_configuration_name: attachedDatabaseConfigurations1
        cluster_name: kustoclusterrptest4
        resource_group_name: kustorptest
        

'''

RETURN = '''
attached_database_configurations:
  description: >-
    A list of dict results where the key is the name of the
    AttachedDatabaseConfiguration and the values are the facts for that
    AttachedDatabaseConfiguration.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of attached database configurations.
      returned: always
      type: list
      sample: null
      contains:
        location:
          description:
            - Resource location.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - The provisioned state of the resource.
          returned: always
          type: str
          sample: null
        database_name:
          description:
            - >-
              The name of the database which you would like to attach, use * if
              you want to follow all current and future databases.
          returned: always
          type: str
          sample: null
        cluster_resource_id:
          description:
            - >-
              The resource id of the cluster where the databases you would like
              to attach reside.
          returned: always
          type: str
          sample: null
        attached_database_names:
          description:
            - >-
              The list of databases from the clusterResourceId which are
              currently attached to the cluster.
          returned: always
          type: list
          sample: null
        default_principals_modification_kind:
          description:
            - The default principals modification kind
          returned: always
          type: str
          sample: null
    id:
      description:
        - >-
          Fully qualified resource Id for the resource. Ex -
          /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
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
          The type of the resource. Ex- Microsoft.Compute/virtualMachines or
          Microsoft.Storage/storageAccounts.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioned state of the resource.
      returned: always
      type: str
      sample: null
    database_name:
      description:
        - >-
          The name of the database which you would like to attach, use * if you
          want to follow all current and future databases.
      returned: always
      type: str
      sample: null
    cluster_resource_id:
      description:
        - >-
          The resource id of the cluster where the databases you would like to
          attach reside.
      returned: always
      type: str
      sample: null
    attached_database_names:
      description:
        - >-
          The list of databases from the clusterResourceId which are currently
          attached to the cluster.
      returned: always
      type: list
      sample: null
    default_principals_modification_kind:
      description:
        - The default principals modification kind
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
    from azure.mgmt.kusto import KustoManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMAttachedDatabaseConfigurationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            cluster_name=dict(
                type='str',
                required=True
            ),
            attached_database_configuration_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.cluster_name = None
        self.attached_database_configuration_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-14'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMAttachedDatabaseConfigurationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(KustoManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-14')

        if (self.resource_group_name is not None and
            self.cluster_name is not None and
            self.attached_database_configuration_name is not None):
            self.results['attached_database_configurations'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.cluster_name is not None):
            self.results['attached_database_configurations'] = self.format_item(self.listbycluster())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.attached_database_configurations.get(resource_group_name=self.resource_group_name,
                                                                             cluster_name=self.cluster_name,
                                                                             attached_database_configuration_name=self.attached_database_configuration_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbycluster(self):
        response = None

        try:
            response = self.mgmt_client.attached_database_configurations.list_by_cluster(resource_group_name=self.resource_group_name,
                                                                                         cluster_name=self.cluster_name)
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
    AzureRMAttachedDatabaseConfigurationInfo()


if __name__ == '__main__':
    main()
