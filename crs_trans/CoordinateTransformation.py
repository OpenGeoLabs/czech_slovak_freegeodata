from qgis.core import *
from qgis.gui import *
from qgis.utils import *


class CoordinateTransformation:
    """
    This class represents coordinate transformation definition between two coordinate systems.
    """

    def __init__(self, regions, crsFrom, crsTo, transformation, gridFileUrl=None):
        """
        region - defines region, for which this transformation should be used
        crsFrom - defines source CRS for this transformation. May be anything that can be handled by QgsCoordinateReferenceSystem constructor.
        crsTo - defines target CRS for this transformation. May be anything that can be handled by QgsCoordinateReferenceSystem constructor.
        tronsformation - defines transformation method. May be name of QgsCoordinateTransform or ProjString.
        gridFileUrl - optional, defines URL to download grid shift file in case transformation needs one
        """

        assert isinstance(regions, (list, tuple))

        self.regions = regions

        self.crsFrom = QgsCoordinateReferenceSystem(crsFrom)
        self.crsTo = QgsCoordinateReferenceSystem(crsTo)

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
