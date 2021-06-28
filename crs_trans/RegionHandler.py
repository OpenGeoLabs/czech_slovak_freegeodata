import os
import configparser
import sys

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.PyQt import QtGui
from qgis.utils import iface
from qgis.core import *
from qgis.gui import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtWidgets import *

from .CoordinateTransformation import CoordinateTransformation
from .CoordinateTransformationList import CoordinateTransformationList
from .ShiftGrid import ShiftGrid
from .ShiftGridList import ShiftGridList

class RegionHandler():
    def __init__(self, iface, parent=None, start=True):
        """Constructor."""

        self.iface = iface

        self.grids = ShiftGridList()
        self.load_shift_grids()
        self.transformations = CoordinateTransformationList()
        self.load_crs_transformations()

    def applyTransformations(self, region=None, destination=None):
        self.transformations.applyTransformations(region, destination)

    def load_crs_transformations(self):
        """
        Loads available transformatios defined in crs_trans.ini
        """

        projVersion = QgsProjUtils.projVersionMajor()

        transConfigFile = os.path.join(os.path.dirname(__file__), "crs_trans.ini")
        transConfig = configparser.ConfigParser()

        try:
            transConfig.read(transConfigFile)
        except Exception:
            self.iface.messageBar().pushMessage(QApplication.translate("GeoData", "Error", None),
                                                QApplication.translate("GeoData", "Unable to read coordinate transformations definition file.", None),
                                                level=Qgis.Critical)
            raise Exception("Unable to read coordinate transformations definition file.")

        for transSection in transConfig:
            if transSection != "DEFAULT":
                transSectionContent = transConfig[transSection]

                regions = transSectionContent.get("Regions", None)
                if isinstance(regions, str) and regions is not None:
                    regions = regions.split(" ")
                crsFrom = transSectionContent.get("CrsFrom")
                crsTo = transSectionContent.get("CrsTo")

                # TransfOld is used only for Proj version 6 and only if present
                if projVersion == 6 and "transfold" in [x[0] for x in transConfig.items(transSection)]:
                    transformation = transSectionContent.get("TransfOld")
                else:
                    transformation = transSectionContent.get("Transf")

                if projVersion == 6:
                    grid = transSectionContent.get("GridOld", None)
                else:
                    grid = transSectionContent.get("Grid", None)

                if grid is not None and len(self.grids.getGridsByKeys(grid)) != 1:
                    self.iface.messageBar().pushMessage(QApplication.translate("GeoData", "Warning", None),
                                                        QApplication.translate("GeoData", "Skipping definition section {} because grid {} is unknown.".format(transSection, grid), None),
                                                        level=Qgis.Warning,
                                                        duration=5)
                    continue

                # print("--------------------\nSection: {}\nRegion: {}\nCrsFrom: {}\nCrsTo: {}\nTransformation: {}\nShiftFile: {}".format(
                #     transSection, regions, crsFrom, crsTo, transformation, gridFileUrl))

                if regions is None or regions == "" or \
                   crsFrom is None or crsFrom == "" or \
                   crsTo is None or crsTo == "" or \
                   transformation is None or transformation == "":
                    self.iface.messageBar().pushMessage(QApplication.translate("GeoData", "Warning", None),
                                                        QApplication.translate("GeoData", "Skipping incomplete transformation definition section {}.".format(transSection), None),
                                                        level=Qgis.Warning,
                                                        duration=5)
                    continue

                try:
                    transf = CoordinateTransformation(regions, crsFrom, crsTo, transformation, self.grids, grid)
                    self.transformations.append(transf)
                except Exception:
                    continue

    def load_shift_grids(self):
        """
        Loads available shift grids defined in grids.ini
        """

        gridsConfigFile = os.path.join(os.path.dirname(__file__), "grids.ini")
        gridsConfig = configparser.ConfigParser()

        try:
            gridsConfig.read(gridsConfigFile)
        except Exception:
            self.iface.messageBar().pushMessage(QApplication.translate("GeoData", "Error", None),
                                                QApplication.translate("GeoData", "Unable to read grids definition file.", None),
                                                level=Qgis.Critical)
            raise Exception("Unable to read grids definition file.")

        for grid in gridsConfig:
            if grid != "DEFAULT":
                gridContent = gridsConfig[grid]

                gridFileUrl = gridContent.get("GridFileUrl")
                gridFileName = gridContent.get("GridFileName")

                if gridFileUrl is None or gridFileName is None:
                    self.iface.messageBar().pushMessage(QApplication.translate("GeoData", "Warning", None),
                                                        QApplication.translate("GeoData", "Skipping grid definition of grid {}.".format(grid), None),
                                                        level=Qgis.Warning,
                                                        duration=5)
                    continue

                try:
                    shiftGrid = ShiftGrid(grid, gridFileUrl, gridFileName)
                    self.grids.append(shiftGrid)
                except Exception:
                    continue
