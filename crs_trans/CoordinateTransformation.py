from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from .ShiftGridList import ShiftGridList


class CoordinateTransformation:
    """
    This class represents coordinate transformation definition between two coordinate systems.
    """

    def __init__(self, regions, crsFrom, crsTo, transformation, grids, grid=None):
        """
        region - defines region, for which this transformation should be used
        crsFrom - defines source CRS for this transformation. May be anything that can be handled by QgsCoordinateReferenceSystem constructor.
        crsTo - defines target CRS for this transformation. May be anything that can be handled by QgsCoordinateReferenceSystem constructor.
        transformation - defines transformation method. May be name of QgsCoordinateTransform or ProjString.
        grids - list of known shift grids
        grid - optional, reference to grid, that needs to be present
        """

        assert isinstance(regions, (list, tuple))
        assert isinstance(grids, ShiftGridList)

        self.regions = regions

        self.crsFrom = QgsCoordinateReferenceSystem(crsFrom)
        self.crsTo = QgsCoordinateReferenceSystem(crsTo)
        self.grids = grids
        self.grid = grid

        if not self.crsFrom.isValid() or not self.crsTo.isValid():
            if not self.crsFrom.isValid():
                invalidCrsDefinition = crsFrom
            else:
                invalidCrsDefinition = crsTo

            iface.messageBar().pushMessage(QApplication.translate("GeoData", "Warning", None),
                                           QApplication.translate("GeoData", "Can not create CRS from definition: {}".format(invalidCrsDefinition), None),
                                           level=Qgis.Warning,
                                           duration=5)
            return

        # Determines if defined transformation is ProjString, or name of known transformation
        if transformation[0] == "+":  # ProjString
            self.transformation = transformation
            self.fullTransformation = None
        else:
            matchingTransformation = None
            for qdt in QgsDatumTransform.operations(self.crsFrom, self.crsTo):
                if qdt.name == transformation:
                    matchingTransformation = qdt
                    break

            if matchingTransformation is None:
                iface.messageBar().pushMessage(QApplication.translate("GeoData", "Warning", None),
                                               QApplication.translate("GeoData", "Unable to find transformation between {} and {} with name: {}.".format(crsFrom, crsTo, transformation), None),
                                               level=Qgis.Warning,
                                               duration=5)
                return

            self.transformation = matchingTransformation.proj
            self.fullTransformation = matchingTransformation

    def __str__(self):
        outStr = 50 * "-" + "\n"
        outStr += "CoordinateTransformation from {} to {}\nRegions: {}\nTronsformation definition: {}\nGrid: {}".format(
            self.crsFrom.authid(), self.crsTo.authid(), self.regions, self.fullTransformation, self.grid)
        outStr += "\n" + 50 * "-"
        return outStr

    def getRegions(self):
        """
        Returns list of regions, which this transformation belongs to.
        """
        return self.regions

    def addToConfig(self):
        """
        Adds this transformation into QGIS configuration as default for specified pairs of coordinate systems.
        """

        if self.grid is not None:
            try:
                shiftGrid = self.grids.getGridsByKeys(self.grid)
                if len(shiftGrid) > 0:
                    shiftGrid.downloadAll()
                else:
                    raise Exception("Grid not found.")

            except Exception:
                iface.messageBar().pushMessage(QApplication.translate("GeoData", "Error", None),
                                               QApplication.translate("GeoData", "Unbale to download grid {} for transformation from {} to {}.".format(self.grid, self.crsFrom.authid(), self.crsTo.authid()), None),
                                               level=Qgis.Warning,
                                               duration=5)
                return

        qgisConfig = QgsSettings()
        section = "Projections"

        authFrom = self.crsFrom.authid()
        authTo = self.crsTo.authid()
        transfProj = self.transformation



        qgisConfig.setValue("{}/{}//{}_coordinateOp".format(section, authFrom, authTo), transfProj)
