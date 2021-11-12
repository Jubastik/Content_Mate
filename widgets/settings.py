from PyQt5.QtWidgets import QFileDialog, QWidget

from .UI_settings import Ui_Form
from .addPreset import AddPresetWidget
from .changePreset import ChangePresetWidget


class SettingsWidget(QWidget, Ui_Form):
    def __init__(self, parent, DB):
        super().__init__()
        self.setupUi(self)
        self.DB = DB
        self.parent = parent  # ссылка на основное окно
        self.connect_btn()
        self.load_settings_db()
        self.load_combobox()

    def connect_btn(self):
        self.choose_path_btn.clicked.connect(self.load_path)
        self.save_btn.clicked.connect(self.save_settings)
        self.delete_preset_btn.clicked.connect(self.delete_preset)
        self.create_preset_btn.clicked.connect(self.start_add_wiget)
        self.change_preset_btn.clicked.connect(self.start_change_widget)
        self.cancel_btn.clicked.connect(self.close_widget)

    def start_add_wiget(self):
        self.aw = AddPresetWidget(self.parent, self, self.DB)
        self.aw.show()

    def start_change_widget(self):
        self.cw = ChangePresetWidget(self.parent, self, self.DB)
        self.cw.show()

    def load_settings_db(self):
        result = self.DB.get_start_settings()
        self.can_edit.setChecked(not result[0])
        self.log.setChecked(result[1])
        self.default_path.setText(result[2])

    def load_combobox(self):
        result = self.DB.get_all_preset_names()
        self.presets.addItems(result)

    def delete_preset(self):
        name = self.presets.currentText()
        if name != "Default":
            self.DB.del_preset(name)
            self.DB.con.commit()
            self.presets.removeItem(self.presets.findText(name))
            self.parent.presets.removeItem(self.parent.presets.findText(name))

    def save_settings(self):
        self.DB.update_settings(
            not self.can_edit.isChecked(),
            self.log.isChecked(),
            self.default_path.text(),
        )
        self.DB.con.commit()
        self.parent.load_settings_db()

    def load_path(self):
        fname = QFileDialog.getExistingDirectory(self, "Выбрать папку", "")
        if fname:
            self.default_path.setText(fname)

    def close_widget(self):
        self.parent.sw.hide()
