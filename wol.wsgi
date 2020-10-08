#!/usr/bin/python2
# -*- coding: iso-8859-1 -*-

import sys, os, bottle

sys.path = ['/home/x4x/srv/www-priv-wsgi/wol/'] + sys.path
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import wol # This loads your application

application = bottle.default_app()
