****************************
Mopidy-Plex
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-Plex.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-Plex/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/Mopidy-Plex.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-Plex/
    :alt: Number of PyPI downloads

.. image:: https://img.shields.io/travis/rthill/mopidy-plex/master.png?style=flat
    :target: https://travis-ci.org/rthill/mopidy-plex
    :alt: Travis CI build status

.. image:: https://img.shields.io/coveralls/rthill/mopidy-plex/master.svg?style=flat
   :target: https://coveralls.io/r/rthill/mopidy-plex?branch=master
   :alt: Test coverage

Mopidy extension for Plex.tv


Installation
============

Install by running::

    pip install Mopidy-Plex

Or, if available, install the Debian/Ubuntu package from `apt.mopidy.com
<http://apt.mopidy.com/>`_.


Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-Plex to your Mopidy configuration file::

    [plex]
    hostname = <ipaddr>
    port = 32400
    library = 3

To find your library location id, navigate inside a web browser to http://[YOUR_PMS_IP]:32400/library/sections and watch
for a similar entry::

    <Directory allowSync="0" art="/:/resources/artist-fanart.jpg" filters="1" refreshing="0" thumb="/:/resources/artist.png" key="3" type="artist" title="Music" ...
      <Location id="3" path="/media/data1/Music"/>
    </Directory>


Project resources
=================

- `Source code <https://github.com/rthill/mopidy-plex>`_
- `Issue tracker <https://github.com/rthill/mopidy-plex/issues>`_
- `Download development snapshot <https://github.com/rthill/mopidy-plex/archive/master.tar.gz#egg=Mopidy-Plex-dev>`_

Thanks
======

The following extensions are great and helped me a lot to build the Plex extension:

- `Mopidy-Beets <https://github.com/mopidy/mopidy-beets>`_
- `Mopidy-Soundcloud <https://github.com/mopidy/mopidy-soundcloud>`_


Changelog
=========

v0.1.0 (UNRELEASED)
----------------------------------------

- Initial release.