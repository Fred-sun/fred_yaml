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
module: azure_rm_reservationorder_info
version_added: '2.9'
short_description: Get ReservationOrder info.
description:
  - Get info of ReservationOrder.
options:
  reservation_order_id:
    description:
      - Order Id of the reservation
    type: str
  expand:
    description:
      - May be used to expand the planInformation.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: ReservationOrderList
      azure_rm_reservationorder_info: 
        {}
        

    - name: GetReservation
      azure_rm_reservationorder_info: 
        reservation_order_id: a075419f-44cc-497f-b68a-14ee811d48b9
        

    - name: GetReservationWithExpandPayments
      azure_rm_reservationorder_info: 
        reservation_order_id: a075419f-44cc-497f-b68a-14ee811d48b9
        

'''

RETURN = '''
reservation_order:
  description: >-
    A list of dict results where the key is the name of the ReservationOrder and
    the values are the facts for that ReservationOrder.
  returned: always
  type: complex
  contains:
    value:
      description:
        - ''
      returned: always
      type: list
      sample: null
      contains:
        etag:
          description:
            - ''
          returned: always
          type: integer
          sample: null
        id:
          description:
            - Identifier of the reservation
          returned: always
          type: str
          sample: null
        name:
          description:
            - Name of the reservation
          returned: always
          type: str
          sample: null
        type:
          description:
            - Type of resource. "Microsoft.Capacity/reservations"
          returned: always
          type: str
          sample: null
        display_name:
          description:
            - Friendly name for user to easily identified the reservation.
          returned: always
          type: str
          sample: null
        request_date_time:
          description:
            - >-
              This is the DateTime when the reservation was initially requested
              for purchase.
          returned: always
          type: str
          sample: null
        created_date_time:
          description:
            - This is the DateTime when the reservation was created.
          returned: always
          type: str
          sample: null
        expiry_date:
          description:
            - This is the date when the Reservation will expire.
          returned: always
          type: date
          sample: null
        original_quantity:
          description:
            - >-
              Quantity of the SKUs that are part of the Reservation. Must be
              greater than zero.
          returned: always
          type: integer
          sample: null
        term:
          description:
            - Represent the term of Reservation.
          returned: always
          type: str
          sample: null
        provisioning_state:
          description:
            - Current state of the reservation.
          returned: always
          type: str
          sample: null
        billing_plan:
          description:
            - Represent the billing plans.
          returned: always
          type: str
          sample: null
        plan_information:
          description:
            - >-
              Information describing the type of billing plan for this
              reservation.
          returned: always
          type: dict
          sample: null
          contains:
            pricing_currency_total:
              description:
                - Amount of money to be paid for the Order. Tax is not included.
              returned: always
              type: dict
              sample: null
              contains:
                currency_code:
                  description:
                    - >-
                      The ISO 4217 3-letter currency code for the currency used
                      by this purchase record.
                  returned: always
                  type: str
                  sample: null
                amount:
                  description:
                    - ''
                  returned: always
                  type: number
                  sample: null
            start_date:
              description:
                - Date when the billing plan has started.
              returned: always
              type: date
              sample: null
            next_payment_due_date:
              description:
                - >-
                  For recurring billing plans, indicates the date when next
                  payment will be processed. Null when total is paid off.
              returned: always
              type: date
              sample: null
            transactions:
              description:
                - ''
              returned: always
              type: list
              sample: null
              contains:
                due_date:
                  description:
                    - Date when the payment needs to be done.
                  returned: always
                  type: date
                  sample: null
                payment_date:
                  description:
                    - >-
                      Date when the transaction is completed. Is null when it is
                      scheduled.
                  returned: always
                  type: date
                  sample: null
                pricing_currency_total:
                  description:
                    - Amount in pricing currency. Tax not included.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    currency_code:
                      description:
                        - >-
                          The ISO 4217 3-letter currency code for the currency
                          used by this purchase record.
                      returned: always
                      type: str
                      sample: null
                    amount:
                      description:
                        - ''
                      returned: always
                      type: number
                      sample: null
                billing_currency_total:
                  description:
                    - >-
                      Amount charged in Billing currency. Tax not included. Is
                      null for future payments
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    currency_code:
                      description:
                        - >-
                          The ISO 4217 3-letter currency code for the currency
                          used by this purchase record.
                      returned: always
                      type: str
                      sample: null
                    amount:
                      description:
                        - ''
                      returned: always
                      type: number
                      sample: null
                billing_account:
                  description:
                    - Shows the Account that is charged for this payment.
                  returned: always
                  type: str
                  sample: null
                status:
                  description:
                    - >-
                      Describes whether the payment is completed, failed,
                      cancelled or scheduled in the future.
                  returned: always
                  type: str
                  sample: null
                extended_status_info:
                  description:
                    - ''
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    status_code:
                      description:
                        - ''
                      returned: always
                      type: str
                      sample: null
                    message:
                      description:
                        - >-
                          The message giving detailed information about the
                          status code.
                      returned: always
                      type: str
                      sample: null
        reservations:
          description:
            - ''
          returned: always
          type: list
          sample: null
          contains:
            location:
              description:
                - The Azure Region where the reserved resource lives.
              returned: always
              type: str
              sample: null
            etag:
              description:
                - ''
              returned: always
              type: integer
              sample: null
            id:
              description:
                - Identifier of the reservation
              returned: always
              type: str
              sample: null
            name:
              description:
                - Name of the reservation
              returned: always
              type: str
              sample: null
            sku:
              description:
                - ''
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - ''
                  returned: always
                  type: str
                  sample: null
            properties:
              description:
                - ''
              returned: always
              type: dict
              sample: null
              contains:
                reserved_resource_type:
                  description:
                    - The type of the resource that is being reserved.
                  returned: always
                  type: str
                  sample: null
                instance_flexibility:
                  description:
                    - >-
                      Turning this on will apply the reservation discount to
                      other VMs in the same VM size group. Only specify for
                      VirtualMachines reserved resource type.
                  returned: always
                  type: str
                  sample: null
                display_name:
                  description:
                    - Friendly name for user to easily identify the reservation
                  returned: always
                  type: str
                  sample: null
                applied_scopes:
                  description:
                    - >-
                      List of the subscriptions that the benefit will be
                      applied. Do not specify if AppliedScopeType is Shared.
                  returned: always
                  type: list
                  sample: null
                applied_scope_type:
                  description:
                    - Type of the Applied Scope.
                  returned: always
                  type: str
                  sample: null
                quantity:
                  description:
                    - >-
                      Quantity of the SKUs that are part of the Reservation.
                      Must be greater than zero.
                  returned: always
                  type: integer
                  sample: null
                provisioning_state:
                  description:
                    - Current state of the reservation.
                  returned: always
                  type: str
                  sample: null
                effective_date_time:
                  description:
                    - >-
                      DateTime of the Reservation starting when this version is
                      effective from.
                  returned: always
                  type: str
                  sample: null
                last_updated_date_time:
                  description:
                    - DateTime of the last time the Reservation was updated.
                  returned: always
                  type: str
                  sample: null
                expiry_date:
                  description:
                    - This is the date when the Reservation will expire.
                  returned: always
                  type: date
                  sample: null
                sku_description:
                  description:
                    - Description of the SKU in english.
                  returned: always
                  type: str
                  sample: null
                extended_status_info:
                  description:
                    - ''
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    status_code:
                      description:
                        - ''
                      returned: always
                      type: str
                      sample: null
                    message:
                      description:
                        - >-
                          The message giving detailed information about the
                          status code.
                      returned: always
                      type: str
                      sample: null
                billing_plan:
                  description:
                    - Represent the billing plans.
                  returned: always
                  type: str
                  sample: null
                split_properties:
                  description:
                    - ''
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    split_destinations:
                      description:
                        - >-
                          List of destination Resource Id that are created due
                          to split. Format of the resource Id is
                          /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}
                      returned: always
                      type: list
                      sample: null
                    split_source:
                      description:
                        - >-
                          Resource Id of the Reservation from which this is
                          split. Format of the resource Id is
                          /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}
                      returned: always
                      type: str
                      sample: null
                merge_properties:
                  description:
                    - ''
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    merge_destination:
                      description:
                        - >-
                          Reservation Resource Id Created due to the merge.
                          Format of the resource Id is
                          /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}
                      returned: always
                      type: str
                      sample: null
                    merge_sources:
                      description:
                        - >-
                          Resource Ids of the Source Reservation's merged to
                          form this Reservation. Format of the resource Id is
                          /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}
                      returned: always
                      type: list
                      sample: null
                billing_scope_id:
                  description:
                    - >-
                      Subscription that will be charged for purchasing
                      Reservation
                  returned: always
                  type: str
                  sample: null
                renew:
                  description:
                    - >-
                      Setting this to true will automatically purchase a new
                      reservation on the expiration date time.
                  returned: always
                  type: bool
                  sample: null
                renew_source:
                  description:
                    - >-
                      Reservation Id of the reservation from which this
                      reservation is renewed. Format of the resource Id is
                      /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}.
                  returned: always
                  type: str
                  sample: null
                renew_destination:
                  description:
                    - >-
                      Reservation Id of the reservation which is purchased
                      because of renew. Format of the resource Id is
                      /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}.
                  returned: always
                  type: str
                  sample: null
                renew_properties:
                  description:
                    - ''
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    purchase_properties:
                      description:
                        - ''
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        location:
                          description:
                            - >-
                              The Azure Region where the reserved resource
                              lives.
                          returned: always
                          type: str
                          sample: null
                        reserved_resource_type:
                          description:
                            - The type of the resource that is being reserved.
                          returned: always
                          type: str
                          sample: null
                        billing_scope_id:
                          description:
                            - >-
                              Subscription that will be charged for purchasing
                              Reservation
                          returned: always
                          type: str
                          sample: null
                        term:
                          description:
                            - Represent the term of Reservation.
                          returned: always
                          type: str
                          sample: null
                        billing_plan:
                          description:
                            - Represent the billing plans.
                          returned: always
                          type: str
                          sample: null
                        quantity:
                          description:
                            - >-
                              Quantity of the SKUs that are part of the
                              Reservation. Must be greater than zero.
                          returned: always
                          type: integer
                          sample: null
                        display_name:
                          description:
                            - Friendly name of the Reservation
                          returned: always
                          type: str
                          sample: null
                        applied_scope_type:
                          description:
                            - Type of the Applied Scope.
                          returned: always
                          type: str
                          sample: null
                        applied_scopes:
                          description:
                            - >-
                              List of the subscriptions that the benefit will be
                              applied. Do not specify if AppliedScopeType is
                              Shared.
                          returned: always
                          type: list
                          sample: null
                        renew:
                          description:
                            - >-
                              Setting this to true will automatically purchase a
                              new reservation on the expiration date time.
                          returned: always
                          type: bool
                          sample: null
                        instance_flexibility:
                          description:
                            - >-
                              Turning this on will apply the reservation
                              discount to other VMs in the same VM size group.
                              Only specify for VirtualMachines reserved resource
                              type.
                          returned: always
                          type: str
                          sample: null
                        name:
                          description:
                            - ''
                          returned: always
                          type: str
                          sample: null
                    pricing_currency_total:
                      description:
                        - >-
                          Amount that Microsoft uses for record. Used during
                          refund for calculating refund limit. Tax is not
                          included. This is locked price 30 days before expiry.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        currency_code:
                          description:
                            - ''
                          returned: always
                          type: str
                          sample: null
                        amount:
                          description:
                            - ''
                          returned: always
                          type: number
                          sample: null
                    billing_currency_total:
                      description:
                        - >-
                          Currency and amount that customer will be charged in
                          customer's local currency for renewal purchase. Tax is
                          not included.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        currency_code:
                          description:
                            - ''
                          returned: always
                          type: str
                          sample: null
                        amount:
                          description:
                            - ''
                          returned: always
                          type: number
                          sample: null
                term:
                  description:
                    - Represent the term of Reservation.
                  returned: always
                  type: str
                  sample: null
            type:
              description:
                - >-
                  Type of resource.
                  "Microsoft.Capacity/reservationOrders/reservations"
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - Url to get the next page of reservationOrders.
      returned: always
      type: str
      sample: null
    etag:
      description:
        - ''
      returned: always
      type: integer
      sample: null
    id:
      description:
        - Identifier of the reservation
      returned: always
      type: str
      sample: null
    name:
      description:
        - Name of the reservation
      returned: always
      type: str
      sample: null
    type:
      description:
        - Type of resource. "Microsoft.Capacity/reservations"
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - Friendly name for user to easily identified the reservation.
      returned: always
      type: str
      sample: null
    request_date_time:
      description:
        - >-
          This is the DateTime when the reservation was initially requested for
          purchase.
      returned: always
      type: str
      sample: null
    created_date_time:
      description:
        - This is the DateTime when the reservation was created.
      returned: always
      type: str
      sample: null
    expiry_date:
      description:
        - This is the date when the Reservation will expire.
      returned: always
      type: date
      sample: null
    original_quantity:
      description:
        - >-
          Quantity of the SKUs that are part of the Reservation. Must be greater
          than zero.
      returned: always
      type: integer
      sample: null
    term:
      description:
        - Represent the term of Reservation.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - Current state of the reservation.
      returned: always
      type: str
      sample: null
    billing_plan:
      description:
        - Represent the billing plans.
      returned: always
      type: str
      sample: null
    plan_information:
      description:
        - Information describing the type of billing plan for this reservation.
      returned: always
      type: dict
      sample: null
      contains:
        pricing_currency_total:
          description:
            - Amount of money to be paid for the Order. Tax is not included.
          returned: always
          type: dict
          sample: null
          contains:
            currency_code:
              description:
                - >-
                  The ISO 4217 3-letter currency code for the currency used by
                  this purchase record.
              returned: always
              type: str
              sample: null
            amount:
              description:
                - ''
              returned: always
              type: number
              sample: null
        start_date:
          description:
            - Date when the billing plan has started.
          returned: always
          type: date
          sample: null
        next_payment_due_date:
          description:
            - >-
              For recurring billing plans, indicates the date when next payment
              will be processed. Null when total is paid off.
          returned: always
          type: date
          sample: null
        transactions:
          description:
            - ''
          returned: always
          type: list
          sample: null
          contains:
            due_date:
              description:
                - Date when the payment needs to be done.
              returned: always
              type: date
              sample: null
            payment_date:
              description:
                - >-
                  Date when the transaction is completed. Is null when it is
                  scheduled.
              returned: always
              type: date
              sample: null
            pricing_currency_total:
              description:
                - Amount in pricing currency. Tax not included.
              returned: always
              type: dict
              sample: null
              contains:
                currency_code:
                  description:
                    - >-
                      The ISO 4217 3-letter currency code for the currency used
                      by this purchase record.
                  returned: always
                  type: str
                  sample: null
                amount:
                  description:
                    - ''
                  returned: always
                  type: number
                  sample: null
            billing_currency_total:
              description:
                - >-
                  Amount charged in Billing currency. Tax not included. Is null
                  for future payments
              returned: always
              type: dict
              sample: null
              contains:
                currency_code:
                  description:
                    - >-
                      The ISO 4217 3-letter currency code for the currency used
                      by this purchase record.
                  returned: always
                  type: str
                  sample: null
                amount:
                  description:
                    - ''
                  returned: always
                  type: number
                  sample: null
            billing_account:
              description:
                - Shows the Account that is charged for this payment.
              returned: always
              type: str
              sample: null
            status:
              description:
                - >-
                  Describes whether the payment is completed, failed, cancelled
                  or scheduled in the future.
              returned: always
              type: str
              sample: null
            extended_status_info:
              description:
                - ''
              returned: always
              type: dict
              sample: null
              contains:
                status_code:
                  description:
                    - ''
                  returned: always
                  type: str
                  sample: null
                message:
                  description:
                    - >-
                      The message giving detailed information about the status
                      code.
                  returned: always
                  type: str
                  sample: null
    reservations:
      description:
        - ''
      returned: always
      type: list
      sample: null
      contains:
        location:
          description:
            - The Azure Region where the reserved resource lives.
          returned: always
          type: str
          sample: null
        etag:
          description:
            - ''
          returned: always
          type: integer
          sample: null
        id:
          description:
            - Identifier of the reservation
          returned: always
          type: str
          sample: null
        name:
          description:
            - Name of the reservation
          returned: always
          type: str
          sample: null
        sku:
          description:
            - ''
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - ''
              returned: always
              type: str
              sample: null
        properties:
          description:
            - ''
          returned: always
          type: dict
          sample: null
          contains:
            reserved_resource_type:
              description:
                - The type of the resource that is being reserved.
              returned: always
              type: str
              sample: null
            instance_flexibility:
              description:
                - >-
                  Turning this on will apply the reservation discount to other
                  VMs in the same VM size group. Only specify for
                  VirtualMachines reserved resource type.
              returned: always
              type: str
              sample: null
            display_name:
              description:
                - Friendly name for user to easily identify the reservation
              returned: always
              type: str
              sample: null
            applied_scopes:
              description:
                - >-
                  List of the subscriptions that the benefit will be applied. Do
                  not specify if AppliedScopeType is Shared.
              returned: always
              type: list
              sample: null
            applied_scope_type:
              description:
                - Type of the Applied Scope.
              returned: always
              type: str
              sample: null
            quantity:
              description:
                - >-
                  Quantity of the SKUs that are part of the Reservation. Must be
                  greater than zero.
              returned: always
              type: integer
              sample: null
            provisioning_state:
              description:
                - Current state of the reservation.
              returned: always
              type: str
              sample: null
            effective_date_time:
              description:
                - >-
                  DateTime of the Reservation starting when this version is
                  effective from.
              returned: always
              type: str
              sample: null
            last_updated_date_time:
              description:
                - DateTime of the last time the Reservation was updated.
              returned: always
              type: str
              sample: null
            expiry_date:
              description:
                - This is the date when the Reservation will expire.
              returned: always
              type: date
              sample: null
            sku_description:
              description:
                - Description of the SKU in english.
              returned: always
              type: str
              sample: null
            extended_status_info:
              description:
                - ''
              returned: always
              type: dict
              sample: null
              contains:
                status_code:
                  description:
                    - ''
                  returned: always
                  type: str
                  sample: null
                message:
                  description:
                    - >-
                      The message giving detailed information about the status
                      code.
                  returned: always
                  type: str
                  sample: null
            billing_plan:
              description:
                - Represent the billing plans.
              returned: always
              type: str
              sample: null
            split_properties:
              description:
                - ''
              returned: always
              type: dict
              sample: null
              contains:
                split_destinations:
                  description:
                    - >-
                      List of destination Resource Id that are created due to
                      split. Format of the resource Id is
                      /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}
                  returned: always
                  type: list
                  sample: null
                split_source:
                  description:
                    - >-
                      Resource Id of the Reservation from which this is split.
                      Format of the resource Id is
                      /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}
                  returned: always
                  type: str
                  sample: null
            merge_properties:
              description:
                - ''
              returned: always
              type: dict
              sample: null
              contains:
                merge_destination:
                  description:
                    - >-
                      Reservation Resource Id Created due to the merge. Format
                      of the resource Id is
                      /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}
                  returned: always
                  type: str
                  sample: null
                merge_sources:
                  description:
                    - >-
                      Resource Ids of the Source Reservation's merged to form
                      this Reservation. Format of the resource Id is
                      /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}
                  returned: always
                  type: list
                  sample: null
            billing_scope_id:
              description:
                - Subscription that will be charged for purchasing Reservation
              returned: always
              type: str
              sample: null
            renew:
              description:
                - >-
                  Setting this to true will automatically purchase a new
                  reservation on the expiration date time.
              returned: always
              type: bool
              sample: null
            renew_source:
              description:
                - >-
                  Reservation Id of the reservation from which this reservation
                  is renewed. Format of the resource Id is
                  /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}.
              returned: always
              type: str
              sample: null
            renew_destination:
              description:
                - >-
                  Reservation Id of the reservation which is purchased because
                  of renew. Format of the resource Id is
                  /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}.
              returned: always
              type: str
              sample: null
            renew_properties:
              description:
                - ''
              returned: always
              type: dict
              sample: null
              contains:
                purchase_properties:
                  description:
                    - ''
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    location:
                      description:
                        - The Azure Region where the reserved resource lives.
                      returned: always
                      type: str
                      sample: null
                    reserved_resource_type:
                      description:
                        - The type of the resource that is being reserved.
                      returned: always
                      type: str
                      sample: null
                    billing_scope_id:
                      description:
                        - >-
                          Subscription that will be charged for purchasing
                          Reservation
                      returned: always
                      type: str
                      sample: null
                    term:
                      description:
                        - Represent the term of Reservation.
                      returned: always
                      type: str
                      sample: null
                    billing_plan:
                      description:
                        - Represent the billing plans.
                      returned: always
                      type: str
                      sample: null
                    quantity:
                      description:
                        - >-
                          Quantity of the SKUs that are part of the Reservation.
                          Must be greater than zero.
                      returned: always
                      type: integer
                      sample: null
                    display_name:
                      description:
                        - Friendly name of the Reservation
                      returned: always
                      type: str
                      sample: null
                    applied_scope_type:
                      description:
                        - Type of the Applied Scope.
                      returned: always
                      type: str
                      sample: null
                    applied_scopes:
                      description:
                        - >-
                          List of the subscriptions that the benefit will be
                          applied. Do not specify if AppliedScopeType is Shared.
                      returned: always
                      type: list
                      sample: null
                    renew:
                      description:
                        - >-
                          Setting this to true will automatically purchase a new
                          reservation on the expiration date time.
                      returned: always
                      type: bool
                      sample: null
                    instance_flexibility:
                      description:
                        - >-
                          Turning this on will apply the reservation discount to
                          other VMs in the same VM size group. Only specify for
                          VirtualMachines reserved resource type.
                      returned: always
                      type: str
                      sample: null
                    name:
                      description:
                        - ''
                      returned: always
                      type: str
                      sample: null
                pricing_currency_total:
                  description:
                    - >-
                      Amount that Microsoft uses for record. Used during refund
                      for calculating refund limit. Tax is not included. This is
                      locked price 30 days before expiry.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    currency_code:
                      description:
                        - ''
                      returned: always
                      type: str
                      sample: null
                    amount:
                      description:
                        - ''
                      returned: always
                      type: number
                      sample: null
                billing_currency_total:
                  description:
                    - >-
                      Currency and amount that customer will be charged in
                      customer's local currency for renewal purchase. Tax is not
                      included.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    currency_code:
                      description:
                        - ''
                      returned: always
                      type: str
                      sample: null
                    amount:
                      description:
                        - ''
                      returned: always
                      type: number
                      sample: null
            term:
              description:
                - Represent the term of Reservation.
              returned: always
              type: str
              sample: null
        type:
          description:
            - >-
              Type of resource.
              "Microsoft.Capacity/reservationOrders/reservations"
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
    from azure.mgmt.azure import Azure Reservation API
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMReservationOrderInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            reservation_order_id=dict(
                type='str'
            ),
            expand=dict(
                type='str'
            )
        )

        self.reservation_order_id = None
        self.expand = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMReservationOrderInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Azure Reservation API,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-04-01')

        if (self.reservation_order_id is not None):
            self.results['reservation_order'] = self.format_item(self.get())
        else:
            self.results['reservation_order'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.reservation_order.get(reservation_order_id=self.reservation_order_id,
                                                              expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.reservation_order.list()
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
    AzureRMReservationOrderInfo()


if __name__ == '__main__':
    main()
