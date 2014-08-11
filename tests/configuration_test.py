import unittest
import os
import tempfile

from tweet_dns import configuration

class ConfigurationTest(unittest.TestCase):

    def build_fake_config(self, **kwargs):
        kwargs['custom_path'] = os.path.join(tempfile.mkdtemp(), '.config', 'clacks', 'settings')
        return configuration.Config(**kwargs)

    def test_can_touch(self):
        self.assert_(configuration.config.__class__.__name__ == 'Config')

    def test_access(self):

        test_config = self.build_fake_config(auto_load=True)

        test_config.set('key1', 'key2', 'key3', 'value')
        test_config.set('key1', 'key2', 'key4', 'value2')
        test_config.set('key1', 'key2', 'key5', 'key6', 'value3')

        self.assert_(test_config.get('key1', 'key2', 'key3') == 'value')
        self.assert_(test_config.get('key1', 'key2', 'key4') == 'value2')
        self.assert_(test_config.get('key1', 'key2', 'key5', 'key6') == 'value3')


    def test_example(self):
        # set up

        test_config = self.build_fake_config(auto_load=True)

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

    def test_blank_new_config(self):
        c = self.build_fake_config()

        # file should not exist
        self.assert_(not os.path.exists(c.file_path))

        # load
        c.load()

        # config should be blank
        self.assert_(c._tree == {})

        # should not be able to load anything
        with self.assertRaises(KeyError):
            c.get('a')

        # save
        c.save()

        # file should exist
        self.assert_(os.path.exists(c.file_path))

    def test_save_before_load(self):
        c = self.build_fake_config()
        with self.assertRaises(RuntimeError):
            c.save()

    def test_double_load(self):
        c = self.build_fake_config(auto_load=True)
        with self.assertRaises(RuntimeError):
            c.load()

    def test_get_and_set(self):
        # create fake config
        c = self.build_fake_config(auto_load=True)

        # test that set and get work
        c.set('a', 'b', 'hello')
        self.assert_(c.get('a', 'b') == 'hello')
        self.assert_(c._tree == {'a':{'b':'hello'}})

        # save
        c.save()

        # open new config with same file
        c2 = configuration.Config(custom_path=c.file_path, auto_load=True)

        # check that contents are the same
        self.assert_(c.get('a', 'b') == 'hello')
