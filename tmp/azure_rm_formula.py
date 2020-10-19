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
module: azure_rm_formula
version_added: '2.9'
short_description: Manage Azure Formula instance.
description:
  - 'Create, update and delete instance of Azure Formula.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  lab_name:
    description:
      - The name of the lab.
    required: true
    type: str
  name:
    description:
      - The name of the formula.
    required: true
    type: str
  expand:
    description:
      - 'Specify the $expand query. Example: ''properties($select=description)'''
    type: str
  location:
    description:
      - The location of the resource.
      - The location of the new virtual machine or environment
    type: str
  description:
    description:
      - The description of the formula.
    type: str
  author:
    description:
      - The author of the formula.
    type: str
  os_type:
    description:
      - The OS type of the formula.
      - The OS type of the virtual machine.
    type: str
  lab_vm_id:
    description:
      - The identifier of the VM from which a formula is to be created.
    type: str
  lab_virtual_machine_creation_parameter_name:
    description:
      - The name of the virtual machine or environment
    type: str
  lab_virtual_machine_creation_parameter_location:
    description:
      - The location of the new virtual machine or environment
    type: str
  lab_virtual_machine_creation_parameter_tags:
    description:
      - The tags of the resource.
    type: dictionary
  bulk_creation_parameters:
    description:
      - The number of virtual machine instances to create.
    type: dict
    suboptions:
      instance_count:
        description:
          - The number of virtual machine instances to create.
        type: integer
  notes:
    description:
      - The notes of the virtual machine.
    type: str
  owner_object_id:
    description:
      - The object identifier of the owner of the virtual machine.
    type: str
  owner_user_principal_name:
    description:
      - The user principal name of the virtual machine owner.
    type: str
  created_by_user_id:
    description:
      - The object identifier of the creator of the virtual machine.
    type: str
  created_by_user:
    description:
      - The email address of creator of the virtual machine.
    type: str
  created_date:
    description:
      - The creation date of the virtual machine.
    type: str
  compute_id:
    description:
      - The resource identifier (Microsoft.Compute) of the virtual machine.
    type: str
  custom_image_id:
    description:
      - The custom image identifier of the virtual machine.
    type: str
  size:
    description:
      - The size of the virtual machine.
    type: str
  user_name:
    description:
      - The user name of the virtual machine.
    type: str
  password:
    description:
      - The password of the virtual machine administrator.
    type: str
  ssh_key:
    description:
      - The SSH key of the virtual machine administrator.
    type: str
  is_authentication_with_ssh_key:
    description:
      - >-
        Indicates whether this virtual machine uses an SSH key for
        authentication.
    type: bool
  fqdn:
    description:
      - The fully-qualified domain name of the virtual machine.
    type: str
  lab_subnet_name:
    description:
      - The lab subnet name of the virtual machine.
    type: str
  lab_virtual_network_id:
    description:
      - The lab virtual network identifier of the virtual machine.
    type: str
  disallow_public_ip_address:
    description:
      - >-
        Indicates whether the virtual machine is to be created without a public
        IP address.
    type: bool
  artifacts:
    description:
      - The artifacts to be installed on the virtual machine.
    type: list
    suboptions:
      artifact_id:
        description:
          - The artifact's identifier.
        type: str
      artifact_title:
        description:
          - The artifact's title.
        type: str
      parameters:
        description:
          - The parameters of the artifact.
        type: list
        suboptions:
          name:
            description:
              - The name of the artifact parameter.
            type: str
          value:
            description:
              - The value of the artifact parameter.
            type: str
      status:
        description:
          - The status of the artifact.
        type: str
      deployment_status_message:
        description:
          - The status message from the deployment.
        type: str
      vm_extension_status_message:
        description:
          - The status message from the virtual machine extension.
        type: str
      install_time:
        description:
          - The time that the artifact starts to install on the virtual machine.
        type: str
  artifact_deployment_status:
    description:
      - The artifact deployment status for the virtual machine.
    type: dict
    suboptions:
      deployment_status:
        description:
          - The deployment status of the artifact.
        type: str
      artifacts_applied:
        description:
          - The total count of the artifacts that were successfully applied.
        type: integer
      total_artifacts:
        description:
          - The total count of the artifacts that were tentatively applied.
        type: integer
  gallery_image_reference:
    description:
      - The Microsoft Azure Marketplace image reference of the virtual machine.
    type: dict
    suboptions:
      offer:
        description:
          - The offer of the gallery image.
        type: str
      publisher:
        description:
          - The publisher of the gallery image.
        type: str
      sku:
        description:
          - The SKU of the gallery image.
        type: str
      os_type:
        description:
          - The OS type of the gallery image.
        type: str
      version:
        description:
          - The version of the gallery image.
        type: str
  plan_id:
    description:
      - The id of the plan associated with the virtual machine image
    type: str
  network_interface:
    description:
      - The network interface properties.
    type: dict
    suboptions:
      virtual_network_id:
        description:
          - The resource ID of the virtual network.
        type: str
      subnet_id:
        description:
          - The resource ID of the sub net.
        type: str
      public_ip_address_id:
        description:
          - The resource ID of the public IP address.
        type: str
      public_ip_address:
        description:
          - The public IP address.
        type: str
      private_ip_address:
        description:
          - The private IP address.
        type: str
      dns_name:
        description:
          - The DNS name.
        type: str
      rdp_authority:
        description:
          - >-
            The RdpAuthority property is a server DNS host name or IP address
            followed by the service port number for RDP (Remote Desktop
            Protocol).
        type: str
      ssh_authority:
        description:
          - >-
            The SshAuthority property is a server DNS host name or IP address
            followed by the service port number for SSH.
        type: str
      shared_public_ip_address_configuration:
        description:
          - >-
            The configuration for sharing a public IP address across multiple
            virtual machines.
        type: dict
        suboptions:
          inbound_nat_rules:
            description:
              - The incoming NAT rules
            type: list
            suboptions:
              transport_protocol:
                description:
                  - The transport protocol for the endpoint.
                type: str
                choices:
                  - Tcp
                  - Udp
              frontend_port:
                description:
                  - >-
                    The external endpoint port of the inbound connection.
                    Possible values range between 1 and 65535, inclusive. If
                    unspecified, a value will be allocated automatically.
                type: integer
              backend_port:
                description:
                  - The port to which the external traffic will be redirected.
                type: integer
  expiration_date:
    description:
      - The expiration date for VM.
    type: str
  allow_claim:
    description:
      - Indicates whether another user can take ownership of the virtual machine
    type: bool
  storage_type:
    description:
      - 'Storage type to use for virtual machine (i.e. Standard, Premium).'
    type: str
  virtual_machine_creation_source:
    description:
      - Tells source of creation of lab virtual machine. Output property only.
    type: str
    choices:
      - FromCustomImage
      - FromGalleryImage
      - FromSharedGalleryImage
  environment_id:
    description:
      - >-
        The resource ID of the environment that contains this virtual machine,
        if any.
    type: str
  data_disk_parameters:
    description:
      - >-
        New or existing data disks to attach to the virtual machine after
        creation
    type: list
    suboptions:
      attach_new_data_disk_options:
        description:
          - Specifies options to attach a new disk to the virtual machine.
        type: dict
        suboptions:
          disk_size_gi_b:
            description:
              - Size of the disk to be attached in GibiBytes.
            type: integer
          disk_name:
            description:
              - The name of the disk to be attached.
            type: str
          disk_type:
            description:
              - 'The storage type for the disk (i.e. Standard, Premium).'
            type: str
            choices:
              - Standard
              - Premium
              - StandardSSD
      existing_lab_disk_id:
        description:
          - Specifies the existing lab disk id to attach to virtual machine.
        type: str
      host_caching:
        description:
          - 'Caching option for a data disk (i.e. None, ReadOnly, ReadWrite).'
        type: str
        choices:
          - None
          - ReadOnly
          - ReadWrite
  schedule_parameters:
    description:
      - Virtual Machine schedules to be created
    type: list
    suboptions:
      name:
        description:
          - The name of the virtual machine or environment
        type: str
      location:
        description:
          - The location of the new virtual machine or environment
        type: str
      status:
        description:
          - 'The status of the schedule (i.e. Enabled, Disabled)'
        type: str
        choices:
          - Enabled
          - Disabled
      task_type:
        description:
          - >-
            The task type of the schedule (e.g. LabVmsShutdownTask,
            LabVmAutoStart).
        type: str
      weekly_recurrence:
        description:
          - >-
            If the schedule will occur only some days of the week, specify the
            weekly recurrence.
        type: dict
        suboptions:
          weekdays:
            description:
              - >-
                The days of the week for which the schedule is set (e.g. Sunday,
                Monday, Tuesday, etc.).
            type: list
          time:
            description:
              - The time of the day the schedule will occur.
            type: str
      daily_recurrence:
        description:
          - >-
            If the schedule will occur once each day of the week, specify the
            daily recurrence.
        type: dict
        suboptions:
          time:
            description:
              - The time of day the schedule will occur.
            type: str
      hourly_recurrence:
        description:
          - >-
            If the schedule will occur multiple times a day, specify the hourly
            recurrence.
        type: dict
        suboptions:
          minute:
            description:
              - Minutes of the hour the schedule will run.
            type: integer
      time_zone_id:
        description:
          - The time zone ID (e.g. Pacific Standard time).
        type: str
      notification_settings:
        description:
          - Notification settings.
        type: dict
        suboptions:
          status:
            description:
              - >-
                If notifications are enabled for this schedule (i.e. Enabled,
                Disabled).
            type: str
            choices:
              - Enabled
              - Disabled
          time_in_minutes:
            description:
              - Time in minutes before event at which notification will be sent.
            type: integer
          webhook_url:
            description:
              - The webhook URL to which the notification will be sent.
            type: str
          email_recipient:
            description:
              - >-
                The email recipient to send notifications to (can be a list of
                semi-colon separated email addresses).
            type: str
          notification_locale:
            description:
              - >-
                The locale to use when sending a notification (fallback for
                unsupported languages is EN).
            type: str
      target_resource_id:
        description:
          - The resource ID to which the schedule belongs
        type: str
  last_known_power_state:
    description:
      - Last known compute power state captured in DTL
    type: str
  lab_virtual_machine_creation_parameter_fragment_name:
    description:
      - The name of the virtual machine or environment
    type: str
  lab_virtual_machine_creation_parameter_fragment_tags:
    description:
      - The tags of the resource.
    type: dictionary
  state:
    description:
      - Assert the state of the Formula.
      - >-
        Use C(present) to create or update an Formula and C(absent) to delete
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
'''

RETURN = '''
id:
  description:
    - The identifier of the resource.
  returned: always
  type: str
  sample: null
