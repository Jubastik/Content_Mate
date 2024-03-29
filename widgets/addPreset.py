import webbrowser
from PyQt5.QtWidgets import QWidget, QMessageBox
import sqlite3

from UI_widgets.UI_addPreset import Ui_Add_Preset


class AddPresetWidget(QWidget, Ui_Add_Preset):
    def __init__(self, pmain, psettings, DB):
        super().__init__()
        self.setupUi(self)
        self.DB = DB
        self.pmain = pmain  # ссылка на основное окно
        self.psettings = psettings  # ссылка на окно настроек
        self.default_settings()
        self.connect_btn()
        self.create_dialog()

    def connect_btn(self):
        self.save_btn.clicked.connect(self.save_preset)
        self.default_btn.clicked.connect(self.default_settings)
        self.cancel_btn.clicked.connect(self.close_widget)
        self.info_btn.clicked.connect(self.open_info_web)

    def open_info_web(self):
        webbrowser.open(
            "https://docs.google.com/document/d/1Ei-w7j8RJc28rdgABKlUQFaKFfyEBid7K358f7bJuhY/edit#bookmark=id.t8ov2pdm0t5"
        )

    def default_settings(self):
        result = self.DB.get_default_processing_parameters()
        self.sensitivity_settings.setValue(result[0])
        self.indent_settings.setValue(result[1])
        self.step_settings.setValue(result[2])

    def save_preset(self):
        if self.preset_name.text() == "":
            self.msg_no_name.exec_()
        else:
            try:
                self.DB.save_preset(
                    self.preset_name.text(),
                    self.sensitivity_settings.value(),
                    self.indent_settings.value(),
                    self.step_settings.value(),
                )
                self.DB.con.commit()
                self.pmain.presets.addItem(self.preset_name.text())
                self.psettings.presets.addItem(self.preset_name.text())
            except sqlite3.IntegrityError:
                self.msg_bad_name.exec_()

    def close_widget(self):
        self.psettings.aw.hide()

    def create_dialog(self):
        self.msg_no_name = QMessageBox()
        self.msg_no_name.setIcon(QMessageBox.Warning)
        self.msg_no_name.setWindowTitle("Ошибка создания пресета")
        self.msg_no_name.setText("Пустое имя пресета")
        self.msg_no_name.setInformativeText("Пожалуйста введите имя для нового пресета")

        self.msg_bad_name = QMessageBox()
        self.msg_bad_name.setIcon(QMessageBox.Warning)
        self.msg_bad_name.setWindowTitle("Ошибка создания пресета")
        self.msg_bad_name.setText("Не уникальное имя пресета")
        self.msg_bad_name.setInformativeText(
            "Пожалуйста, введите уникальное имя пресета"
        )
