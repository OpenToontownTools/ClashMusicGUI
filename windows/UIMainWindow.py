''' Auto Generated from QTDesigner '''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(906, 682)
        MainWindow.setStyleSheet(u"*{font-family:\n"
" \"Impress BT\";}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(240)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(41)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.overrideTable_HA = QTableWidget(self.tab_2)
        if (self.overrideTable_HA.columnCount() < 2):
            self.overrideTable_HA.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.overrideTable_HA.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.overrideTable_HA.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.overrideTable_HA.setObjectName(u"overrideTable_HA")
        self.overrideTable_HA.setSelectionMode(QAbstractItemView.NoSelection)
        self.overrideTable_HA.setGridStyle(Qt.SolidLine)
        self.overrideTable_HA.setCornerButtonEnabled(False)
        self.overrideTable_HA.horizontalHeader().setCascadingSectionResizes(False)
        self.overrideTable_HA.horizontalHeader().setMinimumSectionSize(60)
        self.overrideTable_HA.horizontalHeader().setDefaultSectionSize(240)
        self.overrideTable_HA.horizontalHeader().setProperty("showSortIndicator", False)
        self.overrideTable_HA.horizontalHeader().setStretchLastSection(True)
        self.overrideTable_HA.verticalHeader().setCascadingSectionResizes(False)
        self.overrideTable_HA.verticalHeader().setMinimumSectionSize(41)
        self.overrideTable_HA.verticalHeader().setProperty("showSortIndicator", False)
        self.overrideTable_HA.verticalHeader().setStretchLastSection(False)

        self.gridLayout_4.addWidget(self.overrideTable_HA, 1, 0, 1, 2)

        self.addOverrideButton_HA = QPushButton(self.tab_2)
        self.addOverrideButton_HA.setObjectName(u"addOverrideButton_HA")
        self.addOverrideButton_HA.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_4.addWidget(self.addOverrideButton_HA, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.overrideTable_WI = QTableWidget(self.tab_3)
        if (self.overrideTable_WI.columnCount() < 2):
            self.overrideTable_WI.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.overrideTable_WI.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.overrideTable_WI.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.overrideTable_WI.setObjectName(u"overrideTable_WI")
        self.overrideTable_WI.setSelectionMode(QAbstractItemView.NoSelection)
        self.overrideTable_WI.setGridStyle(Qt.SolidLine)
        self.overrideTable_WI.setCornerButtonEnabled(False)
        self.overrideTable_WI.horizontalHeader().setCascadingSectionResizes(False)
        self.overrideTable_WI.horizontalHeader().setMinimumSectionSize(60)
        self.overrideTable_WI.horizontalHeader().setDefaultSectionSize(240)
        self.overrideTable_WI.horizontalHeader().setProperty("showSortIndicator", False)
        self.overrideTable_WI.horizontalHeader().setStretchLastSection(True)
        self.overrideTable_WI.verticalHeader().setCascadingSectionResizes(False)
        self.overrideTable_WI.verticalHeader().setMinimumSectionSize(41)
        self.overrideTable_WI.verticalHeader().setProperty("showSortIndicator", False)
        self.overrideTable_WI.verticalHeader().setStretchLastSection(False)

        self.gridLayout_5.addWidget(self.overrideTable_WI, 1, 0, 1, 2)

        self.addOverrideButton_WI = QPushButton(self.tab_3)
        self.addOverrideButton_WI.setObjectName(u"addOverrideButton_WI")
        self.addOverrideButton_WI.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_5.addWidget(self.addOverrideButton_WI, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_6 = QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.overrideTable_AF = QTableWidget(self.tab_4)
        if (self.overrideTable_AF.columnCount() < 2):
            self.overrideTable_AF.setColumnCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.overrideTable_AF.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.overrideTable_AF.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        self.overrideTable_AF.setObjectName(u"overrideTable_AF")
        self.overrideTable_AF.setSelectionMode(QAbstractItemView.NoSelection)
        self.overrideTable_AF.setGridStyle(Qt.SolidLine)
        self.overrideTable_AF.setCornerButtonEnabled(False)
        self.overrideTable_AF.horizontalHeader().setCascadingSectionResizes(False)
        self.overrideTable_AF.horizontalHeader().setMinimumSectionSize(60)
        self.overrideTable_AF.horizontalHeader().setDefaultSectionSize(240)
        self.overrideTable_AF.horizontalHeader().setProperty("showSortIndicator", False)
        self.overrideTable_AF.horizontalHeader().setStretchLastSection(True)
        self.overrideTable_AF.verticalHeader().setCascadingSectionResizes(False)
        self.overrideTable_AF.verticalHeader().setMinimumSectionSize(41)
        self.overrideTable_AF.verticalHeader().setProperty("showSortIndicator", False)
        self.overrideTable_AF.verticalHeader().setStretchLastSection(False)

        self.gridLayout_6.addWidget(self.overrideTable_AF, 1, 0, 1, 2)

        self.addOverrideButton_AF = QPushButton(self.tab_4)
        self.addOverrideButton_AF.setObjectName(u"addOverrideButton_AF")
        self.addOverrideButton_AF.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_6.addWidget(self.addOverrideButton_AF, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_7 = QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_5 = QLabel(self.tab_5)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamily(u"Impress BT")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_5, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 6, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.label_4 = QLabel(self.tab_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(128, 0))
        font1 = QFont()
        font1.setFamily(u"Impress BT")
        font1.setPointSize(20)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_4, 2, 1, 1, 1)

        self.graphicsView = QGraphicsView(self.tab_5)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setEnabled(False)
        self.graphicsView.setMaximumSize(QSize(128, 128))

        self.gridLayout_7.addWidget(self.graphicsView, 3, 1, 1, 1)

        self.textEdit = QTextEdit(self.tab_5)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 24))

        self.gridLayout_7.addWidget(self.textEdit, 1, 2, 1, 1)

        self.pushButton = QPushButton(self.tab_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(128, 0))
        self.pushButton.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"Impress BT")
        font2.setKerning(True)
        self.pushButton.setFont(font2)
        self.pushButton.setFlat(False)

        self.gridLayout_7.addWidget(self.pushButton, 4, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_2 = QGridLayout(self.tab_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.tab_6)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamily(u"Impress BT")
        font3.setPointSize(14)
        self.label_2.setFont(font3)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.optionsBrowsePandaPath = QPushButton(self.tab_6)
        self.optionsBrowsePandaPath.setObjectName(u"optionsBrowsePandaPath")
        sizePolicy.setHeightForWidth(self.optionsBrowsePandaPath.sizePolicy().hasHeightForWidth())
        self.optionsBrowsePandaPath.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.optionsBrowsePandaPath, 0, 1, 1, 1)

        self.label_3 = QLabel(self.tab_6)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamily(u"Impress BT")
        font4.setItalic(True)
        self.label_3.setFont(font4)
        self.label_3.setFrameShadow(QFrame.Plain)

        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 4)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 16777215))
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setFlat(False)

        self.gridLayout.addWidget(self.saveButton, 5, 2, 1, 1)

        self.compileButton = QPushButton(self.centralwidget)
        self.compileButton.setObjectName(u"compileButton")

        self.gridLayout.addWidget(self.compileButton, 5, 3, 1, 1)

        self.rootDisplay = QLabel(self.centralwidget)
        self.rootDisplay.setObjectName(u"rootDisplay")
        self.rootDisplay.setFrameShape(QFrame.StyledPanel)
        self.rootDisplay.setScaledContents(True)

        self.gridLayout.addWidget(self.rootDisplay, 5, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 906, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Corporate Clash Resource Pack Editor", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"file", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Default", None))
        ___qtablewidgetitem2 = self.overrideTable_HA.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem3 = self.overrideTable_HA.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"file", None));
        self.addOverrideButton_HA.setText(QCoreApplication.translate("MainWindow", u"Add Override", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Halloween Overrides", None))
        ___qtablewidgetitem4 = self.overrideTable_WI.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem5 = self.overrideTable_WI.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"file", None));
        self.addOverrideButton_WI.setText(QCoreApplication.translate("MainWindow", u"Add Override", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Winter Overrides", None))
        ___qtablewidgetitem6 = self.overrideTable_AF.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem7 = self.overrideTable_AF.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"file", None));
        self.addOverrideButton_AF.setText(QCoreApplication.translate("MainWindow", u"Add Override", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"April Fools Overrides", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Pack Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pack Icon", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Pack Info", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Panda Path", None))
        self.optionsBrowsePandaPath.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Options", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pack Root", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.compileButton.setText(QCoreApplication.translate("MainWindow", u"Compile Resource Pack", None))
        self.rootDisplay.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi


