# coding: utf-8
"""Response message implementation.
"""
import attr

from .common import MessageId, ParseBuffer, Version, register_message


@register_message(MessageId.Response)
@attr.s
class ResponseMessage(object):

    response = attr.ib()  # type: str

    @classmethod
    def deserialize(cls, data, version):
        """Deserialize an Response message.

        :type data: ParseBuffer
        :type version: Version"""

        response = data.unpack_cstr()
        return cls(response)

    def serialize(self, version=None):
        return self.response.encode('utf-8') + b'\0'*(256 - len(self.response))