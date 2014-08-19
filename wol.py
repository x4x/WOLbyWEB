#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

"""
Wake on LAN WEB interface for waking up server sided systehms.
Copyright (C) 2013 x4x georg.la8585@gmx.at

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

Name: wol.py
Programteil: 
Thema: Wake on LAN
Date: 19.8.2014
Version:
"""

from bottle import route
from bottle import run

from wakeonlan import wol

from xml.dom.minidom import parse, parseString

@route('/')
def wol_menue():
    dom1 = parse( "hosts.xml" )

    hosts= dom1.getElementsByTagName('hosts')
    help(hosts)
    return( dom1.toxml())

run(host='localhost', port=8080, debug=True)
