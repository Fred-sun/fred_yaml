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
module: azure_rm_guestconfigurationhcrpassignment
version_added: '2.9'
short_description: Manage Azure GuestConfigurationHCRPAssignment instance.
description:
  - >-
    Create, update and delete instance of Azure
    GuestConfigurationHCRPAssignment.
options:
  guest_configuration_assignment_name:
    description:
      - Name of the guest configuration assignment.
      - The guest configuration assignment name.
    required: true
    type: str
  resource_group_name:
    description:
      - The resource group name.
    required: true
    type: str
  machine_name:
    description:
      - The name of the ARC machine.
    required: true
    type: str
  name:
    description:
      - Name of the guest configuration assignment.
    type: str
  location:
    description:
      - Region where the VM is located.
    type: str
  properties:
    description:
      - Properties of the Guest configuration assignment.
    type: dict
    suboptions:
      target_resource_id:
        description:
          - VM resource Id.
        type: str
      compliance_status:
        description:
          - >-
            A value indicating compliance status of the machine for the assigned
            guest configuration.
        type: str
        choices:
          - Compliant
          - NonCompliant
          - Pending
      last_compliance_status_checked:
        description:
          - Date and time when last compliance status was checked.
        type: str
      latest_report_id:
        description:
          - 'Id of the latest report for the guest configuration assignment. '
        type: str
      context:
        description:
          - >-
            The source which initiated the guest configuration assignment. Ex:
            Azure Policy
        type: str
      assignment_hash:
        description:
          - Combined hash of the configuration package and parameters.
        type: str
      provisioning_state:
        description:
          - 'The provisioning state, which only appears in the response.'
        type: str
        choices:
          - Succeeded
          - Failed
          - Canceled
          - Created
      id:
        description:
          - >-
            ARM resource id of the report for the guest configuration
            assignment.
        type: str
      report_id:
        description:
          - >-
            GUID that identifies the guest configuration assignment report under
            a subscription, resource group.
        type: str
      assignment:
        description:
          - Configuration details of the guest configuration assignment.
        type: dict
        suboptions:
          name:
            description:
              - Name of the guest configuration assignment.
            type: str
          configuration:
            description:
              - Information about the configuration.
            type: dict
            suboptions:
              name:
                description:
                  - Name of the configuration.
                type: str
              version:
                description:
                  - Version of the configuration.
                type: str
      vm:
        description:
          - Information about the VM.
        type: dict
        suboptions:
          id:
            description:
              - Azure resource Id of the VM.
            type: str
          uuid:
            description:
              - UUID(Universally Unique Identifier) of the VM.
            type: str
      start_time:
        description:
          - >-
            Start date and time of the guest configuration assignment compliance
            status check.
        type: str
      end_time:
        description:
          - >-
            End date and time of the guest configuration assignment compliance
            status check.
        type: str
      compliance_status_latest_assignment_report_compliance_status:
        description:
          - >-
            A value indicating compliance status of the machine for the assigned
            guest configuration.
        type: str
        choices:
          - Compliant
          - NonCompliant
          - Pending
      operation_type:
        description:
          - 'Type of report, Consistency or Initial'
        type: str
        choices:
          - Consistency
          - Initial
      resources:
        description:
          - >-
            The list of resources for which guest configuration assignment
            compliance is checked.
        type: list
        suboptions:
          compliance_status:
            description:
              - >-
                A value indicating compliance status of the machine for the
                assigned guest configuration.
            type: str
            choices:
              - Compliant
              - NonCompliant
              - Pending
          resource_id:
            description:
              - Name of the guest configuration assignment resource setting.
            type: str
          reasons:
            description:
              - Compliance reason and reason code for a resource.
            type: list
            suboptions:
              phrase:
                description:
                  - >-
                    Reason for the compliance of the guest configuration
                    assignment resource.
                type: str
              code:
                description:
                  - >-
                    Code for the compliance of the guest configuration
                    assignment resource.
                type: str
          properties:
            description:
              - Properties of a guest configuration assignment resource.
            type: any
      kind:
        description:
          - 'Kind of the guest configuration. For example:DSC'
        type: str
        choices:
          - DSC
      name:
        description:
          - Name of the guest configuration.
        type: str
      version:
        description:
          - Version of the guest configuration.
        type: str
      content_uri:
        description:
          - Uri of the storage where guest configuration package is uploaded.
        type: str
      content_hash:
        description:
          - >-
            Combined hash of the guest configuration package and configuration
            parameters.
        type: str
      configuration_parameter:
        description:
          - The configuration parameters for the guest configuration.
        type: list
        suboptions:
          name:
            description:
              - Name of the configuration parameter.
            type: str
          value:
            description:
              - Value of the configuration parameter.
            type: str
      configuration_setting:
        description:
          - The configuration setting for the guest configuration.
        type: dict
        suboptions:
          configuration_mode:
            description:
              - >-
                Specifies how the LCM(Local Configuration Manager) actually
                applies the configuration to the target nodes. Possible values
                are ApplyOnly, ApplyAndMonitor, and ApplyAndAutoCorrect.
            type: str
            choices:
              - ApplyOnly
              - ApplyAndMonitor
              - ApplyAndAutoCorrect
          allow_module_overwrite:
            description:
              - >-
                If true - new configurations downloaded from the pull service
                are allowed to overwrite the old ones on the target node.
                Otherwise, false
            type: str
            choices:
              - 'True'
              - 'False'
          action_after_reboot:
            description:
              - >-
                Specifies what happens after a reboot during the application of
                a configuration. The possible values are ContinueConfiguration
                and StopConfiguration
            type: str
            choices:
              - ContinueConfiguration
              - StopConfiguration
          refresh_frequency_mins:
            description:
              - >-
                The time interval, in minutes, at which the LCM checks a pull
                service to get updated configurations. This value is ignored if
                the LCM is not configured in pull mode. The default value is 30.
            type: number
          reboot_if_needed:
            description:
              - >-
                Set this to true to automatically reboot the node after a
                configuration that requires reboot is applied. Otherwise, you
                will have to manually reboot the node for any configuration that
                requires it. The default value is false. To use this setting
                when a reboot condition is enacted by something other than DSC
                (such as Windows Installer), combine this setting with the
                xPendingReboot module.
            type: str
            choices:
              - 'True'
              - 'False'
          configuration_mode_frequency_mins:
            description:
              - >-
                How often, in minutes, the current configuration is checked and
                applied. This property is ignored if the ConfigurationMode
                property is set to ApplyOnly. The default value is 15.
            type: number
  state:
    description:
      - Assert the state of the GuestConfigurationHCRPAssignment.
      - >-
        Use C(present) to create or update an GuestConfigurationHCRPAssignment
        and C(absent) to delete it.
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
    - name: Create or update guest configuration assignment
      azure_rm_guestconfigurationhcrpassignment: 
        guest_configuration_assignment_name: WhitelistedApplication
        machine_name: myMachineName
        resource_group_name: myResourceGroupName
        name: WhitelistedApplication
        location: westcentralus
        properties:
          context: Azure policy
          guest_configuration:
            name: WhitelistedApplication
            configuration_parameter:
              - name: '[InstalledApplication]bwhitelistedapp;Name'
                value: 'NotePad,sql'
            configuration_setting:
              action_after_reboot: ContinueConfiguration
              configuration_mode: MonitorOnly
              configuration_mode_frequency_mins: 15
              reboot_if_needed: 'False'
            version: 1.*
        

    - name: Delete an guest configuration assignment
      azure_rm_guestconfigurationhcrpassignment: 
        guest_configuration_assignment_name: SecureProtocol
        machine_name: myMachineName
        resource_group_name: myResourceGroupName
        

