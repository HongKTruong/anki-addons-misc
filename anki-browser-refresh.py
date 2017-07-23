# -*- coding: utf-8 -*-

"""
Anki Add-on: Refresh Browser List

Refreshes browser view and optionally changes the sorting column
(e.g. to show newly added cards since last search)

Copyright: (c) Glutanimate 2016-2017
License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
"""

# Do not modify the following line
from __future__ import unicode_literals

######## USER CONFIGURATION START ########

SORTING_COLUMN = "noteCrt"
# Custom column sorting applied on hotkey toggle
#   - only works if that column is active in the first place
#   - set to note creation time by default ("noteCrt")
#   - can be disabled by setting SORTING_COLUM = ""
#
# Valid Values (regular browser):
#
# 'question' 'answer' 'template' 'deck' 'noteFld' 'noteCrt' 'noteMod'
# 'cardMod' 'cardDue' 'cardIvl' 'cardEase' 'cardReps' 'cardLapses'
# 'noteTags' 'note'
#
# Additional values (advanced browser):
#
# 'cfirst' 'clast' 'cavgtime' 'ctottime' 'ntags' 'coverdueivl' 'cprevivl'


######## USER CONFIGURATION END ########

from aqt.qt import *
from aqt.browser import Browser
from anki.hooks import addHook

def refreshView(self):
    self.onSearch(reset=True)
    if SORTING_COLUMN:
        try:
            col_index = self.model.activeCols.index(SORTING_COLUMN)
            self.onSortChanged(col_index, True)
            self.form.tableView.selectRow(0)
        except ValueError:
            pass

def setupMenu(self):
    menu = self.form.menuEdit
    menu.addSeparator()
    a = menu.addAction('Refresh View')
    a.setShortcut(QKeySequence("F5"))
    a.triggered.connect(self.refreshView)

Browser.refreshView = refreshView
addHook("browser.setupMenus", setupMenu)