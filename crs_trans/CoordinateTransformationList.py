from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from .CoordinateTransformation import CoordinateTransformation
from .ShiftGridList import ShiftGridList


class CoordinateTransformationList(list):
    """
    Represents list of Coordnate transformations and allows to preform some usefull queries.
    """

    CONFIGURATION = "CONFIGURATION"
    PROJECT = "PROJECT"

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

    def applyTransformations(self, region=None, destination=None):
        """
        Adds all transformations conatined in this list to QGIS configuration file as defaults or to QGIS project.
        region - optional region filter. When specified only transformations of defined region will be applied.
        destination - optional destination of transformation configuration { CONFIGURATION | PROJECT } - if not defined, configuration is assumed
        """

        if region is not None:
            assert isinstance(region, str)

        if destination is None:
            destination = CoordinateTransformationList.CONFIGURATION

        assert isinstance(destination, str) and destination.upper() in (CoordinateTransformationList.CONFIGURATION, CoordinateTransformationList.PROJECT)

        if region is None:
            transformations = self
        else:
            transformations = self.getTransformationsForRegion(region)

            if len(transformations) == 0:
                iface.messageBar().pushMessage(QApplication.translate("GeoData", "Warting", None),
                                               QApplication.translate("GeoData", "No transformation found for region {}.".format(region)),
                                               level=Qgis.Warning,
                                               duration=5)
                return

        if len(transformations) > 0:
            for transform in transformations:
                try:
                    if destination == CoordinateTransformationList.CONFIGURATION:
                        transform.addToConfig()
                    else:
                        transform.addToProject()
                except Exception:
                    pass

            # It is assumed that grids were already downloaded when plugin had been initialized, thus restart is not requested when transformations are added to project
            if destination == CoordinateTransformationList.CONFIGURATION:
                iface.messageBar().pushMessage(QApplication.translate("GeoData", "Info", None),
                                               QApplication.translate("GeoData", "QGIS restart is needed to apply transformation settings."),
                                               level=Qgis.Info)
        else:
            iface.messageBar().pushMessage(QApplication.translate("GeoData", "Info", None),
                                           QApplication.translate("GeoData", "No transformation selected."),
                                           level=Qgis.Info)
