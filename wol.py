#!/usr/bin/python2
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
Info: 
Thema: Wake on LAN
Date: 19.8.2014
Version:
"""

from bottle import route, post, get, request
#from bottle import run

from wakeonlan import wol

import xmltodict

html= """<!DOCTYPE html>
<html>
<body>

<h1>{0}</h1>
{1}

</body>
</html>
"""


@route('/', method='GET')
def wol_menue():
    
    # read xml file and convert it do a dict.
    with open('hosts.xml') as fd:
        xml = xmltodict.parse(fd.read())

    # crate table with hosts
    table="""<table border="1">
    <tr>
    <td>Name</td><td>mac</td><td>IP</td><td>Info</td> <td>WakeUP</td>
    </tr>
    {0} </table>"""
    row=""
    for each in xml['hosts']['host']:
        row += """<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td>
        <td>
        <form action="/apps/wol/wol.wsgi" method="get">
        <button name="mac" type="submit" value="{1}">Wake up</button>
        </form>
        </td></tr>""".format(each['name'], each['mac'], each['ip'], each['info'] )
    table= table.format(row)

    # crate final HTML page.
    html_out= html.format( xml['hosts']['title'], table)
    
    # POST methods
    try:
        wol_mac= request.query['mac']
        #print( wol_mac)
    except:
        wol_mac= None

    if wol_mac is not None:
        wol.send_magic_packet(wol_mac)

    return( html_out.encode('utf-8') )

#run(host='localhost', port=8081, debug=True)
