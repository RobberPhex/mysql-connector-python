# MySQL Connector/Python - MySQL driver written in Python.
# Copyright (c) 2016, Oracle and/or its affiliates. All rights reserved.

# MySQL Connector/Python is licensed under the terms of the GPLv2
# <http://www.gnu.org/licenses/old-licenses/gpl-2.0.html>, like most
# MySQL Connectors. There are special exceptions to the terms and
# conditions of the GPLv2 as it is applied to this software, see the
# FOSS License Exception
# <http://www.mysql.com/about/legal/licensing/foss-exception.html>.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mysqlx_resultset.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mysqlx_resultset.proto',
  package='Mysqlx.Resultset',
  serialized_pb=_b('\n\x16mysqlx_resultset.proto\x12\x10Mysqlx.Resultset\"\x18\n\x16\x46\x65tchDoneMoreOutParams\"\x19\n\x17\x46\x65tchDoneMoreResultsets\"\x0b\n\tFetchDone\"\x9f\x03\n\x0e\x43olumnMetaData\x12\x38\n\x04type\x18\x01 \x02(\x0e\x32*.Mysqlx.Resultset.ColumnMetaData.FieldType\x12\x0c\n\x04name\x18\x02 \x01(\x0c\x12\x15\n\roriginal_name\x18\x03 \x01(\x0c\x12\r\n\x05table\x18\x04 \x01(\x0c\x12\x16\n\x0eoriginal_table\x18\x05 \x01(\x0c\x12\x0e\n\x06schema\x18\x06 \x01(\x0c\x12\x0f\n\x07\x63\x61talog\x18\x07 \x01(\x0c\x12\x11\n\tcollation\x18\x08 \x01(\x04\x12\x19\n\x11\x66ractional_digits\x18\t \x01(\r\x12\x0e\n\x06length\x18\n \x01(\r\x12\r\n\x05\x66lags\x18\x0b \x01(\r\x12\x14\n\x0c\x63ontent_type\x18\x0c \x01(\r\"\x82\x01\n\tFieldType\x12\x08\n\x04SINT\x10\x01\x12\x08\n\x04UINT\x10\x02\x12\n\n\x06\x44OUBLE\x10\x05\x12\t\n\x05\x46LOAT\x10\x06\x12\t\n\x05\x42YTES\x10\x07\x12\x08\n\x04TIME\x10\n\x12\x0c\n\x08\x44\x41TETIME\x10\x0c\x12\x07\n\x03SET\x10\x0f\x12\x08\n\x04\x45NUM\x10\x10\x12\x07\n\x03\x42IT\x10\x11\x12\x0b\n\x07\x44\x45\x43IMAL\x10\x12\"\x14\n\x03Row\x12\r\n\x05\x66ield\x18\x01 \x03(\x0c\x42\x1e\n\x1c\x63om.mysql.cj.mysqlx.protobuf')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_COLUMNMETADATA_FIELDTYPE = _descriptor.EnumDescriptor(
  name='FieldType',
  full_name='Mysqlx.Resultset.ColumnMetaData.FieldType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SINT', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=2, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=3, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BYTES', index=4, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIME', index=5, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATETIME', index=6, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET', index=7, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENUM', index=8, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIT', index=9, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DECIMAL', index=10, number=18,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=396,
  serialized_end=526,
)
_sym_db.RegisterEnumDescriptor(_COLUMNMETADATA_FIELDTYPE)


_FETCHDONEMOREOUTPARAMS = _descriptor.Descriptor(
  name='FetchDoneMoreOutParams',
  full_name='Mysqlx.Resultset.FetchDoneMoreOutParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=68,
)


_FETCHDONEMORERESULTSETS = _descriptor.Descriptor(
  name='FetchDoneMoreResultsets',
  full_name='Mysqlx.Resultset.FetchDoneMoreResultsets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=95,
)


