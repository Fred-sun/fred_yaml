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
module: azure_rm_actiongroup
version_added: '2.9'
short_description: Manage Azure ActionGroup instance.
description:
  - 'Create, update and delete instance of Azure ActionGroup.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  action_group_name:
    description:
      - The name of the action group.
    required: true
    type: str
  location:
    description:
      - Resource location
    type: str
  group_short_name:
    description:
      - The short name of the action group. This will be used in SMS messages.
    type: str
  enabled:
    description:
      - >-
        Indicates whether this action group is enabled. If an action group is
        not enabled, then none of its receivers will receive communications.
      - >-
        Indicates whether this action group is enabled. If an action group is
        not enabled, then none of its actions will be activated.
    type: bool
  email_receivers:
    description:
      - The list of email receivers that are part of this action group.
    type: list
    suboptions:
      name:
        description:
          - >-
            The name of the email receiver. Names must be unique across all
            receivers within an action group.
        required: true
        type: str
      email_address:
        description:
          - The email address of this receiver.
        required: true
        type: str
      use_common_alert_schema:
        description:
          - Indicates whether to use common alert schema.
        required: true
        type: bool
      status:
        description:
          - The receiver status of the e-mail.
        type: sealed-choice
  sms_receivers:
    description:
      - The list of SMS receivers that are part of this action group.
    type: list
    suboptions:
      name:
        description:
          - >-
            The name of the SMS receiver. Names must be unique across all
            receivers within an action group.
        required: true
        type: str
      country_code:
        description:
          - The country code of the SMS receiver.
        required: true
        type: str
      phone_number:
        description:
          - The phone number of the SMS receiver.
        required: true
        type: str
      status:
        description:
          - The status of the receiver.
        type: sealed-choice
  webhook_receivers:
    description:
      - The list of webhook receivers that are part of this action group.
    type: list
    suboptions:
      name:
        description:
          - >-
            The name of the webhook receiver. Names must be unique across all
            receivers within an action group.
        required: true
        type: str
      service_uri:
        description:
          - The URI where webhooks should be sent.
        required: true
        type: str
      use_common_alert_schema:
        description:
          - Indicates whether to use common alert schema.
        required: true
        type: bool
      use_aadauth:
        description:
          - Indicates whether or not use AAD authentication.
        type: bool
      object_id:
        description:
          - Indicates the webhook app object Id for aad auth.
        type: str
      identifier_uri:
        description:
          - Indicates the identifier uri for aad auth.
        type: str
      tenant_id:
        description:
          - Indicates the tenant id for aad auth.
        type: str
  itsm_receivers:
    description:
      - The list of ITSM receivers that are part of this action group.
    type: list
    suboptions:
      name:
        description:
          - >-
            The name of the Itsm receiver. Names must be unique across all
            receivers within an action group.
        required: true
        type: str
      workspace_id:
        description:
          - OMS LA instance identifier.
        required: true
        type: str
      connection_id:
        description:
          - >-
            Unique identification of ITSM connection among multiple defined in
            above workspace.
        required: true
        type: str
      ticket_configuration:
        description:
          - >-
            JSON blob for the configurations of the ITSM action.
            CreateMultipleWorkItems option will be part of this blob as well.
        required: true
        type: str
      region:
        description:
          - >-
            Region in which workspace resides. Supported
            values:'centralindia','japaneast','southeastasia','australiasoutheast','uksouth','westcentralus','canadacentral','eastus','westeurope'
        required: true
        type: str
  azure_app_push_receivers:
    description:
      - The list of AzureAppPush receivers that are part of this action group.
    type: list
    suboptions:
      name:
        description:
          - >-
            The name of the Azure mobile app push receiver. Names must be unique
            across all receivers within an action group.
        required: true
        type: str
      email_address:
        description:
          - The email address registered for the Azure mobile app.
        required: true
        type: str
  automation_runbook_receivers:
    description:
      - >-
        The list of AutomationRunbook receivers that are part of this action
        group.
    type: list
    suboptions:
      automation_account_id:
        description:
          - >-
            The Azure automation account Id which holds this runbook and
            authenticate to Azure resource.
        required: true
        type: str
      runbook_name:
        description:
          - The name for this runbook.
        required: true
        type: str
      webhook_resource_id:
        description:
          - The resource id for webhook linked to this runbook.
        required: true
        type: str
      is_global_runbook:
        description:
          - Indicates whether this instance is global runbook.
        required: true
        type: bool
      name:
        description:
          - Indicates name of the webhook.
        type: str
      service_uri:
        description:
          - The URI where webhooks should be sent.
        type: str
      use_common_alert_schema:
        description:
          - Indicates whether to use common alert schema.
        required: true
        type: bool
  voice_receivers:
    description:
      - The list of voice receivers that are part of this action group.
    type: list
    suboptions:
      name:
        description:
          - >-
            The name of the voice receiver. Names must be unique across all
            receivers within an action group.
        required: true
        type: str
      country_code:
        description:
          - The country code of the voice receiver.
        required: true
        type: str
      phone_number:
        description:
          - The phone number of the voice receiver.
        required: true
        type: str
  logic_app_receivers:
    description:
      - The list of logic app receivers that are part of this action group.
    type: list
    suboptions:
      name:
        description:
          - >-
            The name of the logic app receiver. Names must be unique across all
            receivers within an action group.
        required: true
        type: str
      resource_id:
        description:
          - The azure resource id of the logic app receiver.
        required: true
        type: str
      callback_url:
        description:
          - The callback url where http request sent to.
        required: true
        type: str
      use_common_alert_schema:
        description:
          - Indicates whether to use common alert schema.
        required: true
        type: bool
  azure_function_receivers:
    description:
      - The list of azure function receivers that are part of this action group.
    type: list
    suboptions:
      name:
        description:
          - >-
            The name of the azure function receiver. Names must be unique across
            all receivers within an action group.
        required: true
        type: str
      function_app_resource_id:
        description:
          - The azure resource id of the function app.
        required: true
        type: str
      function_name:
        description:
          - The function name in the function app.
        required: true
        type: str
      http_trigger_url:
        description:
          - The http trigger url where http request sent to.
        required: true
        type: str
      use_common_alert_schema:
        description:
          - Indicates whether to use common alert schema.
        required: true
        type: bool
  arm_role_receivers:
    description:
      - >-
        The list of ARM role receivers that are part of this action group. Roles
        are Azure RBAC roles and only built-in roles are supported.
    type: list
    suboptions:
      name:
        description:
          - >-
            The name of the arm role receiver. Names must be unique across all
            receivers within an action group.
        required: true
        type: str
      role_id:
        description:
          - The arm role id.
        required: true
        type: str
      use_common_alert_schema:
        description:
          - Indicates whether to use common alert schema.
        required: true
        type: bool
  state:
    description:
      - Assert the state of the ActionGroup.
      - >-
        Use C(present) to create or update an ActionGroup and C(absent) to
        delete it.
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
    - name: Create or update an action group
      azure_rm_actiongroup: 
        action_group_name: SampleActionGroup
        resource_group_name: Default-NotificationRules
        

    - name: Delete an action group
      azure_rm_actiongroup: 
        action_group_name: SampleActionGroup
        resource_group_name: Default-NotificationRules
        

    - name: Patch an action group
      azure_rm_actiongroup: 
        action_group_name: SampleActionGroup
        resource_group_name: Default-NotificationRules
        

