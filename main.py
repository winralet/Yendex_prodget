import sys
import requests
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
from PyQt6.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.lon = "88.192256"
        self.lat = "69.353411"
        self.delta = "0.001"

        self.set_map()


    def set_map(self):
        map_params = {
            "ll": f"{self.lon},{self.lat}",
            "spn": f"{self.delta},{self.delta}",
            "l": "map",
        }

        api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(api_server, params=map_params)

        if not response:
            print(response.status_code)
            return

        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        self.label_3.setPixmap(pixmap)
        self.label_2.setText(f"Координаты: {self.lon}, {self.lat}")

    def keyPressEvent(self, event):
        def change(symbol):
            if 0.001 <= float(self.delta) + (0.001 if symbol else -0.001) < 0.005:
                self.delta = str((float(self.delta) + (0.001 if symbol else -0.001)))

        if event.key() == Qt.Key.Key_PageUp:
            change(True)
        elif event.key() == Qt.Key.Key_PageDown:
            change(False)
        print(self.delta)
        self.set_map()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())