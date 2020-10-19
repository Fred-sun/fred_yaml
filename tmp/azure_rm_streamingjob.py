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
module: azure_rm_streamingjob
version_added: '2.9'
short_description: Manage Azure StreamingJob instance.
description:
  - 'Create, update and delete instance of Azure StreamingJob.'
options:
  if_match:
    description:
      - >-
        The ETag of the streaming job. Omit this value to always overwrite the
        current record set. Specify the last-seen ETag value to prevent
        accidentally overwriting concurrent changes.
    type: str
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    required: true
    type: str
  job_name:
    description:
      - The name of the streaming job.
    required: true
    type: str
  location:
    description:
      - The geo-location where the resource lives
    type: str
  identity:
    description:
      - >-
        Describes the system-assigned managed identity assigned to this job that
        can be used to authenticate with inputs and outputs.
    type: dict
    suboptions:
      tenant_id:
        description:
          - undefined
        type: str
      principal_id:
        description:
          - undefined
        type: str
      type:
        description:
          - undefined
        type: str
  sku:
    description:
      - >-
        Describes the SKU of the streaming job. Required on PUT
        (CreateOrReplace) requests.
    type: dict
    suboptions:
      name:
        description:
          - The name of the SKU. Required on PUT (CreateOrReplace) requests.
        type: str
        choices:
          - Standard
  job_type:
    description:
      - Describes the type of the job. Valid modes are `Cloud` and 'Edge'.
    type: str
    choices:
      - Cloud
      - Edge
  output_start_mode:
    description:
      - >-
        This property should only be utilized when it is desired that the job be
        started immediately upon creation. Value may be JobStartTime,
        CustomTime, or LastOutputEventTime to indicate whether the starting
        point of the output event stream should start whenever the job is
        started, start at a custom user time stamp specified via the
        outputStartTime property, or start from the last event output time.
    type: str
    choices:
      - JobStartTime
      - CustomTime
      - LastOutputEventTime
  output_start_time:
    description:
      - >-
        Value is either an ISO-8601 formatted time stamp that indicates the
        starting point of the output event stream, or null to indicate that the
        output event stream will start whenever the streaming job is started.
        This property must have a value if outputStartMode is set to CustomTime.
    type: str
  events_out_of_order_policy:
    description:
      - >-
        Indicates the policy to apply to events that arrive out of order in the
        input event stream.
    type: str
    choices:
      - Adjust
      - Drop
  output_error_policy:
    description:
      - >-
        Indicates the policy to apply to events that arrive at the output and
        cannot be written to the external storage due to being malformed
        (missing column values, column values of wrong type or size).
    type: str
    choices:
      - Stop
      - Drop
  events_out_of_order_max_delay_in_seconds:
    description:
      - >-
        The maximum tolerable delay in seconds where out-of-order events can be
        adjusted to be back in order.
    type: integer
  events_late_arrival_max_delay_in_seconds:
    description:
      - >-
        The maximum tolerable delay in seconds where events arriving late could
        be included.  Supported range is -1 to 1814399 (20.23:59:59 days) and -1
        is used to specify wait indefinitely. If the property is absent, it is
        interpreted to have a value of -1.
    type: integer
  data_locale:
    description:
      - >-
        The data locale of the stream analytics job. Value should be the name of
        a supported .NET Culture from the set
        https://msdn.microsoft.com/en-us/library/system.globalization.culturetypes(v=vs.110).aspx.
        Defaults to 'en-US' if none specified.
    type: str
  compatibility_level:
    description:
      - Controls certain runtime behaviors of the streaming job.
    type: str
    choices:
      - '1.0'
  inputs:
    description:
      - >-
        A list of one or more inputs to the streaming job. The name property for
        each input is required when specifying this property in a PUT request.
        This property cannot be modify via a PATCH operation. You must use the
        PATCH API available for the individual input.
    type: list
    suboptions:
      properties:
        description:
          - >-
            The properties that are associated with an input. Required on PUT
            (CreateOrReplace) requests.
        type: dict
        suboptions:
          type:
            description:
              - >-
                Indicates whether the input is a source of reference data or
                stream data. Required on PUT (CreateOrReplace) requests.
            required: true
            type: str
          serialization:
            description:
              - >-
                Describes how data from an input is serialized or how data is
                serialized when written to an output. Required on PUT
                (CreateOrReplace) requests.
            type: dict
            suboptions:
              type:
                description:
                  - >-
                    Indicates the type of serialization that the input or output
                    uses. Required on PUT (CreateOrReplace) requests.
                required: true
                type: str
                choices:
                  - Csv
                  - Avro
                  - Json
                  - CustomClr
                  - Parquet
          diagnostics:
            description:
              - >-
                Describes conditions applicable to the Input, Output, or the job
                overall, that warrant customer attention.
            type: dict
            suboptions:
              conditions:
                description:
                  - >-
                    A collection of zero or more conditions applicable to the
                    resource, or to the job overall, that warrant customer
                    attention.
                type: list
                suboptions:
                  since:
                    description:
                      - >-
                        The UTC timestamp of when the condition started.
                        Customers should be able to find a corresponding event
                        in the ops log around this time.
                    type: str
                  code:
                    description:
                      - The opaque diagnostic code.
                    type: str
                  message:
                    description:
                      - >-
                        The human-readable message describing the condition in
                        detail. Localized in the Accept-Language of the client
                        request.
                    type: str
          etag:
            description:
              - >-
                The current entity tag for the input. This is an opaque string.
                You can use it to detect whether the resource has changed
                between requests. You can also use it in the If-Match or
                If-None-Match headers for write operations for optimistic
                concurrency.
            type: str
          compression:
            description:
              - Describes how input data is compressed
            type: dict
            suboptions:
              type:
                description:
                  - undefined
                required: true
                type: str
          partition_key:
            description:
              - >-
                partitionKey Describes a key in the input data which is used for
                partitioning the input data
            type: str
  transformation:
    description:
      - >-
        Indicates the query and the number of streaming units to use for the
        streaming job. The name property of the transformation is required when
        specifying this property in a PUT request. This property cannot be
        modify via a PATCH operation. You must use the PATCH API available for
        the individual transformation.
    type: dict
    suboptions:
      streaming_units:
        description:
          - Specifies the number of streaming units that the streaming job uses.
        type: integer
      query:
        description:
          - >-
            Specifies the query that will be run in the streaming job. You can
            learn more about the Stream Analytics Query Language (SAQL) here:
            https://msdn.microsoft.com/library/azure/dn834998 . Required on PUT
            (CreateOrReplace) requests.
        type: str
      etag:
        description:
          - >-
            The current entity tag for the transformation. This is an opaque
            string. You can use it to detect whether the resource has changed
            between requests. You can also use it in the If-Match or
            If-None-Match headers for write operations for optimistic
            concurrency.
        type: str
  outputs:
    description:
      - >-
        A list of one or more outputs for the streaming job. The name property
        for each output is required when specifying this property in a PUT
        request. This property cannot be modify via a PATCH operation. You must
        use the PATCH API available for the individual output.
    type: list
    suboptions:
      datasource:
        description:
          - >-
            Describes the data source that output will be written to. Required
            on PUT (CreateOrReplace) requests.
        type: dict
        suboptions:
          type:
            description:
              - >-
                Indicates the type of data source output will be written to.
                Required on PUT (CreateOrReplace) requests.
            required: true
            type: str
      time_window:
        description:
          - undefined
        type: str
      size_window:
        description:
          - undefined
        type: number
      serialization:
        description:
          - >-
            Describes how data from an input is serialized or how data is
            serialized when written to an output. Required on PUT
            (CreateOrReplace) requests.
        type: dict
        suboptions:
          type:
            description:
              - >-
                Indicates the type of serialization that the input or output
                uses. Required on PUT (CreateOrReplace) requests.
            required: true
            type: str
            choices:
              - Csv
              - Avro
              - Json
              - CustomClr
              - Parquet
      diagnostics:
        description:
          - >-
            Describes conditions applicable to the Input, Output, or the job
            overall, that warrant customer attention.
        type: dict
        suboptions:
          conditions:
            description:
              - >-
                A collection of zero or more conditions applicable to the
                resource, or to the job overall, that warrant customer
                attention.
            type: list
            suboptions:
              since:
                description:
                  - >-
                    The UTC timestamp of when the condition started. Customers
                    should be able to find a corresponding event in the ops log
                    around this time.
                type: str
              code:
                description:
                  - The opaque diagnostic code.
                type: str
              message:
                description:
                  - >-
                    The human-readable message describing the condition in
                    detail. Localized in the Accept-Language of the client
                    request.
                type: str
      etag:
        description:
          - >-
            The current entity tag for the output. This is an opaque string. You
            can use it to detect whether the resource has changed between
            requests. You can also use it in the If-Match or If-None-Match
            headers for write operations for optimistic concurrency.
        type: str
  functions:
    description:
      - >-
        A list of one or more functions for the streaming job. The name property
        for each function is required when specifying this property in a PUT
        request. This property cannot be modify via a PATCH operation. You must
        use the PATCH API available for the individual transformation.
    type: list
    suboptions:
      properties:
        description:
          - The properties that are associated with a function.
        type: dict
        suboptions:
          type:
            description:
              - Indicates the type of function.
            required: true
            type: str
          etag:
            description:
              - >-
                The current entity tag for the function. This is an opaque
                string. You can use it to detect whether the resource has
                changed between requests. You can also use it in the If-Match or
                If-None-Match headers for write operations for optimistic
                concurrency.
            type: str
          inputs:
            description:
              - undefined
            type: list
            suboptions:
              data_type:
                description:
                  - >-
                    The (Azure Stream Analytics supported) data type of the
                    function input parameter. A list of valid Azure Stream
                    Analytics data types are described at
                    https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
                type: str
              is_configuration_parameter:
                description:
                  - >-
                    A flag indicating if the parameter is a configuration
                    parameter. True if this input parameter is expected to be a
                    constant. Default is false.
                type: bool
          output:
            description:
              - Describes the output of a function.
            type: dict
            suboptions:
              data_type:
                description:
                  - >-
                    The (Azure Stream Analytics supported) data type of the
                    function output. A list of valid Azure Stream Analytics data
                    types are described at
                    https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
                type: str
          binding:
            description:
              - >-
                The physical binding of the function. For example, in the Azure
                Machine Learning web service’s case, this describes the
                endpoint.
            type: dict
            suboptions:
              type:
                description:
                  - Indicates the function binding type.
                required: true
                type: str
  job_storage_account:
    description:
      - >-
        The properties that are associated with an Azure Storage account with
        MSI
    type: dict
    suboptions:
      authentication_mode:
        description:
          - Authentication Mode.
        type: str
        choices:
          - Msi
          - UserToken
          - ConnectionString
  externals:
    description:
      - The storage account where the custom code artifacts are located.
    type: dict
    suboptions:
      storage_account:
        description:
          - The properties that are associated with an Azure Storage account
        type: dict
        suboptions:
          account_name:
            description:
              - >-
                The name of the Azure Storage account. Required on PUT
                (CreateOrReplace) requests.
            type: str
          account_key:
            description:
              - >-
                The account key for the Azure Storage account. Required on PUT
                (CreateOrReplace) requests.
            type: str
      container:
        description:
          - undefined
        type: str
      path:
        description:
          - undefined
        type: str
  cluster:
    description:
      - The cluster which streaming jobs will run on.
    type: dict
    suboptions:
      id:
        description:
          - The resource id of cluster.
        type: str
  expand:
    description:
      - >-
        The $expand OData query parameter. This is a comma-separated list of
        additional streaming job properties to include in the response, beyond
        the default set returned when this parameter is absent. The default set
        is all streaming job properties other than 'inputs', 'transformation',
        'outputs', and 'functions'.
    type: str
  state:
    description:
      - Assert the state of the StreamingJob.
      - >-
        Use C(present) to create or update an StreamingJob and C(absent) to
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
    - name: Update a streaming job
      azure_rm_streamingjob: 
        job_name: sj59
        resource_group_name: sjrg
        

    - name: Delete a streaming job
      azure_rm_streamingjob: 
        job_name: sj59
        resource_group_name: sjrg
        

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
identity:
  description:
    - >-
      Describes the system-assigned managed identity assigned to this job that
      can be used to authenticate with inputs and outputs.
  returned: always
  type: dict
  sample: null
  contains:
    tenant_id:
      description:
        - ''
      returned: always
      type: str
      sample: null
    principal_id:
      description:
        - ''
      returned: always
      type: str
      sample: null
    type:
      description:
        - ''
      returned: always
      type: str
      sample: null