'''

RETURN = '''
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
      Indicates whether this action group is enabled. If an action group is not
      enabled, then none of its receivers will receive communications.
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
          The name of the Azure mobile app push receiver. Names must be unique
          across all receivers within an action group.
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
          The name of the logic app receiver. Names must be unique across all
          receivers within an action group.
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
    - The list of azure function receivers that are part of this action group.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - >-
          The name of the azure function receiver. Names must be unique across
          all receivers within an action group.
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
      The list of ARM role receivers that are part of this action group. Roles
      are Azure RBAC roles and only built-in roles are supported.
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

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.monitor import MonitorClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMActionGroup(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            action_group_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            group_short_name=dict(
                type='str',
                disposition='/group_short_name'
            ),
            enabled=dict(
                type='bool',
                disposition='/enabled'
            ),
            email_receivers=dict(
                type='list',
                disposition='/email_receivers',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    email_address=dict(
                        type='str',
                        disposition='email_address',
                        required=True
                    ),
                    use_common_alert_schema=dict(
                        type='bool',
                        disposition='use_common_alert_schema',
                        required=True
                    ),
                    status=dict(
                        type='sealed-choice',
                        updatable=False,
                        disposition='status'
                    )
                )
            ),
            sms_receivers=dict(
                type='list',
                disposition='/sms_receivers',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    country_code=dict(
                        type='str',
                        disposition='country_code',
                        required=True
                    ),
                    phone_number=dict(
                        type='str',
                        disposition='phone_number',
                        required=True
                    ),
                    status=dict(
                        type='sealed-choice',
                        updatable=False,
                        disposition='status'
                    )
                )
            ),
            webhook_receivers=dict(
                type='list',
                disposition='/webhook_receivers',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    service_uri=dict(
                        type='str',
                        disposition='service_uri',
                        required=True
                    ),
                    use_common_alert_schema=dict(
                        type='bool',
                        disposition='use_common_alert_schema',
                        required=True
                    ),
                    use_aadauth=dict(
                        type='bool',
                        disposition='use_aadauth'
                    ),
                    object_id=dict(
                        type='str',
                        disposition='object_id'
                    ),
                    identifier_uri=dict(
                        type='str',
                        disposition='identifier_uri'
                    ),
                    tenant_id=dict(
                        type='str',
                        disposition='tenant_id'
                    )
                )
            ),
            itsm_receivers=dict(
                type='list',
                disposition='/itsm_receivers',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    workspace_id=dict(
                        type='str',
                        disposition='workspace_id',
                        required=True
                    ),
                    connection_id=dict(
                        type='str',
                        disposition='connection_id',
                        required=True
                    ),
                    ticket_configuration=dict(
                        type='str',
                        disposition='ticket_configuration',
                        required=True
                    ),
                    region=dict(
                        type='str',
                        disposition='region',
                        required=True
                    )
                )
            ),
            azure_app_push_receivers=dict(
                type='list',
                disposition='/azure_app_push_receivers',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    email_address=dict(
                        type='str',
                        disposition='email_address',
                        required=True
                    )
                )
            ),
            automation_runbook_receivers=dict(
                type='list',
                disposition='/automation_runbook_receivers',
                elements='dict',
                options=dict(
                    automation_account_id=dict(
                        type='str',
                        disposition='automation_account_id',
                        required=True
                    ),
                    runbook_name=dict(
                        type='str',
                        disposition='runbook_name',
                        required=True
                    ),
                    webhook_resource_id=dict(
                        type='str',
                        disposition='webhook_resource_id',
                        required=True
                    ),
                    is_global_runbook=dict(
                        type='bool',
                        disposition='is_global_runbook',
                        required=True
                    ),
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    service_uri=dict(
                        type='str',
                        disposition='service_uri'
                    ),
                    use_common_alert_schema=dict(
                        type='bool',
                        disposition='use_common_alert_schema',
                        required=True
                    )
                )
            ),
            voice_receivers=dict(
                type='list',
                disposition='/voice_receivers',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    country_code=dict(
                        type='str',
                        disposition='country_code',
                        required=True
                    ),
                    phone_number=dict(
                        type='str',
                        disposition='phone_number',
                        required=True
                    )
                )
            ),
            logic_app_receivers=dict(
                type='list',
                disposition='/logic_app_receivers',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    resource_id=dict(
                        type='str',
                        disposition='resource_id',
                        required=True
                    ),
                    callback_url=dict(
                        type='str',
                        disposition='callback_url',
                        required=True
                    ),
                    use_common_alert_schema=dict(
                        type='bool',
                        disposition='use_common_alert_schema',
                        required=True
                    )
                )
            ),
            azure_function_receivers=dict(
                type='list',
                disposition='/azure_function_receivers',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    function_app_resource_id=dict(
                        type='str',
                        disposition='function_app_resource_id',
                        required=True
                    ),
                    function_name=dict(
                        type='str',
                        disposition='function_name',
                        required=True
                    ),
                    http_trigger_url=dict(
                        type='str',
                        disposition='http_trigger_url',
                        required=True
                    ),
                    use_common_alert_schema=dict(
                        type='bool',
                        disposition='use_common_alert_schema',
                        required=True
                    )
                )
            ),
            arm_role_receivers=dict(
                type='list',
                disposition='/arm_role_receivers',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    role_id=dict(
                        type='str',
                        disposition='role_id',
                        required=True
                    ),
                    use_common_alert_schema=dict(
                        type='bool',
                        disposition='use_common_alert_schema',
                        required=True
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
        self.action_group_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMActionGroup, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(MonitorClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

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
            response = self.mgmt_client.action_groups.create_or_update(resource_group_name=self.resource_group_name,
                                                                       action_group_name=self.action_group_name,
                                                                       action_group=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ActionGroup instance.')
            self.fail('Error creating the ActionGroup instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.action_groups.delete(resource_group_name=self.resource_group_name,
                                                             action_group_name=self.action_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the ActionGroup instance.')
            self.fail('Error deleting the ActionGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.action_groups.get(resource_group_name=self.resource_group_name,
                                                          action_group_name=self.action_group_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMActionGroup()


if __name__ == '__main__':
    main()
