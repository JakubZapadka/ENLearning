from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6 import uic
import random
from googletrans import Translator
from google_images_search import GoogleImagesSearch
import os.path
import config


class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("data/menu/mygui.ui", self)
        self.show()
        self.pushButton.clicked.connect(self.change_world)

    file = open("data/assets/words.txt", "r")
    list_of_words = file.readlines()

    def change_world(self):
        rand = random.randint(0, len(self.list_of_words)) - 1
        self.label_en_trans.setText(self.list_of_words[rand][:-1])
        self.label_pl_trans.setText(Translator().translate(self.list_of_words[rand][:-1], dest='pl', src="en").text)

        # images downloader
        if not os.path.exists("data/assets/pictures/"+self.list_of_words[rand][:-1]+".jpg") and self.checkBox_show_images.isChecked():
            gis = GoogleImagesSearch(config.api_key, config.cx_key)
            _search_params = {
                "q": self.list_of_words[rand],
                "num": 1,
                'fileType': 'jpg',
                'imgSize': 'medium'
            }
            gis.search(search_params=_search_params, path_to_dir="data/assets/pictures/", custom_image_name=self.list_of_words[rand][:-1])
        self.photo.setPixmap(QPixmap("data/assets/pictures/"+self.list_of_words[rand][:-1]+".jpg"))
    file.close()


def main():
    app = QApplication([])
    window = MyGUI()
    window.setWindowIcon(QIcon("data/menu/logo.png"))
    window.setWindowTitle("ENlearning")
    app.exec()


if __name__ == "__main__":
    main()
