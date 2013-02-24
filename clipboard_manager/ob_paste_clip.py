#!/usr/bin/env python
# Script for pasting clips from cliboard manager. Required by ob_clipboard_manager.py
#
# Copyright 2013 Joe Bloggs (vapniks@yahoo.com)
#
# Installation: this file should be copied along with ob_clipboard_manager.py & ob_clipboard_pipe_menu.py
# to your openbox config directory (on Ubuntu its ~/.config/openbox/).
# See ob_clipboard_pipe_menu.py for further installation instructions.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from ob_clipboard_manager import ob_cb_manager
import gtk


manager = ob_cb_manager()

