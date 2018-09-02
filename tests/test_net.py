import pytest

from io import BytesIO as _BytesIO

from bitcoin.core import lx

from squeak.core.signing import CSigningKey
from squeak.net import CInv
from squeak.net import CSqueakLocator
from squeak.net import CInterested


@pytest.fixture
def signing_key():
    return CSigningKey.generate()


@pytest.fixture
def verifying_key(signing_key):
    return signing_key.get_verifying_key()


@pytest.fixture
def fake_squeak_hash():
    return lx('DEADBEAFDEADBEAFDEADBEAFDEADBEAFDEADBEAFDEADBEAFDEADBEAFDEADBEAF')


class TestCInv(object):
    def test_serialization(self):
        inv = CInv(type=1)
        stream = _BytesIO()

        inv.stream_serialize(stream)
        serialized = _BytesIO(stream.getvalue())

        deserialized = CInv.stream_deserialize(serialized)

        assert deserialized.typemap[deserialized.type] == "Squeak"
        assert deserialized == inv


class TestCSqueakLocator(object):
    def test_serialization(self, verifying_key, fake_squeak_hash):
        interested = [
            CInterested(verifying_key.serialize(), -1, 10, fake_squeak_hash),
            CInterested(verifying_key.serialize(), 30, 2000, fake_squeak_hash),
        ]
        locator = CSqueakLocator(interested)
        stream = _BytesIO()

        locator.stream_serialize(stream)
        serialized = _BytesIO(stream.getvalue())

        deserialized = CSqueakLocator.stream_deserialize(serialized)
        assert deserialized == locator
        assert len(deserialized.vInterested) == 2