name:
  description:
    - The name of the resource.
  returned: always
  type: str
  sample: null
type:
  description:
    - The type of the resource.
  returned: always
  type: str
  sample: null
location:
  description:
    - The location of the resource.
  returned: always
  type: str
  sample: null
tags:
  description:
    - The tags of the resource.
  returned: always
  type: dictionary
  sample: null
description:
  description:
    - The description of the formula.
  returned: always
  type: str
  sample: null
author:
  description:
    - The author of the formula.
  returned: always
  type: str
  sample: null
os_type_properties_os_type:
  description:
    - The OS type of the formula.
  returned: always
  type: str
  sample: null
creation_date:
  description:
    - The creation date of the formula.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning status of the resource.
  returned: always
  type: str
  sample: null
unique_identifier:
  description:
    - The unique immutable identifier of a resource (Guid).
  returned: always
  type: str
  sample: null
lab_vm_id:
  description:
    - The identifier of the VM from which a formula is to be created.
  returned: always
  type: str
  sample: null
name_properties_formula_content_name:
  description:
    - The name of the virtual machine or environment
  returned: always
  type: str
  sample: null
location_properties_formula_content_location:
  description:
    - The location of the new virtual machine or environment
  returned: always
  type: str
  sample: null
tags_properties_formula_content_tags:
  description:
    - The tags of the resource.
  returned: always
  type: dictionary
  sample: null
