# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AppDataBase\AppDataBaseUI\TasksWindowsUI\TasksUpdateWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TasksUpdateWindow(object):
    def setupUi(self, TasksUpdateWindow):
        TasksUpdateWindow.setObjectName("TasksUpdateWindow")
        TasksUpdateWindow.resize(880, 510)
        TasksUpdateWindow.setMinimumSize(QtCore.QSize(880, 510))
        TasksUpdateWindow.setMaximumSize(QtCore.QSize(880, 510))
        self.UpdateTaskGroupBox = QtWidgets.QGroupBox(TasksUpdateWindow)
        self.UpdateTaskGroupBox.setGeometry(QtCore.QRect(20, 10, 840, 480))
        self.UpdateTaskGroupBox.setObjectName("UpdateTaskGroupBox")
        self.TaskName = QtWidgets.QGroupBox(self.UpdateTaskGroupBox)
        self.TaskName.setGeometry(QtCore.QRect(20, 20, 120, 110))
        self.TaskName.setObjectName("TaskName")
        self.TaskNamePlainTextEdit = QtWidgets.QPlainTextEdit(self.TaskName)
        self.TaskNamePlainTextEdit.setGeometry(QtCore.QRect(10, 20, 100, 80))
        self.TaskNamePlainTextEdit.setObjectName("TaskNamePlainTextEdit")
        self.DescriptionGroupBox = QtWidgets.QGroupBox(self.UpdateTaskGroupBox)
        self.DescriptionGroupBox.setGeometry(QtCore.QRect(280, 20, 240, 170))
        self.DescriptionGroupBox.setObjectName("DescriptionGroupBox")
        self.DescriptionPlainTextEdit = QtWidgets.QPlainTextEdit(self.DescriptionGroupBox)
        self.DescriptionPlainTextEdit.setGeometry(QtCore.QRect(10, 20, 220, 140))
        self.DescriptionPlainTextEdit.setObjectName("DescriptionPlainTextEdit")
        self.DueDateGroupBox = QtWidgets.QGroupBox(self.UpdateTaskGroupBox)
        self.DueDateGroupBox.setGeometry(QtCore.QRect(150, 80, 120, 50))
        self.DueDateGroupBox.setObjectName("DueDateGroupBox")
        self.DueDateDateEdit = QtWidgets.QDateEdit(self.DueDateGroupBox)
        self.DueDateDateEdit.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.DueDateDateEdit.setObjectName("DueDateDateEdit")
        self.PriorityGroupBox = QtWidgets.QGroupBox(self.UpdateTaskGroupBox)
        self.PriorityGroupBox.setGeometry(QtCore.QRect(20, 140, 250, 50))
        self.PriorityGroupBox.setObjectName("PriorityGroupBox")
        self.PriorityComboBox = QtWidgets.QComboBox(self.PriorityGroupBox)
        self.PriorityComboBox.setGeometry(QtCore.QRect(10, 20, 230, 20))
        self.PriorityComboBox.setObjectName("PriorityComboBox")
        self.PriorityComboBox.addItem("")
        self.PriorityComboBox.addItem("")
        self.PriorityComboBox.addItem("")
        self.PriorityComboBox.addItem("")
        self.StatusGroupBox = QtWidgets.QGroupBox(self.UpdateTaskGroupBox)
        self.StatusGroupBox.setGeometry(QtCore.QRect(150, 20, 120, 50))
        self.StatusGroupBox.setObjectName("StatusGroupBox")
        self.StatusComboBox = QtWidgets.QComboBox(self.StatusGroupBox)
        self.StatusComboBox.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.StatusComboBox.setObjectName("StatusComboBox")
        self.StatusComboBox.addItem("")
        self.StatusComboBox.addItem("")
        self.StatusComboBox.addItem("")
        self.EventsGroupBox = QtWidgets.QGroupBox(self.UpdateTaskGroupBox)
        self.EventsGroupBox.setGeometry(QtCore.QRect(20, 200, 500, 210))
        self.EventsGroupBox.setObjectName("EventsGroupBox")
        self.EventsTableView = QtWidgets.QTableView(self.EventsGroupBox)
        self.EventsTableView.setGeometry(QtCore.QRect(10, 20, 480, 180))
        self.EventsTableView.setObjectName("EventsTableView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.UpdateTaskGroupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 420, 800, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.HorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.HorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.HorizontalLayout.setObjectName("HorizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HorizontalLayout.addItem(spacerItem)
        self.UpdateTaskButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.UpdateTaskButton.setObjectName("UpdateTaskButton")
        self.HorizontalLayout.addWidget(self.UpdateTaskButton)
        self.CancelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.CancelButton.setObjectName("CancelButton")
        self.HorizontalLayout.addWidget(self.CancelButton)
        self.TasksForTheEventGroupBox = QtWidgets.QGroupBox(self.UpdateTaskGroupBox)
        self.TasksForTheEventGroupBox.setGeometry(QtCore.QRect(530, 20, 290, 390))
        self.TasksForTheEventGroupBox.setObjectName("TasksForTheEventGroupBox")
        self.TasksForTheEventTableView = QtWidgets.QTableView(self.TasksForTheEventGroupBox)
        self.TasksForTheEventTableView.setGeometry(QtCore.QRect(10, 20, 270, 360))
        self.TasksForTheEventTableView.setObjectName("TasksForTheEventTableView")

        self.retranslateUi(TasksUpdateWindow)
        QtCore.QMetaObject.connectSlotsByName(TasksUpdateWindow)

    def retranslateUi(self, TasksUpdateWindow):
        _translate = QtCore.QCoreApplication.translate
        TasksUpdateWindow.setWindowTitle(_translate("TasksUpdateWindow", "Dialog"))
        self.UpdateTaskGroupBox.setTitle(_translate("TasksUpdateWindow", "Update Task"))
        self.TaskName.setTitle(_translate("TasksUpdateWindow", "Task Name"))
        self.DescriptionGroupBox.setTitle(_translate("TasksUpdateWindow", "Description"))
        self.DueDateGroupBox.setTitle(_translate("TasksUpdateWindow", "Due Date"))
        self.PriorityGroupBox.setTitle(_translate("TasksUpdateWindow", "Priority"))
        self.PriorityComboBox.setItemText(0, _translate("TasksUpdateWindow", "Urgent and important"))
        self.PriorityComboBox.setItemText(1, _translate("TasksUpdateWindow", "Not urgent, but important"))
        self.PriorityComboBox.setItemText(2, _translate("TasksUpdateWindow", "Urgent, but not important"))
        self.PriorityComboBox.setItemText(3, _translate("TasksUpdateWindow", "Not urgent and not important"))
        self.StatusGroupBox.setTitle(_translate("TasksUpdateWindow", "Status"))
        self.StatusComboBox.setItemText(0, _translate("TasksUpdateWindow", "Done"))
        self.StatusComboBox.setItemText(1, _translate("TasksUpdateWindow", "In process"))
        self.StatusComboBox.setItemText(2, _translate("TasksUpdateWindow", "Waiting"))
        self.EventsGroupBox.setTitle(_translate("TasksUpdateWindow", "Events"))
        self.UpdateTaskButton.setText(_translate("TasksUpdateWindow", "Update Task"))
        self.CancelButton.setText(_translate("TasksUpdateWindow", "Cancel"))
        self.TasksForTheEventGroupBox.setTitle(_translate("TasksUpdateWindow", "Tasks For The Event "))
