#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'臺大開源社'
SITENAME = u'臺灣大學開源社 / NTU Open Source Community'
SITESUBTITLE = '讓我們一起推廣開源理念，許世界更美好的未來！'
SITEURL = ''

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'zh-TW'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Resources
PATH = 'content'
STATIC_PATHS = ['images', 'vendor']
THEME = 'themes/ntuosc'

# Alter template behavior
DIRECT_TEMPLATES = ('index', 'archives')
PAGINATED_DIRECT_TEMPLATES = ('archives',)

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
ARTICLE_LANG_URL = ARTICLE_URL + '{lang}/'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_LANG_URL = PAGE_URL + '{lang}/'
PAGE_LANG_SAVE_AS = PAGE_LANG_URL + 'index.html'

ARCHIVES_URL = 'posts/'
ARCHIVES_SAVE_AS = 'posts/index.html'

CATEGORIES_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)


# Metadata
LINKS =  []
SOCIAL = []

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
