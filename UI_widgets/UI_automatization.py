from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(695, 243)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.info_btn_2 = QtWidgets.QPushButton(Form)
        self.info_btn_2.setObjectName("info_btn_2")
        self.horizontalLayout.addWidget(self.info_btn_2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.in_edit = QtWidgets.QLineEdit(Form)
        self.in_edit.setReadOnly(True)
        self.in_edit.setObjectName("in_edit")
        self.horizontalLayout_2.addWidget(self.in_edit)
        self.in_btn = QtWidgets.QPushButton(Form)
        self.in_btn.setObjectName("in_btn")
        self.horizontalLayout_2.addWidget(self.in_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.out_edit = QtWidgets.QLineEdit(Form)
        self.out_edit.setReadOnly(True)
        self.out_edit.setObjectName("out_edit")
        self.horizontalLayout_6.addWidget(self.out_edit)
        self.out_btn = QtWidgets.QPushButton(Form)
        self.out_btn.setObjectName("out_btn")
        self.horizontalLayout_6.addWidget(self.out_btn)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_7)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.start_btn = QtWidgets.QPushButton(Form)
        self.start_btn.setObjectName("start_btn")
        self.verticalLayout.addWidget(self.start_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
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
        self.indent_settings.setMinimum(0.05)
        self.indent_settings.setMaximum(2.0)
        self.indent_settings.setSingleStep(0.01)
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
        self.step_settings.setMinimum(0.05)
        self.step_settings.setMaximum(2.0)
        self.step_settings.setSingleStep(0.01)
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
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.use_presets = QtWidgets.QCheckBox(Form)
        self.use_presets.setObjectName("use_presets")
        self.verticalLayout_6.addWidget(self.use_presets)
        self.presets = QtWidgets.QComboBox(Form)
        self.presets.setEnabled(True)
        self.presets.setObjectName("presets")
        self.verticalLayout_6.addWidget(self.presets)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Настройки автоматизации"))
        self.info_btn_2.setText(_translate("Form", "Инфо"))
        self.label.setText(_translate("Form", "Пожалуйста, прочтите инструкцию перед использованием"))
        self.label_2.setText(_translate("Form", "Выберите папку для мониторинга"))
        self.in_btn.setText(_translate("Form", "Выбрать папку"))
        self.label_10.setText(_translate("Form", "Выберете папку для сохранения результатов:"))
        self.out_btn.setText(_translate("Form", "Выбрать папку"))
        self.checkBox.setText(_translate("Form", "Сохранять оригинал в подпапке RAW"))
        self.start_btn.setText(_translate("Form", "Запустить отслеживание папки"))
        self.label_9.setText(_translate("Form", "Настройки обработки видео: "))
        self.label_5.setText(_translate("Form", "Чувствительность"))
        self.label_6.setText(_translate("Form", "%"))
        self.label_4.setText(_translate("Form", "Отступ"))
        self.label_8.setText(_translate("Form", "сек."))
        self.label_3.setText(_translate("Form", "Шаг"))
        self.label_7.setText(_translate("Form", "сек."))
        self.info_btn.setText(_translate("Form", "Инфо"))
        self.default_btn.setText(_translate("Form", "По умолчанию"))
        self.use_presets.setText(_translate("Form", "Использовать пресеты"))