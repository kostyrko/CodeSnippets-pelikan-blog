#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'mkostyrko'
SITENAME = 'Notatki z frontu'
SITEURL = 'http://localhost:8000'
SITETITLE = "Notatki z frontu"
SITESUBTITLE = "JS/CSS/PY"
FAVICON = SITEURL + 'theme/img/favicon.ico'
BROWSER_COLOR = "#383838"

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
LINKS = (('Pelian', 'http://getpelican.com/'),)


# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/m_kostyrko'),
    ('Github', 'https://github.com/kostyrko'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MAIN_MENU = True

DISPLAY_CATEGORIES_ON_MENU = True

# MENUITEMS = (('CSS', '/css.html'),
#              ('JS', '/js.html'))

#set output path
OUTPUT_PATH = '../output'

#article path
ARTICLE_PATHS = ['articles']

# where to look for the static media files
STATIC_PATHS = ['img', 'pdf']

# It is not necessary to state the path but it is a good practice to do so
PAGE_PATHS = ['pages']

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


# set path for articles/blog posts     
# ARTICLE_PATHS = ['articles']

# set path for translation
DEFAULT_LANG = 'pl'
OG_LOCALE = 'pl_PL'
LOCALE = 'pl_PL.UTF-8'
# Default theme language.
I18N_TEMPLATES_LANG = 'en'


# set custom css path
# CUSTOM_CSS = 'static/custom.css'

# set to False to disable using the hard-coded combined CSS file
# COMBINED_CSS = True

# setting Pygments code highlighter
# from source/theme/static/css/pygments
PYGMENTS_STYLE = 'monokai'

# few ideas taken from https://github.com/pzelnip/www.codependentcodr.com/blob/master/pelicanconf.py
# set copyright year
COPYRIGHT_YEAR = str(datetime.now().year)

# license
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
}

# defining url structure

ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'