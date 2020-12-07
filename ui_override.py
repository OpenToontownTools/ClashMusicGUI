''' Auto Generated from QTDesigner '''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_OverrideUI(object):
    def setupUi(self, OverrideUI):
        if not OverrideUI.objectName():
            OverrideUI.setObjectName(u"OverrideUI")
        OverrideUI.setWindowModality(Qt.ApplicationModal)
        OverrideUI.resize(811, 622)
        OverrideUI.setModal(True)
        self.gridLayout = QGridLayout(OverrideUI)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(OverrideUI)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.listWidget = QListWidget(OverrideUI)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFrameShape(QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QFrame.Raised)
        self.listWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.listWidget.setViewMode(QListView.ListMode)
        self.listWidget.setSelectionRectVisible(True)
        self.listWidget.setSortingEnabled(True)

        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)


        self.retranslateUi(OverrideUI)
        self.buttonBox.accepted.connect(OverrideUI.accept)
        self.buttonBox.rejected.connect(OverrideUI.reject)

        QMetaObject.connectSlotsByName(OverrideUI)
    # setupUi

    def retranslateUi(self, OverrideUI):
        OverrideUI.setWindowTitle(QCoreApplication.translate("OverrideUI", u"Add Override", None))
    # retranslateUi

