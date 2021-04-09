from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(881, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(11, 11, 581, 344))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        self.grp_box_pgen = QtWidgets.QGroupBox(self.centralwidget)
        self.grp_box_pgen.setGeometry(QtCore.QRect(10, 370, 426, 119))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grp_box_pgen.sizePolicy().hasHeightForWidth())
        self.grp_box_pgen.setSizePolicy(sizePolicy)
        self.grp_box_pgen.setMinimumSize(QtCore.QSize(0, 111))
        self.grp_box_pgen.setAutoFillBackground(False)
        self.grp_box_pgen.setFlat(False)
        self.grp_box_pgen.setObjectName("grp_box_pgen")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.grp_box_pgen)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_slen_pgen = QtWidgets.QLabel(self.grp_box_pgen)
        self.lbl_slen_pgen.setObjectName("lbl_slen_pgen")
        self.gridLayout_2.addWidget(self.lbl_slen_pgen, 0, 0, 1, 1)
        self.tbox_slen_pgen = QtWidgets.QLineEdit(self.grp_box_pgen)
        self.tbox_slen_pgen.setMinimumSize(QtCore.QSize(0, 20))
        self.tbox_slen_pgen.setFrame(True)
        self.tbox_slen_pgen.setObjectName("tbox_slen_pgen")
        self.gridLayout_2.addWidget(self.tbox_slen_pgen, 0, 1, 1, 2)
        self.btn_genpass = QtWidgets.QPushButton(self.grp_box_pgen)
        self.btn_genpass.setMinimumSize(QtCore.QSize(100, 23))
        self.btn_genpass.setObjectName("btn_genpass")
        self.gridLayout_2.addWidget(self.btn_genpass, 0, 3, 1, 1)
        self.lbl_genpass_pgen = QtWidgets.QLabel(self.grp_box_pgen)
        self.lbl_genpass_pgen.setObjectName("lbl_genpass_pgen")
        self.gridLayout_2.addWidget(self.lbl_genpass_pgen, 1, 0, 1, 1)
        self.btn_cpy_pass = QtWidgets.QPushButton(self.grp_box_pgen)
        self.btn_cpy_pass.setMinimumSize(QtCore.QSize(80, 23))
        self.btn_cpy_pass.setObjectName("btn_cpy_pass")
        self.gridLayout_2.addWidget(self.btn_cpy_pass, 2, 1, 1, 1)
        self.lbl_warn_pgen = QtWidgets.QLabel(self.grp_box_pgen)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lbl_warn_pgen.setPalette(palette)
        self.lbl_warn_pgen.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl_warn_pgen.setTextFormat(QtCore.Qt.PlainText)
        self.lbl_warn_pgen.setObjectName("lbl_warn_pgen")
        self.gridLayout_2.addWidget(self.lbl_warn_pgen, 2, 2, 1, 2)
        self.tbox_genpass_pgen = QtWidgets.QLineEdit(self.grp_box_pgen)
        self.tbox_genpass_pgen.setMinimumSize(QtCore.QSize(242, 20))
        self.tbox_genpass_pgen.setStyleSheet("")
        self.tbox_genpass_pgen.setFrame(True)
        self.tbox_genpass_pgen.setObjectName("tbox_genpass_pgen")
        self.gridLayout_2.addWidget(self.tbox_genpass_pgen, 1, 1, 1, 3)
        self.lbl_showpass_pgen = QtWidgets.QLabel(self.grp_box_pgen)
        self.lbl_showpass_pgen.setEnabled(True)
        self.lbl_showpass_pgen.setGeometry(QtCore.QRect(336, 52, 20, 20))
        self.lbl_showpass_pgen.setStyleSheet("background-color: transparent;")
        self.lbl_showpass_pgen.setText("")
        self.lbl_showpass_pgen.setPixmap(QtGui.QPixmap("../../Mega/Downloads/showpass.png"))
        self.lbl_showpass_pgen.setScaledContents(True)
        self.lbl_showpass_pgen.setObjectName("lbl_showpass_pgen")
        self.tbox_genpass_pgen.raise_()
        self.lbl_genpass_pgen.raise_()
        self.lbl_warn_pgen.raise_()
        self.btn_genpass.raise_()
        self.lbl_slen_pgen.raise_()
        self.tbox_slen_pgen.raise_()
        self.btn_cpy_pass.raise_()
        self.lbl_showpass_pgen.raise_()
        self.btn_logout = QtWidgets.QPushButton(self.centralwidget)
        self.btn_logout.setGeometry(QtCore.QRect(460, 370, 126, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QtCore.QSize(0, 23))
        self.btn_logout.setMaximumSize(QtCore.QSize(126, 16777215))
        self.btn_logout.setObjectName("btn_logout")
        self.tab_login = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_login.setGeometry(QtCore.QRect(600, 10, 265, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_login.sizePolicy().hasHeightForWidth())
        self.tab_login.setSizePolicy(sizePolicy)
        self.tab_login.setMinimumSize(QtCore.QSize(0, 215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tab_login.setPalette(palette)
        self.tab_login.setAutoFillBackground(False)
        
        self.tab_login.setObjectName("tab_login")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget_login = QtWidgets.QWidget(self.tab)
        self.widget_login.setGeometry(QtCore.QRect(3, 3, 261, 111))
        self.widget_login.setObjectName("widget_login")
        self.lbl_user_login = QtWidgets.QLabel(self.widget_login)
        self.lbl_user_login.setGeometry(QtCore.QRect(9, 9, 48, 16))
        self.lbl_user_login.setObjectName("lbl_user_login")
        self.tbox_user_login = QtWidgets.QLineEdit(self.widget_login)
        self.tbox_user_login.setGeometry(QtCore.QRect(63, 9, 184, 20))
        self.tbox_user_login.setFrame(True)
        self.tbox_user_login.setObjectName("tbox_user_login")
        self.lbl_pass_login = QtWidgets.QLabel(self.widget_login)
        self.lbl_pass_login.setGeometry(QtCore.QRect(9, 35, 46, 16))
        self.lbl_pass_login.setObjectName("lbl_pass_login")
        self.tbox_pass_login = QtWidgets.QLineEdit(self.widget_login)
        self.tbox_pass_login.setGeometry(QtCore.QRect(63, 35, 184, 20))
        self.tbox_pass_login.setFrame(True)
        self.tbox_pass_login.setObjectName("tbox_pass_login")
        self.btn_login = QtWidgets.QPushButton(self.widget_login)
        self.btn_login.setGeometry(QtCore.QRect(10, 64, 241, 23))
        self.btn_login.setMinimumSize(QtCore.QSize(0, 23))
        self.btn_login.setObjectName("btn_login")
        self.lbl_warn_login = QtWidgets.QLabel(self.widget_login)
        self.lbl_warn_login.setGeometry(QtCore.QRect(10, 87, 241, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_warn_login.sizePolicy().hasHeightForWidth())
        self.lbl_warn_login.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lbl_warn_login.setPalette(palette)
        self.lbl_warn_login.setTextFormat(QtCore.Qt.PlainText)
        self.lbl_warn_login.setObjectName("lbl_warn_login")
        self.lbl_showpass_login = QtWidgets.QLabel(self.widget_login)
        self.lbl_showpass_login.setEnabled(True)
        self.lbl_showpass_login.setGeometry(QtCore.QRect(224, 35, 21, 20))
        self.lbl_showpass_login.setStyleSheet("background-color: transparent;")
        self.lbl_showpass_login.setText("")
        self.lbl_showpass_login.setPixmap(QtGui.QPixmap("../../Mega/Downloads/showpass.png"))
        self.lbl_showpass_login.setScaledContents(True)
        self.lbl_showpass_login.setObjectName("lbl_showpass_login")
        self.tab_login.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget_signup = QtWidgets.QWidget(self.tab_2)
        self.widget_signup.setGeometry(QtCore.QRect(3, 3, 261, 311))
        self.widget_signup.setObjectName("widget_signup")
        self.lbl_user_signup = QtWidgets.QLabel(self.widget_signup)
        self.lbl_user_signup.setGeometry(QtCore.QRect(9, 9, 48, 16))
        self.lbl_user_signup.setObjectName("lbl_user_signup")
        self.tbox_user_signup = QtWidgets.QLineEdit(self.widget_signup)
        self.tbox_user_signup.setGeometry(QtCore.QRect(76, 9, 171, 20))
        self.tbox_user_signup.setInputMask("")
        self.tbox_user_signup.setFrame(True)
        self.tbox_user_signup.setObjectName("tbox_user_signup")
        self.lbl_pass_signup = QtWidgets.QLabel(self.widget_signup)
        self.lbl_pass_signup.setGeometry(QtCore.QRect(9, 35, 46, 16))
        self.lbl_pass_signup.setObjectName("lbl_pass_signup")
        self.tbox_pass_signup = QtWidgets.QLineEdit(self.widget_signup)
        self.tbox_pass_signup.setGeometry(QtCore.QRect(76, 35, 171, 20))
        self.tbox_pass_signup.setInputMask("")
        self.tbox_pass_signup.setFrame(True)
        self.tbox_pass_signup.setObjectName("tbox_pass_signup")
        self.lbl_repass_signup = QtWidgets.QLabel(self.widget_signup)
        self.lbl_repass_signup.setGeometry(QtCore.QRect(9, 61, 61, 16))
        self.lbl_repass_signup.setObjectName("lbl_repass_signup")
        self.tbox_repass_signup = QtWidgets.QLineEdit(self.widget_signup)
        self.tbox_repass_signup.setGeometry(QtCore.QRect(76, 61, 171, 20))
        self.tbox_repass_signup.setFrame(True)
        self.tbox_repass_signup.setObjectName("tbox_repass_signup")
        self.chkbox_2fa_signup = QtWidgets.QCheckBox(self.widget_signup)
        self.chkbox_2fa_signup.setGeometry(QtCore.QRect(76, 86, 100, 17))
        self.chkbox_2fa_signup.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkbox_2fa_signup.setChecked(True)
        self.chkbox_2fa_signup.setTristate(False)
        self.chkbox_2fa_signup.setObjectName("chkbox_2fa_signup")
        self.btn_signup = QtWidgets.QPushButton(self.widget_signup)
        self.btn_signup.setGeometry(QtCore.QRect(9, 264, 241, 23))
        self.btn_signup.setCheckable(False)
        self.btn_signup.setFlat(False)
        self.btn_signup.setObjectName("btn_signup")
        self.lbl_warn_signup = QtWidgets.QLabel(self.widget_signup)
        self.lbl_warn_signup.setGeometry(QtCore.QRect(8, 287, 241, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lbl_warn_signup.setPalette(palette)
        self.lbl_warn_signup.setTextFormat(QtCore.Qt.PlainText)
        self.lbl_warn_signup.setObjectName("lbl_warn_signup")
        self.lbl_qr_signup = QtWidgets.QLabel(self.widget_signup)
        self.lbl_qr_signup.setGeometry(QtCore.QRect(55, 107, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_qr_signup.sizePolicy().hasHeightForWidth())
        self.lbl_qr_signup.setSizePolicy(sizePolicy)
        self.lbl_qr_signup.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_qr_signup.setMaximumSize(QtCore.QSize(150, 150))
        self.lbl_qr_signup.setText("")
        self.lbl_qr_signup.setPixmap(QtGui.QPixmap("../../Mega/Pictures/Screenshots/Screenshot (1).png"))
        self.lbl_qr_signup.setScaledContents(True)
        self.lbl_qr_signup.setObjectName("lbl_qr_signup")
        self.lbl_showpass1_signup = QtWidgets.QLabel(self.widget_signup)
        self.lbl_showpass1_signup.setEnabled(True)
        self.lbl_showpass1_signup.setGeometry(QtCore.QRect(224, 35, 21, 20))
        self.lbl_showpass1_signup.setText("")
        self.lbl_showpass1_signup.setPixmap(QtGui.QPixmap("../../Mega/Downloads/showpass.png"))
        self.lbl_showpass1_signup.setScaledContents(True)
        self.lbl_showpass1_signup.setObjectName("lbl_showpass1_signup")
        self.lbl_showpass2_signup = QtWidgets.QLabel(self.widget_signup)
        self.lbl_showpass2_signup.setEnabled(True)
        self.lbl_showpass2_signup.setGeometry(QtCore.QRect(224, 61, 21, 20))
        self.lbl_showpass2_signup.setText("")
        self.lbl_showpass2_signup.setPixmap(QtGui.QPixmap("../../Mega/Downloads/showpass.png"))
        self.lbl_showpass2_signup.setScaledContents(True)
        self.lbl_showpass2_signup.setObjectName("lbl_showpass2_signup")
        self.tab_login.addTab(self.tab_2, "")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(600, 370, 268, 111))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 881, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_login.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Account Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "User Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date Created"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Google"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "sadadw"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "dwdw"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "wdwd"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Facebook"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "dwdwdw"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "dwdw"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "wdwdw"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "wdwd"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "dwd"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "dwdwd"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("MainWindow", "wdwdwd"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "dwdwdwd"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "wdw"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("MainWindow", "wdwd"))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("MainWindow", "wdwd"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.grp_box_pgen.setTitle(_translate("MainWindow", "PassWord Generator"))
        self.lbl_slen_pgen.setText(_translate("MainWindow", "String Length"))
        self.tbox_slen_pgen.setPlaceholderText(_translate("MainWindow", "8"))
        self.btn_genpass.setText(_translate("MainWindow", "Generate Password"))
        self.lbl_genpass_pgen.setText(_translate("MainWindow", "Generated Password"))
        self.btn_cpy_pass.setText(_translate("MainWindow", "Copy Password"))
        self.lbl_warn_pgen.setText(_translate("MainWindow", "String Length Cannot Be Empty!"))
        self.tbox_genpass_pgen.setPlaceholderText(_translate("MainWindow", "●●●●●●●●●●"))
        self.btn_logout.setText(_translate("MainWindow", "Logout"))
        self.lbl_user_login.setText(_translate("MainWindow", "Username"))
        self.tbox_user_login.setPlaceholderText(_translate("MainWindow", "qwe123"))
        self.lbl_pass_login.setText(_translate("MainWindow", "Password"))
        self.tbox_pass_login.setPlaceholderText(_translate("MainWindow", "●●●●●●●●●●"))
        self.btn_login.setText(_translate("MainWindow", "Login"))
        self.lbl_warn_login.setText(_translate("MainWindow", "awdawdawddwdw"))
        self.tab_login.setTabText(self.tab_login.indexOf(self.tab), _translate("MainWindow", "Login"))
        self.lbl_user_signup.setText(_translate("MainWindow", "Username"))
        self.tbox_user_signup.setPlaceholderText(_translate("MainWindow", "qwe123"))
        self.lbl_pass_signup.setText(_translate("MainWindow", "Password"))
        self.tbox_pass_signup.setPlaceholderText(_translate("MainWindow", "●●●●●●●●●●"))
        self.lbl_repass_signup.setText(_translate("MainWindow", "Retype-Pass"))
        self.tbox_repass_signup.setPlaceholderText(_translate("MainWindow", "●●●●●●●●●●"))
        self.chkbox_2fa_signup.setText(_translate("MainWindow", "Enable OTP 2FA"))
        self.btn_signup.setText(_translate("MainWindow", "SignUp"))
        self.lbl_warn_signup.setText(_translate("MainWindow", "Changes Made Successfully!"))
        self.tab_login.setTabText(self.tab_login.indexOf(self.tab_2), _translate("MainWindow", "New User"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "dwdwd"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "w"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "dw"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "d"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "wd"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "wd"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "w"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "dw"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "d"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "wd"))
        item = self.listWidget.item(10)
        item.setText(_translate("MainWindow", "wd"))
        item = self.listWidget.item(11)
        item.setText(_translate("MainWindow", "wd"))
        item = self.listWidget.item(12)
        item.setText(_translate("MainWindow", "w"))
        item = self.listWidget.item(13)
        item.setText(_translate("MainWindow", "dw"))
        item = self.listWidget.item(14)
        item.setText(_translate("MainWindow", "d"))
        item = self.listWidget.item(15)
        item.setText(_translate("MainWindow", "wd"))
        item = self.listWidget.item(16)
        item.setText(_translate("MainWindow", "d"))
        item = self.listWidget.item(17)
        item.setText(_translate("MainWindow", "w"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())