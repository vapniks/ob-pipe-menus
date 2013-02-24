#!/usr/bin/env python
# OpenBox pipe menu clipboard manager. Show parcellite clipboard, and inserts selected clip.
#
# Copyright 2013 Joe Bloggs (vapniks@yahoo.com)
#
# Installation: copy this file along with ob_paste_clip.py to your openbox config directory
# (on Ubuntu its ~/.config/openbox), then add an item to your openbox menu.xml file
# (also in the config dir) in the form:
#
#   <menu execute="~/.config/openbox/ob_clipboard_manager.py" id="clipboard" label="Clipboard"/>
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
from os.path import expanduser

# following line needs to be set to point the xml file containing your openbox keybindings
historyfile = expanduser('~') + "/.local/share/parcellite/history"


if __name__ == '__main__':
    manager = ob_cb_manager()
    print '<?xml version="1.0" encoding="UTF-8"?>' # header
    print '<openbox_pipe_menu>' # main pipe menu element
    # read the history file
    manager.read_history_file()
    manager.print_all_items()
    print '</openbox_pipe_menu>\n' # end pipe menu element
    

