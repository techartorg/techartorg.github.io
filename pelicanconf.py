#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import datetime

CURRENT_YEAR = datetime.datetime.now().year

AUTHOR = 'TAO-community'
SITENAME = 'Tech-Artists.Org Wiki'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

THEME = 'themes/tao-wiki-bootstrap-next'

BOOTSTRAP_THEME = 'tao'

PLUGIN_PATHS = ['plugins/pelican-plugins', 'plugins/tao']
PLUGINS = [
    'i18n_subsites',
    'pelican-page-hierarchy',
    'data_driven_wiki',
    'page_tags',
    'page_contributors',
    'page_post_auto_format',
]

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

GITHUB_REPO = 'https://github.com/techartorg/techartorg.github.io'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Tech-Artists.Org', 'http://discourse.techart.online'),
    ('Tech-Artists YouTube', 'https://www.youtube.com/channel/UC99UTFaBcPAf6pbYhU8B9nQ'),
)

# Social widget
SOCIAL = (('Tech-Artists Slack', 'https://tech-artists.slack.com'),)

DEFAULT_PAGINATION = False

BOOTSTRAP_FLUID = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True