import sys
import requests
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
