from PyQt5.QtWidgets import QFileDialog, QWidget, QMessageBox
import os

from .UI_settings import Ui_Form
from .addPreset import AddPresetWidget
from .changePreset import ChangePresetWidget

class SettingsWidget(QWidget, Ui_Form):
    def __init__(self, parent):
        super().__init__()
        # uic.loadUi('settings_v2.ui', self)
        self.setupUi(self)
        self.parent = parent #ссылка на основное окно
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
        self.aw = AddPresetWidget(self.parent, self)
        self.aw.show()

    def start_change_widget(self):
        self.cw = ChangePresetWidget(self.parent, self)
        self.cw.show()

    def load_settings_db(self):
        cur = self.parent.con.cursor()
        result = cur.execute(
            """select PathReadOnly, Log, OutPath from main 
            where id = 1"""
        ).fetchone()
        self.can_edit.setChecked(not result[0])
        self.log.setChecked(result[1])
        self.default_path.setText(result[2])

    def load_combobox(self):
        cur = self.parent.con.cursor()
        result = cur.execute(
            """select Name from preset"""
        ).fetchall()
        # result = [f'{n} - {s}% {i}сек. {st}сек.' for n, s, i, st in result]
        result = [f'{i[0]}' for i in result]
        self.presets.addItems(result)

    def delete_preset(self):
        name = self.presets.currentText()
        if name != "Default":
            cur = self.parent.con.cursor()
            cur.execute(
                """DELETE from preset
                    where Name = ?
                        """, [name])
            self.parent.con.commit()
            self.presets.removeItem(self.presets.findText(name))
            self.parent.presets.removeItem(self.parent.presets.findText(name))

    def save_settings(self):
        cur = self.parent.con.cursor()
        cur.execute("""
            update main
            set PathReadOnly = ?
            where id = 1
                """, [not self.can_edit.isChecked()]
                    ).fetchone()

        cur = self.parent.con.cursor()
        cur.execute("""
                update main
                set Log = ?
                where id = 1
                    """, [self.log.isChecked()]
                    ).fetchone()

        if self.default_path.text() == "" or os.path.isdir(self.default_path.text()):
            cur = self.parent.con.cursor()
            cur.execute("""
                    update main
                    set OutPath = ?
                    where id = 1
                            """, [self.default_path.text()]).fetchone()

        self.parent.con.commit()
        self.parent.load_settings_db()

    def load_path(self):
        fname = QFileDialog.getExistingDirectory(self, 'Выбрать папку', '')
        if fname:
            self.default_path.setText(fname)

    def close_widget(self):
        self.parent.sw.hide()