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
module: azure_rm_streamingjob_info
version_added: '2.9'
short_description: Get StreamingJob info.
description:
  - Get info of StreamingJob.
options:
  expand:
    description:
      - >-
        The $expand OData query parameter. This is a comma-separated list of
        additional streaming job properties to include in the response, beyond
        the default set returned when this parameter is absent. The default set
        is all streaming job properties other than 'inputs', 'transformation',
        'outputs', and 'functions'.
    required: true
    type: str
  resource_group_name:
    description:
      - The name of the resource group. The name is case insensitive.
    type: str
  job_name:
    description:
      - The name of the streaming job.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a streaming job and do not use the $expand OData query parameter
      azure_rm_streamingjob_info: 
        job_name: sj59
        resource_group_name: sjrg
        

    - name: Get a streaming job and use the $expand OData query parameter to expand inputs, outputs, transformation, and functions
      azure_rm_streamingjob_info: 
        job_name: sj7804
        resource_group_name: sjrg
        

    - name: List all streaming jobs in a resource group and do not use the $expand OData query parameter
      azure_rm_streamingjob_info: 
        resource_group_name: sjrg
        

    - name: List all streaming jobs in a resource group and use the $expand OData query parameter to expand inputs, outputs, transformation, and functions
      azure_rm_streamingjob_info: 
        resource_group_name: sjrg
        

    - name: List all streaming jobs in a subscription and do not use the $expand OData query parameter
      azure_rm_streamingjob_info: 
        {}
        

    - name: List all streaming jobs in a subscription and use the $expand OData query parameter to expand inputs, outputs, transformation, and functions
      azure_rm_streamingjob_info: 
        {}
        

