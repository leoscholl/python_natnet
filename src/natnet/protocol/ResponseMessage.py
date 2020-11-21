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
        """Deserialize an Request message.

        :type data: ParseBuffer
        :type version: Version"""

        response = data.unpack_cstr(256)
        return cls(response)

    def serialize(self, version=None):
        return self.response.encode('utf-8') + b'\0'*(256 - len(self.response))