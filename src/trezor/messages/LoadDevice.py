# Automatically generated by pb2py
import protobuf as p
from micropython import const
from .HDNodeType import HDNodeType
t = p.MessageType('LoadDevice')
t.wire_type = const(13)
t.add_field(1, 'mnemonic', p.UnicodeType)
t.add_field(2, 'node', p.EmbeddedMessage(HDNodeType))
t.add_field(3, 'pin', p.UnicodeType)
t.add_field(4, 'passphrase_protection', p.BoolType)
t.add_field(5, 'language', p.UnicodeType, default=u'english')
t.add_field(6, 'label', p.UnicodeType)
t.add_field(7, 'skip_checksum', p.BoolType)
LoadDevice = t