#!/usr/bin/env python
# OpenBox pipe menu clipboard manager. Show parcellite clipboard, and inserts selected clip.
#
# Copyright 2013 Joe Bloggs (vapniks@yahoo.com)
#
# Installation: copy this file along with ob_paste_clip.py & ob_clipboard_pipe_menu.py to your openbox
# config directory (on Ubuntu its ~/.config/openbox).
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

import struct
from os.path import expanduser

class ob_cb_manager:
    def __init__(self): # constructor 
        # alter the following line if your history file is found elsewhere
        self.__historyfile = expanduser('~') + "/.local/share/parcellite/history"
        self.__clippings = []
    
    # def add_to_history(self,text):
    #     self.clipboard = gtk.clipboard_get(gtk.gdk.SELECTION_CLIPBOARD)
    #     self.clipboard.set_text(text)
    #     self.clipboard.store()    

    def read_history_file(self, filepath=None):
        if filepath is None:
            filepath = self.__historyfile
        self.__clippings = []
        # open the file as binary
        f = open(filepath,"rb")
        # read the first 4 bytes (which should indicate the size of the first clipping)
        size = struct.unpack('i',f.read(4))[0]
        # stop if we reach a clipping of length 0
        while size != 0:
            # read the clipping and append it to clippings
            self.__clippings.append(f.read(size))
            # read the next 4 bytes
            data = f.read(4)
            # convert to a size, or quit if we've reached the end of the file
            if data:
                size = struct.unpack('i',data)[0]
            else:
                size = 0

    def print_all_items(self):
        for i in range(0,len(self.__clippings)-1):
            clip = self.__clippings[i]
            sanetext = clip.split('\n',1)[0].replace('"','').replace('<','').replace('>','')
            # command = "sh -c 'echo " + sanetext + "| xsel -i -b; xsel -b | xvkbd -xsendevent -file - 2>/dev/null'"
            command = " hi " # need to execute ob_paste_clip.py file with clip number as argument
            print '<item label="' + sanetext + '">\n<action name="execute"><execute>' + \
                command + '</execute></action>\n</item>'


