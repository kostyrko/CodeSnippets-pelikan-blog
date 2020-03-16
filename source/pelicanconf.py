#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'kostyrko'
SITENAME = 'Code Snippets'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# set output folder
OUTPUT_PATH = '../output'

# set theme folder
THEME = 'theme'

# set plugin folder
PLUGIN_PATHS = ['plugins/', ]

# set plugins
PLUGINS = ['i18n_subsites', ]

# add jinja envir. for i18n_subsite
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# setting bootstrap theme
# from source/theme/css
BOOTSTRAP_THEME = 'flatly'

# setting Pygments code highlighter
# from source/theme/css/pygments
PYGMENTS_STYLE = 'monokai'