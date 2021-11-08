from PyQt5.QtWidgets import QWidget

from .UI_changePreset import Ui_Change_Preset


class ChangePresetWidget(QWidget, Ui_Change_Preset):
    def __init__(self, pmain, psettings):
        super().__init__()
        self.setupUi(self)
        self.pmain = pmain
        self.psettings = psettings
        self.load_combobox()
        self.combobox_changing()
        self.connect_all()

    def connect_all(self):
        self.presets.currentTextChanged.connect(self.combobox_changing)
        self.save_btn.clicked.connect(self.save_settings)
        self.cancel_btn.clicked.connect(self.close_widget)
        self.default_btn.clicked.connect(self.default_settings)

    def default_settings(self):
        cur = self.pmain.con.cursor()
        result = cur.execute(
            """select * from preset
            where Name = 'Default'"""
        ).fetchone()
        self.sensitivity_settings.setValue(result[1])
        self.indent_settings.setValue(result[2])
        self.step_settings.setValue(result[3])

    def combobox_changing(self):
        preset_name = self.presets.currentText()
        cur = self.pmain.con.cursor()
        result = cur.execute(
            """select Sensitivity, Indent, Step from preset 
            where Name = ?""", [preset_name]
        ).fetchone()
        self.sensitivity_settings.setValue(result[0])
        self.indent_settings.setValue(result[1])
        self.step_settings.setValue(result[2])

    def load_combobox(self):
        cur = self.pmain.con.cursor()
        result = cur.execute(
            """select Name from preset"""
        ).fetchall()
        result = [f'{i[0]}' for i in result]
        self.presets.addItems(result)

    def save_settings(self):
        cur = self.pmain.con.cursor()

        cur.execute("""
            update preset
            set Sensitivity = ?,
            Indent = ?,
            Step = ?
            where Name = ?""",
            [self.sensitivity_settings.value(), self.indent_settings.value(),
             self.step_settings.value(), self.presets.currentText()])
        self.pmain.con.commit()
        self.pmain.combobox_changing()

    def close_widget(self):
        self.psettings.cw.hide()