'''

RETURN = '''
id:
  description:
    - ARM resource id of the guest configuration assignment.
  returned: always
  type: str
  sample: null
name:
  description:
    - Name of the guest configuration assignment.
  returned: always
  type: str
  sample: null
location:
  description:
    - Region where the VM is located.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the resource.
  returned: always
  type: str
  sample: null
properties:
  description:
    - Properties of the Guest configuration assignment.
  returned: always
  type: dict
  sample: null
  contains:
    target_resource_id:
      description:
        - VM resource Id.
      returned: always
      type: str
      sample: null
    compliance_status:
      description:
        - >-
          A value indicating compliance status of the machine for the assigned
          guest configuration.
      returned: always
      type: str
      sample: null
    last_compliance_status_checked:
      description:
        - Date and time when last compliance status was checked.
      returned: always
      type: str
      sample: null
    latest_report_id:
      description:
        - 'Id of the latest report for the guest configuration assignment. '
      returned: always
      type: str
      sample: null
    context:
      description:
        - >-
          The source which initiated the guest configuration assignment. Ex:
          Azure Policy
      returned: always
      type: str
      sample: null
    assignment_hash:
      description:
        - Combined hash of the configuration package and parameters.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - 'The provisioning state, which only appears in the response.'
      returned: always
      type: str
      sample: null
    id:
      description:
        - ARM resource id of the report for the guest configuration assignment.
      returned: always
      type: str
      sample: null
    report_id:
      description:
        - >-
          GUID that identifies the guest configuration assignment report under a
          subscription, resource group.
      returned: always
      type: str
      sample: null
    assignment:
      description:
        - Configuration details of the guest configuration assignment.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - Name of the guest configuration assignment.
          returned: always
          type: str
          sample: null
        configuration:
          description:
            - Information about the configuration.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Name of the configuration.
              returned: always
              type: str
              sample: null
            version:
              description:
                - Version of the configuration.
              returned: always
              type: str
              sample: null
    vm:
      description:
        - Information about the VM.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - Azure resource Id of the VM.
          returned: always
          type: str
          sample: null
        uuid:
          description:
            - UUID(Universally Unique Identifier) of the VM.
          returned: always
          type: str
          sample: null
    start_time:
      description:
        - >-
          Start date and time of the guest configuration assignment compliance
          status check.
      returned: always
      type: str
      sample: null
    end_time:
      description:
        - >-
          End date and time of the guest configuration assignment compliance
          status check.
      returned: always
      type: str
      sample: null
    compliance_status_latest_assignment_report_compliance_status:
      description:
        - >-
          A value indicating compliance status of the machine for the assigned
          guest configuration.
      returned: always
      type: str
      sample: null
    operation_type:
      description:
        - 'Type of report, Consistency or Initial'
      returned: always
      type: str
      sample: null
    resources:
      description:
        - >-
          The list of resources for which guest configuration assignment
          compliance is checked.
      returned: always
      type: list
      sample: null
      contains:
        compliance_status:
          description:
            - >-
              A value indicating compliance status of the machine for the
              assigned guest configuration.
          returned: always
          type: str
          sample: null
        resource_id:
          description:
            - Name of the guest configuration assignment resource setting.
          returned: always
          type: str
          sample: null
        reasons:
          description:
            - Compliance reason and reason code for a resource.
          returned: always
          type: list
          sample: null
          contains:
            phrase:
              description:
                - >-
                  Reason for the compliance of the guest configuration
                  assignment resource.
              returned: always
              type: str
              sample: null
            code:
              description:
                - >-
                  Code for the compliance of the guest configuration assignment
                  resource.
              returned: always
              type: str
              sample: null
        properties:
          description:
            - Properties of a guest configuration assignment resource.
          returned: always
          type: any
          sample: null
    kind:
      description:
        - 'Kind of the guest configuration. For example:DSC'
      returned: always
      type: str
      sample: null
    name:
      description:
        - Name of the guest configuration.
      returned: always
      type: str
      sample: null
    version:
      description:
        - Version of the guest configuration.
      returned: always
      type: str
      sample: null
    content_uri:
      description:
        - Uri of the storage where guest configuration package is uploaded.
      returned: always
      type: str
      sample: null
    content_hash:
      description:
        - >-
          Combined hash of the guest configuration package and configuration
          parameters.
      returned: always
      type: str
      sample: null
    configuration_parameter:
      description:
        - The configuration parameters for the guest configuration.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - Name of the configuration parameter.
          returned: always
          type: str
          sample: null
        value:
          description:
            - Value of the configuration parameter.
          returned: always
          type: str
          sample: null
    configuration_setting:
      description:
        - The configuration setting for the guest configuration.
      returned: always
      type: dict
      sample: null
      contains:
        configuration_mode:
          description:
            - >-
              Specifies how the LCM(Local Configuration Manager) actually
              applies the configuration to the target nodes. Possible values are
              ApplyOnly, ApplyAndMonitor, and ApplyAndAutoCorrect.
          returned: always
          type: str
          sample: null
        allow_module_overwrite:
          description:
            - >-
              If true - new configurations downloaded from the pull service are
              allowed to overwrite the old ones on the target node. Otherwise,
              false
          returned: always
          type: str
          sample: null
        action_after_reboot:
          description:
            - >-
              Specifies what happens after a reboot during the application of a
              configuration. The possible values are ContinueConfiguration and
              StopConfiguration
          returned: always
          type: str
          sample: null
        refresh_frequency_mins:
          description:
            - >-
              The time interval, in minutes, at which the LCM checks a pull
              service to get updated configurations. This value is ignored if
              the LCM is not configured in pull mode. The default value is 30.
          returned: always
          type: number
          sample: null
        reboot_if_needed:
          description:
            - >-
              Set this to true to automatically reboot the node after a
              configuration that requires reboot is applied. Otherwise, you will
              have to manually reboot the node for any configuration that
              requires it. The default value is false. To use this setting when
              a reboot condition is enacted by something other than DSC (such as
              Windows Installer), combine this setting with the xPendingReboot
              module.
          returned: always
          type: str
          sample: null
        configuration_mode_frequency_mins:
          description:
            - >-
              How often, in minutes, the current configuration is checked and
              applied. This property is ignored if the ConfigurationMode
              property is set to ApplyOnly. The default value is 15.
          returned: always
          type: number
          sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.guest import GuestConfigurationClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMGuestConfigurationHCRPAssignment(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            guest_configuration_assignment_name=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            machine_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            properties=dict(
                type='dict',
                disposition='/properties',
                options=dict(
                    target_resource_id=dict(
                        type='str',
                        updatable=False,
                        disposition='target_resource_id'
                    ),
                    compliance_status=dict(
                        type='str',
                        updatable=False,
                        disposition='compliance_status',
                        choices=['Compliant',
                                 'NonCompliant',
                                 'Pending']
                    ),
                    last_compliance_status_checked=dict(
                        type='str',
                        updatable=False,
                        disposition='last_compliance_status_checked'
                    ),
                    latest_report_id=dict(
                        type='str',
                        updatable=False,
                        disposition='latest_report_id'
                    ),
                    context=dict(
                        type='str',
                        disposition='context'
                    ),
                    assignment_hash=dict(
                        type='str',
                        updatable=False,
                        disposition='assignment_hash'
                    ),
                    provisioning_state=dict(
                        type='str',
                        updatable=False,
                        disposition='provisioning_state',
                        choices=['Succeeded',
                                 'Failed',
                                 'Canceled',
                                 'Created']
                    ),
                    id=dict(
                        type='str',
                        updatable=False,
                        disposition='id'
                    ),
                    report_id=dict(
                        type='str',
                        updatable=False,
                        disposition='report_id'
                    ),
                    assignment=dict(
                        type='dict',
                        disposition='assignment',
                        options=dict(
                            name=dict(
                                type='str',
                                updatable=False,
                                disposition='name'
                            ),
                            configuration=dict(
                                type='dict',
                                disposition='configuration',
                                options=dict(
                                    name=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='name'
                                    ),
                                    version=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='version'
                                    )
                                )
                            )
                        )
                    ),
                    vm=dict(
                        type='dict',
                        disposition='vm',
                        options=dict(
                            id=dict(
                                type='str',
                                updatable=False,
                                disposition='id'
                            ),
                            uuid=dict(
                                type='str',
                                updatable=False,
                                disposition='uuid'
                            )
                        )
                    ),
                    start_time=dict(
                        type='str',
                        updatable=False,
                        disposition='start_time'
                    ),
                    end_time=dict(
                        type='str',
                        updatable=False,
                        disposition='end_time'
                    ),
                    compliance_status_latest_assignment_report_compliance_status=dict(
                        type='str',
                        updatable=False,
                        disposition='compliance_status_latest_assignment_report_compliance_status',
                        choices=['Compliant',
                                 'NonCompliant',
                                 'Pending']
                    ),
                    operation_type=dict(
                        type='str',
                        updatable=False,
                        disposition='operation_type',
                        choices=['Consistency',
                                 'Initial']
                    ),
                    resources=dict(
                        type='list',
                        disposition='resources',
                        elements='dict',
                        options=dict(
                            compliance_status=dict(
                                type='str',
                                updatable=False,
                                disposition='compliance_status',
                                choices=['Compliant',
                                         'NonCompliant',
                                         'Pending']
                            ),
                            resource_id=dict(
                                type='str',
                                updatable=False,
                                disposition='resource_id'
                            ),
                            reasons=dict(
                                type='list',
                                disposition='reasons',
                                elements='dict',
                                options=dict(
                                    phrase=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='phrase'
                                    ),
                                    code=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='code'
                                    )
                                )
                            ),
                            properties=dict(
                                type='any',
                                updatable=False,
                                disposition='properties'
                            )
                        )
                    ),
                    kind=dict(
                        type='str',
                        disposition='kind',
                        choices=['DSC']
                    ),
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    version=dict(
                        type='str',
                        disposition='version'
                    ),
                    content_uri=dict(
                        type='str',
                        updatable=False,
                        disposition='content_uri'
                    ),
                    content_hash=dict(
                        type='str',
                        updatable=False,
                        disposition='content_hash'
                    ),
                    configuration_parameter=dict(
                        type='list',
                        disposition='configuration_parameter',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name'
                            ),
                            value=dict(
                                type='str',
                                disposition='value'
                            )
                        )
                    ),
                    configuration_setting=dict(
                        type='dict',
                        disposition='configuration_setting',
                        options=dict(
                            configuration_mode=dict(
                                type='str',
                                disposition='configuration_mode',
                                choices=['ApplyOnly',
                                         'ApplyAndMonitor',
                                         'ApplyAndAutoCorrect']
                            ),
                            allow_module_overwrite=dict(
                                type='str',
                                disposition='allow_module_overwrite',
                                choices=['True',
                                         'False']
                            ),
                            action_after_reboot=dict(
                                type='str',
                                disposition='action_after_reboot',
                                choices=['ContinueConfiguration',
                                         'StopConfiguration']
                            ),
                            refresh_frequency_mins=dict(
                                type='number',
                                disposition='refresh_frequency_mins'
                            ),
                            reboot_if_needed=dict(
                                type='str',
                                disposition='reboot_if_needed',
                                choices=['True',
                                         'False']
                            ),
                            configuration_mode_frequency_mins=dict(
                                type='number',
                                disposition='configuration_mode_frequency_mins'
                            )
                        )
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.guest_configuration_assignment_name = None
        self.resource_group_name = None
        self.machine_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGuestConfigurationHCRPAssignment, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(GuestConfigurationClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-25')

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
            response = self.mgmt_client.guest_configuration_hcrpassignments.create_or_update(guest_configuration_assignment_name=self.guest_configuration_assignment_name,
                                                                                             resource_group_name=self.resource_group_name,
                                                                                             machine_name=self.machine_name,
                                                                                             parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the GuestConfigurationHCRPAssignment instance.')
            self.fail('Error creating the GuestConfigurationHCRPAssignment instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.guest_configuration_hcrpassignments.delete(resource_group_name=self.resource_group_name,
                                                                                   guest_configuration_assignment_name=self.guest_configuration_assignment_name,
                                                                                   machine_name=self.machine_name)
        except CloudError as e:
            self.log('Error attempting to delete the GuestConfigurationHCRPAssignment instance.')
            self.fail('Error deleting the GuestConfigurationHCRPAssignment instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.guest_configuration_hcrpassignments.get(resource_group_name=self.resource_group_name,
                                                                                guest_configuration_assignment_name=self.guest_configuration_assignment_name,
                                                                                machine_name=self.machine_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGuestConfigurationHCRPAssignment()


if __name__ == '__main__':
    main()
