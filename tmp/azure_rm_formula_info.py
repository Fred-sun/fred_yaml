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
module: azure_rm_formula_info
version_added: '2.9'
short_description: Get Formula info.
description:
  - Get info of Formula.
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
  expand:
    description:
      - 'Specify the $expand query. Example: ''properties($select=description)'''
    required: true
    type: str
  filter:
    description:
      - >-
        The filter to apply to the operation. Example:
        '$filter=contains(name,'myName')
    type: str
  top:
    description:
      - >-
        The maximum number of resources to return from the operation. Example:
        '$top=10'
    type: integer
  orderby:
    description:
      - >-
        The ordering expression for the results, using OData notation. Example:
        '$orderby=name desc'
    type: str
  name:
    description:
      - The name of the formula.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
formulas:
  description: >-
    A list of dict results where the key is the name of the Formula and the
    values are the facts for that Formula.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Results of the list operation.
      returned: always
      type: list
      sample: null
      contains:
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
            - >-
              The resource identifier (Microsoft.Compute) of the virtual
              machine.
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
            - >-
              Indicates whether this virtual machine uses an SSH key for
              authentication.
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
              Indicates whether the virtual machine is to be created without a
              public IP address.
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
                - >-
                  The time that the artifact starts to install on the virtual
                  machine.
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
                - >-
                  The total count of the artifacts that were successfully
                  applied.
              returned: always
              type: integer
              sample: null
            total_artifacts:
              description:
                - >-
                  The total count of the artifacts that were tentatively
                  applied.
              returned: always
              type: integer
              sample: null
        gallery_image_reference:
          description:
            - >-
              The Microsoft Azure Marketplace image reference of the virtual
              machine.
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
                  The RdpAuthority property is a server DNS host name or IP
                  address followed by the service port number for RDP (Remote
                  Desktop Protocol).
              returned: always
              type: str
              sample: null
            ssh_authority:
              description:
                - >-
                  The SshAuthority property is a server DNS host name or IP
                  address followed by the service port number for SSH.
              returned: always
              type: str
              sample: null
            shared_public_ip_address_configuration:
              description:
                - >-
                  The configuration for sharing a public IP address across
                  multiple virtual machines.
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
                          The external endpoint port of the inbound connection.
                          Possible values range between 1 and 65535, inclusive.
                          If unspecified, a value will be allocated
                          automatically.
                      returned: always
                      type: integer
                      sample: null
                    backend_port:
                      description:
                        - >-
                          The port to which the external traffic will be
                          redirected.
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
            - >-
              Indicates whether another user can take ownership of the virtual
              machine
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
            - >-
              Tells source of creation of lab virtual machine. Output property
              only.
          returned: always
          type: str
          sample: null
        environment_id:
          description:
            - >-
              The resource ID of the environment that contains this virtual
              machine, if any.
          returned: always
          type: str
          sample: null
        data_disk_parameters:
          description:
            - >-
              New or existing data disks to attach to the virtual machine after
              creation
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
                - >-
                  Specifies the existing lab disk id to attach to virtual
                  machine.
              returned: always
              type: str
              sample: null
            host_caching:
              description:
                - >-
                  Caching option for a data disk (i.e. None, ReadOnly,
                  ReadWrite).
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
                  If the schedule will occur only some days of the week, specify
                  the weekly recurrence.
              returned: always
              type: dict
              sample: null
              contains:
                weekdays:
                  description:
                    - >-
                      The days of the week for which the schedule is set (e.g.
                      Sunday, Monday, Tuesday, etc.).
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
                  If the schedule will occur once each day of the week, specify
                  the daily recurrence.
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
                  If the schedule will occur multiple times a day, specify the
                  hourly recurrence.
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
                      If notifications are enabled for this schedule (i.e.
                      Enabled, Disabled).
                  returned: always
                  type: str
                  sample: null
                time_in_minutes:
                  description:
                    - >-
                      Time in minutes before event at which notification will be
                      sent.
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
                      The email recipient to send notifications to (can be a
                      list of semi-colon separated email addresses).
                  returned: always
                  type: str
                  sample: null
                notification_locale:
                  description:
                    - >-
                      The locale to use when sending a notification (fallback
                      for unsupported languages is EN).
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
    next_link:
      description:
        - Link for next set of results.
      returned: always
      type: str
      sample: null
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
        - >-
          Indicates whether this virtual machine uses an SSH key for
          authentication.
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
          Indicates whether the virtual machine is to be created without a
          public IP address.
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
            - >-
              The time that the artifact starts to install on the virtual
              machine.
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
        - >-
          The Microsoft Azure Marketplace image reference of the virtual
          machine.
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
              followed by the service port number for RDP (Remote Desktop
              Protocol).
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
                      The external endpoint port of the inbound connection.
                      Possible values range between 1 and 65535, inclusive. If
                      unspecified, a value will be allocated automatically.
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
        - >-
          Indicates whether another user can take ownership of the virtual
          machine
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
          The resource ID of the environment that contains this virtual machine,
          if any.
      returned: always
      type: str
      sample: null
    data_disk_parameters:
      description:
        - >-
          New or existing data disks to attach to the virtual machine after
          creation
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
                  The days of the week for which the schedule is set (e.g.
                  Sunday, Monday, Tuesday, etc.).
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
              If the schedule will occur multiple times a day, specify the
              hourly recurrence.
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
                - >-
                  Time in minutes before event at which notification will be
                  sent.
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
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.dev import DevTestLabsClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMFormulaInfo(AzureRMModuleBase):
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
            expand=dict(
                type='str',
                required=True
            ),
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            orderby=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.lab_name = None
        self.expand = None
        self.filter = None
        self.top = None
        self.orderby = None
        self.name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-09-15'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMFormulaInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(DevTestLabsClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-15')

        if (self.resource_group_name is not None and
            self.lab_name is not None and
            self.name is not None):
            self.results['formulas'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.lab_name is not None):
            self.results['formulas'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.formulas.get(resource_group_name=self.resource_group_name,
                                                     lab_name=self.lab_name,
                                                     name=self.name,
                                                     expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.formulas.list(resource_group_name=self.resource_group_name,
                                                      lab_name=self.lab_name,
                                                      expand=self.expand,
                                                      filter=self.filter,
                                                      top=self.top,
                                                      orderby=self.orderby)
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
    AzureRMFormulaInfo()


if __name__ == '__main__':
    main()
