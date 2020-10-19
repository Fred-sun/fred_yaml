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
module: azure_rm_attestationprovider
version_added: '2.9'
short_description: Manage Azure AttestationProvider instance.
description:
  - 'Create, update and delete instance of Azure AttestationProvider.'
options:
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  provider_name:
    description:
      - Name of the attestation service instance
    required: true
    type: str
  location:
    description:
      - >-
        The supported Azure location where the attestation service instance
        should be created.
    type: str
  attestation_policy:
    description:
      - Name of attestation policy.
    type: str
  keys:
    description:
      - The value of the "keys" parameter is an array of JWK values.  By
      - 'default, the order of the JWK values within the array does not imply'
      - 'an order of preference among them, although applications of JWK Sets'
      - 'can choose to assign a meaning to the order for their purposes, if'
      - desired.
    type: list
    suboptions:
      alg:
        description:
          - >-
            The "alg" (algorithm) parameter identifies the algorithm intended
            for
          - >-
            use with the key.  The values used should either be registered in
            the
          - IANA "JSON Web Signature and Encryption Algorithms" registry
          - 'established by [JWA] or be a value that contains a Collision-'
          - Resistant Name.
        required: true
        type: str
      crv:
        description:
          - The "crv" (curve) parameter identifies the curve type
        type: str
      d:
        description:
          - RSA private exponent or ECC private key
        type: str
      dp:
        description:
          - RSA Private Key Parameter
        type: str
      dq:
        description:
          - RSA Private Key Parameter
        type: str
      e:
        description:
          - 'RSA public exponent, in Base64'
        type: str
      k:
        description:
          - Symmetric key
        type: str
      kid:
        description:
          - The "kid" (key ID) parameter is used to match a specific key.  This
          - >-
            is used, for instance, to choose among a set of keys within a JWK
            Set
          - during key rollover.  The structure of the "kid" value is
          - 'unspecified.  When "kid" values are used within a JWK Set, different'
          - keys within the JWK Set SHOULD use distinct "kid" values.  (One
          - example in which different keys might use the same "kid" value is if
          - they have different "kty" (key type) values but are considered to be
          - equivalent alternatives by the application using them.)  The "kid"
          - value is a case-sensitive string.
        required: true
        type: str
      kty:
        description:
          - >-
            The "kty" (key type) parameter identifies the cryptographic
            algorithm
          - 'family used with the key, such as "RSA" or "EC". "kty" values should'
          - either be registered in the IANA "JSON Web Key Types" registry
          - 'established by [JWA] or be a value that contains a Collision-'
          - Resistant Name.  The "kty" value is a case-sensitive string.
        required: true
        type: str
      'n':
        description:
          - 'RSA modulus, in Base64'
        type: str
      p:
        description:
          - RSA secret prime
        type: str
      q:
        description:
          - 'RSA secret prime, with p < q'
        type: str
      qi:
        description:
          - RSA Private Key Parameter
        type: str
      use:
        description:
          - Use ("public key use") identifies the intended use of
          - the public key. The "use" parameter is employed to indicate whether
          - a public key is used for encrypting data or verifying the signature
          - >-
            on data. Values are commonly "sig" (signature) or "enc"
            (encryption).
        required: true
        type: str
      x:
        description:
          - X coordinate for the Elliptic Curve point
        type: str
      x5c:
        description:
          - >-
            The "x5c" (X.509 certificate chain) parameter contains a chain of
            one
          - 'or more PKIX certificates [RFC5280].  The certificate chain is'
          - represented as a JSON array of certificate value strings.  Each
          - 'string in the array is a base64-encoded (Section 4 of [RFC4648] --'
          - 'not base64url-encoded) DER [ITU.X690.1994] PKIX certificate value.'
          - The PKIX certificate containing the key value MUST be the first
          - certificate.
        type: list
      'y':
        description:
          - Y coordinate for the Elliptic Curve point
        type: str
  state:
    description:
      - Assert the state of the AttestationProvider.
      - >-
        Use C(present) to create or update an AttestationProvider and C(absent)
        to delete it.
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
    - name: AttestationProviders_Create
      azure_rm_attestationprovider: 
        provider_name: myattestationprovider
        resource_group_name: MyResourceGroup
        

    - name: AttestationProviders_Update
      azure_rm_attestationprovider: 
        provider_name: myattestationprovider
        resource_group_name: MyResourceGroup
        

    - name: AttestationProviders_Delete
      azure_rm_attestationprovider: 
        provider_name: myattestationprovider
        resource_group_name: sample-resource-group
        

'''

RETURN = '''
tags:
  description:
    - Resource tags.
  returned: always
  type: dictionary
  sample: null
location:
  description:
    - The geo-location where the resource lives
  returned: always
  type: str
  sample: null
trust_model:
  description:
    - Trust model for the attestation service instance.
  returned: always
  type: str
  sample: null
status:
  description:
    - Status of attestation service.
  returned: always
  type: str
  sample: null
attest_uri:
  description:
    - Gets the uri of attestation service
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
    from azure.mgmt.attestation import AttestationManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMAttestationProvider(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            provider_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            attestation_policy=dict(
                type='str',
                disposition='/attestation_policy'
            ),
            keys=dict(
                type='list',
                disposition='/keys',
                elements='dict',
                options=dict(
                    alg=dict(
                        type='str',
                        disposition='alg',
                        required=True
                    ),
                    crv=dict(
                        type='str',
                        disposition='crv'
                    ),
                    d=dict(
                        type='str',
                        disposition='d'
                    ),
                    dp=dict(
                        type='str',
                        disposition='dp'
                    ),
                    dq=dict(
                        type='str',
                        disposition='dq'
                    ),
                    e=dict(
                        type='str',
                        disposition='e'
                    ),
                    k=dict(
                        type='str',
                        disposition='k'
                    ),
                    kid=dict(
                        type='str',
                        disposition='kid',
                        required=True
                    ),
                    kty=dict(
                        type='str',
                        disposition='kty',
                        required=True
                    ),
                    n=dict(
                        type='str',
                        disposition='n'
                    ),
                    p=dict(
                        type='str',
                        disposition='p'
                    ),
                    q=dict(
                        type='str',
                        disposition='q'
                    ),
                    qi=dict(
                        type='str',
                        disposition='qi'
                    ),
                    use=dict(
                        type='str',
                        disposition='use',
                        required=True
                    ),
                    x=dict(
                        type='str',
                        disposition='x'
                    ),
                    x5c=dict(
                        type='list',
                        disposition='x5c',
                        elements='str'
                    ),
                    y=dict(
                        type='str',
                        disposition='y'
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
        self.provider_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAttestationProvider, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(AttestationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2018-09-01-preview')

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
                response = self.mgmt_client.attestation_providers.create(resource_group_name=self.resource_group_name,
                                                                         provider_name=self.provider_name,
                                                                         creation_params=self.body)
            else:
                response = self.mgmt_client.attestation_providers.update(resource_group_name=self.resource_group_name,
                                                                         provider_name=self.provider_name,
                                                                         update_params=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the AttestationProvider instance.')
            self.fail('Error creating the AttestationProvider instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.attestation_providers.delete(resource_group_name=self.resource_group_name,
                                                                     provider_name=self.provider_name)
        except CloudError as e:
            self.log('Error attempting to delete the AttestationProvider instance.')
            self.fail('Error deleting the AttestationProvider instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.attestation_providers.get(resource_group_name=self.resource_group_name,
                                                                  provider_name=self.provider_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAttestationProvider()


if __name__ == '__main__':
    main()
