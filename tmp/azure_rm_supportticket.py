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
module: azure_rm_supportticket
version_added: '2.9'
short_description: Manage Azure SupportTicket instance.
description:
  - 'Create, update and delete instance of Azure SupportTicket.'
options:
  support_ticket_name:
    description:
      - Support ticket name.
    required: true
    type: str
  severity:
    description:
      - Severity level.
      - >-
        A value that indicates the urgency of the case, which in turn determines
        the response time according to the service level agreement of the
        technical support plan you have with Azure. Note: 'Highest critical
        impact', also known as the 'Emergency - Severe impact' level in the
        Azure portal is reserved only for our Premium customers.
    type: str
    choices:
      - minimal
      - moderate
      - critical
      - highestcriticalimpact
  status:
    description:
      - Status to be updated on the ticket.
    type: str
    choices:
      - open
      - closed
  contact_details:
    description:
      - Contact details to be updated on the support ticket.
      - Contact information of the user requesting to create a support ticket.
    type: dict
    suboptions:
      first_name:
        description:
          - First name.
        type: str
      last_name:
        description:
          - Last name.
        type: str
      preferred_contact_method:
        description:
          - Preferred contact method.
        type: str
        choices:
          - email
          - phone
      primary_email_address:
        description:
          - Primary email address.
        type: str
      additional_email_addresses:
        description:
          - >-
            Email addresses listed will be copied on any correspondence about
            the support ticket.
        type: list
      phone_number:
        description:
          - Phone number. This is required if preferred contact method is phone.
        type: str
      preferred_time_zone:
        description:
          - >-
            Time zone of the user. This is the name of the time zone from
            [Microsoft Time Zone Index
            Values](https://support.microsoft.com/help/973627/microsoft-time-zone-index-values).
        type: str
      country:
        description:
          - Country of the user. This is the ISO 3166-1 alpha-3 code.
        type: str
      preferred_support_language:
        description:
          - >-
            Preferred language of support from Azure. Support languages vary
            based on the severity you choose for your support ticket. Learn more
            at [Azure Severity and
            responsiveness](https://azure.microsoft.com/support/plans/response/).
            Use the standard language-country code. Valid values are 'en-us' for
            English, 'zh-hans' for Chinese, 'es-es' for Spanish, 'fr-fr' for
            French, 'ja-jp' for Japanese, 'ko-kr' for Korean, 'ru-ru' for
            Russian, 'pt-br' for Portuguese, 'it-it' for Italian, 'zh-tw' for
            Chinese and 'de-de' for German.
        type: str
  support_ticket_id:
    description:
      - System generated support ticket Id that is unique.
    type: str
  description:
    description:
      - Detailed description of the question or issue.
    type: str
  problem_classification_id:
    description:
      - >-
        Each Azure service has its own set of issue categories, also known as
        problem classification. This parameter is the unique Id for the type of
        problem you are experiencing.
    type: str
  require24x7response:
    description:
      - Indicates if this requires a 24x7 response from Azure.
    type: bool
  title:
    description:
      - Title of the support ticket.
    type: str
  problem_start_time:
    description:
      - Time in UTC (ISO 8601 format) when the problem started.
    type: str
  service_id:
    description:
      - >-
        This is the resource Id of the Azure service resource associated with
        the support ticket.
    type: str
  quota_change_request_sub_type:
    description:
      - >-
        Required for certain quota types when there is a sub type, such as
        Batch, for which you are requesting a quota increase.
    type: str
  quota_change_request_version:
    description:
      - Quota change request version.
    type: str
  quota_change_requests:
    description:
      - This property is required for providing the region and new quota limits.
    type: list
    suboptions:
      region:
        description:
          - Region for which the quota increase request is being made.
        type: str
      payload:
        description:
          - Payload of the quota increase request.
        type: str
  resource_id:
    description:
      - >-
        This is the resource Id of the Azure service resource (For example: A
        virtual machine resource or an HDInsight resource) for which the support
        ticket is created.
    type: str
  state:
    description:
      - Assert the state of the SupportTicket.
      - >-
        Use C(present) to create or update an SupportTicket and C(absent) to
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
    - name: Update contact details of a support ticket
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Update severity of a support ticket
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Update status of a support ticket
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket for Billing related issues
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket for Subscription Management related issues
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket for Technical issue related to a specific resource
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket to request Quota increase for Active Jobs and Job Schedules for a Batch account
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket to request Quota increase for Azure SQL managed instance
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket to request Quota increase for Batch accounts for a subscription
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket to request Quota increase for Compute VM Cores
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket to request Quota increase for DTUs for Azure Synapse Analytics
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket to request Quota increase for DTUs for SQL Database
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket to request Quota increase for Low-priority cores for Machine Learning service
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket to request Quota increase for Low-priority cores for a Batch account
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket to request Quota increase for Pools for a Batch account
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket to request Quota increase for Servers for Azure Synapse Analytics
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket to request Quota increase for Servers for SQL Database
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket to request Quota increase for services that do not require additional details in the quotaTicketDetails object
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket to request Quota increase for specific VM family cores for Machine Learning service
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

    - name: Create a ticket to request Quota increase for specific VM family cores for a Batch account
      azure_rm_supportticket: 
        support_ticket_name: testticket
        

'''

RETURN = '''
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
    - Type of the resource 'Microsoft.Support/supportTickets'.
  returned: always
  type: str
  sample: null
support_ticket_id:
  description:
    - System generated support ticket Id that is unique.
  returned: always
  type: str
  sample: null
description:
  description:
    - Detailed description of the question or issue.
  returned: always
  type: str
  sample: null
problem_classification_id:
  description:
    - >-
      Each Azure service has its own set of issue categories, also known as
      problem classification. This parameter is the unique Id for the type of
      problem you are experiencing.
  returned: always
  type: str
  sample: null
problem_classification_display_name:
  description:
    - Localized name of problem classification.
  returned: always
  type: str
  sample: null
severity:
  description:
    - >-
      A value that indicates the urgency of the case, which in turn determines
      the response time according to the service level agreement of the
      technical support plan you have with Azure. Note: 'Highest critical
      impact', also known as the 'Emergency - Severe impact' level in the Azure
      portal is reserved only for our Premium customers.
  returned: always
  type: str
  sample: null
enrollment_id:
  description:
    - Enrollment Id associated with the support ticket.
  returned: always
  type: str
  sample: null
require24x7response:
  description:
    - Indicates if this requires a 24x7 response from Azure.
  returned: always
  type: bool
  sample: null
contact_details:
  description:
    - Contact information of the user requesting to create a support ticket.
  returned: always
  type: dict
  sample: null
  contains:
    first_name:
      description:
        - First name.
      returned: always
      type: str
      sample: null
    last_name:
      description:
        - Last name.
      returned: always
      type: str
      sample: null
    preferred_contact_method:
      description:
        - Preferred contact method.
      returned: always
      type: str
      sample: null
    primary_email_address:
      description:
        - Primary email address.
      returned: always
      type: str
      sample: null
    additional_email_addresses:
      description:
        - >-
          Additional email addresses listed will be copied on any correspondence
          about the support ticket.
      returned: always
      type: list
      sample: null
    phone_number:
      description:
        - Phone number. This is required if preferred contact method is phone.
      returned: always
      type: str
      sample: null
    preferred_time_zone:
      description:
        - >-
          Time zone of the user. This is the name of the time zone from
          [Microsoft Time Zone Index
          Values](https://support.microsoft.com/help/973627/microsoft-time-zone-index-values).
      returned: always
      type: str
      sample: null
    country:
      description:
        - Country of the user. This is the ISO 3166-1 alpha-3 code.
      returned: always
      type: str
      sample: null
    preferred_support_language:
      description:
        - >-
          Preferred language of support from Azure. Support languages vary based
          on the severity you choose for your support ticket. Learn more at
          [Azure Severity and
          responsiveness](https://azure.microsoft.com/support/plans/response).
          Use the standard language-country code. Valid values are 'en-us' for
          English, 'zh-hans' for Chinese, 'es-es' for Spanish, 'fr-fr' for
          French, 'ja-jp' for Japanese, 'ko-kr' for Korean, 'ru-ru' for Russian,
          'pt-br' for Portuguese, 'it-it' for Italian, 'zh-tw' for Chinese and
          'de-de' for German.
      returned: always
      type: str
      sample: null
service_level_agreement:
  description:
    - Service Level Agreement information for this support ticket.
  returned: always
  type: dict
  sample: null
  contains:
    start_time:
      description:
        - Time in UTC (ISO 8601 format) when the service level agreement starts.
      returned: always
      type: str
      sample: null
    expiration_time:
      description:
        - >-
          Time in UTC (ISO 8601 format) when the service level agreement
          expires.
      returned: always
      type: str
      sample: null
    sla_minutes:
      description:
        - Service Level Agreement in minutes.
      returned: always
      type: integer
      sample: null
support_engineer:
  description:
    - Information about the support engineer working on this support ticket.
  returned: always
  type: dict
  sample: null
  contains:
    email_address:
      description:
        - >-
          Email address of the Azure Support engineer assigned to the support
          ticket.
      returned: always
      type: str
      sample: null
support_plan_type:
  description:
    - Support plan type associated with the support ticket.
  returned: always
  type: str
  sample: null
title:
  description:
    - Title of the support ticket.
  returned: always
  type: str
  sample: null
problem_start_time:
  description:
    - Time in UTC (ISO 8601 format) when the problem started.
  returned: always
  type: str
  sample: null
service_id:
  description:
    - >-
      This is the resource Id of the Azure service resource associated with the
      support ticket.
  returned: always
  type: str
  sample: null
service_display_name:
  description:
    - Localized name of the Azure service.
  returned: always
  type: str
  sample: null
status:
  description:
    - Status of the support ticket.
  returned: always
  type: str
  sample: null
created_date:
  description:
    - Time in UTC (ISO 8601 format) when the support ticket was created.
  returned: always
  type: str
  sample: null
modified_date:
  description:
    - Time in UTC (ISO 8601 format) when the support ticket was last modified.
  returned: always
  type: str
  sample: null
quota_change_request_sub_type:
  description:
    - >-
      Required for certain quota types when there is a sub type, such as Batch,
      for which you are requesting a quota increase.
  returned: always
  type: str
  sample: null
quota_change_request_version:
  description:
    - Quota change request version.
  returned: always
  type: str
  sample: null
quota_change_requests:
  description:
    - This property is required for providing the region and new quota limits.
  returned: always
  type: list
  sample: null
  contains:
    region:
      description:
        - Region for which the quota increase request is being made.
      returned: always
      type: str
      sample: null
    payload:
      description:
        - Payload of the quota increase request.
      returned: always
      type: str
      sample: null
resource_id:
  description:
    - >-
      This is the resource Id of the Azure service resource (For example: A
      virtual machine resource or an HDInsight resource) for which the support
      ticket is created.
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
    from azure.mgmt.microsoft.support import Microsoft.Support
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSupportTicket(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            support_ticket_name=dict(
                type='str',
                required=True
            ),
            severity=dict(
                type='str',
                disposition='/severity',
                choices=['minimal',
                         'moderate',
                         'critical',
                         'highestcriticalimpact']
            ),
            status=dict(
                type='str',
                disposition='/status',
                choices=['open',
                         'closed']
            ),
            contact_details=dict(
                type='dict',
                disposition='/contact_details',
                options=dict(
                    first_name=dict(
                        type='str',
                        disposition='first_name'
                    ),
                    last_name=dict(
                        type='str',
                        disposition='last_name'
                    ),
                    preferred_contact_method=dict(
                        type='str',
                        disposition='preferred_contact_method',
                        choices=['email',
                                 'phone']
                    ),
                    primary_email_address=dict(
                        type='str',
                        disposition='primary_email_address'
                    ),
                    additional_email_addresses=dict(
                        type='list',
                        disposition='additional_email_addresses',
                        elements='str'
                    ),
                    phone_number=dict(
                        type='str',
                        disposition='phone_number'
                    ),
                    preferred_time_zone=dict(
                        type='str',
                        disposition='preferred_time_zone'
                    ),
                    country=dict(
                        type='str',
                        disposition='country'
                    ),
                    preferred_support_language=dict(
                        type='str',
                        disposition='preferred_support_language'
                    )
                )
            ),
            support_ticket_id=dict(
                type='str',
                disposition='/support_ticket_id'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            problem_classification_id=dict(
                type='str',
                disposition='/problem_classification_id'
            ),
            require24x7response=dict(
                type='bool',
                disposition='/require24x7response'
            ),
            title=dict(
                type='str',
                disposition='/title'
            ),
            problem_start_time=dict(
                type='str',
                disposition='/problem_start_time'
            ),
            service_id=dict(
                type='str',
                disposition='/service_id'
            ),
            quota_change_request_sub_type=dict(
                type='str',
                disposition='/quota_change_request_sub_type'
            ),
            quota_change_request_version=dict(
                type='str',
                disposition='/quota_change_request_version'
            ),
            quota_change_requests=dict(
                type='list',
                disposition='/quota_change_requests',
                elements='dict',
                options=dict(
                    region=dict(
                        type='str',
                        disposition='region'
                    ),
                    payload=dict(
                        type='str',
                        disposition='payload'
                    )
                )
            ),
            resource_id=dict(
                type='str',
                disposition='/resource_id'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.support_ticket_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSupportTicket, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Microsoft.Support,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.support_tickets.create(support_ticket_name=self.support_ticket_name,
                                                                   create_support_ticket_parameters=self.body)
            else:
                response = self.mgmt_client.support_tickets.update(support_ticket_name=self.support_ticket_name,
                                                                   update_support_ticket=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SupportTicket instance.')
            self.fail('Error creating the SupportTicket instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.support_tickets.delete()
        except CloudError as e:
            self.log('Error attempting to delete the SupportTicket instance.')
            self.fail('Error deleting the SupportTicket instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.support_tickets.get(support_ticket_name=self.support_ticket_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSupportTicket()


if __name__ == '__main__':
    main()
