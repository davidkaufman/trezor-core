# Automatically generated by pb2py
import protobuf as p
from micropython import const
t = p.MessageType('TxRequestDetailsType')
t.add_field(1, 'request_index', p.UVarintType)
t.add_field(2, 'tx_hash', p.BytesType)
TxRequestDetailsType = t