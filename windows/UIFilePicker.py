''' Auto Generated from QTDesigner '''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_FileSelectDial(object):
    def setupUi(self, FileSelectDial):
        if not FileSelectDial.objectName():
            FileSelectDial.setObjectName(u"FileSelectDial")
        FileSelectDial.setWindowModality(Qt.ApplicationModal)
        FileSelectDial.resize(241, 197)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FileSelectDial.sizePolicy().hasHeightForWidth())
        FileSelectDial.setSizePolicy(sizePolicy)
        FileSelectDial.setMinimumSize(QSize(241, 197))
        FileSelectDial.setMaximumSize(QSize(241, 197))
        FileSelectDial.setModal(True)
        self.verticalLayout = QVBoxLayout(FileSelectDial)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(FileSelectDial)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.selectedLabel = QLabel(FileSelectDial)
        self.selectedLabel.setObjectName(u"selectedLabel")

        self.verticalLayout.addWidget(self.selectedLabel)

        self.pushButton = QPushButton(FileSelectDial)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(FileSelectDial)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(FileSelectDial)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(FileSelectDial)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.buttonBox = QDialogButtonBox(FileSelectDial)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(FileSelectDial)
        self.buttonBox.accepted.connect(FileSelectDial.accept)
        self.buttonBox.rejected.connect(FileSelectDial.reject)

        QMetaObject.connectSlotsByName(FileSelectDial)
    # setupUi

    def retranslateUi(self, FileSelectDial):
        FileSelectDial.setWindowTitle(QCoreApplication.translate("FileSelectDial", u"Select File", None))
        self.label.setText(QCoreApplication.translate("FileSelectDial", u"Selected File", None))
        self.selectedLabel.setText(QCoreApplication.translate("FileSelectDial", u"No File Selected", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("FileSelectDial", u"Use this if the file you want to use is from the base game, and is not located in your content pack", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButton.setWhatsThis(QCoreApplication.translate("FileSelectDial", u"Use this if the file you want to use is from the base game, and is not located in your content pack", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton.setText(QCoreApplication.translate("FileSelectDial", u"Manual Input", None))
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("FileSelectDial", u"[Coming Soon] Use this if the file you want to use is from the base game, and is not located in your content pack", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButton_3.setWhatsThis(QCoreApplication.translate("FileSelectDial", u"[Coming Soon] Use this if the file you want to use is from the base game, and is not located in your content pack", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_3.setText(QCoreApplication.translate("FileSelectDial", u"Select File from vanilla reources", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("FileSelectDial", u"Use this if you are using a file included in your resource pack", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButton_2.setWhatsThis(QCoreApplication.translate("FileSelectDial", u"Use this if you are using a file included in your resource pack", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_2.setText(QCoreApplication.translate("FileSelectDial", u"Select File in pack directory", None))
        self.pushButton_4.setText(QCoreApplication.translate("FileSelectDial", u"Disable this track", None))
    # retranslateUi

