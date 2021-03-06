from .. source import Source
import os
from qgis.core import QgsVectorLayer, QgsMessageLog

class SilniceDalnice(Source):

    def get_vector(self, extent, EPSG):
        url = 'https://dibavod.cz/download.php?id_souboru=1413'
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'dib_A02_Vodni_tok_JU.zip')
        self.download_data(url, path, "VÚVTGM DIBAVOD")
        path = '/vsizip/' + os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'dib_A02_Vodni_tok_JU.zip') + '/A02_Vodni_tok_JU.shp'
        vector = QgsVectorLayer(path, "VÚVTGM DIBAVOD - vodní tok (jemné úseky)", "ogr")
        vector.loadNamedStyle(os.path.dirname(__file__) + '/data/style.qml')
        if not vector.isValid():
            QgsMessageLog.logMessage("Vrstvu " + path + " se nepodařilo načíst", "GeoData")
            return None
        else:
            return vector

    def get_raster(self, extent, EPSG):
        return None
