import unittest

from tweet_dns.sources.icanhazip_source import ICanHazIPSource

class ICanHazIPSourceTest(unittest.TestCase):
    def test_run(self):
        self.assert_(len(list(ICanHazIPSource().get())) == 1)