bulk_creation_parameters:
  description:
    - The number of virtual machine instances to create.
  returned: always
  type: dict
  sample: null
  contains:
    instance_count:
      description:
        - The number of virtual machine instances to create.
      returned: always
      type: integer
      sample: null
notes:
  description:
    - The notes of the virtual machine.
  returned: always
  type: str
  sample: null
owner_object_id:
  description:
    - The object identifier of the owner of the virtual machine.
  returned: always
  type: str
  sample: null
owner_user_principal_name:
  description:
    - The user principal name of the virtual machine owner.
  returned: always
  type: str
  sample: null
created_by_user_id:
  description:
    - The object identifier of the creator of the virtual machine.
  returned: always
  type: str
  sample: null
created_by_user:
  description:
    - The email address of creator of the virtual machine.
  returned: always
  type: str
  sample: null
created_date:
  description:
    - The creation date of the virtual machine.
  returned: always
  type: str
  sample: null
compute_id:
  description:
    - The resource identifier (Microsoft.Compute) of the virtual machine.
  returned: always
  type: str
  sample: null
custom_image_id:
  description:
    - The custom image identifier of the virtual machine.
  returned: always
  type: str
  sample: null
os_type_properties_formula_content_properties_os_type:
  description:
    - The OS type of the virtual machine.
  returned: always
  type: str
  sample: null