sku:
  description:
    - >-
      Describes the SKU of the streaming job. Required on PUT (CreateOrReplace)
      requests.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - The name of the SKU. Required on PUT (CreateOrReplace) requests.
      returned: always
      type: str
      sample: null
job_id:
  description:
    - >-
      A GUID uniquely identifying the streaming job. This GUID is generated upon
      creation of the streaming job.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - Describes the provisioning status of the streaming job.
  returned: always
  type: str
  sample: null
job_state:
  description:
    - Describes the state of the streaming job.
  returned: always
  type: str
  sample: null
job_type:
  description:
    - Describes the type of the job. Valid modes are `Cloud` and 'Edge'.
  returned: always
  type: str
  sample: null
output_start_mode:
  description:
    - >-
      This property should only be utilized when it is desired that the job be
      started immediately upon creation. Value may be JobStartTime, CustomTime,
      or LastOutputEventTime to indicate whether the starting point of the
      output event stream should start whenever the job is started, start at a
      custom user time stamp specified via the outputStartTime property, or
      start from the last event output time.
  returned: always
  type: str
  sample: null
output_start_time:
  description:
    - >-
      Value is either an ISO-8601 formatted time stamp that indicates the
      starting point of the output event stream, or null to indicate that the
      output event stream will start whenever the streaming job is started. This
      property must have a value if outputStartMode is set to CustomTime.
  returned: always
  type: str
  sample: null
