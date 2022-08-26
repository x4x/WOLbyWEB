#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

"""
Wake on LAN WEB interface for waking up server sided systehms.
Copyright (C) 2022 x4x georg.la8585@gmx.at

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

Name: run.py
Info:
Thema: Wake on LAN
Date: 24.08.2022
"""

from bottle import run

import wol
run(host='0.0.0.0', port=80, debug=False)