size:
  description:
    - The size of the virtual machine.
  returned: always
  type: str
  sample: null
user_name:
  description:
    - The user name of the virtual machine.
  returned: always
  type: str
  sample: null
password:
  description:
    - The password of the virtual machine administrator.
  returned: always
  type: str
  sample: null
ssh_key:
  description:
    - The SSH key of the virtual machine administrator.
  returned: always
  type: str
  sample: null
is_authentication_with_ssh_key:
  description:
    - Indicates whether this virtual machine uses an SSH key for authentication.
  returned: always
  type: bool
  sample: null
fqdn:
  description:
    - The fully-qualified domain name of the virtual machine.
  returned: always
  type: str
  sample: null
lab_subnet_name:
  description:
    - The lab subnet name of the virtual machine.
  returned: always
  type: str
  sample: null
lab_virtual_network_id:
  description:
    - The lab virtual network identifier of the virtual machine.
  returned: always
  type: str
  sample: null
disallow_public_ip_address:
  description:
    - >-
      Indicates whether the virtual machine is to be created without a public IP
      address.
  returned: always
  type: bool
  sample: null
artifacts:
  description:
    - The artifacts to be installed on the virtual machine.
  returned: always
  type: list
  sample: null
  contains:
    artifact_id:
      description:
        - The artifact's identifier.
      returned: always
      type: str
      sample: null
    artifact_title:
      description:
        - The artifact's title.
      returned: always
      type: str
      sample: null
    parameters:
      description:
        - The parameters of the artifact.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The name of the artifact parameter.
          returned: always
          type: str
          sample: null
        value:
          description:
            - The value of the artifact parameter.
          returned: always
          type: str
          sample: null
    status:
      description:
        - The status of the artifact.
      returned: always
      type: str
      sample: null
    deployment_status_message:
      description:
        - The status message from the deployment.
      returned: always
      type: str
      sample: null
    vm_extension_status_message:
      description:
        - The status message from the virtual machine extension.
      returned: always
      type: str
      sample: null
    install_time:
      description:
        - The time that the artifact starts to install on the virtual machine.
      returned: always
      type: str
      sample: null
artifact_deployment_status:
  description:
    - The artifact deployment status for the virtual machine.
  returned: always
  type: dict
  sample: null
  contains:
    deployment_status:
      description:
        - The deployment status of the artifact.
      returned: always
      type: str
      sample: null
    artifacts_applied:
      description:
        - The total count of the artifacts that were successfully applied.
      returned: always
      type: integer
      sample: null
    total_artifacts:
      description:
        - The total count of the artifacts that were tentatively applied.
      returned: always
      type: integer
      sample: null
gallery_image_reference:
  description:
    - The Microsoft Azure Marketplace image reference of the virtual machine.
  returned: always
  type: dict
  sample: null
  contains:
    offer:
      description:
        - The offer of the gallery image.
      returned: always
      type: str
      sample: null
    publisher:
      description:
        - The publisher of the gallery image.
      returned: always
      type: str
      sample: null
    sku:
      description:
        - The SKU of the gallery image.
      returned: always
      type: str
      sample: null
    os_type:
      description:
        - The OS type of the gallery image.
      returned: always
      type: str
      sample: null
    version:
      description:
        - The version of the gallery image.
      returned: always
      type: str
      sample: null