'''

RETURN = '''
streaming_jobs:
  description: >-
    A list of dict results where the key is the name of the StreamingJob and the
    values are the facts for that StreamingJob.
  returned: always
  type: complex
  contains:
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
          Describes the system-assigned managed identity assigned to this job
          that can be used to authenticate with inputs and outputs.
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
          Describes the SKU of the streaming job. Required on PUT
          (CreateOrReplace) requests.
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
          A GUID uniquely identifying the streaming job. This GUID is generated
          upon creation of the streaming job.
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
          This property should only be utilized when it is desired that the job
          be started immediately upon creation. Value may be JobStartTime,
          CustomTime, or LastOutputEventTime to indicate whether the starting
          point of the output event stream should start whenever the job is
          started, start at a custom user time stamp specified via the
          outputStartTime property, or start from the last event output time.
      returned: always
      type: str
      sample: null
    output_start_time:
      description:
        - >-
          Value is either an ISO-8601 formatted time stamp that indicates the
          starting point of the output event stream, or null to indicate that
          the output event stream will start whenever the streaming job is
          started. This property must have a value if outputStartMode is set to
          CustomTime.
      returned: always
      type: str
      sample: null
    last_output_event_time:
      description:
        - >-
          Value is either an ISO-8601 formatted timestamp indicating the last
          output event time of the streaming job or null indicating that output
          has not yet been produced. In case of multiple outputs or multiple
          streams, this shows the latest value in that set.
      returned: always
      type: str
      sample: null
    events_out_of_order_policy:
      description:
        - >-
          Indicates the policy to apply to events that arrive out of order in
          the input event stream.
      returned: always
      type: str
      sample: null
    output_error_policy:
      description:
        - >-
          Indicates the policy to apply to events that arrive at the output and
          cannot be written to the external storage due to being malformed
          (missing column values, column values of wrong type or size).
      returned: always
      type: str
      sample: null
    events_out_of_order_max_delay_in_seconds:
      description:
        - >-
          The maximum tolerable delay in seconds where out-of-order events can
          be adjusted to be back in order.
      returned: always
      type: integer
      sample: null
    events_late_arrival_max_delay_in_seconds:
      description:
        - >-
          The maximum tolerable delay in seconds where events arriving late
          could be included.  Supported range is -1 to 1814399 (20.23:59:59
          days) and -1 is used to specify wait indefinitely. If the property is
          absent, it is interpreted to have a value of -1.
      returned: always
      type: integer
      sample: null
    data_locale:
      description:
        - >-
          The data locale of the stream analytics job. Value should be the name
          of a supported .NET Culture from the set
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
          Value is an ISO-8601 formatted UTC timestamp indicating when the
          streaming job was created.
      returned: always
      type: str
      sample: null
    inputs:
      description:
        - >-
          A list of one or more inputs to the streaming job. The name property
          for each input is required when specifying this property in a PUT
          request. This property cannot be modify via a PATCH operation. You
          must use the PATCH API available for the individual input.
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
                      Indicates the type of serialization that the input or
                      output uses. Required on PUT (CreateOrReplace) requests.
                  returned: always
                  type: str
                  sample: null
            diagnostics:
              description:
                - >-
                  Describes conditions applicable to the Input, Output, or the
                  job overall, that warrant customer attention.
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
                          The UTC timestamp of when the condition started.
                          Customers should be able to find a corresponding event
                          in the ops log around this time.
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
                  The current entity tag for the input. This is an opaque
                  string. You can use it to detect whether the resource has
                  changed between requests. You can also use it in the If-Match
                  or If-None-Match headers for write operations for optimistic
                  concurrency.
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
                  partitionKey Describes a key in the input data which is used
                  for partitioning the input data
              returned: always
              type: str
              sample: null
    transformation:
      description:
        - >-
          Indicates the query and the number of streaming units to use for the
          streaming job. The name property of the transformation is required
          when specifying this property in a PUT request. This property cannot
          be modify via a PATCH operation. You must use the PATCH API available
          for the individual transformation.
      returned: always
      type: dict
      sample: null
      contains:
        streaming_units:
          description:
            - >-
              Specifies the number of streaming units that the streaming job
              uses.
          returned: always
          type: integer
          sample: null
        query:
          description:
            - >-
              Specifies the query that will be run in the streaming job. You can
              learn more about the Stream Analytics Query Language (SAQL) here:
              https://msdn.microsoft.com/library/azure/dn834998 . Required on
              PUT (CreateOrReplace) requests.
          returned: always
          type: str
          sample: null
        etag:
          description:
            - >-
              The current entity tag for the transformation. This is an opaque
              string. You can use it to detect whether the resource has changed
              between requests. You can also use it in the If-Match or
              If-None-Match headers for write operations for optimistic
              concurrency.
          returned: always
          type: str
          sample: null
    outputs:
      description:
        - >-
          A list of one or more outputs for the streaming job. The name property
          for each output is required when specifying this property in a PUT
          request. This property cannot be modify via a PATCH operation. You
          must use the PATCH API available for the individual output.
      returned: always
      type: list
      sample: null
      contains:
        datasource:
          description:
            - >-
              Describes the data source that output will be written to. Required
              on PUT (CreateOrReplace) requests.
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
              The current entity tag for the output. This is an opaque string.
              You can use it to detect whether the resource has changed between
              requests. You can also use it in the If-Match or If-None-Match
              headers for write operations for optimistic concurrency.
          returned: always
          type: str
          sample: null
    functions:
      description:
        - >-
          A list of one or more functions for the streaming job. The name
          property for each function is required when specifying this property
          in a PUT request. This property cannot be modify via a PATCH
          operation. You must use the PATCH API available for the individual
          transformation.
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
                  The current entity tag for the function. This is an opaque
                  string. You can use it to detect whether the resource has
                  changed between requests. You can also use it in the If-Match
                  or If-None-Match headers for write operations for optimistic
                  concurrency.
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
                      parameter. True if this input parameter is expected to be
                      a constant. Default is false.
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
                      function output. A list of valid Azure Stream Analytics
                      data types are described at
                      https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
                  returned: always
                  type: str
                  sample: null
            binding:
              description:
                - >-
                  The physical binding of the function. For example, in the
                  Azure Machine Learning web service’s case, this describes the
                  endpoint.
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
          The current entity tag for the streaming job. This is an opaque
          string. You can use it to detect whether the resource has changed
          between requests. You can also use it in the If-Match or If-None-Match
          headers for write operations for optimistic concurrency.
      returned: always
      type: str
      sample: null
    job_storage_account:
      description:
        - >-
          The properties that are associated with an Azure Storage account with
          MSI
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
    value:
      description:
        - A list of streaming jobs. Populated by a 'List' operation.
      returned: always
      type: list
      sample: null
      contains:
        identity:
          description:
            - >-
              Describes the system-assigned managed identity assigned to this
              job that can be used to authenticate with inputs and outputs.
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
              Describes the SKU of the streaming job. Required on PUT
              (CreateOrReplace) requests.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the SKU. Required on PUT (CreateOrReplace)
                  requests.
              returned: always
              type: str
              sample: null
        job_id:
          description:
            - >-
              A GUID uniquely identifying the streaming job. This GUID is
              generated upon creation of the streaming job.
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
              This property should only be utilized when it is desired that the
              job be started immediately upon creation. Value may be
              JobStartTime, CustomTime, or LastOutputEventTime to indicate
              whether the starting point of the output event stream should start
              whenever the job is started, start at a custom user time stamp
              specified via the outputStartTime property, or start from the last
              event output time.
          returned: always
          type: str
          sample: null
        output_start_time:
          description:
            - >-
              Value is either an ISO-8601 formatted time stamp that indicates
              the starting point of the output event stream, or null to indicate
              that the output event stream will start whenever the streaming job
              is started. This property must have a value if outputStartMode is
              set to CustomTime.
          returned: always
          type: str
          sample: null
        last_output_event_time:
          description:
            - >-
              Value is either an ISO-8601 formatted timestamp indicating the
              last output event time of the streaming job or null indicating
              that output has not yet been produced. In case of multiple outputs
              or multiple streams, this shows the latest value in that set.
          returned: always
          type: str
          sample: null
        events_out_of_order_policy:
          description:
            - >-
              Indicates the policy to apply to events that arrive out of order
              in the input event stream.
          returned: always
          type: str
          sample: null
        output_error_policy:
          description:
            - >-
              Indicates the policy to apply to events that arrive at the output
              and cannot be written to the external storage due to being
              malformed (missing column values, column values of wrong type or
              size).
          returned: always
          type: str
          sample: null
        events_out_of_order_max_delay_in_seconds:
          description:
            - >-
              The maximum tolerable delay in seconds where out-of-order events
              can be adjusted to be back in order.
          returned: always
          type: integer
          sample: null
        events_late_arrival_max_delay_in_seconds:
          description:
            - >-
              The maximum tolerable delay in seconds where events arriving late
              could be included.  Supported range is -1 to 1814399 (20.23:59:59
              days) and -1 is used to specify wait indefinitely. If the property
              is absent, it is interpreted to have a value of -1.
          returned: always
          type: integer
          sample: null
        data_locale:
          description:
            - >-
              The data locale of the stream analytics job. Value should be the
              name of a supported .NET Culture from the set
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
              Value is an ISO-8601 formatted UTC timestamp indicating when the
              streaming job was created.
          returned: always
          type: str
          sample: null
        inputs:
          description:
            - >-
              A list of one or more inputs to the streaming job. The name
              property for each input is required when specifying this property
              in a PUT request. This property cannot be modify via a PATCH
              operation. You must use the PATCH API available for the individual
              input.
          returned: always
          type: list
          sample: null
          contains:
            properties:
              description:
                - >-
                  The properties that are associated with an input. Required on
                  PUT (CreateOrReplace) requests.
              returned: always
              type: dict
              sample: null
              contains:
                type:
                  description:
                    - >-
                      Indicates whether the input is a source of reference data
                      or stream data. Required on PUT (CreateOrReplace)
                      requests.
                  returned: always
                  type: str
                  sample: null
                serialization:
                  description:
                    - >-
                      Describes how data from an input is serialized or how data
                      is serialized when written to an output. Required on PUT
                      (CreateOrReplace) requests.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    type:
                      description:
                        - >-
                          Indicates the type of serialization that the input or
                          output uses. Required on PUT (CreateOrReplace)
                          requests.
                      returned: always
                      type: str
                      sample: null
                diagnostics:
                  description:
                    - >-
                      Describes conditions applicable to the Input, Output, or
                      the job overall, that warrant customer attention.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    conditions:
                      description:
                        - >-
                          A collection of zero or more conditions applicable to
                          the resource, or to the job overall, that warrant
                          customer attention.
                      returned: always
                      type: list
                      sample: null
                      contains:
                        since:
                          description:
                            - >-
                              The UTC timestamp of when the condition started.
                              Customers should be able to find a corresponding
                              event in the ops log around this time.
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
                              The human-readable message describing the
                              condition in detail. Localized in the
                              Accept-Language of the client request.
                          returned: always
                          type: str
                          sample: null
                etag:
                  description:
                    - >-
                      The current entity tag for the input. This is an opaque
                      string. You can use it to detect whether the resource has
                      changed between requests. You can also use it in the
                      If-Match or If-None-Match headers for write operations for
                      optimistic concurrency.
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
                      partitionKey Describes a key in the input data which is
                      used for partitioning the input data
                  returned: always
                  type: str
                  sample: null
        transformation:
          description:
            - >-
              Indicates the query and the number of streaming units to use for
              the streaming job. The name property of the transformation is
              required when specifying this property in a PUT request. This
              property cannot be modify via a PATCH operation. You must use the
              PATCH API available for the individual transformation.
          returned: always
          type: dict
          sample: null
          contains:
            streaming_units:
              description:
                - >-
                  Specifies the number of streaming units that the streaming job
                  uses.
              returned: always
              type: integer
              sample: null
            query:
              description:
                - >-
                  Specifies the query that will be run in the streaming job. You
                  can learn more about the Stream Analytics Query Language
                  (SAQL) here: https://msdn.microsoft.com/library/azure/dn834998
                  . Required on PUT (CreateOrReplace) requests.
              returned: always
              type: str
              sample: null
            etag:
              description:
                - >-
                  The current entity tag for the transformation. This is an
                  opaque string. You can use it to detect whether the resource
                  has changed between requests. You can also use it in the
                  If-Match or If-None-Match headers for write operations for
                  optimistic concurrency.
              returned: always
              type: str
              sample: null
        outputs:
          description:
            - >-
              A list of one or more outputs for the streaming job. The name
              property for each output is required when specifying this property
              in a PUT request. This property cannot be modify via a PATCH
              operation. You must use the PATCH API available for the individual
              output.
          returned: always
          type: list
          sample: null
          contains:
            datasource:
              description:
                - >-
                  Describes the data source that output will be written to.
                  Required on PUT (CreateOrReplace) requests.
              returned: always
              type: dict
              sample: null
              contains:
                type:
                  description:
                    - >-
                      Indicates the type of data source output will be written
                      to. Required on PUT (CreateOrReplace) requests.
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
                      Indicates the type of serialization that the input or
                      output uses. Required on PUT (CreateOrReplace) requests.
                  returned: always
                  type: str
                  sample: null
            diagnostics:
              description:
                - >-
                  Describes conditions applicable to the Input, Output, or the
                  job overall, that warrant customer attention.
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
                          The UTC timestamp of when the condition started.
                          Customers should be able to find a corresponding event
                          in the ops log around this time.
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
                  The current entity tag for the output. This is an opaque
                  string. You can use it to detect whether the resource has
                  changed between requests. You can also use it in the If-Match
                  or If-None-Match headers for write operations for optimistic
                  concurrency.
              returned: always
              type: str
              sample: null
        functions:
          description:
            - >-
              A list of one or more functions for the streaming job. The name
              property for each function is required when specifying this
              property in a PUT request. This property cannot be modify via a
              PATCH operation. You must use the PATCH API available for the
              individual transformation.
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
                      The current entity tag for the function. This is an opaque
                      string. You can use it to detect whether the resource has
                      changed between requests. You can also use it in the
                      If-Match or If-None-Match headers for write operations for
                      optimistic concurrency.
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
                          The (Azure Stream Analytics supported) data type of
                          the function input parameter. A list of valid Azure
                          Stream Analytics data types are described at
                          https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
                      returned: always
                      type: str
                      sample: null
                    is_configuration_parameter:
                      description:
                        - >-
                          A flag indicating if the parameter is a configuration
                          parameter. True if this input parameter is expected to
                          be a constant. Default is false.
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
                          The (Azure Stream Analytics supported) data type of
                          the function output. A list of valid Azure Stream
                          Analytics data types are described at
                          https://msdn.microsoft.com/en-us/library/azure/dn835065.aspx
                      returned: always
                      type: str
                      sample: null
                binding:
                  description:
                    - >-
                      The physical binding of the function. For example, in the
                      Azure Machine Learning web service’s case, this describes
                      the endpoint.
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
              The current entity tag for the streaming job. This is an opaque
              string. You can use it to detect whether the resource has changed
              between requests. You can also use it in the If-Match or
              If-None-Match headers for write operations for optimistic
              concurrency.
          returned: always
          type: str
          sample: null
        job_storage_account:
          description:
            - >-
              The properties that are associated with an Azure Storage account
              with MSI
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
                - >-
                  The properties that are associated with an Azure Storage
                  account
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
                      The account key for the Azure Storage account. Required on
                      PUT (CreateOrReplace) requests.
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
    next_link:
      description:
        - The link (url) to the next page of results.
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
    from azure.mgmt.stream import Stream Analytics Management Client
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMStreamingJobInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            expand=dict(
                type='str',
                required=True
            ),
            resource_group_name=dict(
                type='str'
            ),
            job_name=dict(
                type='str'
            )
        )

        self.expand = None
        self.resource_group_name = None
        self.job_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-04-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMStreamingJobInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(Stream Analytics Management Client,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-04-01-preview')

        if (self.resource_group_name is not None and
            self.job_name is not None):
            self.results['streaming_jobs'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['streaming_jobs'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['streaming_jobs'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.streaming_jobs.get(expand=self.expand,
                                                           resource_group_name=self.resource_group_name,
                                                           job_name=self.job_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.streaming_jobs.list_by_resource_group(expand=self.expand,
                                                                              resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.streaming_jobs.list(expand=self.expand)
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
    AzureRMStreamingJobInfo()


if __name__ == '__main__':
    main()
