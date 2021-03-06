from .. source import Source
import os
from qgis.core import QgsVectorLayer, QgsMessageLog

class BlokBudov(Source):

    def get_vector(self, extent, EPSG):
        url = 'http://geoportal.cuzk.cz/ZAKAZKY/Data50/vsechnyVrstvy.zip'
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'vsechnyVrstvy.zip')
        self.download_data(url, path, "ČUZK DATA 50")
        path = '/vsizip/' + os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'vsechnyVrstvy.zip') + '/shp/BlokBudov.shp'
        vector = QgsVectorLayer(path, "ČÚZK DATA 50 - Bloky budov", "ogr")
        vector.loadNamedStyle(os.path.dirname(__file__) + '/data/styleBlokBudov.qml')
        if not vector.isValid():
            QgsMessageLog.logMessage("Vrstvu " + path + " se nepodařilo načíst", "GeoData")
            return None
        else:
            return vector

    def get_raster(self, extent, EPSG):
        return None

