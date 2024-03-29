# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OptionsDialog
                                 A QGIS plugin
 This plugin gathers cz/sk data sources.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-08-04
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Test
        email                : test
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtWidgets import *
import os

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'options_dialog_base.ui'))

class OptionsDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(OptionsDialog, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.accepted)


    def accepted(self):
        current_dir_to_id = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        path_to_id = os.path.join(current_dir_to_id, 'data', 'temporar.csv')
        if self.radioButtonId.isChecked():
            katuzidstored = self.lineEdit.text()
            with open(path_to_id, "w") as writer:
                writer.write(katuzidstored)
                writer.close()
            if not self.lineEdit.text():
                return
        else:
            if os.path.exists(path_to_id):
                os.remove(path_to_id)



