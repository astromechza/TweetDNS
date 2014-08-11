import unittest

from tweet_dns import configuration

class ConfigurationTest(unittest.TestCase):

    def test_can_touch(self):
        self.assert_(configuration.config.__class__.__name__ == 'Config')

    def test_access(self):

        test_config = configuration.Config()

        test_config.set('key1', 'key2', 'key3', 'value')
        test_config.set('key1', 'key2', 'key4', 'value2')
        test_config.set('key1', 'key2', 'key5', 'key6', 'value3')

        print test_config._tree

        self.assert_(test_config.get('key1', 'key2', 'key3') == 'value')
        self.assert_(test_config.get('key1', 'key2', 'key4') == 'value2')
        self.assert_(test_config.get('key1', 'key2', 'key5', 'key6') == 'value3')
