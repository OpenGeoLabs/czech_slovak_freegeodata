# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoDataDialog
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

import os
import configparser
import sys
import webbrowser
import unicodedata
import re

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.PyQt import QtGui
from qgis.utils import iface
from qgis.core import *
from qgis.gui import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtWidgets import *

import importlib, inspect
from .data_sources.source import Source
from urllib.request import urlopen
import json
from .crs_trans.CoordinateTransformation import CoordinateTransformation
from .crs_trans.CoordinateTransformationList import CoordinateTransformationList
from .crs_trans.ShiftGrid import ShiftGrid
from .crs_trans.ShiftGridList import ShiftGridList

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Geo_Data_dialog_base.ui'))

# Return lowered unicoded string 
def get_unicode_string(word: str):
    """Filter out diacritics from keyword."""
    output = ''
    line = unicodedata.normalize('NFKD', word)

    for c in line:
        if not unicodedata.combining(c):
            output += c

    return output.lower()

# Merge strings from list into one unicoded string
def get_unicoded_list(words: list):
    output = ''
    for word in words:
        unicodedWord = get_unicode_string(word)
        output += unicodedWord

    return output.lower()


class GeoDataDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, iface, regionhandler, parent=None):
        """Constructor."""
        super(GeoDataDialog, self).__init__(parent)
        self.current_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.iface = iface
        self.setupUi(self)
        self.region_handler = regionhandler
        # self.pushButtonAbout.setIcon(QIcon(os.path.join(os.path.dirname(__file__), "icons/cropped-opengeolabs-logo-small.png")))
        # self.pushButtonAbout.clicked.connect(self.showAbout)
        self.pushButtonLoadRuianPlugin.clicked.connect(self.load_ruian_plugin)
        self.pushButtonLoadData.clicked.connect(self.load_data)
        self.pushButtonSourceOptions.clicked.connect(self.show_source_options_dialog)
        self.data_sources = []
        self.treeWidgetSources.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidgetSources.customContextMenuRequested.connect(self.open_context_menu)
        self.statuses = {}
        self.load_statuses()
        self.load_sources_into_tree()
        self.selectedSource = -1
        self.filterBox.valueChanged.connect(self.load_filtered_sources_into_tree)
        self.checkBoxOnlyRegionSources.stateChanged.connect(self.load_filtered_sources_into_tree)
        self.comboBoxRegion.currentIndexChanged.connect(self.set_region)
        self.load_region()

    def load_statuses(self):
        try:
            response = urlopen("https://raw.githubusercontent.com/OpenGeoLabs/czech_slovak_freegeodata/ruz76/feature/service-status/data_sources/statuses.json")
            self.statuses = json.loads(response.read())
        except:
            self.statuses = {}

    def get_url(self, config):
        if config['general']['type'].upper() == 'WMS':
            # TODO check CRS? Maybe.
            url = 'url=' + config['wms']['url']
            layers = config['wms']['layers'].split(',')
            for layer in layers:
                url += "&layers=" + layer
            styles = config['wms']['styles'].split(',')
            for style in styles:
                url += "&styles=" + style
            url += "&" + config['wms']['params']
            return url

        elif config['general']['type'].upper() == 'TMS':
            return "type=xyz&url=" + config['tms']['url']

        elif config['general']['type'].upper() == 'WMTS':
            url = config['wmts']['url']
            tilematrixset = config['wmts']['tilematrixset']
            layer = config['wmts']['layer']
            frmt = config['wmts']['format']
            crs = config['wmts']['crs']
            url = "contextualWMSLegend=0&featureCount=10&crs={crs}&format={frmt}&layers={layer}&styles=default&tileMatrixSet={tilematrixset}&url={url}".format(
                    url=url, tilematrixset=tilematrixset, layer=layer,
                    crs=crs, frmt=frmt)
            if 'SmoothPixmapTransform' in config['wmts'].keys():
                spt = config['wmts']['SmoothPixmapTransform']
                url = "SmoothPixmapTransform=" + str(spt) + "&" + url
            return url

    def uncheck_sub_tree(self, item):
        item.setCheckState(0, Qt.Unchecked);
        for i in range(item.childCount()):
            self.uncheck_sub_tree(item.child(i));

    def uncheck_all(self):
        tree = self.treeWidgetSources
        for i in range(tree.topLevelItemCount()):
            self.uncheck_sub_tree(tree.topLevelItem(i))

    def load_data(self):
        # print("LOAD DATA")
        for data_source in self.data_sources:
            # print(data_source)
            if data_source['checked'] == "True":
                if "WMS" in data_source['type'] or "TMS" in data_source['type']:
                    self.add_layer(data_source, layer_type="wms")
                    self.addSourceToBrowser(data_source)
                elif "WMTS" in data_source["type"]:
                    self.add_layer(data_source, layer_type="wms")
                    self.addSourceToBrowser(data_source)
                elif "PROC" in data_source['type']:
                    if data_source['proc_class'] is not None:
                        self.add_proc_data_source_layer(data_source)
        self.uncheck_all()

    def load_sources_into_tree(self):

        self.treeWidgetSources.itemChanged.connect(self.handleChanged)
        self.treeWidgetSources.itemSelectionChanged.connect(self.handleSelected)
        tree = self.treeWidgetSources
        tree.header().setSectionResizeMode(0,QHeaderView.ResizeToContents)
        paths = []

        sources_dir = os.path.join(self.current_dir, 'data_sources')

        for name in os.listdir(sources_dir):
            if os.path.isdir(os.path.join(sources_dir, name)) and name[:2] != "__":
                paths.append(name)

        paths.sort()

        for path in paths:
            # config neads to be initializen in loop, otherwise it may
            # retain values that are unititialized in current source,
            # but were initiarized in some of the previous
            config = configparser.ConfigParser()
            config_file = os.path.join(sources_dir, path, 'metadata.ini')

            try:
                config.read(config_file, 'UTF-8')
            except (UnicodeDecodeError, configparser.DuplicateOptionError) as e:
                iface.messageBar().pushMessage(
                    "Error", "Unable load {}: {}".format(config_file, e), level=Qgis.Critical)
                continue

            url = ""
            proc_class = None
            service_name = None
            try:
                if "WMS" in config['general']['type'] or "TMS" in config['general']['type']:
                    url = self.get_url(config)

                    if config['general']['type'].upper() == 'WMS' and config.has_option("wms", "service_name"):
                        service_name = config["wms"]["service_name"]

                elif "WMTS" in config['general']['type']:
                    url = self.get_url(config)

                    if config.has_option("wmts", "service_name"):
                        service_name = config["wmts"]["service_name"]

                elif "PROC" in config['general']['type']:
                    proc_class = self.get_proc_class(path)

            except KeyError as e:
                iface.messageBar().pushMessage(
                    "Error", "Invalid metadata {} (missing key {})".format(config_file, e), level=Qgis.Critical)
                continue

            try:
                key_word = config['ui']['keywords'].split(',')
            except KeyError:
                key_word = []

            self.data_sources.append(
                {
                    "logo": os.path.join(sources_dir, path, config['ui']['icon']),
                    "path": path,
                    "group": config['ui']['group'],
                    "type": config['general']['type'],
                    "alias": config['ui']['alias'],
                    "url": url,
                    "checked": config['ui']['checked'],
                    "proc_class": proc_class,
                    "service_name": service_name,
                    "keywords": key_word
                }
            )

        self.load_filtered_sources_into_tree()

    def is_in_region(self, data_source_keywords):
        if not self.checkBoxOnlyRegionSources.isChecked():
            return True
        s = QgsSettings()
        region = s.value("geodata_cz_sk/region", "")
        if region == '':
            return True
        else:
