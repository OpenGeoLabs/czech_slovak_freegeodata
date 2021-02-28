from qgis.core import *
from qgis.gui import *

from .CoordinateTransformation import CoordinateTransformation


class CoordinateTransformationList(list):
    """
    Represents list of Coordnate transformations and allows to preform some usefull queries.
    """

    def __str__(self):
        outStr = ""
        for transform in self:
            outStr += str(transform)
        return outStr

    def getTransformationsForRegion(self, regionCode):
        """
        Returns all transformations (that are contained in called list) which belogs to specified region code.
        """

        outTarnsforms = CoordinateTransformationList()
        for transform in self:
            if regionCode in transform.getRegions():
                outTarnsforms.append(transform)
        return outTarnsforms

    def addAllTransformationsToConfig(self):
        """
        Adds all transformations conatined in this list to QGIS configuration file as defaults.
        """

        for transform in self:
            transform.addToConfig()
