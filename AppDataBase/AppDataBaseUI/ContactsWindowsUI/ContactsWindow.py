# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AppDataBase\AppDataBaseUI\ContactsWindowsUI\ContactsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ContactsWindow(object):
    def setupUi(self, ContactsWindow):
        ContactsWindow.setObjectName("ContactsWindow")
        ContactsWindow.resize(510, 480)
        ContactsWindow.setMinimumSize(QtCore.QSize(510, 480))
        ContactsWindow.setMaximumSize(QtCore.QSize(510, 480))
        self.ContactsFunctionsBox = QtWidgets.QGroupBox(ContactsWindow)
        self.ContactsFunctionsBox.setGeometry(QtCore.QRect(20, 20, 470, 440))
        self.ContactsFunctionsBox.setObjectName("ContactsFunctionsBox")
        self.CreateContactBox = QtWidgets.QGroupBox(self.ContactsFunctionsBox)
        self.CreateContactBox.setGeometry(QtCore.QRect(20, 20, 120, 80))
        self.CreateContactBox.setObjectName("CreateContactBox")
        self.CreateContactButton = QtWidgets.QPushButton(self.CreateContactBox)
        self.CreateContactButton.setGeometry(QtCore.QRect(10, 20, 100, 50))
        self.CreateContactButton.setObjectName("CreateContactButton")
        self.UpdateContactBox = QtWidgets.QGroupBox(self.ContactsFunctionsBox)
        self.UpdateContactBox.setGeometry(QtCore.QRect(20, 110, 120, 80))
        self.UpdateContactBox.setObjectName("UpdateContactBox")
        self.UpdateContactButton = QtWidgets.QPushButton(self.UpdateContactBox)
        self.UpdateContactButton.setGeometry(QtCore.QRect(10, 20, 100, 50))
        self.UpdateContactButton.setObjectName("UpdateContactButton")
        self.DeleteContactBox = QtWidgets.QGroupBox(self.ContactsFunctionsBox)
        self.DeleteContactBox.setGeometry(QtCore.QRect(20, 200, 120, 80))
        self.DeleteContactBox.setObjectName("DeleteContactBox")
        self.DeleteContactButton = QtWidgets.QPushButton(self.DeleteContactBox)
        self.DeleteContactButton.setGeometry(QtCore.QRect(10, 20, 100, 50))
        self.DeleteContactButton.setObjectName("DeleteContactButton")
        self.EventsBox = QtWidgets.QGroupBox(self.ContactsFunctionsBox)
        self.EventsBox.setGeometry(QtCore.QRect(150, 20, 300, 170))
        self.EventsBox.setObjectName("EventsBox")
        self.EventsTableView = QtWidgets.QTableView(self.EventsBox)
        self.EventsTableView.setGeometry(QtCore.QRect(10, 20, 280, 140))
        self.EventsTableView.setObjectName("EventsTableView")
        self.ContactsForTheEventBox = QtWidgets.QGroupBox(self.ContactsFunctionsBox)
        self.ContactsForTheEventBox.setGeometry(QtCore.QRect(150, 200, 300, 170))
        self.ContactsForTheEventBox.setObjectName("ContactsForTheEventBox")
        self.ContactsForTheEventTableView = QtWidgets.QTableView(self.ContactsForTheEventBox)
        self.ContactsForTheEventTableView.setGeometry(QtCore.QRect(10, 20, 280, 140))
        self.ContactsForTheEventTableView.setObjectName("ContactsForTheEventTableView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.ContactsFunctionsBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 380, 430, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.HorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.HorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.HorizontalLayout.setObjectName("HorizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HorizontalLayout.addItem(spacerItem)
        self.CancelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.CancelButton.setObjectName("CancelButton")
        self.HorizontalLayout.addWidget(self.CancelButton)

        self.retranslateUi(ContactsWindow)
        QtCore.QMetaObject.connectSlotsByName(ContactsWindow)

    def retranslateUi(self, ContactsWindow):
        _translate = QtCore.QCoreApplication.translate
        ContactsWindow.setWindowTitle(_translate("ContactsWindow", "Dialog"))
        self.ContactsFunctionsBox.setTitle(_translate("ContactsWindow", "Contacts Functions"))
        self.CreateContactBox.setTitle(_translate("ContactsWindow", "Create Contact"))
        self.CreateContactButton.setText(_translate("ContactsWindow", "Create Contact"))
        self.UpdateContactBox.setTitle(_translate("ContactsWindow", "Update Contact"))
        self.UpdateContactButton.setText(_translate("ContactsWindow", "Update Contact"))
        self.DeleteContactBox.setTitle(_translate("ContactsWindow", "Delete Contact"))
        self.DeleteContactButton.setText(_translate("ContactsWindow", "Delete Contact"))
        self.EventsBox.setTitle(_translate("ContactsWindow", "Events"))
        self.ContactsForTheEventBox.setTitle(_translate("ContactsWindow", "Contacts For The Event"))
        self.CancelButton.setText(_translate("ContactsWindow", "Cancel"))
