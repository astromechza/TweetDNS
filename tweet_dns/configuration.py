from .exceptions import ConfigKeyError

class Config(object):
    """

    """

    def __init__(self):
        self._tree = {}

    def set(self, param_one, param_two, *other_params):
        """
        Set the given setting value. The path is given as a list of nodes in a
        tree. So set('a', 'b', 'value') will result in {'a':{'b': 'value'}}
        """

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

        keys = tuple([key_one]) + other_keys
        str_keys = [str(k) for k in keys]

        current_level = self._tree
        for k in str_keys[:-1]:
            if k in current_level.keys():
                current_level = current_level[k]
            else:
                raise ConfigKeyError("Key does not exist! %s" % (".".join(str_keys)))
        return current_level[str_keys[-1]]

config = Config()
