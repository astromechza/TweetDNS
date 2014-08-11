import unittest

from tweet_dns.sources.source_base import SourceBase

class SourceBaseTest(unittest.TestCase):

    def test_regex(self):

        text = """
            1.1.1.1

            192.168.0.1

            127.0.0.1

            255.255.255.255

            256.

            1.1..1

            1.200.3.4
        """

        correct_ips = ['1.1.1.1', '192.168.0.1', '127.0.0.1', '255.255.255.255', '1.200.3.4']

        self.assert_(list(SourceBase._search_for_ips(text)) == correct_ips)

        with self.assertRaises(RuntimeError):
            SourceBase().get()
