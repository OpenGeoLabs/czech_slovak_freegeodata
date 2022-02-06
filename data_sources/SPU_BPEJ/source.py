from .. source import Source
import os
from qgis.core import QgsVectorLayer, QgsMessageLog

class SPU_BPEJ(Source):

    def get_vector(self, extent, EPSG):
        url = 'https://www.spucr.cz/frontend/webroot/uploads/files/2022/02/bpej_2022020111855.zip'                      #adresa pro stazeni datove vrstvy
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'bpej_2022020111855.zip')   #Cesta pro ulozeni
        self.download_data(url, path, "BPEJ")                                                                           #Nazev vrsty v qgis
        path = '/vsizip/' + os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'bpej_2022020111855.zip') + '/BPEJ_20220201.shp' #nazev nacitaneho shapefile
        vector = QgsVectorLayer(path, "BPEJ", "ogr")
        vector.loadNamedStyle(os.path.dirname(__file__) + '/data/style.qml')
        if not vector.isValid():
            QgsMessageLog.logMessage("Vrstvu " + path + " se nepodarilo nacist", "GeoData")
            return None
        else:
            return vector

    def get_raster(self, extent, EPSG):
        return None
