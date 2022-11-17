#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spark/connect/base.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from pyspark.sql.connect.proto import commands_pb2 as spark_dot_connect_dot_commands__pb2
from pyspark.sql.connect.proto import relations_pb2 as spark_dot_connect_dot_relations__pb2
from pyspark.sql.connect.proto import types_pb2 as spark_dot_connect_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x18spark/connect/base.proto\x12\rspark.connect\x1a\x19google/protobuf/any.proto\x1a\x1cspark/connect/commands.proto\x1a\x1dspark/connect/relations.proto\x1a\x19spark/connect/types.proto"t\n\x04Plan\x12-\n\x04root\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationH\x00R\x04root\x12\x32\n\x07\x63ommand\x18\x02 \x01(\x0b\x32\x16.spark.connect.CommandH\x00R\x07\x63ommandB\t\n\x07op_type"\xc8\x02\n\x07Request\x12\x1b\n\tclient_id\x18\x01 \x01(\tR\x08\x63lientId\x12\x45\n\x0cuser_context\x18\x02 \x01(\x0b\x32".spark.connect.Request.UserContextR\x0buserContext\x12\'\n\x04plan\x18\x03 \x01(\x0b\x32\x13.spark.connect.PlanR\x04plan\x12$\n\x0b\x63lient_type\x18\x04 \x01(\tH\x00R\nclientType\x88\x01\x01\x1az\n\x0bUserContext\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x1b\n\tuser_name\x18\x02 \x01(\tR\x08userName\x12\x35\n\nextensions\x18\xe7\x07 \x03(\x0b\x32\x14.google.protobuf.AnyR\nextensionsB\x0e\n\x0c_client_type"\xe0\x06\n\x08Response\x12\x1b\n\tclient_id\x18\x01 \x01(\tR\x08\x63lientId\x12\x45\n\x0b\x61rrow_batch\x18\x02 \x01(\x0b\x32".spark.connect.Response.ArrowBatchH\x00R\narrowBatch\x12\x42\n\njson_batch\x18\x03 \x01(\x0b\x32!.spark.connect.Response.JSONBatchH\x00R\tjsonBatch\x12\x39\n\x07metrics\x18\x04 \x01(\x0b\x32\x1f.spark.connect.Response.MetricsR\x07metrics\x1a=\n\nArrowBatch\x12\x1b\n\trow_count\x18\x01 \x01(\x03R\x08rowCount\x12\x12\n\x04\x64\x61ta\x18\x02 \x01(\x0cR\x04\x64\x61ta\x1a<\n\tJSONBatch\x12\x1b\n\trow_count\x18\x01 \x01(\x03R\x08rowCount\x12\x12\n\x04\x64\x61ta\x18\x02 \x01(\x0cR\x04\x64\x61ta\x1a\xe4\x03\n\x07Metrics\x12\x46\n\x07metrics\x18\x01 \x03(\x0b\x32,.spark.connect.Response.Metrics.MetricObjectR\x07metrics\x1a\xb6\x02\n\x0cMetricObject\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x17\n\x07plan_id\x18\x02 \x01(\x03R\x06planId\x12\x16\n\x06parent\x18\x03 \x01(\x03R\x06parent\x12o\n\x11\x65xecution_metrics\x18\x04 \x03(\x0b\x32\x42.spark.connect.Response.Metrics.MetricObject.ExecutionMetricsEntryR\x10\x65xecutionMetrics\x1ap\n\x15\x45xecutionMetricsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32+.spark.connect.Response.Metrics.MetricValueR\x05value:\x02\x38\x01\x1aX\n\x0bMetricValue\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05value\x18\x02 \x01(\x03R\x05value\x12\x1f\n\x0bmetric_type\x18\x03 \x01(\tR\nmetricTypeB\r\n\x0bresult_type"\x86\x01\n\x0f\x41nalyzeResponse\x12\x1b\n\tclient_id\x18\x01 \x01(\tR\x08\x63lientId\x12/\n\x06schema\x18\x02 \x01(\x0b\x32\x17.spark.connect.DataTypeR\x06schema\x12%\n\x0e\x65xplain_string\x18\x03 \x01(\tR\rexplainString2\xa2\x01\n\x13SparkConnectService\x12\x42\n\x0b\x45xecutePlan\x12\x16.spark.connect.Request\x1a\x17.spark.connect.Response"\x00\x30\x01\x12G\n\x0b\x41nalyzePlan\x12\x16.spark.connect.Request\x1a\x1e.spark.connect.AnalyzeResponse"\x00\x42"\n\x1eorg.apache.spark.connect.protoP\x01\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "spark.connect.base_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\036org.apache.spark.connect.protoP\001"
    _RESPONSE_METRICS_METRICOBJECT_EXECUTIONMETRICSENTRY._options = None
    _RESPONSE_METRICS_METRICOBJECT_EXECUTIONMETRICSENTRY._serialized_options = b"8\001"
    _PLAN._serialized_start = 158
    _PLAN._serialized_end = 274
    _REQUEST._serialized_start = 277
    _REQUEST._serialized_end = 605
    _REQUEST_USERCONTEXT._serialized_start = 467
    _REQUEST_USERCONTEXT._serialized_end = 589
    _RESPONSE._serialized_start = 608
    _RESPONSE._serialized_end = 1472
    _RESPONSE_ARROWBATCH._serialized_start = 847
    _RESPONSE_ARROWBATCH._serialized_end = 908
    _RESPONSE_JSONBATCH._serialized_start = 910
    _RESPONSE_JSONBATCH._serialized_end = 970
    _RESPONSE_METRICS._serialized_start = 973
    _RESPONSE_METRICS._serialized_end = 1457
    _RESPONSE_METRICS_METRICOBJECT._serialized_start = 1057
    _RESPONSE_METRICS_METRICOBJECT._serialized_end = 1367
    _RESPONSE_METRICS_METRICOBJECT_EXECUTIONMETRICSENTRY._serialized_start = 1255
    _RESPONSE_METRICS_METRICOBJECT_EXECUTIONMETRICSENTRY._serialized_end = 1367
    _RESPONSE_METRICS_METRICVALUE._serialized_start = 1369
    _RESPONSE_METRICS_METRICVALUE._serialized_end = 1457
    _ANALYZERESPONSE._serialized_start = 1475
    _ANALYZERESPONSE._serialized_end = 1609
    _SPARKCONNECTSERVICE._serialized_start = 1612
    _SPARKCONNECTSERVICE._serialized_end = 1774
# @@protoc_insertion_point(module_scope)