# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mxtt_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(578, 345)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tab_broker = QTabWidget(Form)
        self.tab_broker.setObjectName(u"tab_broker")
        self.tab_messages = QWidget()
        self.tab_messages.setObjectName(u"tab_messages")
        self.tab_messages.setMinimumSize(QSize(558, 0))
        self.verticalLayout_3 = QVBoxLayout(self.tab_messages)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listView_msg = QListWidget(self.tab_messages)
        self.listView_msg.setObjectName(u"listView_msg")

        self.verticalLayout_3.addWidget(self.listView_msg)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.input_send_msg = QLineEdit(self.tab_messages)
        self.input_send_msg.setObjectName(u"input_send_msg")

        self.horizontalLayout_2.addWidget(self.input_send_msg)

        self.pb_send = QPushButton(self.tab_messages)
        self.pb_send.setObjectName(u"pb_send")

        self.horizontalLayout_2.addWidget(self.pb_send)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tab_broker.addTab(self.tab_messages, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.input_port = QLineEdit(self.tab_2)
        self.input_port.setObjectName(u"input_port")
        self.input_port.setMaximumSize(QSize(16777215, 16777215))
        self.input_port.setMaxLength(50)

        self.horizontalLayout_3.addWidget(self.input_port)

        self.check_tls = QCheckBox(self.tab_2)
        self.check_tls.setObjectName(u"check_tls")
        self.check_tls.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.check_tls)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 3, 1, 1)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.input_password = QLineEdit(self.tab_2)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setMaxLength(50)
        self.input_password.setFrame(True)
        self.input_password.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.input_password, 1, 3, 1, 1)

        self.input_user = QLineEdit(self.tab_2)
        self.input_user.setObjectName(u"input_user")
        self.input_user.setMaxLength(50)

        self.gridLayout.addWidget(self.input_user, 1, 1, 1, 1)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)

        self.input_url = QLineEdit(self.tab_2)
        self.input_url.setObjectName(u"input_url")
        self.input_url.setMaxLength(100)
        self.input_url.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.input_url, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.input_topic_1 = QLineEdit(self.tab_2)
        self.input_topic_1.setObjectName(u"input_topic_1")

        self.horizontalLayout_4.addWidget(self.input_topic_1)

        self.pb_subscribe = QPushButton(self.tab_2)
        self.pb_subscribe.setObjectName(u"pb_subscribe")

        self.horizontalLayout_4.addWidget(self.pb_subscribe)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_config_save = QPushButton(self.tab_2)
        self.pb_config_save.setObjectName(u"pb_config_save")
        self.pb_config_save.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.pb_config_save)

        self.pb_connect = QPushButton(self.tab_2)
        self.pb_connect.setObjectName(u"pb_connect")
        self.pb_connect.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.pb_connect)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tab_broker.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tab_broker)

        QWidget.setTabOrder(self.input_url, self.input_port)
        QWidget.setTabOrder(self.input_port, self.check_tls)
        QWidget.setTabOrder(self.check_tls, self.input_user)
        QWidget.setTabOrder(self.input_user, self.input_password)
        QWidget.setTabOrder(self.input_password, self.input_topic_1)
        QWidget.setTabOrder(self.input_topic_1, self.pb_subscribe)
        QWidget.setTabOrder(self.pb_subscribe, self.pb_config_save)
        QWidget.setTabOrder(self.pb_config_save, self.pb_connect)
        QWidget.setTabOrder(self.pb_connect, self.tab_broker)
        QWidget.setTabOrder(self.tab_broker, self.input_send_msg)
        QWidget.setTabOrder(self.input_send_msg, self.pb_send)
        QWidget.setTabOrder(self.pb_send, self.listView_msg)

        self.retranslateUi(Form)

        self.tab_broker.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.input_send_msg.setPlaceholderText(QCoreApplication.translate("Form", u"topic : value", None))
        self.pb_send.setText(QCoreApplication.translate("Form", u"Send", None))
        self.tab_broker.setTabText(self.tab_broker.indexOf(self.tab_messages), QCoreApplication.translate("Form", u"Messages", None))
        self.input_port.setPlaceholderText(QCoreApplication.translate("Form", u"1883", None))
        self.check_tls.setText(QCoreApplication.translate("Form", u"TLS", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"User", None))
        self.label.setText(QCoreApplication.translate("Form", u"URL", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Port", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Topic", None))
        self.pb_subscribe.setText(QCoreApplication.translate("Form", u"Subscribe", None))
        self.pb_config_save.setText(QCoreApplication.translate("Form", u"Save Config", None))
        self.pb_connect.setText(QCoreApplication.translate("Form", u"Connect", None))
        self.tab_broker.setTabText(self.tab_broker.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Broker", None))
    # retranslateUi

