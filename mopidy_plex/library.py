from __future__ import unicode_literals

import logging

from mopidy import backend
from mopidy.models import SearchResult

logger = logging.getLogger(__name__)


class PlexLibraryProvider(backend.LibraryProvider):

    def __init__(self, *args, **kwargs):
        super(PlexLibraryProvider, self).__init__(*args, **kwargs)
        self.remote = self.backend.plex_api

    def find_exact(self, query=None, uris=None):
        return self.search(query=query, uris=uris)

    def search(self, query=None, uris=None):
        logger.debug('Query "%s":' % query)
        if not self.remote.has_connection:
            return []

        if not query:
            # Fetch all data(browse library)
            return SearchResult(uri='plex:search', tracks=self.remote.get_tracks())

        self._validate_query(query)
        if 'any' in query:
            return SearchResult(uri='plex:search-any', tracks=self.remote.get_item_by(query['any'][0]) or [])
        else:
            search = []
            for (field, val) in query.iteritems():
                if field == "album":
                    search.append(val[0])
                if field == "artist":
                    search.append(val[0])
                if field == "track_name":
                    search.append(val[0])
                if field == "date":
                    search.append(val[0])
            logger.debug('Search query "%s":' % search)
            return SearchResult(uri='plex:search-' + '-'.join(search),
                                tracks=self.remote.get_item_by('/'.join(search)) or [])

    def lookup(self, uri):
        try:
            id = uri.split(";")[1]
            logger.debug('Plex track id for "%s": %s' % (id, uri))
            return [self.remote.get_track(id, True)]
        except Exception as error:
            logger.debug('Failed to lookup "%s": %s' % (uri, error))
            return []

    def _validate_query(self, query):
        for (_, values) in query.iteritems():
            if not values:
                raise LookupError('Missing query')
            for value in values:
                if not value:
                    raise LookupError('Missing query')