from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from .CoordinateTransformation import CoordinateTransformation
from .ShiftGridList import ShiftGridList


class CoordinateTransformationList(list):
    """
    Represents list of Coordnate transformations and allows to preform some usefull queries.
    """

    def __str__(self):
        outStr = ""
        for transform in self:
            outStr += str(transform) + "\n"
        return outStr

    def getRegions(self):
        """
        Returns list of available regions.
        """

        regions = []

        for transf in self:
            for region in transf.regions:
                if region not in regions:
                    regions.append(region)

        return regions

    def getTransformationsForRegion(self, regionCode):
        """
        Returns all transformations (that are contained in called list) which belogs to specified region code.
        """

        outTarnsforms = CoordinateTransformationList()
        for transform in self:
            if regionCode in transform.getRegions():
                outTarnsforms.append(transform)
        return outTarnsforms

    def applyTransforations(self, region=None):
        """
        Adds all transformations conatined in this list to QGIS configuration file as defaults.
        region - optional region filter. When specified only transformations of defined region will be applied.
        """

        assert isinstance(region, str)

        if region is None:
            transformatios = self
        else:
            transformations = self.getTransformationsForRegion(region)

        for transform in transformations:
            transform.addToConfig()

        iface.messageBar().pushMessage(QApplication.translate("GeoData", "Info", None),
                                       QApplication.translate("GeoData", "QGIS restart is needed to apply transfarmation settings."),
                                       level=Qgis.Info)
