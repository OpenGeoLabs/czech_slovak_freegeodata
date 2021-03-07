from qgis.utils import iface
from qgis.core import *
from qgis.gui import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtWidgets import *
from zipfile import ZipFile

from urllib.parse import urlparse
import os


class ShiftGrid:
    """
    Represents shift grid needed to enable certain transformations.
    """

    gridDirectory = os.path.join(QgsApplication.qgisSettingsDirPath(), "proj")

    def __init__(self, gridKey, gridFileUrl, gridFileName):
        """
        gridKey - unique grid key
        gridFileUrl - URL to download grid
        gridFileName - grid filename
        """

        self.key = gridKey
        self.fileUrl = gridFileUrl
        self.fileName = gridFileName
        self.fullGridPath = os.path.join(ShiftGrid.gridDirectory, self.fileName)
        destinationFileName = os.path.basename(urlparse(self.fileUrl).path)
        self.fullDownloadedFilePath = os.path.join(ShiftGrid.gridDirectory, destinationFileName)

    def isPresent(self):
        """
        Returns True if grid is already present and does not need to be downloaded.
        """

        return os.path.isfile(self.fullGridPath)

    def downloadFailed(self):
        """
        Defines actions made after unsuccesfull download.
        """
        iface.messageBar().pushMessage(QApplication.translate("GeoData", "Error", None),
                                       QApplication.translate("GeoData", "Unable to download grid {} from {}.".format(self.key, self.fileUrl), None),
                                       level=Qgis.Critical,
                                       duration=5)

    def downloadCompletedJtsk03(self):
        """
        Defines actions made after succesfull download of JTSK03_JTSK grid.
        """

        try:
            with ZipFile(self.fullDownloadedFilePath, "r") as zipfile:
                zipfile.extractall(ShiftGrid.gridDirectory)
        except:
            iface.messageBar().pushMessage(QApplication.translate("GeoData", "Error", None),
                                           QApplication.translate("GeoData", "Unable extract grid file for grid {}.".format(self.key), None),
                                           level=Qgis.Critical,
                                           duration=5)

    def download(self):
        """
        Downloads grid and puts it into correct directory, so it is usable
        for QGIS. If file downloadable from internet needs to be
        decompressed, renamed or any other processing needs to be
        done, dedicated function has to be defined and used in downloader.downloadCompleted.connect
        """

        if not os.path.isdir(ShiftGrid.gridDirectory):
            try:
                os.mkdir(ShiftGrid.gridDirectory)
            except Exception:
                iface.messageBar().pushMessage(QApplication.translate("GeoData", "Error", None),
                                               QApplication.translate("GeoData", "Unable to create directory {} to download grid {}.".format(ShiftGrid.gridDirectory, self.key), None),
                                               level=Qgis.Critical,
                                               duration=5)
                return

        # based on gird key, this decides, how it should be processed
        if self.key == "JTSK03_JTSK":
            successFunction = self.downloadCompletedJtsk03
        else:
            raise NotImplementedError

        if not self.isPresent():
            loop = QEventLoop()
            downloader = QgsFileDownloader(QUrl(self.fileUrl), self.fullDownloadedFilePath, delayStart=True)

            downloader.downloadExited.connect(loop.quit)
            downloader.downloadError.connect(self.downloadFailed)
            downloader.downloadCompleted.connect(self.downloadCompletedJtsk03)
            downloader.startDownload()
            loop.exec_()
