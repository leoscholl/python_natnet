"""Tests for parsing and creating Response messages."""

from natnet.protocol import EchoResponseMessage, Version, deserialize, serialize  # noqa: F401

def test_real_packet():
    import natnet
    client = natnet.Client.connect()
    response = client._send_command_and_wait("LiveMode")
    assert response

if __name__ == "__main__":
    test_real_packet()