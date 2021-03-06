# Automatically generated by pb2py
import protobuf as p
from micropython import const
t = p.MessageType('CipherKeyValue')
t.wire_type = const(23)
t.add_field(1, 'address_n', p.UVarintType, flags=p.FLAG_REPEATED)
t.add_field(2, 'key', p.UnicodeType)
t.add_field(3, 'value', p.BytesType)
t.add_field(4, 'encrypt', p.BoolType)
t.add_field(5, 'ask_on_encrypt', p.BoolType)
t.add_field(6, 'ask_on_decrypt', p.BoolType)
t.add_field(7, 'iv', p.BytesType)
CipherKeyValue = t