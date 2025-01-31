"""Test for localtuya."""

from . import *
from custom_components.localtuya.discovery import TuyaDiscovery


DEVICE3_3 = b"\x00\x00U\xaa\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\x9c\x00\x00\x00\x00\xd0\x97fgo3i\xeb\x10\xb5\xe9\xf12\xfd\x80*\xfcL\xa4\x07\xf4\x8b\x98A\xad\xe0d\xbd\xa76\x9d\xa2\xb6^b\xea\xdc7\x1d\xb4!'\x98\xca\x04+\xff\xc3\xd9I_\xff\x17L)\x02\xe4^;:\xad$\x8f^\xc2\xfb\x84Y\xb1\x15_\xc7]K\xf6i\x9f\x92\xcb\xa4\xc0\xbaR\x01H\x04^v\x05\xfa\x04\x98\xdf\xeaZ\xab\xf1\xb12s\x08\xc3\x92q\x11\xc6!H\x94*+\xc1\x96\xcb\xf5b\x168\xef\x10\x01d\xbb\x81\x94n\xa8]n\xda\x8e\xea@\xe9;\x1e?\xc1J%p\xe1\x82yf3\xd2\xf1\x00\x00\xaaU"
DEVICE3_4 = b"\x00\x00U\xaa\x00\x00\x00\x00\x00\x00\x00#\x00\x00\x00\xbc\x00\x00\x00\x00\xd0\x97fgo3i\xeb\x10\xb5\xe9\xf12\xfd\x80*L+\xe5,T(z\x15\xb0(+\xe3\x88\xa4T\x0eYb\xdd\x10\xb3\xf1f%\x8f\xff\xbc\x11q>-}-\xaf_kr\xdb\x94?\xb0\x82D\xc3\xe4\xee\x98\xf0\xc2\xfb\x84Y\xb1\x15_\xc7]K\xf6i\x9f\x92\xcb\xa4\xc0\xbaR\x01H\x04^v\x05\xfa\x04\x98\xdf\xeaZ\xab'\xa7\xaf\xd2\xbdmF\xefr\xb6\xdfi\xa1V\x00-<\x9d\xd05t\xec\x0e\x0b\r\x8f\x86\x0f7KA\x98\x06\x16\xcdD\x03ov\x01\xabq\xf0\xaa\x83\x91\xa5\\\xe0\x91:y7B2+\x90\x96IH\xda\xd4\xb6\x0c\xc0\t{l\xdc\xaaZ\x14\x82#\xb3$f\x86\xa1.\xbb\x961[\x00\x00\xaaU"
DEVICE3_5 = b"\x00\x00f\x99\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\xf0\x93\x07 \xd5\x92~\xcf\xf2\x91\x85S\xdc\x9f\x8dY=dS\x18\xca>\xae\xc2\xcf\xe7iV\xf2{\xc4!\xe7\xb8\x00i\x11K\x11j\x0e5\xed\x8c\xe7mO\x91c\xceAGS\x7f@\xd6\x12\n\xce\x92\xb4\x9a\xe5\xef\xf4\x8e\xdf\xd3\xe1\xda\rt\xf1\xee\x1b\x86z\xb28\x9a\x11\xebx\x9c\xe4\x9b\x19t6L\x13JZ7\xe7\xa6\x88\xb9\xa9\xcc\xf91\xdc\x8f\x1d%>\x13\x10M'\xeeG\x9e\xf7\xe5\xd6\xdeK1W\xe0\xa9\xf5\x8c\\\xa1\xd6<\x1e\x1ec\xfb\xc9 CV\x9d\xa3C@I\x1c\x15\xb4=6\xa0\xce\n+\xef\x1c\xc1\x96\xf1_\xc0Y2\xe2\xcd\xc4j\xa7H\xcf\xe1B\xe1\xed^\x98\xfe;\xf1P:!%\x82*\xc9\xf6\xbd\x17\x8e\xd9\xb5\xdf\xba\x19\x8d\x03\x9b\xfa\x00\x99s\xd6t\x0eD=&\xd8\xd1\xd7\x827\xec\xac\xf2\x19\x8a\xfe\x94\x1f\xd5\xe6\xe1a\xc1\xfb 1\xa8\xf4]vd\x18\xed\x86<\x11\x13\xde\x14\xf2\xba\x00\x00\x99f"


@pytest.mark.asyncio
async def test_dsicovery():
    mock_callback = AsyncMock()
    discovery = TuyaDiscovery(mock_callback)

    discovery.datagram_received(DEVICE3_3, None)
    discovery.datagram_received(DEVICE3_4, None)
    discovery.datagram_received(DEVICE3_5, None)

    mock_callback.assert_called()
    assert len(discovery.devices) == 3
