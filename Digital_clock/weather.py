import sys
from PyQt5.QtWidgets import QApplication,QPushButton, QLineEdit, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt



class WeatherApp(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.city_label = QLabel(self) 
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("70`F", self)
        self.emoji_label = QLabel("🌞", self)
        self.description_label = QLabel("Sunny", self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("DigitalClock") 
        self.setGeometry(400, 400, 300, 100)

        vbox = QVBoxLayout() 
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        vbox.addWidget(self.temperature_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)


        self.city_input.setObjectName("city_input")
        self.city_label.setObjectName("city_label")
        self.get_weather_button.setObjectName("get_weather_button")
        self.description_label.setObjectName("description_label")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")


        self.setStyleSheet("""
    QWidget {
        background-color: #121212;   /* sleek dark background */
        color: #EAEAEA;              /* soft white text */
        font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    }

    QLabel {
        font-size: 1.2rem;
        font-weight: 500;
        padding: 6px;
    }

    #city_label {
        font-size: 1.5rem;
        font-weight: bold;
        color: #4FC3F7;  /* elegant sky blue */
    }

    #temperature_label {
        font-size: 3rem;
        font-weight: 600;
        color: #FFD54F;  /* warm yellow */
    }

    #description_label {
        font-size: 1.2rem;
        color: #B0BEC5;  /* soft gray */
        font-style: italic;
    }

    #emoji_label {
        font-size: 3.5rem;
        margin: 12px;
    }

    #city_input {
        font-size: 1.1rem;
        padding: 8px 14px;
        border: 2px solid #333;
        border-radius: 10px;
        background-color: #1E1E1E;
        color: #ffffff;
        transition: 0.3s;
    }

    #city_input:focus {
        border: 2px solid #4FC3F7;
        background-color: #2A2A2A;
        outline: none;
    }

    #get_weather_button {
        font-size: 1.2rem;
        padding: 10px 18px;
        border-radius: 12px;
        background-color: #4FC3F7;
        color: #121212;
        font-weight: bold;
        border: none;
        cursor: pointer;
        transition: 0.3s;
    }

    #get_weather_button:hover {
        background-color: #29B6F6;
        color: #ffffff;
    }

    #get_weather_button:pressed {
        background-color: #0288D1;
        transform: scale(0.98);   /* subtle press effect */
    }
""")

        # self.time_label.setStyleSheet("font-size:130px;" "color:hsl(11, 10%,50%);")
        self.setStyleSheet("background-color:hsl(101, 10%, 20%);""color:white")

 








if __name__ == "__main__":
    app = QApplication(sys.argv) 
    click = WeatherApp() 
    click.show() 
    sys.exit(app.exec_())

