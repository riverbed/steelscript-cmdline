
from __future__ import (absolute_import, unicode_literals, print_function,
                        division)

import re

from pq_cmdline import channel

# Fill in abstract methods so we can instantiate a Chennel
class FakeChannel(channel.Channel):
    def receive_all(self):
        return ''

    def send(self, text_to_send):
        pass

    def expect(self, match_res, timeout):
        return '', re.search(match_res, '')


def test_safe_line_feeds():
    c = FakeChannel()
    assert c.safe_line_feeds(' \n \r ') == ' \\n \\r '


def test_fixup_carriage_returns():
    c = FakeChannel()
    assert c.fixup_carriage_returns('a\r\r\nb\n\rc\n\r') == 'a\nb\nc\n\r'