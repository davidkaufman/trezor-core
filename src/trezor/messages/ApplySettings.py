# Automatically generated by pb2py
import protobuf as p
from micropython import const
t = p.MessageType('ApplySettings')
t.wire_type = const(25)
t.add_field(1, 'language', p.UnicodeType)
t.add_field(2, 'label', p.UnicodeType)
t.add_field(3, 'use_passphrase', p.BoolType)
t.add_field(4, 'homescreen', p.BytesType)
ApplySettings = t