#             print(data_source_keywords)
            if region == 'CZE' and 'cz' in data_source_keywords:
                return True
            if region == 'SVK' and 'sk' in data_source_keywords:
                return True
        return False

    def load_filtered_sources_into_tree(self):
        """
        Loads filtered data into tree based on string given by filterBox.
        """
        self.keyword = self.filterBox.value()
        self.treeWidgetSources.clear()

        keywordString = get_unicode_string(self.keyword)
        tree = self.treeWidgetSources
        group = ""
        index = 0

        for data_source in self.data_sources:
#             print(self.is_in_region(get_unicoded_list(data_source['keywords'])))
            if ((keywordString == '' and self.is_in_region(get_unicoded_list(data_source['keywords'])))
                or (self.is_in_region(get_unicoded_list(data_source['keywords'])) and keywordString in get_unicode_string(data_source['alias']))
               or (self.is_in_region(get_unicoded_list(data_source['keywords'])) and keywordString in get_unicode_string(data_source['group']))
               or (self.is_in_region(get_unicoded_list(data_source['keywords'])) and keywordString in get_unicoded_list(data_source['keywords']))):
                current_group = data_source['path'].split("_")[0]

                if current_group != group:
                    group = current_group
                    parent = QTreeWidgetItem(tree)
                    parent.setText(0, current_group)  # TODO read from metadata.ini (maybe)
                    parent.setFlags(parent.flags()
                                    | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
                    parent.setIcon(0, QIcon(os.path.join(data_source['logo'])))

                child = QTreeWidgetItem(parent)
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setText(0, data_source['alias'])
                child.setIcon(0, QIcon(os.path.join(data_source['logo'])))
                if "PROC" in data_source['type']:
                    child.setIcon(1, QIcon(os.path.join(self.current_dir, 'icons/timer.png')))
                if data_source['path'] in self.statuses:
                    child.setIcon(2, QIcon(os.path.join(self.current_dir, 'icons/' + self.statuses[data_source['path']] + '.png')))
                else:
                    child.setIcon(2, QIcon(os.path.join(self.current_dir, 'icons/question.png')))

                child.setData(0, Qt.UserRole, index)
                if data_source['checked'] == "True":
                    child.setCheckState(0, Qt.Checked)
                else:
                    child.setCheckState(0, Qt.Unchecked)
            index += 1
        tree.expandAll()
        if self.keyword == "":
            tree.collapseAll()


    def handleSelected(self):
        self.selectedSource = -1
        self.pushButtonSourceOptions.setEnabled(False)
#         print(self.treeWidgetSources.selectedItems())
        for item in self.treeWidgetSources.selectedItems():
            if item.data(0, Qt.UserRole) is not None:
                id = int(item.data(0, Qt.UserRole))
                # print(str(id))
                # print(self.data_sources[id])
                if self.data_sources[id]['proc_class'] is not None and self.data_sources[id]['proc_class'].has_options_dialog():
                    self.selectedSource = id
                    self.pushButtonSourceOptions.setEnabled(True)
                    # print("HAS OPTIONS DIALOG")

    def handleChanged(self, item, column):
        # Get his status when the check status changes.
        if item.data(0, Qt.UserRole) is not None:
            id = int(item.data(0, Qt.UserRole))
            if item.checkState(column) == Qt.Checked:
                # print("checked", item, item.text(column))
                self.data_sources[id]['checked'] = "True"
            if item.checkState(column) == Qt.Unchecked:
                # print("unchecked", item, item.text(column))
                self.data_sources[id]['checked'] = "False"
            # print(item.data(0, Qt.UserRole))

    def open_context_menu(self):
        # TODO - if we want context menu
        # https://wiki.python.org/moin/PyQt/Creating%20a%20context%20menu%20for%20a%20tree%20view
        print("MENU")

    def show_source_options_dialog(self):
        if self.selectedSource >= 0:
            self.data_sources[self.selectedSource]['proc_class'].show_options_dialog()

    def add_layer(self, data_source, layer_type="wms"):
        # print("Add Layer " + (self.wms_sources[index]))
        # rlayer = QgsRasterLayer(self.wms_sources[index], 'MA-ALUS', 'wms')
        layer = QgsRasterLayer(data_source['url'], data_source['alias'], layer_type)
#         print(data_source, layer_type)
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
        else:
#             print(data_source['url'])
            iface.messageBar().pushMessage("Error", "The layer was not valid and could not be loaded.", level=Qgis.Critical)

    def get_proc_class(self, path):
        current_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        current_module_name = os.path.splitext(os.path.basename(current_dir))[0]
        module = importlib.import_module(".data_sources." + path + ".source", package=current_module_name)
        for member in dir(module):
            if member != 'Source':
                handler_class = getattr(module, member)
                # if member == 'SampleOne':
                #     print("GPC")
                #     print(handler_class)
                #     print(inspect.isclass(handler_class))
                #     print(issubclass(handler_class, Source))
                if handler_class and inspect.isclass(handler_class) and issubclass(handler_class, Source):
                    current_source = handler_class()
                    return current_source
        return None

    def addSourceToBrowser(self, data_source):
        source = None
        if data_source['type'] == "TMS":
            url = data_source['url'][13:]
            source = ["connections-xyz", data_source['alias'], "", "", "", url, "", "19", "0", data_source["service_name"]]
        if data_source['type'] == "WMS":
            url = data_source['url'][4:].split("&")[0]
            source = ["connections-wms", data_source['alias'], "", "", "", url, "", "19", "0", data_source["service_name"]]
        if data_source['type'] == "WMTS":
            url = re.match("^.*url=(.[^&]*)", data_source['url'])[1]
            source = ["connections-wms", data_source['alias'], "", "", "", url, "", "19", "0", data_source["service_name"]]

#         print(self.sourcePresentInBrowser(source[0], url))
        if source != None and not self.sourcePresentInBrowser(source[0], url):
            connectionType = source[0]
            connectionName = source[1] if source[9] is None else source[9]
            QSettings().setValue("qgis/%s/%s/authcfg" % (connectionType, connectionName), source[2])
            QSettings().setValue("qgis/%s/%s/password" % (connectionType, connectionName), source[3])
            QSettings().setValue("qgis/%s/%s/referer" % (connectionType, connectionName), source[4])
            QSettings().setValue("qgis/%s/%s/url" % (connectionType, connectionName), source[5])
            QSettings().setValue("qgis/%s/%s/username" % (connectionType, connectionName), source[6])
            QSettings().setValue("qgis/%s/%s/zmax" % (connectionType, connectionName), source[7])
            QSettings().setValue("qgis/%s/%s/zmin" % (connectionType, connectionName), source[8])

        iface.reloadConnections()

    def sourcePresentInBrowser(self, connectionType, serviceUrl):
        """ Determines presence of data source in Browser """

        configKeys = QSettings().allKeys()
        for key in configKeys:
            keySplit = key.split("/")
            if len(keySplit) >= 4 and keySplit[0] == "qgis" and keySplit[1] == connectionType and keySplit[3] == 'url':
                confUrl = QgsSettings().value(key)
                if confUrl == serviceUrl:
                    return True

        return False


    def add_proc_data_source_layer(self, data_source):
        if data_source['type'] == "PROC_VEC":
            data_source['proc_class'].set_iface(self.iface)
            layer = data_source['proc_class'].get_vector(self.get_extent(), self.get_epsg())
        if data_source['type'] == "PROC_RAS":
            data_source['proc_class'].set_iface(self.iface)
            layer = data_source['proc_class'].get_raster(self.get_extent(), self.get_epsg())
        if layer is not None:
            QgsProject.instance().addMapLayer(layer)

    def get_extent(self):
        return self.iface.mapCanvas().extent()

    def get_epsg(self):
        srs = self.iface.mapCanvas().mapSettings().destinationCrs()
        return srs.authid()

    def load_ruian_plugin(self):
        ruian_found = False
        for x in iface.mainWindow().findChildren(QAction):
            if "RUIAN" in x.toolTip():
                ruian_found = True
                x.trigger()

        if not ruian_found:
            self.labelRuianError.setText(QApplication.translate("GeoData","This functionality requires RUIAN plugin", None))

    def load_region(self):
        s = QgsSettings()
        region = s.value("geodata_cz_sk/region", "")
        if region == "SVK":
            self.comboBoxRegion.setCurrentIndex(1)
        if region == "CZE":
            self.comboBoxRegion.setCurrentIndex(2)

    def set_region(self):
        s = QgsSettings()
        region_saved = s.value("geodata_cz_sk/region", "")
        region = self.comboBoxRegion.currentText()
        if region_saved != region:
            if region != '':
                self.setCursor(Qt.WaitCursor)
                self.region_handler.applyTransformations(region)
                QMessageBox.information(None, QApplication.translate("GeoData", "Info", None),
                                                QApplication.translate("GeoData", "You have to restart QGIS to apply all settings.", None))
                s = QgsSettings()
                s.setValue("geodata_cz_sk/region", region)
                self.load_filtered_sources_into_tree()
                self.setCursor(Qt.ArrowCursor)
