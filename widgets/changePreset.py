import webbrowser

from PyQt5.QtWidgets import QWidget

from .UI_changePreset import Ui_Change_Preset


class ChangePresetWidget(QWidget, Ui_Change_Preset):
    def __init__(self, pmain, psettings, DB):
        super().__init__()
        self.setupUi(self)
        self.DB = DB
        self.pmain = pmain  # ссылка на основное окно
        self.psettings = psettings  # ссылка на окно настроек
        self.load_combobox()
        self.combobox_changing()
        self.connect_all()

    def connect_all(self):
        self.presets.currentTextChanged.connect(self.combobox_changing)
        self.save_btn.clicked.connect(self.save_settings)
        self.cancel_btn.clicked.connect(self.close_widget)
        self.default_btn.clicked.connect(self.default_settings)
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

    def combobox_changing(self):
        preset_name = self.presets.currentText()
        result = self.DB.get_processing_parameters(preset_name)
        self.sensitivity_settings.setValue(result[0])
        self.indent_settings.setValue(result[1])
        self.step_settings.setValue(result[2])

    def load_combobox(self):
        result = self.DB.get_all_preset_names()
        self.presets.addItems(result)

    def save_settings(self):
        self.DB.update_processing_parameters(
            self.presets.currentText(),
            self.sensitivity_settings.value(),
            self.indent_settings.value(),
            self.step_settings.value(),
        )
        self.DB.con.commit()
        self.pmain.combobox_changing()

    def close_widget(self):
        self.psettings.cw.hide()