last_output_event_time:
  description:
    - >-
      Value is either an ISO-8601 formatted timestamp indicating the last output
      event time of the streaming job or null indicating that output has not yet
      been produced. In case of multiple outputs or multiple streams, this shows
      the latest value in that set.
  returned: always
  type: str
  sample: null
events_out_of_order_policy:
  description:
    - >-
      Indicates the policy to apply to events that arrive out of order in the
      input event stream.
  returned: always
  type: str
  sample: null
output_error_policy:
  description:
    - >-
      Indicates the policy to apply to events that arrive at the output and
      cannot be written to the external storage due to being malformed (missing
      column values, column values of wrong type or size).
  returned: always
  type: str
  sample: null
events_out_of_order_max_delay_in_seconds:
  description:
    - >-
      The maximum tolerable delay in seconds where out-of-order events can be
      adjusted to be back in order.
  returned: always
  type: integer
  sample: null
events_late_arrival_max_delay_in_seconds:
  description:
    - >-
      The maximum tolerable delay in seconds where events arriving late could be
      included.  Supported range is -1 to 1814399 (20.23:59:59 days) and -1 is
      used to specify wait indefinitely. If the property is absent, it is
      interpreted to have a value of -1.
  returned: always
  type: integer
  sample: null
data_locale:
  description:
    - >-
      The data locale of the stream analytics job. Value should be the name of a
      supported .NET Culture from the set
      https://msdn.microsoft.com/en-us/library/system.globalization.culturetypes(v=vs.110).aspx.
      Defaults to 'en-US' if none specified.
  returned: always
  type: str
  sample: null
