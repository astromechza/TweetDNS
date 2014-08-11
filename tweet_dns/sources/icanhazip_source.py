import urllib2

from .source_base import SourceBase

class ICanHazIPSource(SourceBase):
    def get(self):
        return self._search_for_ips(urllib2.urlopen('http://www.icanhazip.com').read())

