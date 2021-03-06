# Automatically generated by pb2py
import protobuf as p
from micropython import const
t = p.MessageType('EthereumSignTx')
t.wire_type = const(58)
t.add_field(1, 'address_n', p.UVarintType, flags=p.FLAG_REPEATED)
t.add_field(2, 'nonce', p.BytesType)
t.add_field(3, 'gas_price', p.BytesType)
t.add_field(4, 'gas_limit', p.BytesType)
t.add_field(5, 'to', p.BytesType)
t.add_field(6, 'value', p.BytesType)
t.add_field(7, 'data_initial_chunk', p.BytesType)
t.add_field(8, 'data_length', p.UVarintType)
EthereumSignTx = t