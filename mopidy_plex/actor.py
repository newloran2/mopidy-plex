from __future__ import unicode_literals

import logging
import pykka

from mopidy import backend

from .library import PlexLibraryProvider
from .plex import PlexRemoteClient

logger = logging.getLogger(__name__)


class PlexBackend(pykka.ThreadingActor, backend.Backend):

    def __init__(self, config, audio):
        super(PlexBackend, self).__init__()

        plex_endpoint = 'http://%s:%s/library/sections/%s' % (config['plex']['hostname'],
                                                              config['plex']['port'],
                                                              config['plex']['library'])
        self.plex_api = PlexRemoteClient(plex_endpoint)
        self.library = PlexLibraryProvider(backend=self)
        self.playback = PlexPlaybackProvider(audio=audio, backend=self)
        # self.playlists = None

        self.uri_schemes = ['plex']


class PlexPlaybackProvider(backend.PlaybackProvider):

    def play(self, track):
        id = track.uri.split(';')[1]
        logger.info('Getting info for track %s with id %s' % (track.uri, id))
        track = self.backend.plex_api.get_track(id, True)
        return super(PlexPlaybackProvider, self).play(track)