plan_id:
  description:
    - The id of the plan associated with the virtual machine image
  returned: always
  type: str
  sample: null
network_interface:
  description:
    - The network interface properties.
  returned: always
  type: dict
  sample: null
  contains:
    virtual_network_id:
      description:
        - The resource ID of the virtual network.
      returned: always
      type: str
      sample: null
    subnet_id:
      description:
        - The resource ID of the sub net.
      returned: always
      type: str
      sample: null
    public_ip_address_id:
      description:
        - The resource ID of the public IP address.
      returned: always
      type: str
      sample: null
    public_ip_address:
      description:
        - The public IP address.
      returned: always
      type: str
      sample: null
    private_ip_address:
      description:
        - The private IP address.
      returned: always
      type: str
      sample: null
    dns_name:
      description:
        - The DNS name.
      returned: always
      type: str
      sample: null
    rdp_authority:
      description:
        - >-
          The RdpAuthority property is a server DNS host name or IP address
          followed by the service port number for RDP (Remote Desktop Protocol).
      returned: always
      type: str
      sample: null
    ssh_authority:
      description:
        - >-
          The SshAuthority property is a server DNS host name or IP address
          followed by the service port number for SSH.
      returned: always
      type: str
      sample: null
    shared_public_ip_address_configuration:
      description:
        - >-
          The configuration for sharing a public IP address across multiple
          virtual machines.
      returned: always
      type: dict
      sample: null
      contains:
        inbound_nat_rules:
          description:
            - The incoming NAT rules
          returned: always
          type: list
          sample: null
          contains:
            transport_protocol:
              description:
                - The transport protocol for the endpoint.
              returned: always
              type: str
              sample: null
            frontend_port:
              description:
                - >-
                  The external endpoint port of the inbound connection. Possible
                  values range between 1 and 65535, inclusive. If unspecified, a
                  value will be allocated automatically.
              returned: always
              type: integer
              sample: null
            backend_port:
              description:
                - The port to which the external traffic will be redirected.
              returned: always
              type: integer
              sample: null
expiration_date:
  description:
    - The expiration date for VM.
  returned: always
  type: str
  sample: null
allow_claim:
  description:
    - Indicates whether another user can take ownership of the virtual machine
  returned: always
  type: bool
  sample: null
storage_type:
  description:
    - 'Storage type to use for virtual machine (i.e. Standard, Premium).'
  returned: always
  type: str
  sample: null
virtual_machine_creation_source:
  description:
    - Tells source of creation of lab virtual machine. Output property only.
  returned: always
  type: str
  sample: null
environment_id:
  description:
    - >-
      The resource ID of the environment that contains this virtual machine, if
      any.
  returned: always
  type: str
  sample: null
data_disk_parameters:
  description:
    - New or existing data disks to attach to the virtual machine after creation
  returned: always
  type: list
  sample: null
  contains:
    attach_new_data_disk_options:
      description:
        - Specifies options to attach a new disk to the virtual machine.
      returned: always
      type: dict
      sample: null
      contains:
        disk_size_gi_b:
          description:
            - Size of the disk to be attached in GibiBytes.
          returned: always
          type: integer
          sample: null
        disk_name:
          description:
            - The name of the disk to be attached.
          returned: always
          type: str
          sample: null
        disk_type:
          description:
            - 'The storage type for the disk (i.e. Standard, Premium).'
          returned: always
          type: str
          sample: null
    existing_lab_disk_id:
      description:
        - Specifies the existing lab disk id to attach to virtual machine.
      returned: always
      type: str
      sample: null
    host_caching:
      description:
        - 'Caching option for a data disk (i.e. None, ReadOnly, ReadWrite).'
      returned: always
      type: str
      sample: null
