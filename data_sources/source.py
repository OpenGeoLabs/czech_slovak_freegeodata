import os, urllib3, time
from qgis.PyQt.QtWidgets import QProgressBar
from qgis.PyQt.QtCore import *
from qgis.core import *
from qgis.gui import *

class Source:
    def __init__(self):
        placeholder = 100

    def set_iface(self, iface):
        self.iface = iface

    def has_options_dialog(self):
        return False

    def download_data(self, url, path, msg):
        if not os.path.exists(path):
            try:
                progressMessageBar = self.iface.messageBar().createMessage("Downloading " + msg)
                self.progress = QProgressBar()
                self.progress.setMaximum(100)
                self.progress.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
                progressMessageBar.layout().addWidget(self.progress)
                self.iface.messageBar().pushWidget(progressMessageBar, Qgis.Info)
                http = urllib3.PoolManager()
                response = http.request('GET', url, preload_content=False)
                content_length = response.headers['Content-Length']
                total_size = int(content_length)
                downloaded = 0
                CHUNK = 256 * 10240
                self.progress.setMinimum(0)
                self.progress.setMaximum(total_size)
                with open(path, 'wb') as fp:
                    while True:
                        time.sleep(1)
                        chunk = response.read(CHUNK)
                        downloaded += len(chunk)
                        self.progress.setValue(downloaded)
                        if not chunk:
                            break
                        fp.write(chunk)
                response.release_conn()
                self.iface.messageBar().clearWidgets()

            except urllib3.exceptions.MaxRetryError:
                QMessageBox.information(self.iface.mainWindow(),
                                        "HTTP Error",
                                        "Unable to download file")