compatibility_level:
  description:
    - Controls certain runtime behaviors of the streaming job.
  returned: always
  type: str
  sample: null
created_date:
  description:
    - >-
      Value is an ISO-8601 formatted UTC timestamp indicating when the streaming
      job was created.
  returned: always
  type: str
  sample: null
inputs:
  description:
    - >-
      A list of one or more inputs to the streaming job. The name property for
      each input is required when specifying this property in a PUT request.
      This property cannot be modify via a PATCH operation. You must use the
      PATCH API available for the individual input.
  returned: always
  type: list
  sample: null
  contains:
    properties:
      description:
        - >-
          The properties that are associated with an input. Required on PUT
          (CreateOrReplace) requests.
      returned: always
      type: dict
      sample: null
      contains:
        type:
          description:
            - >-
              Indicates whether the input is a source of reference data or
              stream data. Required on PUT (CreateOrReplace) requests.
          returned: always
          type: str
          sample: null
        serialization:
          description:
            - >-
              Describes how data from an input is serialized or how data is
              serialized when written to an output. Required on PUT
              (CreateOrReplace) requests.
          returned: always
          type: dict
          sample: null
          contains:
            type:
              description:
                - >-
                  Indicates the type of serialization that the input or output
                  uses. Required on PUT (CreateOrReplace) requests.
              returned: always
              type: str
              sample: null
        diagnostics:
          description:
            - >-
              Describes conditions applicable to the Input, Output, or the job
              overall, that warrant customer attention.
          returned: always
          type: dict
          sample: null
          contains:
            conditions:
              description:
                - >-
                  A collection of zero or more conditions applicable to the
                  resource, or to the job overall, that warrant customer
                  attention.
              returned: always
              type: list
              sample: null
              contains:
                since:
                  description:
                    - >-
                      The UTC timestamp of when the condition started. Customers
                      should be able to find a corresponding event in the ops
                      log around this time.
                  returned: always
                  type: str
                  sample: null
                code:
                  description:
                    - The opaque diagnostic code.
                  returned: always
                  type: str
                  sample: null
                message:
                  description:
                    - >-
                      The human-readable message describing the condition in
                      detail. Localized in the Accept-Language of the client
                      request.
                  returned: always
                  type: str
                  sample: null
        etag:
          description:
            - >-
              The current entity tag for the input. This is an opaque string.
              You can use it to detect whether the resource has changed between
              requests. You can also use it in the If-Match or If-None-Match
              headers for write operations for optimistic concurrency.
          returned: always
          type: str
          sample: null
        compression:
          description:
            - Describes how input data is compressed
          returned: always
          type: dict
          sample: null
          contains:
            type:
              description:
                - ''
              returned: always
              type: str
              sample: null
        partition_key:
          description:
            - >-
              partitionKey Describes a key in the input data which is used for
              partitioning the input data
          returned: always
          type: str
          sample: null
