from .. source import Source
import os
from qgis.core import QgsVectorLayer, QgsMessageLog


class Okres(Source):

    def get_vector(self, extent, EPSG):
        url = "https://www.geoportal.sk/files/zbgis/na_stiahnutie/gpkg/ah_gpkg_0.zip"
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'ah_gpkg_0.zip')
        self.download_data(url, path, "ZBGIS - administratívne hranice SR - okres")
        path = '/vsizip/' + os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'ah_gpkg_0.zip') + '/USJ_hranice_0.gpkg|layername=okres_0'
        vector = QgsVectorLayer(path, "ZBGIS - administratívne hranice SR - okres", "ogr")
        vector.loadNamedStyle(os.path.dirname(__file__) + '/data/style.qml')
        if not vector.isValid():
            QgsMessageLog.logMessage("Unable to load layer " + path, "GeoData")
            return None
        else:
            return vector

    def get_raster(self, extent, EPSG):
        return None