_FETCHDONE = _descriptor.Descriptor(
  name='FetchDone',
  full_name='Mysqlx.Resultset.FetchDone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=108,
)


_COLUMNMETADATA = _descriptor.Descriptor(
  name='ColumnMetaData',
  full_name='Mysqlx.Resultset.ColumnMetaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Mysqlx.Resultset.ColumnMetaData.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Mysqlx.Resultset.ColumnMetaData.name', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='original_name', full_name='Mysqlx.Resultset.ColumnMetaData.original_name', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table', full_name='Mysqlx.Resultset.ColumnMetaData.table', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='original_table', full_name='Mysqlx.Resultset.ColumnMetaData.original_table', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='schema', full_name='Mysqlx.Resultset.ColumnMetaData.schema', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='catalog', full_name='Mysqlx.Resultset.ColumnMetaData.catalog', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collation', full_name='Mysqlx.Resultset.ColumnMetaData.collation', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fractional_digits', full_name='Mysqlx.Resultset.ColumnMetaData.fractional_digits', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='Mysqlx.Resultset.ColumnMetaData.length', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='Mysqlx.Resultset.ColumnMetaData.flags', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='Mysqlx.Resultset.ColumnMetaData.content_type', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COLUMNMETADATA_FIELDTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=526,
)


_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='Mysqlx.Resultset.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='Mysqlx.Resultset.Row.field', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=528,
  serialized_end=548,
)

_COLUMNMETADATA.fields_by_name['type'].enum_type = _COLUMNMETADATA_FIELDTYPE
_COLUMNMETADATA_FIELDTYPE.containing_type = _COLUMNMETADATA
DESCRIPTOR.message_types_by_name['FetchDoneMoreOutParams'] = _FETCHDONEMOREOUTPARAMS
DESCRIPTOR.message_types_by_name['FetchDoneMoreResultsets'] = _FETCHDONEMORERESULTSETS
DESCRIPTOR.message_types_by_name['FetchDone'] = _FETCHDONE
DESCRIPTOR.message_types_by_name['ColumnMetaData'] = _COLUMNMETADATA
DESCRIPTOR.message_types_by_name['Row'] = _ROW

FetchDoneMoreOutParams = _reflection.GeneratedProtocolMessageType('FetchDoneMoreOutParams', (_message.Message,), dict(
  DESCRIPTOR = _FETCHDONEMOREOUTPARAMS,
  __module__ = 'mysqlx_resultset_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Resultset.FetchDoneMoreOutParams)
  ))
_sym_db.RegisterMessage(FetchDoneMoreOutParams)

FetchDoneMoreResultsets = _reflection.GeneratedProtocolMessageType('FetchDoneMoreResultsets', (_message.Message,), dict(
  DESCRIPTOR = _FETCHDONEMORERESULTSETS,
  __module__ = 'mysqlx_resultset_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Resultset.FetchDoneMoreResultsets)
  ))
_sym_db.RegisterMessage(FetchDoneMoreResultsets)

FetchDone = _reflection.GeneratedProtocolMessageType('FetchDone', (_message.Message,), dict(
  DESCRIPTOR = _FETCHDONE,
  __module__ = 'mysqlx_resultset_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Resultset.FetchDone)
  ))
_sym_db.RegisterMessage(FetchDone)

ColumnMetaData = _reflection.GeneratedProtocolMessageType('ColumnMetaData', (_message.Message,), dict(
  DESCRIPTOR = _COLUMNMETADATA,
  __module__ = 'mysqlx_resultset_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Resultset.ColumnMetaData)
  ))
_sym_db.RegisterMessage(ColumnMetaData)

Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
  DESCRIPTOR = _ROW,
  __module__ = 'mysqlx_resultset_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Resultset.Row)
  ))
_sym_db.RegisterMessage(Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034com.mysql.cj.mysqlx.protobuf'))
# @@protoc_insertion_point(module_scope)
