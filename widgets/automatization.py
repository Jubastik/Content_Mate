import webbrowser
from PyQt5.QtWidgets import QFileDialog, QWidget, QMessageBox
import os

from .UI_automatization import Ui_Form
from .searchTask import SearchWidget


class AutomatizationWidget(QWidget, Ui_Form):
    def __init__(self, parent, DB):
        super().__init__()
        self.setupUi(self)
        self.DB = DB
        self.parent = parent  # ссылка на основное окно
        self.connect_all()
        self.load_combobox()
        self.checkbox_changing()
        self.create_dialog()
        self.default_settings()

    def connect_all(self):
        self.use_presets.stateChanged.connect(self.checkbox_changing)
        self.presets.currentTextChanged.connect(self.combobox_changing)
        self.in_btn.clicked.connect(self.load_in)
        self.out_btn.clicked.connect(self.load_out)
        self.start_btn.clicked.connect(self.start_search_task)
        self.default_btn.clicked.connect(self.default_settings)
        self.info_btn.clicked.connect(self.open_info_web)
        self.info_btn_2.clicked.connect(self.open_info_automation_web)

    def open_info_web(self):
        webbrowser.open(
            "https://docs.google.com/document/d/1Ei-w7j8RJc28rdgABKlUQFaKFfyEBid7K358f7bJuhY/edit#bookmark=id.t8ov2pdm0t5"
        )

    def open_info_automation_web(self):
        # информация об автоматизации
        webbrowser.open(
            "https://docs.google.com/document/d/1Ei-w7j8RJc28rdgABKlUQFaKFfyEBid7K358f7bJuhY/edit#bookmark=id.o7ls0r51164r"
        )

    def default_settings(self):
        result = self.DB.get_default_processing_parameters()
        self.sensitivity_settings.setValue(result[0])
        self.indent_settings.setValue(result[1])
        self.step_settings.setValue(result[2])

    def interface_on_off(self, position):
        # отключение интерфейса на время работы задачи по поиску  файлов
        self.presets.setEnabled(position)
        self.sensitivity_settings.setEnabled(position)
        self.indent_settings.setEnabled(position)
        self.step_settings.setEnabled(position)
        self.start_btn.setEnabled(position)
        self.default_btn.setEnabled(position)
        self.use_presets.setEnabled(position)
        self.in_btn.setEnabled(position)
        self.out_btn.setEnabled(position)
        self.checkBox.setEnabled(position)

    def start_search_task(self):
        if self.check_path():
            self.interface_on_off(False)
            self.sw = SearchWidget(
                self,
                self.checkBox.isChecked(),
                self.in_edit.text(),
                self.out_edit.text(),
                float("0." + self.sensitivity_settings.text()),
                self.indent_settings.value(),
                self.step_settings.value(),
            )
            self.sw.show()
            self.parent.aw.hide()

    def check_path(self):
        if self.in_edit.text() == "" and self.out_edit.text() == "":
            self.msg_in_out_path.exec_()
            return False
        if self.in_edit.text() == "":
            self.msg_in_path.exec_()
            return False
        if self.out_edit.text() == "":
            self.msg_out_path.exec_()
            return False
        if not os.path.isdir(self.in_edit.text()) and not os.path.isdir(
            self.out_edit.text()
        ):
            self.msg_err_path.exec_()
            return False
        return True

    def task_completed(self):
        # вызываетсяпосле остановки поиска новых файлов
        self.interface_on_off(True)

    def load_in(self):
        fname = QFileDialog.getExistingDirectory(self, "Выбрать папку", "")
        if fname:
            self.in_edit.setText(fname)

    def load_out(self):
        fname = QFileDialog.getExistingDirectory(self, "Выбрать папку", "")
        if fname:
            self.out_edit.setText(fname)

    def load_combobox(self):
        result = self.DB.get_all_preset_names()
        self.presets.addItems(result)

    def checkbox_changing(self):
        if not self.use_presets.isChecked():
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
        result = self.DB.get_processing_parameters(preset_name)
        self.sensitivity_settings.setValue(result[0])
        self.indent_settings.setValue(result[1])
        self.step_settings.setValue(result[2])

    def create_dialog(self):
        self.msg_in_path = QMessageBox()
        self.msg_in_path.setIcon(QMessageBox.Warning)
        self.msg_in_path.setWindowTitle("Пустой путь")
        self.msg_in_path.setText("Не выбрана входная папка")
        self.msg_in_path.setInformativeText(
            'Пожалуйста, выберите папку из которой будут автоматически обрабатываться файлы. \
Это можно сделать  с помощью верхней кнопки "выбрать папку".'
        )

        self.msg_out_path = QMessageBox()
        self.msg_out_path.setIcon(QMessageBox.Warning)
        self.msg_out_path.setWindowTitle("Пустой путь")
        self.msg_out_path.setText("Не выбрана выходная папка")
        self.msg_out_path.setInformativeText(
            'Пожалуйста, выберите папку в которую будут сохраняться файлы. \
Это можно сделать  с помощью нижней кнопки "выбрать папку".'
        )

        self.msg_in_out_path = QMessageBox()
        self.msg_in_out_path.setIcon(QMessageBox.Warning)
        self.msg_in_out_path.setWindowTitle("Пустой путь")
        self.msg_in_out_path.setText("Не выбрана входная и выходная папка")
        self.msg_in_out_path.setInformativeText(
            'Пожалуйста, выберите папку из которой будут автоматически обрабатываться файлы и папку в которую будут сохраняться файлы. \
Это можно сделать с помощью кнопок "выбрать папку".'
        )

        self.msg_err_path = QMessageBox()
        self.msg_err_path.setIcon(QMessageBox.Warning)
        self.msg_err_path.setWindowTitle("Неправильный путь")
        self.msg_err_path.setText(
            "Входной или выходной путь содержит ошибку или не существует."
        )
        self.msg_err_path.setInformativeText(
            "Пожалуйста, выберите повторно входной и выходной путь. \
Если проблема не исчезла, поменяйте их на другие."
        )
