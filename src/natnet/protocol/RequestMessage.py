# coding: utf-8
"""RecordingMessage message implementation.
"""
import attr

from .common import MessageId, ParseBuffer, Version, register_message


@register_message(MessageId.Request)
@attr.s
class RequestMessage(object):

    command = attr.ib()  # type: str

    @classmethod
    def deserialize(cls, data, version):
        """Deserialize an Request message.

        :type data: ParseBuffer
        :type version: Version"""

        command = data.unpack_cstr(256)
        return cls(command)

    def serialize(self, version=None):
        return self.command.encode('utf-8') + b'\0'*(256 - len(self.command))
