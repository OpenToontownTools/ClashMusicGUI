''' Auto Generated from QTDesigner '''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_CompilingDialog(object):
    def setupUi(self, CompilingDialog):
        if not CompilingDialog.objectName():
            CompilingDialog.setObjectName(u"CompilingDialog")
        CompilingDialog.setWindowModality(Qt.ApplicationModal)
        CompilingDialog.setEnabled(True)
        CompilingDialog.resize(587, 371)
        CompilingDialog.setAutoFillBackground(False)
        CompilingDialog.setSizeGripEnabled(False)
        CompilingDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(CompilingDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.output = QTextEdit(CompilingDialog)
        self.output.setObjectName(u"output")
        self.output.setReadOnly(True)

        self.verticalLayout.addWidget(self.output)

        self.buttonBox = QDialogButtonBox(CompilingDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setEnabled(False)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Open)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(CompilingDialog)
        self.buttonBox.accepted.connect(CompilingDialog.accept)
        self.buttonBox.rejected.connect(CompilingDialog.reject)

        QMetaObject.connectSlotsByName(CompilingDialog)
    # setupUi

    def retranslateUi(self, CompilingDialog):
        CompilingDialog.setWindowTitle(QCoreApplication.translate("CompilingDialog", u"Clash Resource Pack Editor", None))
        self.output.setDocumentTitle(QCoreApplication.translate("CompilingDialog", u"k", None))
    # retranslateUi

