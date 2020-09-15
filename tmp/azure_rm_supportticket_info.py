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
module: azure_rm_supportticket_info
version_added: '2.9'
short_description: Get SupportTicket info.
description:
  - Get info of SupportTicket.
options:
  top:
    description:
      - >-
        The number of values to return in the collection. Default is 25 and max
        is 100.
    type: integer
  filter:
    description:
      - >-
        The filter to apply on the operation. We support 'odata v4.0' filter
        semantics. [Learn
        more](https://docs.microsoft.com/odata/concepts/queryoptions-overview).
        _Status_ filter can only be used with Equals ('eq') operator. For
        _CreatedDate_ filter, the supported operators are Greater Than ('gt')
        and Greater Than or Equals ('ge'). When using both filters, combine them
        using the logical 'AND'.
    type: str
  support_ticket_name:
    description:
      - Support ticket name.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List support tickets created on or after a certain date and in open state for a subscription
      azure_rm_supportticket_info: 
        {}
        

    - name: List support tickets for a subscription
      azure_rm_supportticket_info: 
        {}
        

    - name: List support tickets in open state for a subscription
      azure_rm_supportticket_info: 
        {}
        

    - name: Get details of a subscription ticket
      azure_rm_supportticket_info: 
        support_ticket_name: testticket
        

'''

RETURN = '''
support_tickets:
  description: >-
    A list of dict results where the key is the name of the SupportTicket and
    the values are the facts for that SupportTicket.
  returned: always
  type: complex
  contains:
    value:
      description:
        - List of SupportTicket resources.
      returned: always
      type: list
      sample: null
      contains:
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
              Each Azure service has its own set of issue categories, also known
              as problem classification. This parameter is the unique Id for the
              type of problem you are experiencing.
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
              A value that indicates the urgency of the case, which in turn
              determines the response time according to the service level
              agreement of the technical support plan you have with Azure. Note:
              'Highest critical impact', also known as the 'Emergency - Severe
              impact' level in the Azure portal is reserved only for our Premium
              customers.
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
            - >-
              Contact information of the user requesting to create a support
              ticket.
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
                  Additional email addresses listed will be copied on any
                  correspondence about the support ticket.
              returned: always
              type: list
              sample: null
            phone_number:
              description:
                - >-
                  Phone number. This is required if preferred contact method is
                  phone.
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
                  Preferred language of support from Azure. Support languages
                  vary based on the severity you choose for your support ticket.
                  Learn more at [Azure Severity and
                  responsiveness](https://azure.microsoft.com/support/plans/response).
                  Use the standard language-country code. Valid values are
                  'en-us' for English, 'zh-hans' for Chinese, 'es-es' for
                  Spanish, 'fr-fr' for French, 'ja-jp' for Japanese, 'ko-kr' for
                  Korean, 'ru-ru' for Russian, 'pt-br' for Portuguese, 'it-it'
                  for Italian, 'zh-tw' for Chinese and 'de-de' for German.
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
                - >-
                  Time in UTC (ISO 8601 format) when the service level agreement
                  starts.
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
            - >-
              Information about the support engineer working on this support
              ticket.
          returned: always
          type: dict
          sample: null
          contains:
            email_address:
              description:
                - >-
                  Email address of the Azure Support engineer assigned to the
                  support ticket.
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
              This is the resource Id of the Azure service resource associated
              with the support ticket.
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
            - >-
              Time in UTC (ISO 8601 format) when the support ticket was last
              modified.
          returned: always
          type: str
          sample: null
        quota_change_request_sub_type:
          description:
            - >-
              Required for certain quota types when there is a sub type, such as
              Batch, for which you are requesting a quota increase.
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
            - >-
              This property is required for providing the region and new quota
              limits.
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
              This is the resource Id of the Azure service resource (For
              example: A virtual machine resource or an HDInsight resource) for
              which the support ticket is created.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The URI to fetch the next page of SupportTicket resources.
      returned: always
      type: str
      sample: null
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
          problem classification. This parameter is the unique Id for the type
          of problem you are experiencing.
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
          A value that indicates the urgency of the case, which in turn
          determines the response time according to the service level agreement
          of the technical support plan you have with Azure. Note: 'Highest
          critical impact', also known as the 'Emergency - Severe impact' level
          in the Azure portal is reserved only for our Premium customers.
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
              Additional email addresses listed will be copied on any
              correspondence about the support ticket.
          returned: always
          type: list
          sample: null
        phone_number:
          description:
            - >-
              Phone number. This is required if preferred contact method is
              phone.
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
              Preferred language of support from Azure. Support languages vary
              based on the severity you choose for your support ticket. Learn
              more at [Azure Severity and
              responsiveness](https://azure.microsoft.com/support/plans/response).
              Use the standard language-country code. Valid values are 'en-us'
              for English, 'zh-hans' for Chinese, 'es-es' for Spanish, 'fr-fr'
              for French, 'ja-jp' for Japanese, 'ko-kr' for Korean, 'ru-ru' for
              Russian, 'pt-br' for Portuguese, 'it-it' for Italian, 'zh-tw' for
              Chinese and 'de-de' for German.
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
            - >-
              Time in UTC (ISO 8601 format) when the service level agreement
              starts.
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
              Email address of the Azure Support engineer assigned to the
              support ticket.
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
          This is the resource Id of the Azure service resource associated with
          the support ticket.
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
        - >-
          Time in UTC (ISO 8601 format) when the support ticket was last
          modified.
      returned: always
      type: str
      sample: null
    quota_change_request_sub_type:
      description:
        - >-
          Required for certain quota types when there is a sub type, such as
          Batch, for which you are requesting a quota increase.
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
        - >-
          This property is required for providing the region and new quota
          limits.
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
          virtual machine resource or an HDInsight resource) for which the
          support ticket is created.
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
    from azure.mgmt.microsoft.support import Microsoft.Support
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSupportTicketInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            top=dict(
                type='integer'
            ),
            filter=dict(
                type='str'
            ),
            support_ticket_name=dict(
                type='str'
            )
        )

        self.top = None
        self.filter = None
        self.support_ticket_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMSupportTicketInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Microsoft.Support,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-04-01')

        if (self.support_ticket_name is not None):
            self.results['support_tickets'] = self.format_item(self.get())
        else:
            self.results['support_tickets'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.support_tickets.get(support_ticket_name=self.support_ticket_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.support_tickets.list(top=self.top,
                                                             filter=self.filter)
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
    AzureRMSupportTicketInfo()


if __name__ == '__main__':
    main()
