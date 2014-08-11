import re

class SourceBase(object):

    _IP_REGEX = re.compile('(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})')

    def get(self):
        raise RuntimeError("not implemented")

    @classmethod
    def _search_for_ips(cls, text):
        for match in cls._IP_REGEX.finditer(text):
            parts = [int(p) for p in match.group().split('.')]
            for p in parts:
                if p < 0 or p > 255:
                    break
            else:
                yield ".".join([str(p) for p in parts])
