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

        self.assert_(test_config.get('key1', 'key2', 'key3') == 'value')
        self.assert_(test_config.get('key1', 'key2', 'key4') == 'value2')
        self.assert_(test_config.get('key1', 'key2', 'key5', 'key6') == 'value3')


    def test_example(self):
        # set up

        test_config = configuration.Config()

        test_config.set('users', 1, 'name', 'Joe Soap')
        test_config.set('users', 1, 'email', '1.example.com')
        test_config.set('users', 1, 'city', 'Cape Town')

        test_config.set('users', 2, 'name', 'John Smith')
        test_config.set('users', 2, 'email', '2.example.com')
        test_config.set('users', 2, 'city', 'London')

        test_config.set('users', 'count', 2)

        test_config.set('complex', {'a': 'b'})

        # test

        self.assert_(test_config.get('complex') == {'a':'b'})

        for i in xrange(test_config.get('users', 'count')):

            self.assert_(test_config.get('users', i+1, 'name') != None)
            self.assert_(test_config.get('users', i+1, 'city') != None)
            self.assert_(test_config.get('users', i+1, 'email') == "%s.example.com" % (i+1))