transformation:
  description:
    - >-
      Indicates the query and the number of streaming units to use for the
      streaming job. The name property of the transformation is required when
      specifying this property in a PUT request. This property cannot be modify
      via a PATCH operation. You must use the PATCH API available for the
      individual transformation.
  returned: always
  type: dict
  sample: null
  contains:
    streaming_units:
      description:
        - Specifies the number of streaming units that the streaming job uses.
      returned: always
      type: integer
      sample: null
    query:
      description:
        - >-
          Specifies the query that will be run in the streaming job. You can
          learn more about the Stream Analytics Query Language (SAQL) here:
          https://msdn.microsoft.com/library/azure/dn834998 . Required on PUT
          (CreateOrReplace) requests.
      returned: always
      type: str
      sample: null
    etag:
      description:
        - >-
          The current entity tag for the transformation. This is an opaque
          string. You can use it to detect whether the resource has changed
          between requests. You can also use it in the If-Match or If-None-Match
          headers for write operations for optimistic concurrency.
      returned: always
      type: str
      sample: null
outputs:
  description:
    - >-
      A list of one or more outputs for the streaming job. The name property for
      each output is required when specifying this property in a PUT request.
      This property cannot be modify via a PATCH operation. You must use the
      PATCH API available for the individual output.
  returned: always
  type: list
  sample: null
  contains:
    datasource:
      description:
        - >-
          Describes the data source that output will be written to. Required on
          PUT (CreateOrReplace) requests.
      returned: always
      type: dict
      sample: null
      contains:
        type:
          description:
            - >-
              Indicates the type of data source output will be written to.
              Required on PUT (CreateOrReplace) requests.
          returned: always
          type: str
          sample: null
    time_window:
      description:
        - ''
      returned: always
      type: str
      sample: null
    size_window:
      description:
        - ''
      returned: always
      type: number
      sample: null
    serialization:
      description:
        - >-
          Describes how data from an input is serialized or how data is
          serialized when written to an output. Required on PUT
          (CreateOrReplace) requests.
      returned: always
      type: dict
      sample: null
      contains:
        type:
          description:
            - >-
              Indicates the type of serialization that the input or output uses.
              Required on PUT (CreateOrReplace) requests.
          returned: always
          type: str
          sample: null
    diagnostics:
      description:
        - >-
          Describes conditions applicable to the Input, Output, or the job
          overall, that warrant customer attention.
      returned: always
      type: dict
      sample: null
      contains:
        conditions:
          description:
            - >-
              A collection of zero or more conditions applicable to the
              resource, or to the job overall, that warrant customer attention.
          returned: always
          type: list
          sample: null
          contains:
            since:
              description:
                - >-
                  The UTC timestamp of when the condition started. Customers
                  should be able to find a corresponding event in the ops log
                  around this time.
              returned: always
              type: str
              sample: null
            code:
              description:
                - The opaque diagnostic code.
              returned: always
              type: str
              sample: null
            message:
              description:
                - >-
                  The human-readable message describing the condition in detail.
                  Localized in the Accept-Language of the client request.
              returned: always
              type: str
              sample: null
    etag:
      description:
        - >-
          The current entity tag for the output. This is an opaque string. You
          can use it to detect whether the resource has changed between
          requests. You can also use it in the If-Match or If-None-Match headers
          for write operations for optimistic concurrency.
      returned: always
      type: str
      sample: null
