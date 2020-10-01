import requests
import sys

from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QApplication

from qt_gui import Ui_MainWindow

HEADERS = {
    'X-Yandex-API-Key': '20d3cd36-6f8e-4486-b0cd-934db7a82722',
    'User-Agent': 'Mozilla/5.0'
}

# city = str(input())
city = 'orenburg'
URL = f'https://api.weather.yandex.ru/v2/forecast?url=https://yandex.ru/pogoda/{city}'


r = requests.get(url=URL, headers=HEADERS).json()
# ==> GET FACT WEATHER DATA-Dictionary
fact = r.get('fact')


# ==> City, temp, humidity, pressure_mm, wind_speed
print(city)
print(f"Температура сейчас: {fact.get('temp')}°C")
print(f"Ощущается как {fact.get('feels_like')}°C")
print(f"Влажность {fact.get('humidity')}%")
print(f"Давление {fact.get('pressure_mm')} мм")
print(f"Скорость ветра {fact.get('wind_speed')} м/c")


# ==> VERY FAST GUI
class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ==> TRANSPARENT
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # ==> FEELS
        self.ui.label_City.setText(city)
        self.ui.label_temp.setText(f"Температура сейчас: {fact.get('temp')}°C")
        self.ui.label_feels_like.setText(f"Ощущается как {fact.get('feels_like')}°C")
        self.ui.label_humidity.setText(f"Влажность {fact.get('humidity')}%")
        self.ui.label_pressure_mm.setText(f"Давление {fact.get('pressure_mm')} мм")
        self.ui.label_wind_speed.setText(f"Скорость ветра {fact.get('wind_speed')} м/c")

    # ==> CALL EVENT
    def calling(self):
        self.ui.pushButton.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # ==> LOOP
    win = mainWindow()
    win.show()

    # ==> CALL EVENT
    win.calling()
    sys.exit(app.exec_())
