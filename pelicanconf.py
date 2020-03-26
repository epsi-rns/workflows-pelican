#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

# -- -- -- Pelican Configuration Starts Here

AUTHOR = 'epsi'
SITENAME = 'Yet Another Static Blog'
SITEURL = '/workflows-pelican/'

THEME = "tutor-07"

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 1

# Feed generation is usually not desired when developing
FEED_RSS              = 'feed.xml'
FEED_ALL_ATOM         = None
CATEGORY_FEED_ATOM    = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM      = None
AUTHOR_FEED_RSS       = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

INDEX_URL             = 'blog/'
INDEX_SAVE_AS         = 'blog/index.html'

ARTICLE_URL           = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS       = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

ARCHIVES_SAVE_AS      = 'archives.html'
YEAR_ARCHIVE_SAVE_AS  = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%m}/index.html'

# No slash / at the end, for pagination friendly.

TAG_URL               = 'tag/{slug}'
TAG_SAVE_AS           = 'tag/{slug}.html'

CATEGORY_URL          = 'category/{slug}'
CATEGORY_SAVE_AS      = 'category/{slug}.html'

AUTHOR_URL            = 'author/{slug}'
AUTHOR_SAVE_AS        = 'author/{slug}.html'

# Custom Theme Variables

CURRENTYEAR = date.today().year


# Opengraph
OG_LOCALE = "en_US"
OG_LOGO   = "/assets/images/logo-gear-opengraph.png"

# Service

# GOOGLE_ANALYTIC_KEY = ""
# DISQUS_KEY = ""

# -- -- -- Pelican Configuration End Here

# Plugin, Filter, Data

# Fix netlify path, credit to Leksono Nanto

import os, sys

path_this = os.path.dirname(os.path.abspath(__file__))
path_lib = os.path.abspath(os.path.join(path_this, 'lib'))
path_plugins = os.path.abspath(os.path.join(path_this, 'plugins'))
sys.path.append(path_lib)
sys.path.append(path_plugins)

# -- Plugins --

from jinja2content import jinja2content

PLUGINS = [
    # ...
    "jinja2content",
]

# -- Filter --
# https://linkpeek.com/blog/how-to-add-a-custom-jinja-filter-to-pelican.html

from libfilter import *
JINJA_FILTERS = {
  'shuffle'    : filter_shuffle,
  'split'      : filter_split,
  'navigation' : filter_navigation,
  'keyjoin'    : filter_keyjoin,
}

# -- Data --

# Blogroll: Helper for friends widget
from friends import *
from archives_gitlab import *
from archives_github import * 
from archives_pelican import *