functions:
  description:
    - >-
      A list of one or more functions for the streaming job. The name property
      for each function is required when specifying this property in a PUT
      request. This property cannot be modify via a PATCH operation. You must
      use the PATCH API available for the individual transformation.
  returned: always
  type: list
  sample: null
  contains:
    properties:
      description:
        - The properties that are associated with a function.
      returned: always
      type: dict
      sample: null
      contains:
        type:
          description:
            - Indicates the type of function.
          returned: always
          type: str
          sample: null
        etag:
          description:
            - >-
              The current entity tag for the function. This is an opaque string.
              You can use it to detect whether the resource has changed between
              requests. You can also use it in the If-Match or If-None-Match
              headers for write operations for optimistic concurrency.
          returned: always
          type: str
          sample: null
        inputs:
          description:
            - ''
          returned: always
          type: list
          sample: null
          contains:
            data_type:
              description:
                - >-
                  The (Azure Stream Analytics supported) data type of the
                  function input parameter. A list of valid Azure Stream
                  Analytics data types are described at
                  https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
              returned: always
              type: str
              sample: null
            is_configuration_parameter:
              description:
                - >-
                  A flag indicating if the parameter is a configuration
                  parameter. True if this input parameter is expected to be a
                  constant. Default is false.
              returned: always
              type: bool
              sample: null
        output:
          description:
            - Describes the output of a function.
          returned: always
          type: dict
          sample: null
          contains:
            data_type:
              description:
                - >-
                  The (Azure Stream Analytics supported) data type of the
                  function output. A list of valid Azure Stream Analytics data
                  types are described at
                  https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
              returned: always
              type: str
              sample: null
        binding:
          description:
            - >-
              The physical binding of the function. For example, in the Azure
              Machine Learning web service’s case, this describes the endpoint.
          returned: always
          type: dict
          sample: null
          contains:
            type:
              description:
                - Indicates the function binding type.
              returned: always
              type: str
              sample: null
etag:
  description:
    - >-
      The current entity tag for the streaming job. This is an opaque string.
      You can use it to detect whether the resource has changed between
      requests. You can also use it in the If-Match or If-None-Match headers for
      write operations for optimistic concurrency.
  returned: always
  type: str
  sample: null
job_storage_account:
  description:
    - The properties that are associated with an Azure Storage account with MSI
  returned: always
  type: dict
  sample: null
  contains:
    authentication_mode:
      description:
        - Authentication Mode.
      returned: always
      type: str
      sample: null
content_storage_policy:
  description:
    - >-
      Valid values are JobStorageAccount and SystemAccount. If set to
      JobStorageAccount, this requires the user to also specify
      jobStorageAccount property. .
  returned: always
  type: str
  sample: null
externals:
  description:
    - The storage account where the custom code artifacts are located.
  returned: always
  type: dict
  sample: null
  contains:
    storage_account:
      description:
        - The properties that are associated with an Azure Storage account
      returned: always
      type: dict
      sample: null
      contains:
        account_name:
          description:
            - >-
              The name of the Azure Storage account. Required on PUT
              (CreateOrReplace) requests.
          returned: always
          type: str
          sample: null
        account_key:
          description:
            - >-
              The account key for the Azure Storage account. Required on PUT
              (CreateOrReplace) requests.
          returned: always
          type: str
          sample: null
    container:
      description:
        - ''
      returned: always
      type: str
      sample: null
    path:
      description:
        - ''
      returned: always
      type: str
      sample: null
