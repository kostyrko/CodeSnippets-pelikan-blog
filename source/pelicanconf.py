#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'mkostyrko'
SITENAME = '...z frontu'
SITEURL = ''
SITETITLE = "Notatki z frontu"
SITESUBTITLE = "JS/CSS/PY"
# FAVICON = SITEURL + '/theme/img/favicon.png'
FAVICON = '/theme/img/favicon.png'
# BROWSER_COLOR = "#44151a"


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
# LINKS = (('Przykładowy link', 'http://getpelican.com/'),)


# Social widget <- important begain with small letter
SOCIAL = (
    ('twitter', 'https://twitter.com/m_kostyrko'),
    ('github', 'https://github.com/kostyrko'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = False

DISPLAY_CATEGORIES_ON_MENU = True

MENUITEMS = (("Kategorie", "categories.html"),
    ("Tagi", "tags.html"),
    # ("Sitemap", "/sitemap.xml")
)


#set output path
OUTPUT_PATH = '../output'

#article path
ARTICLE_PATHS = ['articles']

# where to look for the static media files
STATIC_PATHS = ['img', 'pdf', 'custom_css']

# It is not necessary to state the path but it is a good practice to do so
PAGE_PATHS = ['pages']

# set theme folder
THEME = "theme/Flex"

# set plugin folder
PLUGIN_PATHS = ['plugins/', ]


# set tipe_search
USE_TIPUE_SEARCH = True
# integration added based on https://github.com/JackMcKew

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.8, "indexes": 0.6, "pages": 0.7},
    "changefreqs": {"articles": "weekly", "indexes": "daily", "pages": "monthly"},
}

#set plugins
# PLUGINS = ['i18n_subsites', 'post_stats', 'related_posts']
PLUGINS = ['i18n_subsites', 'post_stats', 'related_posts', 'tipue_search']

#set jinja
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

DIRECT_TEMPLATES = (('index','authors', 'tags', 'categories', 'archives','search'))
# DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

# set path for articles/blog posts     
ARTICLE_PATHS = ['articles']

# set path for translation
DEFAULT_LANG = 'pl'
OG_LOCALE = 'pl_PL'
LOCALE = 'pl_PL.UTF-8'
# Default theme language.
I18N_TEMPLATES_LANG = 'en'



# set custom css path 
# in source/theme/Flex/static/custom_css/custom.css
CUSTOM_CSS = 'theme/custom_css/custom.css'

# set to False to disable using the hard-coded combined CSS file
COMBINED_CSS = True

# setting Pygments code highlighter
# from source/theme/static/css/pygments
PYGMENTS_STYLE = 'github'

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

ARTICLE_URL = '{slug}.html'

ARTICLE_SAVE_AS = '{slug}.html'

# ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
# ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

# PAGE_URL = 'pages/{slug}/'
# PAGE_SAVE_AS = 'pages/{slug}/index.html'

# CATEGORY_URL = 'category/{slug}'
# CATEGORY_SAVE_AS = 'category/{slug}/index.html'

# TAG_URL = 'tag/{slug}'
# TAG_SAVE_AS = 'tag/{slug}/index.html'

DISABLE_URL_HASH = True


# set disqus name // link to disqus.com
DISQUS_SITENAME = 'zfrontu'

# set google analytics
GOOGLE_ANALYTICS = "UA-162203128-1"

