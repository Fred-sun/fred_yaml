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
module: azure_rm_guestconfigurationassignment_info
version_added: '2.9'
short_description: Get GuestConfigurationAssignment info.
description:
  - Get info of GuestConfigurationAssignment.
options:
  resource_group_name:
    description:
      - The resource group name.
    required: true
    type: str
  guest_configuration_assignment_name:
    description:
      - The guest configuration assignment name.
    type: str
  vm_name:
    description:
      - The name of the virtual machine.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a guest configuration assignment
      azure_rm_guestconfigurationassignment_info: 
        guest_configuration_assignment_name: SecureProtocol
        resource_group_name: myResourceGroupName
        vm_name: myVMName
        

    - name: List all guest configuration assignments for a virtual machine
      azure_rm_guestconfigurationassignment_info: 
        resource_group_name: myResourceGroupName
        vm_name: myVMName
        

'''

RETURN = '''
guest_configuration_assignments:
  description: >-
    A list of dict results where the key is the name of the
    GuestConfigurationAssignment and the values are the facts for that
    GuestConfigurationAssignment.
  returned: always
  type: complex
  contains:
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
              A value indicating compliance status of the machine for the
              assigned guest configuration.
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
            - >-
              ARM resource id of the report for the guest configuration
              assignment.
          returned: always
          type: str
          sample: null
        report_id:
          description:
            - >-
              GUID that identifies the guest configuration assignment report
              under a subscription, resource group.
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
              Start date and time of the guest configuration assignment
              compliance status check.
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
              A value indicating compliance status of the machine for the
              assigned guest configuration.
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
                      Code for the compliance of the guest configuration
                      assignment resource.
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
                  applies the configuration to the target nodes. Possible values
                  are ApplyOnly, ApplyAndMonitor, and ApplyAndAutoCorrect.
              returned: always
              type: str
              sample: null
            allow_module_overwrite:
              description:
                - >-
                  If true - new configurations downloaded from the pull service
                  are allowed to overwrite the old ones on the target node.
                  Otherwise, false
              returned: always
              type: str
              sample: null
            action_after_reboot:
              description:
                - >-
                  Specifies what happens after a reboot during the application
                  of a configuration. The possible values are
                  ContinueConfiguration and StopConfiguration
              returned: always
              type: str
              sample: null
            refresh_frequency_mins:
              description:
                - >-
                  The time interval, in minutes, at which the LCM checks a pull
                  service to get updated configurations. This value is ignored
                  if the LCM is not configured in pull mode. The default value
                  is 30.
              returned: always
              type: number
              sample: null
            reboot_if_needed:
              description:
                - >-
                  Set this to true to automatically reboot the node after a
                  configuration that requires reboot is applied. Otherwise, you
                  will have to manually reboot the node for any configuration
                  that requires it. The default value is false. To use this
                  setting when a reboot condition is enacted by something other
                  than DSC (such as Windows Installer), combine this setting
                  with the xPendingReboot module.
              returned: always
              type: str
              sample: null
            configuration_mode_frequency_mins:
              description:
                - >-
                  How often, in minutes, the current configuration is checked
                  and applied. This property is ignored if the ConfigurationMode
                  property is set to ApplyOnly. The default value is 15.
              returned: always
              type: number
              sample: null
    value:
      description:
        - Result of the list guest configuration assignment operation.
      returned: always
      type: list
      sample: null
      contains:
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
                  A value indicating compliance status of the machine for the
                  assigned guest configuration.
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
                - >-
                  Id of the latest report for the guest configuration
                  assignment. 
              returned: always
              type: str
              sample: null
            context:
              description:
                - >-
                  The source which initiated the guest configuration assignment.
                  Ex: Azure Policy
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
                - >-
                  ARM resource id of the report for the guest configuration
                  assignment.
              returned: always
              type: str
              sample: null
            report_id:
              description:
                - >-
                  GUID that identifies the guest configuration assignment report
                  under a subscription, resource group.
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
                  Start date and time of the guest configuration assignment
                  compliance status check.
              returned: always
              type: str
              sample: null
            end_time:
              description:
                - >-
                  End date and time of the guest configuration assignment
                  compliance status check.
              returned: always
              type: str
              sample: null
            compliance_status_latest_assignment_report_compliance_status:
              description:
                - >-
                  A value indicating compliance status of the machine for the
                  assigned guest configuration.
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
                      A value indicating compliance status of the machine for
                      the assigned guest configuration.
                  returned: always
                  type: str
                  sample: null
                resource_id:
                  description:
                    - >-
                      Name of the guest configuration assignment resource
                      setting.
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
                          Code for the compliance of the guest configuration
                          assignment resource.
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
                - >-
                  Uri of the storage where guest configuration package is
                  uploaded.
              returned: always
              type: str
              sample: null
            content_hash:
              description:
                - >-
                  Combined hash of the guest configuration package and
                  configuration parameters.
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
                      Specifies how the LCM(Local Configuration Manager)
                      actually applies the configuration to the target nodes.
                      Possible values are ApplyOnly, ApplyAndMonitor, and
                      ApplyAndAutoCorrect.
                  returned: always
                  type: str
                  sample: null
                allow_module_overwrite:
                  description:
                    - >-
                      If true - new configurations downloaded from the pull
                      service are allowed to overwrite the old ones on the
                      target node. Otherwise, false
                  returned: always
                  type: str
                  sample: null
                action_after_reboot:
                  description:
                    - >-
                      Specifies what happens after a reboot during the
                      application of a configuration. The possible values are
                      ContinueConfiguration and StopConfiguration
                  returned: always
                  type: str
                  sample: null
                refresh_frequency_mins:
                  description:
                    - >-
                      The time interval, in minutes, at which the LCM checks a
                      pull service to get updated configurations. This value is
                      ignored if the LCM is not configured in pull mode. The
                      default value is 30.
                  returned: always
                  type: number
                  sample: null
                reboot_if_needed:
                  description:
                    - >-
                      Set this to true to automatically reboot the node after a
                      configuration that requires reboot is applied. Otherwise,
                      you will have to manually reboot the node for any
                      configuration that requires it. The default value is
                      false. To use this setting when a reboot condition is
                      enacted by something other than DSC (such as Windows
                      Installer), combine this setting with the xPendingReboot
                      module.
                  returned: always
                  type: str
                  sample: null
                configuration_mode_frequency_mins:
                  description:
                    - >-
                      How often, in minutes, the current configuration is
                      checked and applied. This property is ignored if the
                      ConfigurationMode property is set to ApplyOnly. The
                      default value is 15.
                  returned: always
                  type: number
                  sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.guest import GuestConfigurationClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMGuestConfigurationAssignmentInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            guest_configuration_assignment_name=dict(
                type='str'
            ),
            vm_name=dict(
                type='str',
                required=True
            )
        )

        self.resource_group_name = None
        self.guest_configuration_assignment_name = None
        self.vm_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-25'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMGuestConfigurationAssignmentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GuestConfigurationClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-25')

        if (self.resource_group_name is not None and
            self.guest_configuration_assignment_name is not None and
            self.vm_name is not None):
            self.results['guest_configuration_assignments'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.vm_name is not None):
            self.results['guest_configuration_assignments'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.guest_configuration_assignments.get(resource_group_name=self.resource_group_name,
                                                                            guest_configuration_assignment_name=self.guest_configuration_assignment_name,
                                                                            vm_name=self.vm_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.guest_configuration_assignments.list(resource_group_name=self.resource_group_name,
                                                                             vm_name=self.vm_name)
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
    AzureRMGuestConfigurationAssignmentInfo()


if __name__ == '__main__':
    main()
