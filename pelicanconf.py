#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gentoolink Web Services Inc.'
SITENAME = u'Gentoolink Web Services'
SITEURL = ''

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PATH = 'content'


FAVICON = 'images/favpenguin.png'
SITELOGO = 'images/logo.png'
SITELOGO_SIZE = '60x60'
BANNER = 'images/header.jpg'
BANNER_ALL_PAGES = True

TWITTER_WIDGET_ID= 'twsrc%5Etfw'
TWITTER_USERNAME = 'gentoolink'

PLUGIN_PATHS = ['/home/gentoolink/websites/pelican-plugins/']
PLUGINS = ['i18n_subsites']


TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = u'en'

#This is where my blog posts will be kept.
ARTICLE_PATHS = ['blog']


# Delete the output directory, and all of its contents, before generating new files. This can be useful in preventing older, unnecessary files from persisting in your output. However, this is a destructive setting and should be handled with extreme care.
#DELETE_OUTPUT_DIRECTORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Bookmarks
LINKS = (('Helpdesk', 'https://helpdesk.gentoolink.com'),
         ('Nextcloud', 'http://nextcloud.com/'),
         ('My Blog', '/category/blog.html'),
         ('Python', 'https://www.python.org/'),
	 ('Django', 'https://www.djangoproject.com/'),
	)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/gentoolink'),
          ('Facebook', 'https://facebook.com/ken.mcgonigal'),
	('Github', 'https://github.com/gentoolink'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Change the menu order. Stop using categories
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True


GOOGLE_ANALYTICS = 'UA-63217115-2'
DISQUS_SITENAME = 'gentoolink-com.'

