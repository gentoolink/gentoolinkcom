#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gentoolink Web Services Inc.'
SITENAME = u'Gentoolink Web Services'
SITEURL = ''

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'darkly'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PATH = 'content'

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
LINKS = (('Support', 'http://desk.zoho.com/support/kenmcgonigal'),
         ('Nextcloud', 'http://nextcloud.com/'),
         ('My Blog', '/category/blog.html'),
         ('Inspire Wear Store', 'https://inspirewear.store'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/gentoolink'),
          ('Facebook', 'https://facebook.com/ken.mcgonigal'),
	('Github', 'https://github.com/gentoolink'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
