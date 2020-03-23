#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'mkostyrko'
SITENAME = 'Notatki z frontu'
SITEURL = ''
FAVICON = SITEURL + 'theme/img/favicon.ico'

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'pl'

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
SOCIAL = (
    ('Twitter', 'https://twitter.com/m_kostyrko'),
    ('Github', 'https://github.com/kostyrko'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#set output path
OUTPUT_PATH = '../output'

# set theme folder
THEME = "theme/Flex"

# set plugin folder
PLUGIN_PATHS = ['plugins/', ]

#set plugins
PLUGINS = ['i18n_subsites']

#set jinja
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# setting Pygments code highlighter
# from source/theme/static/css/pygments
PYGMENTS_STYLE = 'monokai'

MAIN_MENU = True

# set path for articles/blog posts     
# ARTICLE_PATHS = ['articles']

# set path for translation