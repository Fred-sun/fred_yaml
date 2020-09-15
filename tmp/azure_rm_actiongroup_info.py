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
module: azure_rm_actiongroup_info
version_added: '2.9'
short_description: Get ActionGroup info.
description:
  - Get info of ActionGroup.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  action_group_name:
    description:
      - The name of the action group.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get an action group
      azure_rm_actiongroup_info: 
        action_group_name: SampleActionGroup
        resource_group_name: Default-NotificationRules
        

    - name: List action groups
      azure_rm_actiongroup_info: 
        {}
        

'''

RETURN = '''
action_groups:
  description: >-
    A list of dict results where the key is the name of the ActionGroup and the
    values are the facts for that ActionGroup.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Azure resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - Azure resource name
      returned: always
      type: str
      sample: null
    type:
      description:
        - Azure resource type
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags
      returned: always
      type: dictionary
      sample: null
    group_short_name:
      description:
        - The short name of the action group. This will be used in SMS messages.
      returned: always
      type: str
      sample: null
    enabled:
      description:
        - >-
          Indicates whether this action group is enabled. If an action group is
          not enabled, then none of its receivers will receive communications.
      returned: always
      type: bool
      sample: null
    email_receivers:
      description:
        - The list of email receivers that are part of this action group.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the email receiver. Names must be unique across all
              receivers within an action group.
          returned: always
          type: str
          sample: null
        email_address:
          description:
            - The email address of this receiver.
          returned: always
          type: str
          sample: null
        use_common_alert_schema:
          description:
            - Indicates whether to use common alert schema.
          returned: always
          type: bool
          sample: null
        status:
          description:
            - The receiver status of the e-mail.
          returned: always
          type: sealed-choice
          sample: null
    sms_receivers:
      description:
        - The list of SMS receivers that are part of this action group.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the SMS receiver. Names must be unique across all
              receivers within an action group.
          returned: always
          type: str
          sample: null
        country_code:
          description:
            - The country code of the SMS receiver.
          returned: always
          type: str
          sample: null
        phone_number:
          description:
            - The phone number of the SMS receiver.
          returned: always
          type: str
          sample: null
        status:
          description:
            - The status of the receiver.
          returned: always
          type: sealed-choice
          sample: null
    webhook_receivers:
      description:
        - The list of webhook receivers that are part of this action group.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the webhook receiver. Names must be unique across all
              receivers within an action group.
          returned: always
          type: str
          sample: null
        service_uri:
          description:
            - The URI where webhooks should be sent.
          returned: always
          type: str
          sample: null
        use_common_alert_schema:
          description:
            - Indicates whether to use common alert schema.
          returned: always
          type: bool
          sample: null
        use_aadauth:
          description:
            - Indicates whether or not use AAD authentication.
          returned: always
          type: bool
          sample: null
        object_id:
          description:
            - Indicates the webhook app object Id for aad auth.
          returned: always
          type: str
          sample: null
        identifier_uri:
          description:
            - Indicates the identifier uri for aad auth.
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - Indicates the tenant id for aad auth.
          returned: always
          type: str
          sample: null
    itsm_receivers:
      description:
        - The list of ITSM receivers that are part of this action group.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the Itsm receiver. Names must be unique across all
              receivers within an action group.
          returned: always
          type: str
          sample: null
        workspace_id:
          description:
            - OMS LA instance identifier.
          returned: always
          type: str
          sample: null
        connection_id:
          description:
            - >-
              Unique identification of ITSM connection among multiple defined in
              above workspace.
          returned: always
          type: str
          sample: null
        ticket_configuration:
          description:
            - >-
              JSON blob for the configurations of the ITSM action.
              CreateMultipleWorkItems option will be part of this blob as well.
          returned: always
          type: str
          sample: null
        region:
          description:
            - >-
              Region in which workspace resides. Supported
              values:'centralindia','japaneast','southeastasia','australiasoutheast','uksouth','westcentralus','canadacentral','eastus','westeurope'
          returned: always
          type: str
          sample: null
    azure_app_push_receivers:
      description:
        - The list of AzureAppPush receivers that are part of this action group.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the Azure mobile app push receiver. Names must be
              unique across all receivers within an action group.
          returned: always
          type: str
          sample: null
        email_address:
          description:
            - The email address registered for the Azure mobile app.
          returned: always
          type: str
          sample: null
    automation_runbook_receivers:
      description:
        - >-
          The list of AutomationRunbook receivers that are part of this action
          group.
      returned: always
      type: list
      sample: null
      contains:
        automation_account_id:
          description:
            - >-
              The Azure automation account Id which holds this runbook and
              authenticate to Azure resource.
          returned: always
          type: str
          sample: null
        runbook_name:
          description:
            - The name for this runbook.
          returned: always
          type: str
          sample: null
        webhook_resource_id:
          description:
            - The resource id for webhook linked to this runbook.
          returned: always
          type: str
          sample: null
        is_global_runbook:
          description:
            - Indicates whether this instance is global runbook.
          returned: always
          type: bool
          sample: null
        name:
          description:
            - Indicates name of the webhook.
          returned: always
          type: str
          sample: null
        service_uri:
          description:
            - The URI where webhooks should be sent.
          returned: always
          type: str
          sample: null
        use_common_alert_schema:
          description:
            - Indicates whether to use common alert schema.
          returned: always
          type: bool
          sample: null
    voice_receivers:
      description:
        - The list of voice receivers that are part of this action group.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the voice receiver. Names must be unique across all
              receivers within an action group.
          returned: always
          type: str
          sample: null
        country_code:
          description:
            - The country code of the voice receiver.
          returned: always
          type: str
          sample: null
        phone_number:
          description:
            - The phone number of the voice receiver.
          returned: always
          type: str
          sample: null
    logic_app_receivers:
      description:
        - The list of logic app receivers that are part of this action group.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the logic app receiver. Names must be unique across
              all receivers within an action group.
          returned: always
          type: str
          sample: null
        resource_id:
          description:
            - The azure resource id of the logic app receiver.
          returned: always
          type: str
          sample: null
        callback_url:
          description:
            - The callback url where http request sent to.
          returned: always
          type: str
          sample: null
        use_common_alert_schema:
          description:
            - Indicates whether to use common alert schema.
          returned: always
          type: bool
          sample: null
    azure_function_receivers:
      description:
        - >-
          The list of azure function receivers that are part of this action
          group.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the azure function receiver. Names must be unique
              across all receivers within an action group.
          returned: always
          type: str
          sample: null
        function_app_resource_id:
          description:
            - The azure resource id of the function app.
          returned: always
          type: str
          sample: null
        function_name:
          description:
            - The function name in the function app.
          returned: always
          type: str
          sample: null
        http_trigger_url:
          description:
            - The http trigger url where http request sent to.
          returned: always
          type: str
          sample: null
        use_common_alert_schema:
          description:
            - Indicates whether to use common alert schema.
          returned: always
          type: bool
          sample: null
    arm_role_receivers:
      description:
        - >-
          The list of ARM role receivers that are part of this action group.
          Roles are Azure RBAC roles and only built-in roles are supported.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the arm role receiver. Names must be unique across all
              receivers within an action group.
          returned: always
          type: str
          sample: null
        role_id:
          description:
            - The arm role id.
          returned: always
          type: str
          sample: null
        use_common_alert_schema:
          description:
            - Indicates whether to use common alert schema.
          returned: always
          type: bool
          sample: null
    value:
      description:
        - The list of action groups.
      returned: always
      type: list
      sample: null
      contains:
        group_short_name:
          description:
            - >-
              The short name of the action group. This will be used in SMS
              messages.
          returned: always
          type: str
          sample: null
        enabled:
          description:
            - >-
              Indicates whether this action group is enabled. If an action group
              is not enabled, then none of its receivers will receive
              communications.
          returned: always
          type: bool
          sample: null
        email_receivers:
          description:
            - The list of email receivers that are part of this action group.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the email receiver. Names must be unique across
                  all receivers within an action group.
              returned: always
              type: str
              sample: null
            email_address:
              description:
                - The email address of this receiver.
              returned: always
              type: str
              sample: null
            use_common_alert_schema:
              description:
                - Indicates whether to use common alert schema.
              returned: always
              type: bool
              sample: null
            status:
              description:
                - The receiver status of the e-mail.
              returned: always
              type: sealed-choice
              sample: null
        sms_receivers:
          description:
            - The list of SMS receivers that are part of this action group.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the SMS receiver. Names must be unique across all
                  receivers within an action group.
              returned: always
              type: str
              sample: null
            country_code:
              description:
                - The country code of the SMS receiver.
              returned: always
              type: str
              sample: null
            phone_number:
              description:
                - The phone number of the SMS receiver.
              returned: always
              type: str
              sample: null
            status:
              description:
                - The status of the receiver.
              returned: always
              type: sealed-choice
              sample: null
        webhook_receivers:
          description:
            - The list of webhook receivers that are part of this action group.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the webhook receiver. Names must be unique across
                  all receivers within an action group.
              returned: always
              type: str
              sample: null
            service_uri:
              description:
                - The URI where webhooks should be sent.
              returned: always
              type: str
              sample: null
            use_common_alert_schema:
              description:
                - Indicates whether to use common alert schema.
              returned: always
              type: bool
              sample: null
            use_aadauth:
              description:
                - Indicates whether or not use AAD authentication.
              returned: always
              type: bool
              sample: null
            object_id:
              description:
                - Indicates the webhook app object Id for aad auth.
              returned: always
              type: str
              sample: null
            identifier_uri:
              description:
                - Indicates the identifier uri for aad auth.
              returned: always
              type: str
              sample: null
            tenant_id:
              description:
                - Indicates the tenant id for aad auth.
              returned: always
              type: str
              sample: null
        itsm_receivers:
          description:
            - The list of ITSM receivers that are part of this action group.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the Itsm receiver. Names must be unique across all
                  receivers within an action group.
              returned: always
              type: str
              sample: null
            workspace_id:
              description:
                - OMS LA instance identifier.
              returned: always
              type: str
              sample: null
            connection_id:
              description:
                - >-
                  Unique identification of ITSM connection among multiple
                  defined in above workspace.
              returned: always
              type: str
              sample: null
            ticket_configuration:
              description:
                - >-
                  JSON blob for the configurations of the ITSM action.
                  CreateMultipleWorkItems option will be part of this blob as
                  well.
              returned: always
              type: str
              sample: null
            region:
              description:
                - >-
                  Region in which workspace resides. Supported
                  values:'centralindia','japaneast','southeastasia','australiasoutheast','uksouth','westcentralus','canadacentral','eastus','westeurope'
              returned: always
              type: str
              sample: null
        azure_app_push_receivers:
          description:
            - >-
              The list of AzureAppPush receivers that are part of this action
              group.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the Azure mobile app push receiver. Names must be
                  unique across all receivers within an action group.
              returned: always
              type: str
              sample: null
            email_address:
              description:
                - The email address registered for the Azure mobile app.
              returned: always
              type: str
              sample: null
        automation_runbook_receivers:
          description:
            - >-
              The list of AutomationRunbook receivers that are part of this
              action group.
          returned: always
          type: list
          sample: null
          contains:
            automation_account_id:
              description:
                - >-
                  The Azure automation account Id which holds this runbook and
                  authenticate to Azure resource.
              returned: always
              type: str
              sample: null
            runbook_name:
              description:
                - The name for this runbook.
              returned: always
              type: str
              sample: null
            webhook_resource_id:
              description:
                - The resource id for webhook linked to this runbook.
              returned: always
              type: str
              sample: null
            is_global_runbook:
              description:
                - Indicates whether this instance is global runbook.
              returned: always
              type: bool
              sample: null
            name:
              description:
                - Indicates name of the webhook.
              returned: always
              type: str
              sample: null
            service_uri:
              description:
                - The URI where webhooks should be sent.
              returned: always
              type: str
              sample: null
            use_common_alert_schema:
              description:
                - Indicates whether to use common alert schema.
              returned: always
              type: bool
              sample: null
        voice_receivers:
          description:
            - The list of voice receivers that are part of this action group.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the voice receiver. Names must be unique across
                  all receivers within an action group.
              returned: always
              type: str
              sample: null
            country_code:
              description:
                - The country code of the voice receiver.
              returned: always
              type: str
              sample: null
            phone_number:
              description:
                - The phone number of the voice receiver.
              returned: always
              type: str
              sample: null
        logic_app_receivers:
          description:
            - >-
              The list of logic app receivers that are part of this action
              group.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the logic app receiver. Names must be unique
                  across all receivers within an action group.
              returned: always
              type: str
              sample: null
            resource_id:
              description:
                - The azure resource id of the logic app receiver.
              returned: always
              type: str
              sample: null
            callback_url:
              description:
                - The callback url where http request sent to.
              returned: always
              type: str
              sample: null
            use_common_alert_schema:
              description:
                - Indicates whether to use common alert schema.
              returned: always
              type: bool
              sample: null
        azure_function_receivers:
          description:
            - >-
              The list of azure function receivers that are part of this action
              group.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the azure function receiver. Names must be unique
                  across all receivers within an action group.
              returned: always
              type: str
              sample: null
            function_app_resource_id:
              description:
                - The azure resource id of the function app.
              returned: always
              type: str
              sample: null
            function_name:
              description:
                - The function name in the function app.
              returned: always
              type: str
              sample: null
            http_trigger_url:
              description:
                - The http trigger url where http request sent to.
              returned: always
              type: str
              sample: null
            use_common_alert_schema:
              description:
                - Indicates whether to use common alert schema.
              returned: always
              type: bool
              sample: null
        arm_role_receivers:
          description:
            - >-
              The list of ARM role receivers that are part of this action group.
              Roles are Azure RBAC roles and only built-in roles are supported.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the arm role receiver. Names must be unique across
                  all receivers within an action group.
              returned: always
              type: str
              sample: null
            role_id:
              description:
                - The arm role id.
              returned: always
              type: str
              sample: null
            use_common_alert_schema:
              description:
                - Indicates whether to use common alert schema.
              returned: always
              type: bool
              sample: null
    next_link:
      description:
        - Provides the link to retrieve the next set of elements.
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
    from azure.mgmt.monitor import MonitorClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMActionGroupInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            action_group_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.action_group_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMActionGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.resource_group_name is not None and
            self.action_group_name is not None):
            self.results['action_groups'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['action_groups'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['action_groups'] = self.format_item(self.listbysubscriptionid())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.action_groups.get(resource_group_name=self.resource_group_name,
                                                          action_group_name=self.action_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.action_groups.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbysubscriptionid(self):
        response = None

        try:
            response = self.mgmt_client.action_groups.list_by_subscription_id()
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
    AzureRMActionGroupInfo()


if __name__ == '__main__':
    main()
