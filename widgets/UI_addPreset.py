from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_Preset(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(742, 259)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.sensitivity_settings = QtWidgets.QSpinBox(Form)
        self.sensitivity_settings.setMinimum(1)
        self.sensitivity_settings.setObjectName("sensitivity_settings")
        self.horizontalLayout_3.addWidget(self.sensitivity_settings)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.indent_settings = QtWidgets.QDoubleSpinBox(Form)
        self.indent_settings.setMinimum(0.01)
        self.indent_settings.setObjectName("indent_settings")
        self.horizontalLayout_4.addWidget(self.indent_settings)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.step_settings = QtWidgets.QDoubleSpinBox(Form)
        self.step_settings.setObjectName("step_settings")
        self.horizontalLayout_5.addWidget(self.step_settings)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.info_btn = QtWidgets.QPushButton(Form)
        self.info_btn.setObjectName("info_btn")
        self.verticalLayout_5.addWidget(self.info_btn)
        self.default_btn = QtWidgets.QPushButton(Form)
        self.default_btn.setObjectName("default_btn")
        self.verticalLayout_5.addWidget(self.default_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.preset_name = QtWidgets.QLineEdit(Form)
        self.preset_name.setText("")
        self.preset_name.setObjectName("preset_name")
        self.verticalLayout.addWidget(self.preset_name)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_btn = QtWidgets.QPushButton(Form)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.save_btn = QtWidgets.QPushButton(Form)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Создать новый пресет"))
        self.label_9.setText(_translate("Form", "Настройки обработки видео:"))
        self.label_5.setText(_translate("Form", "Чувствительность"))
        self.label_6.setText(_translate("Form", "%"))
        self.label_4.setText(_translate("Form", "Отступ"))
        self.label_8.setText(_translate("Form", "сек."))
        self.label_3.setText(_translate("Form", "Шаг"))
        self.label_7.setText(_translate("Form", "сек."))
        self.info_btn.setText(_translate("Form", "Инфо"))
        self.default_btn.setText(_translate("Form", "По умолчанию"))
        self.label.setText(_translate("Form", "Имя пресета"))
        self.cancel_btn.setText(_translate("Form", "Выход"))
        self.save_btn.setText(_translate("Form", "Сохранить"))