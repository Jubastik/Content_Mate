from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QMovie

from UI_widgets.UI_wait import Ui_Form_Wait


class WaitWidget(QWidget, Ui_Form_Wait):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.movie = QMovie("./resources/wait.gif")
        self.label.setMovie(self.movie)
        self.movie.setScaledSize(QSize(720, 540))
        self.movie.start()