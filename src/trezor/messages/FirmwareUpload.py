# Automatically generated by pb2py
import protobuf as p
from micropython import const
t = p.MessageType('FirmwareUpload')
t.wire_type = const(7)
t.add_field(1, 'payload', p.BytesType, flags=p.FLAG_REQUIRED)
FirmwareUpload = t