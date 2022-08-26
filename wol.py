#! /usr/bin/env python3
# -*- coding: iso-8859-1 -*-

"""
Wake on LAN WEB interface for waking up server sided systehms.
Copyright (C) 2013 x4x georg.la8585@gmx.at

Updated to new dependencies (C) 2020 sharkcow@gmx.de

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
Date: 26.10.2020
Version: 1.3
23.09.20 V1.2: updated to new dependecies
26.10.20 V1.3: added running detection via ping
"""

from bottle import route, post, get, request
#from bottle import run

import wakeonlan as wol

import xmltodict
import subprocess
import timer
import os
from datetime import datetime

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

    # create table with hosts
    table="""<table border="1">
    <tr>
    <td>Name</td><td>running</td><td>Wake up</td><td>MAC</td><td>IP</td><td>Info</td>
    </tr>
    {0} </table>"""
    row=""
    
    running = "yes", "no"
    for each in xml['hosts']['host']:
        with open(os.devnull, "wb") as limbo:
            ping=subprocess.Popen(["ping", "-c", "1", "-n", "-w", "1", each['ip']],
                stdout=limbo, stderr=limbo).wait()

        row += """<tr><td>{0}</td><td>{4}</td>
        <td>
        <form action="/" method="get">
        <button name="mac" type="submit" value="{1}">Wake up</button>
        </form>
        </td><td>{1}</td><td>{2}</td><td>{3}</td>
        </tr>""".format(each['name'], each['mac'], each['ip'], each['info'], running[ping])
    table= table.format(row)

    # create final HTML page.
    html_out= html.format(xml['hosts']['title'], table)

    # POST methods
    try:
        wol_mac= request.query['mac']
    except:
        wol_mac= None

    if wol_mac is not None:
        wol.send_magic_packet(wol_mac)

    return( html_out.encode('utf-8') )