schedule_parameters:
  description:
    - Virtual Machine schedules to be created
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - The name of the virtual machine or environment
      returned: always
      type: str
      sample: null
    location:
      description:
        - The location of the new virtual machine or environment
      returned: always
      type: str
      sample: null
    tags:
      description:
        - The tags of the resource.
      returned: always
      type: dictionary
      sample: null
    status:
      description:
        - 'The status of the schedule (i.e. Enabled, Disabled)'
      returned: always
      type: str
      sample: null
    task_type:
      description:
        - >-
          The task type of the schedule (e.g. LabVmsShutdownTask,
          LabVmAutoStart).
      returned: always
      type: str
      sample: null
    weekly_recurrence:
      description:
        - >-
          If the schedule will occur only some days of the week, specify the
          weekly recurrence.
      returned: always
      type: dict
      sample: null
      contains:
        weekdays:
          description:
            - >-
              The days of the week for which the schedule is set (e.g. Sunday,
              Monday, Tuesday, etc.).
          returned: always
          type: list
          sample: null
        time:
          description:
            - The time of the day the schedule will occur.
          returned: always
          type: str
          sample: null
    daily_recurrence:
      description:
        - >-
          If the schedule will occur once each day of the week, specify the
          daily recurrence.
      returned: always
      type: dict
      sample: null
      contains:
        time:
          description:
            - The time of day the schedule will occur.
          returned: always
          type: str
          sample: null
    hourly_recurrence:
      description:
        - >-
          If the schedule will occur multiple times a day, specify the hourly
          recurrence.
      returned: always
      type: dict
      sample: null
      contains:
        minute:
          description:
            - Minutes of the hour the schedule will run.
          returned: always
          type: integer
          sample: null
    time_zone_id:
      description:
        - The time zone ID (e.g. Pacific Standard time).
      returned: always
      type: str
      sample: null
    notification_settings:
      description:
        - Notification settings.
      returned: always
      type: dict
      sample: null
      contains:
        status:
          description:
            - >-
              If notifications are enabled for this schedule (i.e. Enabled,
              Disabled).
          returned: always
          type: str
          sample: null
        time_in_minutes:
          description:
            - Time in minutes before event at which notification will be sent.
          returned: always
          type: integer
          sample: null
        webhook_url:
          description:
            - The webhook URL to which the notification will be sent.
          returned: always
          type: str
          sample: null
        email_recipient:
          description:
            - >-
              The email recipient to send notifications to (can be a list of
              semi-colon separated email addresses).
          returned: always
          type: str
          sample: null
        notification_locale:
          description:
            - >-
              The locale to use when sending a notification (fallback for
              unsupported languages is EN).
          returned: always
          type: str
          sample: null
    target_resource_id:
      description:
        - The resource ID to which the schedule belongs
      returned: always
      type: str
      sample: null