cluster:
  description:
    - The cluster which streaming jobs will run on.
  returned: always
  type: dict
  sample: null
  contains:
    id:
      description:
        - The resource id of cluster.
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
    from azure.mgmt.stream import Stream Analytics Management Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMStreamingJob(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            if_match=dict(
                type='str'
            ),
            resource_group_name=dict(
                type='str',
                required=True
            ),
            job_name=dict(
                type='str',
                required=True
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            identity=dict(
                type='dict',
                disposition='/identity',
                options=dict(
                    tenant_id=dict(
                        type='str',
                        disposition='tenant_id'
                    ),
                    principal_id=dict(
                        type='str',
                        disposition='principal_id'
                    ),
                    type=dict(
                        type='str',
                        disposition='type'
                    )
                )
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        choices=['Standard']
                    )
                )
            ),
            job_type=dict(
                type='str',
                disposition='/job_type',
                choices=['Cloud',
                         'Edge']
            ),
            output_start_mode=dict(
                type='str',
                disposition='/output_start_mode',
                choices=['JobStartTime',
                         'CustomTime',
                         'LastOutputEventTime']
            ),
            output_start_time=dict(
                type='str',
                disposition='/output_start_time'
            ),
            events_out_of_order_policy=dict(
                type='str',
                disposition='/events_out_of_order_policy',
                choices=['Adjust',
                         'Drop']
            ),
            output_error_policy=dict(
                type='str',
                disposition='/output_error_policy',
                choices=['Stop',
                         'Drop']
            ),
            events_out_of_order_max_delay_in_seconds=dict(
                type='integer',
                disposition='/events_out_of_order_max_delay_in_seconds'
            ),
            events_late_arrival_max_delay_in_seconds=dict(
                type='integer',
                disposition='/events_late_arrival_max_delay_in_seconds'
            ),
            data_locale=dict(
                type='str',
                disposition='/data_locale'
            ),
            compatibility_level=dict(
                type='str',
                disposition='/compatibility_level',
                choices=['1.0']
            ),
            inputs=dict(
                type='list',
                disposition='/inputs',
                elements='dict',
                options=dict(
                    properties=dict(
                        type='dict',
                        disposition='properties',
                        options=dict(
                            type=dict(
                                type='str',
                                disposition='type',
                                required=True
                            ),
                            serialization=dict(
                                type='dict',
                                disposition='serialization',
                                options=dict(
                                    type=dict(
                                        type='str',
                                        disposition='type',
                                        choices=['Csv',
                                                 'Avro',
                                                 'Json',
                                                 'CustomClr',
                                                 'Parquet'],
                                        required=True
                                    )
                                )
                            ),
                            diagnostics=dict(
                                type='dict',
                                updatable=False,
                                disposition='diagnostics',
                                options=dict(
                                    conditions=dict(
                                        type='list',
                                        updatable=False,
                                        disposition='conditions',
                                        elements='dict',
                                        options=dict(
                                            since=dict(
                                                type='str',
                                                updatable=False,
                                                disposition='since'
                                            ),
                                            code=dict(
                                                type='str',
                                                updatable=False,
                                                disposition='code'
                                            ),
                                            message=dict(
                                                type='str',
                                                updatable=False,
                                                disposition='message'
                                            )
                                        )
                                    )
                                )
                            ),
                            etag=dict(
                                type='str',
                                updatable=False,
                                disposition='etag'
                            ),
                            compression=dict(
                                type='dict',
                                disposition='compression',
                                options=dict(
                                    type=dict(
                                        type='str',
                                        disposition='type',
                                        required=True
                                    )
                                )
                            ),
                            partition_key=dict(
                                type='str',
                                disposition='partition_key'
                            )
                        )
                    )
                )
            ),
            transformation=dict(
                type='dict',
                disposition='/transformation',
                options=dict(
                    streaming_units=dict(
                        type='integer',
                        disposition='streaming_units'
                    ),
                    query=dict(
                        type='str',
                        disposition='query'
                    ),
                    etag=dict(
                        type='str',
                        updatable=False,
                        disposition='etag'
                    )
                )
            ),
            outputs=dict(
                type='list',
                disposition='/outputs',
                elements='dict',
                options=dict(
                    datasource=dict(
                        type='dict',
                        disposition='datasource',
                        options=dict(
                            type=dict(
                                type='str',
                                disposition='type',
                                required=True
                            )
                        )
                    ),
                    time_window=dict(
                        type='str',
                        disposition='time_window'
                    ),
                    size_window=dict(
                        type='number',
                        disposition='size_window'
                    ),
                    serialization=dict(
                        type='dict',
                        disposition='serialization',
                        options=dict(
                            type=dict(
                                type='str',
                                disposition='type',
                                choices=['Csv',
                                         'Avro',
                                         'Json',
                                         'CustomClr',
                                         'Parquet'],
                                required=True
                            )
                        )
                    ),
                    diagnostics=dict(
                        type='dict',
                        updatable=False,
                        disposition='diagnostics',
                        options=dict(
                            conditions=dict(
                                type='list',
                                updatable=False,
                                disposition='conditions',
                                elements='dict',
                                options=dict(
                                    since=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='since'
                                    ),
                                    code=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='code'
                                    ),
                                    message=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='message'
                                    )
                                )
                            )
                        )
                    ),
                    etag=dict(
                        type='str',
                        updatable=False,
                        disposition='etag'
                    )
                )
            ),
            functions=dict(
                type='list',
                disposition='/functions',
                elements='dict',
                options=dict(
                    properties=dict(
                        type='dict',
                        disposition='properties',
                        options=dict(
                            type=dict(
                                type='str',
                                disposition='type',
                                required=True
                            ),
                            etag=dict(
                                type='str',
                                updatable=False,
                                disposition='etag'
                            ),
                            inputs=dict(
                                type='list',
                                disposition='inputs',
                                elements='dict',
                                options=dict(
                                    data_type=dict(
                                        type='str',
                                        disposition='data_type'
                                    ),
                                    is_configuration_parameter=dict(
                                        type='bool',
                                        disposition='is_configuration_parameter'
                                    )
                                )
                            ),
                            output=dict(
                                type='dict',
                                disposition='output',
                                options=dict(
                                    data_type=dict(
                                        type='str',
                                        disposition='data_type'
                                    )
                                )
                            ),
                            binding=dict(
                                type='dict',
                                disposition='binding',
                                options=dict(
                                    type=dict(
                                        type='str',
                                        disposition='type',
                                        required=True
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            job_storage_account=dict(
                type='dict',
                disposition='/job_storage_account',
                options=dict(
                    authentication_mode=dict(
                        type='str',
                        disposition='authentication_mode',
                        choices=['Msi',
                                 'UserToken',
                                 'ConnectionString']
                    )
                )
            ),
            externals=dict(
                type='dict',
                disposition='/externals',
                options=dict(
                    storage_account=dict(
                        type='dict',
                        disposition='storage_account',
                        options=dict(
                            account_name=dict(
                                type='str',
                                disposition='account_name'
                            ),
                            account_key=dict(
                                type='str',
                                disposition='account_key'
                            )
                        )
                    ),
                    container=dict(
                        type='str',
                        disposition='container'
                    ),
                    path=dict(
                        type='str',
                        disposition='path'
                    )
                )
            ),
            cluster=dict(
                type='dict',
                disposition='/cluster',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            expand=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.if_match = None
        self.resource_group_name = None
        self.job_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMStreamingJob, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(Stream Analytics Management Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01-preview')

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
                response = self.mgmt_client.streaming_jobs.create()
            else:
                response = self.mgmt_client.streaming_jobs.update(if_match=self.if_match,
                                                                  resource_group_name=self.resource_group_name,
                                                                  job_name=self.job_name,
                                                                  streaming_job=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the StreamingJob instance.')
            self.fail('Error creating the StreamingJob instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.streaming_jobs.delete(resource_group_name=self.resource_group_name,
                                                              job_name=self.job_name)
        except CloudError as e:
            self.log('Error attempting to delete the StreamingJob instance.')
            self.fail('Error deleting the StreamingJob instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.streaming_jobs.get(expand=self.expand,
                                                           resource_group_name=self.resource_group_name,
                                                           job_name=self.job_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMStreamingJob()


if __name__ == '__main__':
    main()
