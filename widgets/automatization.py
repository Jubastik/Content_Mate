from PyQt5.QtWidgets import QFileDialog, QWidget, QMessageBox
import os

from .UI_automatization import Ui_Form
from .searchTask import SearchWidget

class AutomatizationWidget(QWidget, Ui_Form):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
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

    def default_settings(self):
        cur = self.parent.con.cursor()
        result = cur.execute(
            """select * from preset
            where Name = 'Default'"""
        ).fetchone()
        self.sensitivity_settings.setValue(result[1])
        self.indent_settings.setValue(result[2])
        self.step_settings.setValue(result[3])

    def interface_on_off(self, position):
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
            self.sw = SearchWidget(self, self.checkBox.isChecked(), self.in_edit.text(), self.out_edit.text(), float("0." + self.sensitivity_settings.text()),
                                           self.indent_settings.value(), self.step_settings.value())
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
        if not os.path.isdir(self.in_edit.text()) and not os.path.isdir(self.out_edit.text()):
            self.msg_err_path.exec_()
            return False
        return True

    def task_completed(self):
        self.interface_on_off(True)

    def load_in(self):
        fname = QFileDialog.getExistingDirectory(self, 'Выбрать папку', '')
        if fname:
            self.in_edit.setText(fname)

    def load_out(self):
        fname = QFileDialog.getExistingDirectory(self, 'Выбрать папку', '')
        if fname:
            self.out_edit.setText(fname)

    def load_combobox(self):
        cur = self.parent.con.cursor()
        result = cur.execute(
            """select Name from preset"""
        ).fetchall()
        # result = [f'{n} - {s}% {i}сек. {st}сек.' for n, s, i, st in result]
        result = [f'{i[0]}' for i in result]
        self.presets.addItems(result)

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
        cur = self.parent.con.cursor()
        result = cur.execute(
            """select Sensitivity, Indent, Step from preset 
            where Name = ?""", [preset_name]
        ).fetchone()
        self.sensitivity_settings.setValue(result[0])
        self.indent_settings.setValue(result[1])
        self.step_settings.setValue(result[2])

    def create_dialog(self):
        self.msg_in_path = QMessageBox()
        self.msg_in_path.setIcon(QMessageBox.Warning)
        self.msg_in_path.setWindowTitle("Пустой путь")
        self.msg_in_path.setText("Не выбрана входная папка")
        self.msg_in_path.setInformativeText('Пожалуйста, выберите папку из которой будут автоматически обрабатываться файлы. \
Это можно сделать  с помощью верхней кнопки "выбрать папку".')

        self.msg_out_path = QMessageBox()
        self.msg_out_path.setIcon(QMessageBox.Warning)
        self.msg_out_path.setWindowTitle("Пустой путь")
        self.msg_out_path.setText("Не выбрана выходная папка")
        self.msg_out_path.setInformativeText('Пожалуйста, выберите папку в которую будут сохраняться файлы. \
Это можно сделать  с помощью нижней кнопки "выбрать папку".')

        self.msg_in_out_path = QMessageBox()
        self.msg_in_out_path.setIcon(QMessageBox.Warning)
        self.msg_in_out_path.setWindowTitle("Пустой путь")
        self.msg_in_out_path.setText("Не выбрана входная и выходная папка")
        self.msg_in_out_path.setInformativeText('Пожалуйста, выберите папку из которой будут автоматически обрабатываться файлы и папку в которую будут сохраняться файлы. \
Это можно сделать с помощью кнопок "выбрать папку".')

        self.msg_err_path = QMessageBox()
        self.msg_err_path.setIcon(QMessageBox.Warning)
        self.msg_err_path.setWindowTitle("Неправильный путь")
        self.msg_err_path.setText("Входной или выходной путь содержит ошибку или не существует.")
        self.msg_err_path.setInformativeText('Пожалуйста, выберите повторно входной и выходной путь. \
Если проблема не исчезла, поменяйте их на другие.')