last_known_power_state:
  description:
    - Last known compute power state captured in DTL
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
    from azure.mgmt.dev import DevTestLabsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMFormula(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            lab_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            author=dict(
                type='str',
                disposition='/author'
            ),
            os_type=dict(
                type='str',
                disposition='/os_type'
            ),
            lab_vm_id=dict(
                type='str',
                disposition='/lab_vm_id'
            ),
            lab_virtual_machine_creation_parameter_name=dict(
                type='str',
                disposition='/lab_virtual_machine_creation_parameter_name'
            ),
            lab_virtual_machine_creation_parameter_location=dict(
                type='str',
                disposition='/lab_virtual_machine_creation_parameter_location'
            ),
            lab_virtual_machine_creation_parameter_tags=dict(
                type='dictionary',
                disposition='/lab_virtual_machine_creation_parameter_tags'
            ),
            bulk_creation_parameters=dict(
                type='dict',
                disposition='/bulk_creation_parameters',
                options=dict(
                    instance_count=dict(
                        type='integer',
                        disposition='instance_count'
                    )
                )
            ),
            notes=dict(
                type='str',
                disposition='/notes'
            ),
            owner_object_id=dict(
                type='str',
                disposition='/owner_object_id'
            ),
            owner_user_principal_name=dict(
                type='str',
                disposition='/owner_user_principal_name'
            ),
            created_by_user_id=dict(
                type='str',
                disposition='/created_by_user_id'
            ),
            created_by_user=dict(
                type='str',
                disposition='/created_by_user'
            ),
            created_date=dict(
                type='str',
                disposition='/created_date'
            ),
            compute_id=dict(
                type='str',
                disposition='/compute_id'
            ),
            custom_image_id=dict(
                type='str',
                disposition='/custom_image_id'
            ),
            size=dict(
                type='str',
                disposition='/size'
            ),
            user_name=dict(
                type='str',
                disposition='/user_name'
            ),
            password=dict(
                type='str',
                disposition='/password'
            ),
            ssh_key=dict(
                type='str',
                disposition='/ssh_key'
            ),
            is_authentication_with_ssh_key=dict(
                type='bool',
                disposition='/is_authentication_with_ssh_key'
            ),
            fqdn=dict(
                type='str',
                disposition='/fqdn'
            ),
            lab_subnet_name=dict(
                type='str',
                disposition='/lab_subnet_name'
            ),
            lab_virtual_network_id=dict(
                type='str',
                disposition='/lab_virtual_network_id'
            ),
            disallow_public_ip_address=dict(
                type='bool',
                disposition='/disallow_public_ip_address'
            ),
            artifacts=dict(
                type='list',
                disposition='/artifacts',
                elements='dict',
                options=dict(
                    artifact_id=dict(
                        type='str',
                        disposition='artifact_id'
                    ),
                    artifact_title=dict(
                        type='str',
                        disposition='artifact_title'
                    ),
                    parameters=dict(
                        type='list',
                        disposition='parameters',
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
                    status=dict(
                        type='str',
                        disposition='status'
                    ),
                    deployment_status_message=dict(
                        type='str',
                        disposition='deployment_status_message'
                    ),
                    vm_extension_status_message=dict(
                        type='str',
                        disposition='vm_extension_status_message'
                    ),
                    install_time=dict(
                        type='str',
                        disposition='install_time'
                    )
                )
            ),
            artifact_deployment_status=dict(
                type='dict',
                disposition='/artifact_deployment_status',
                options=dict(
                    deployment_status=dict(
                        type='str',
                        disposition='deployment_status'
                    ),
                    artifacts_applied=dict(
                        type='integer',
                        disposition='artifacts_applied'
                    ),
                    total_artifacts=dict(
                        type='integer',
                        disposition='total_artifacts'
                    )
                )
            ),
            gallery_image_reference=dict(
                type='dict',
                disposition='/gallery_image_reference',
                options=dict(
                    offer=dict(
                        type='str',
                        disposition='offer'
                    ),
                    publisher=dict(
                        type='str',
                        disposition='publisher'
                    ),
                    sku=dict(
                        type='str',
                        disposition='sku'
                    ),
                    os_type=dict(
                        type='str',
                        disposition='os_type'
                    ),
                    version=dict(
                        type='str',
                        disposition='version'
                    )
                )
            ),
            plan_id=dict(
                type='str',
                disposition='/plan_id'
            ),
            network_interface=dict(
                type='dict',
                disposition='/network_interface',
                options=dict(
                    virtual_network_id=dict(
                        type='str',
                        disposition='virtual_network_id'
                    ),
                    subnet_id=dict(
                        type='str',
                        disposition='subnet_id'
                    ),
                    public_ip_address_id=dict(
                        type='str',
                        disposition='public_ip_address_id'
                    ),
                    public_ip_address=dict(
                        type='str',
                        disposition='public_ip_address'
                    ),
                    private_ip_address=dict(
                        type='str',
                        disposition='private_ip_address'
                    ),
                    dns_name=dict(
                        type='str',
                        disposition='dns_name'
                    ),
                    rdp_authority=dict(
                        type='str',
                        disposition='rdp_authority'
                    ),
                    ssh_authority=dict(
                        type='str',
                        disposition='ssh_authority'
                    ),
                    shared_public_ip_address_configuration=dict(
                        type='dict',
                        disposition='shared_public_ip_address_configuration',
                        options=dict(
                            inbound_nat_rules=dict(
                                type='list',
                                disposition='inbound_nat_rules',
                                elements='dict',
                                options=dict(
                                    transport_protocol=dict(
                                        type='str',
                                        disposition='transport_protocol',
                                        choices=['Tcp',
                                                 'Udp']
                                    ),
                                    frontend_port=dict(
                                        type='integer',
                                        disposition='frontend_port'
                                    ),
                                    backend_port=dict(
                                        type='integer',
                                        disposition='backend_port'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            expiration_date=dict(
                type='str',
                disposition='/expiration_date'
            ),
            allow_claim=dict(
                type='bool',
                disposition='/allow_claim'
            ),
            storage_type=dict(
                type='str',
                disposition='/storage_type'
            ),
            virtual_machine_creation_source=dict(
                type='str',
                disposition='/virtual_machine_creation_source',
                choices=['FromCustomImage',
                         'FromGalleryImage',
                         'FromSharedGalleryImage']
            ),
            environment_id=dict(
                type='str',
                disposition='/environment_id'
            ),
            data_disk_parameters=dict(
                type='list',
                disposition='/data_disk_parameters',
                elements='dict',
                options=dict(
                    attach_new_data_disk_options=dict(
                        type='dict',
                        disposition='attach_new_data_disk_options',
                        options=dict(
                            disk_size_gi_b=dict(
                                type='integer',
                                disposition='disk_size_gi_b'
                            ),
                            disk_name=dict(
                                type='str',
                                disposition='disk_name'
                            ),
                            disk_type=dict(
                                type='str',
                                disposition='disk_type',
                                choices=['Standard',
                                         'Premium',
                                         'StandardSSD']
                            )
                        )
                    ),
                    existing_lab_disk_id=dict(
                        type='str',
                        disposition='existing_lab_disk_id'
                    ),
                    host_caching=dict(
                        type='str',
                        disposition='host_caching',
                        choices=['None',
                                 'ReadOnly',
                                 'ReadWrite']
                    )
                )
            ),
            schedule_parameters=dict(
                type='list',
                disposition='/schedule_parameters',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    location=dict(
                        type='str',
                        disposition='location'
                    ),
                    status=dict(
                        type='str',
                        disposition='status',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    task_type=dict(
                        type='str',
                        disposition='task_type'
                    ),
                    weekly_recurrence=dict(
                        type='dict',
                        disposition='weekly_recurrence',
                        options=dict(
                            weekdays=dict(
                                type='list',
                                disposition='weekdays',
                                elements='str'
                            ),
                            time=dict(
                                type='str',
                                disposition='time'
                            )
                        )
                    ),
                    daily_recurrence=dict(
                        type='dict',
                        disposition='daily_recurrence',
                        options=dict(
                            time=dict(
                                type='str',
                                disposition='time'
                            )
                        )
                    ),
                    hourly_recurrence=dict(
                        type='dict',
                        disposition='hourly_recurrence',
                        options=dict(
                            minute=dict(
                                type='integer',
                                disposition='minute'
                            )
                        )
                    ),
                    time_zone_id=dict(
                        type='str',
                        disposition='time_zone_id'
                    ),
                    notification_settings=dict(
                        type='dict',
                        disposition='notification_settings',
                        options=dict(
                            status=dict(
                                type='str',
                                disposition='status',
                                choices=['Enabled',
                                         'Disabled']
                            ),
                            time_in_minutes=dict(
                                type='integer',
                                disposition='time_in_minutes'
                            ),
                            webhook_url=dict(
                                type='str',
                                disposition='webhook_url'
                            ),
                            email_recipient=dict(
                                type='str',
                                disposition='email_recipient'
                            ),
                            notification_locale=dict(
                                type='str',
                                disposition='notification_locale'
                            )
                        )
                    ),
                    target_resource_id=dict(
                        type='str',
                        disposition='target_resource_id'
                    )
                )
            ),
            last_known_power_state=dict(
                type='str',
                disposition='/last_known_power_state'
            ),
            lab_virtual_machine_creation_parameter_fragment_name=dict(
                type='str',
                disposition='/lab_virtual_machine_creation_parameter_fragment_name'
            ),
            lab_virtual_machine_creation_parameter_fragment_tags=dict(
                type='dictionary',
                disposition='/lab_virtual_machine_creation_parameter_fragment_tags'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.lab_name = None
        self.name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMFormula, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(DevTestLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-15')

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
            response = self.mgmt_client.formulas.create_or_update(resource_group_name=self.resource_group_name,
                                                                  lab_name=self.lab_name,
                                                                  name=self.name,
                                                                  formula=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Formula instance.')
            self.fail('Error creating the Formula instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.formulas.delete(resource_group_name=self.resource_group_name,
                                                        lab_name=self.lab_name,
                                                        name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the Formula instance.')
            self.fail('Error deleting the Formula instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.formulas.get(resource_group_name=self.resource_group_name,
                                                     lab_name=self.lab_name,
                                                     name=self.name,
                                                     expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMFormula()


if __name__ == '__main__':
    main()
