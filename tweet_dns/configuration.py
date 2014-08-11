class Config(object):
    """

    """

    def __init__(self):
        self._tree = {}

    def set(self, *params):
        """
        Set the given setting value. The path is given as a list of nodes in a
        tree. So set('a', 'b', 'value') will result in {'a':{'b': 'value'}}
        """

        keys = params[:-1]
        value = params[-1]

        # keys must be present
        if len(keys) == 0:
            raise RuntimeError("Node structure must contain a key!")

        current_level = self._tree
        str_keys = [str(k) for k in keys]
        for k in str_keys[:-1]:
            if not k in current_level.keys():
                current_level[k] = {}
            current_level = current_level[k]

        current_level[str_keys[-1]] = value

    def get(self, *keys):

        # keys must be present
        if len(keys) == 0:
            raise RuntimeError("Node structure must contain a key!")

        current_level = self._tree
        str_keys = [str(k) for k in keys]
        for k in str_keys[:-1]:
            if k in current_level.keys():
                current_level = current_level[k]
            else:
                raise RuntimeError("Key does not exist! %s" % (".".join(str_keys)))
        return current_level[str_keys[-1]]

config = Config()
