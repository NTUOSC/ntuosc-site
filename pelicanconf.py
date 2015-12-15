#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'臺大開源社'
SITENAME = u'臺灣大學開源社'
SITESUBTITLE = '資訊時代公民的必備技能點'
SITEURL = ''
SITETITLE = '開源，改造全世界'
SITEDESCRIPTION = '''
<p>面對高漲的物價、滿街的廢水、爆炸的小鴨，捍衛公民權利的你，也許會有蚍蜉撼樹之感？<br>如果有個理念，得以貫徹自由開放的價值，你願意把握它嗎？</p>
<p>開放原始碼蔚為全球潮流，從 Linux 到 Android，我們早已身處 open source 的世界中；<br>無論你對電腦了解與否，都能跟著全球的開源人改造社會。</p>
<p><strong>歡迎加入臺大開源社！</strong>讓我們一起推廣開源理念，許世界更美好的未來！</p>
'''

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'zh-TW'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Resources
IGNORE_FILES = ['*.md']
ARTICLE_PATHS = ['posts']
ARTICLE_EXCLUDES = ['output', 'themes', 'vendor', 'pages']
STATIC_PATHS = ['images', 'vendor', 'opendata', 'CNAME']
THEME = 'themes/ntuosc'

DEFAULT_DATE = 'fs'
FILENAME_METADATA = r'(?P<slug>[A-Za-z0-9_-]+).*'
EXTRA_PATH_METADATA = {
    'images/favicon.png': {'path': 'favicon.png'},
}

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

DEFAULT_PAGINATIONS = 3
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)


# Metadata
LINKS =  []
SOCIAL = (
    ('Forum', 'https://www.facebook.com/groups/NTUOSC/'),
    ('Facebook', 'https://www.facebook.com/NTUOSC'),
    ('GitHub', 'https://github.com/NTUOSC'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
