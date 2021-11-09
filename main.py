import sys
import  os
import webbrowser

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from datetime import date
import threading
import sqlite3

from content_mate import pause_handler
from widgets.settings import SettingsWidget
from widgets.wait import WaitWidget
from widgets.automatization import AutomatizationWidget
from UI_main import  Ui_MainWindow


class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('main_v2.ui', self)
        self.setupUi(self)
        self.load_settings_db()
        self.connect_all()
        self.checkbox_changing()
        self.load_combobox()
        self.default_settings()
        self.aw = "новый"

    def connect_all(self):
        self.in_btn.clicked.connect(self.load_in)
        self.out_btn.clicked.connect(self.load_out)
        self.start_btn.clicked.connect(self.start)
        self.default_btn.clicked.connect(self.default_settings)
        self.edit_btn.clicked.connect(self.start_settings_widget)
        self.info_btn.clicked.connect(self.open_info_web)

        self.use_presets.stateChanged.connect(self.checkbox_changing)
        self.presets.currentTextChanged.connect(self.combobox_changing)

        self.automatization_btn.clicked.connect(self.start_automatization_widget)


    def start_settings_widget(self):
        self.sw = SettingsWidget(self)
        self.sw.show()

    def start_wait_widget(self):
        self.ww = WaitWidget()
        self.ww.show()

    def open_info_web(self):
        webbrowser.open('https://docs.google.com/document/d/1Ei-w7j8RJc28rdgABKlUQFaKFfyEBid7K358f7bJuhY/edit#bookmark=id.t8ov2pdm0t5')

    def start_automatization_widget(self):
        #виджет создаётся только в первый раз,
        # для исключения одновременного запуска двух задач поиска новых файлов
        if self.aw == "новый":
            self.aw = AutomatizationWidget(self)
        self.aw.show()

    def load_settings_db(self):
        self.con = sqlite3.connect("settings.db")
        cur = self.con.cursor()
        result = cur.execute(
            """select PathReadOnly, Log, OutPath from main 
            where id = 1"""
        ).fetchone()

        self.in_edit.setReadOnly(result[0])
        self.out_edit.setReadOnly(result[0])
        self.out_edit.setText(result[2])
        self.log = result[1]
        if self.log:
            self.log_file = open(f"log-{date.today()}.txt", mode="w", encoding="utf-8")
        else:
            self.log_file = ""

    def load_combobox(self):
        cur = self.con.cursor()
        result = cur.execute(
            """select Name from preset"""
        ).fetchall()
        # result = [f'{n} - {s}% {i}сек. {st}сек.' for n, s, i, st in result]
        result = [f'{i[0]}' for i in result]
        self.presets.addItems(result)

    def default_settings(self):
        cur = self.con.cursor()
        result = cur.execute(
            """select * from preset
            where Name = 'Default'"""
        ).fetchone()
        self.sensitivity_settings.setValue(result[1])
        self.indent_settings.setValue(result[2])
        self.step_settings.setValue(result[3])

    def checkbox_changing(self):
        if self.use_presets.isChecked() == False:
            self.presets.setEnabled(False)
            self.sensitivity_settings.setEnabled(True)
            self.indent_settings.setEnabled(True)
            self.step_settings.setEnabled(True)
        else:
            self.presets.setEnabled(True)
            self.sensitivity_settings.setEnabled(False)
            self.indent_settings.setEnabled(False)
            self.step_settings.setEnabled(False)
            self.combobox_changing()

    def combobox_changing(self):
        preset_name = self.presets.currentText()
        cur = self.con.cursor()
        result = cur.execute(
            """select Sensitivity, Indent, Step from preset 
            where Name = ?""", [preset_name]
        ).fetchone()
        self.sensitivity_settings.setValue(result[0])
        self.indent_settings.setValue(result[1])
        self.step_settings.setValue(result[2])

    def load_in(self):
        fname = QFileDialog.getOpenFileNames(self, 'Выбрать файл (-ы)', '', 'Видео (*.mp4);')
        if fname[0]:
            self.in_edit.setText("\n".join(fname[0]))

    def load_out(self):
        fname = QFileDialog.getExistingDirectory(self, 'Выбрать папку', '')
        if fname:
            self.out_edit.setText(fname)

    def start(self):
        in_path = self.in_edit.toPlainText().split("\n")
        out_path = self.out_edit.text()
        if in_path and out_path and os.path.isfile(in_path[0]) and os.path.isdir(out_path):
            if self.log:
                self.log_file.write(f"Старт обработки файлов {in_path}\n")
            sensitivity = float("0." + self.sensitivity_settings.text())
            indent = self.indent_settings.value()
            step = self.step_settings.value()
            self.start_wait_widget()
            self.start_btn.setEnabled(False)
            my_thread = threading.Thread(target=pause_handler, args=(self.finish_process, in_path, out_path, sensitivity, indent, step, self.log, self.log_file))
            my_thread.start()
        else:
            self.statusbar.showMessage("Неправильный входной или выходной путь.")

    # Завершение обработки видео
    def finish_process(self):
        self.ww.hide()
        self.start_btn.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())

