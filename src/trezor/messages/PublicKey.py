# Automatically generated by pb2py
import protobuf as p
from micropython import const
from .HDNodeType import HDNodeType
t = p.MessageType('PublicKey')
t.wire_type = const(12)
t.add_field(1, 'node', p.EmbeddedMessage(HDNodeType), flags=p.FLAG_REQUIRED)
t.add_field(2, 'xpub', p.UnicodeType)
PublicKey = t