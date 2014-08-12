import os
import json

from .exceptions import ConfigKeyError

class Config(object):

    _DEFAULT_CONFIG_PATH = '~/.config/tweet_dns/settings'

    def __init__(self, custom_path=_DEFAULT_CONFIG_PATH, auto_load=False):
        self.loaded = False
        self.file_path = os.path.expanduser(custom_path)
        if auto_load:
            self.load()

    def load(self):
        if self.loaded:
            raise RuntimeError ("Config has already been loaded!")
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as text_file:
                self._tree = json.loads(text_file.read())
        else:
            self._tree = {}
        self.loaded = True

    def save(self):
        if not self.loaded:
            raise RuntimeError("Config has not been loaded yet!")

        content = json.dumps(self._tree)

        # make sure correct directories exist
        directory = os.path.dirname(self.file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # save to file
        with open(self.file_path, "w") as text_file:
            text_file.write(content)

    def set(self, param_one, param_two, *other_params):
        """
        Set the given setting value. The path is given as a list of nodes in a
        tree. So set('a', 'b', 'value') will result in {'a':{'b': 'value'}}
        """

        if not self.loaded:
            raise RuntimeError("Config has not been loaded yet!")

        params = (param_one, param_two) + other_params
        str_params = [str(p) for p in params[:-1]]

        value = params[-1]

        current_level = self._tree
        for k in str_params[:-1]:
            if not k in current_level.keys():
                current_level[k] = {}
            current_level = current_level[k]
            if type(current_level) != dict:
                raise ConfigKeyError("Key does not map to lower level! %s" % ('.'.join(str_params)))
        current_level[str_params[-1]] = value

    def get(self, key_one, *other_keys):
        """
        """

        if not self.loaded:
            raise RuntimeError("Config has not been loaded yet!")

        keys = tuple([key_one]) + other_keys
        str_keys = [str(k) for k in keys]

        current_level = self._tree
        for k in str_keys[:-1]:
            if k in current_level.keys():
                current_level = current_level[k]
            else:
                raise ConfigKeyError("Key does not exist! %s" % (".".join(str_keys)))
        return current_level[str_keys[-1]]

config = Config(auto_load=True)
