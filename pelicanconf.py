#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Oscar A. Mata T.'
SITENAME = u'Tektronica'
SITEURL = 'https://omata.github.io'
THEME = '/home/omata/Documentos/pelican/pelican-themes/pelican-bootstrap3/'
PLUGIN_PATHS = ['/home/omata/Documentos/pelican/pelican-plugins']
PLUGINS = ['googleplus_comments', 'just_table']

# Configuración de PyEmbed
from pyembed.markdown import PyEmbedMarkdown
MD_EXTENSIONS = [PyEmbedMarkdown()]

PATH = 'content'
TIMEZONE = 'America/Caracas'
DEFAULT_LANG = u'es'

# Configuración del tema de pelican-bootstrap3
BOOTSTRAP_THEME = 'slate'

# Otras variables
GITHUB_URL = 'https://github.com/omata'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Otros Sitios', '#'),)

# Social widget
SOCIAL = (('Twitter', '#'),
          ('LinkedIn', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
