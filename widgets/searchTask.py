import shutil
import threading

from PyQt5 import QtTest
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap
import os

from content_mate import pause_handler
from .UI_searchTask import Ui_Form


class SearchWidget(QWidget, Ui_Form):
    def __init__(self, parent, raw, in_path, out_path, sensitivity_settings, indent_settings, step_settings):
        super().__init__()
        self.setupUi(self)
        self.pixmap = QPixmap("./resources/no.png")
        self.picture.setPixmap(self.pixmap)
        self.label.setText("Задача не запущена")

        self.parent = parent #ссылка на окно настройки автоматизации
        self.raw = raw
        self.in_path = in_path
        self.out_path = out_path
        self.sensitivity_settings = sensitivity_settings
        self.indent_settings = indent_settings
        self.step_settings = step_settings

        self.load_path()
        self.finish_btn.clicked.connect(self.finish_process)
        self.stop = False

        self.star_btn.clicked.connect(self.start_process)

    def load_path(self):
        self.in_edit.setText(self.in_path)
        self.out_edit.setText(self.out_path)
        self.checkBox.setChecked(self.raw)

    def finish_process(self):
        self.stop = True #остановка процесса поиска новый файлов
        self.parent.task_completed()
        self.parent.sw.hide()

    def closeEvent(self, event):
        self.finish_process()

    #Как только завершается обработка одного файла, он удаляется/копируется
    # и запускается поиск нового не обработанного файла.
    def finish_task(self):
        if self.raw:
            if not os.path.exists(self.out_path + "/RAW_Content_Mate"):
                os.mkdir(self.out_path + "/RAW_Content_Mate")
            a = shutil.copy(self.work_file, self.out_path + "/RAW_Content_Mate", follow_symlinks=True)
        os.remove(self.work_file)
        self.search()

    def start_process(self):
        self.pixmap = QPixmap("./resources/ok1.png")
        self.picture.setPixmap(self.pixmap)
        self.label.setText("Задача запущена")
        self.search()

    def search(self):
        while not self.stop:
            files = []
            for i in os.listdir(path=self.in_path):
                if i.split(".")[-1] == "mp4":
                    files.append(i)
            if files:
                self.work_file = f"{self.in_path}/{files[0]}"
                my_thread = threading.Thread(target=pause_handler,
                                             args=(self.finish_task, [self.work_file], self.out_path,
                                                   self.sensitivity_settings, self.indent_settings, self.step_settings,
                                                   False, ""))
                my_thread.start()
                break
            else:
                QtTest.QTest.qWait(10000)
