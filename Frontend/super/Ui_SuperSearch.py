# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperSearch.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SuperSearch(object):
    def setupUi(self, SuperSearch):
        SuperSearch.setObjectName("SuperSearch")
        SuperSearch.resize(511, 409)
        self.horizontalLayout = QtWidgets.QHBoxLayout(SuperSearch)
        self.horizontalLayout.setContentsMargins(-1, 35, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TitleLabel = TitleLabel(SuperSearch)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.verticalLayout_2.addWidget(self.TitleLabel)
        self.CardWidget = CardWidget(SuperSearch)
        self.CardWidget.setObjectName("CardWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.CardWidget)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.CardWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.adminSearchEdit = SearchLineEdit(self.CardWidget)
        self.adminSearchEdit.setObjectName("adminSearchEdit")
        self.horizontalLayout_2.addWidget(self.adminSearchEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.adminList = TableWidget(self.CardWidget)
        self.adminList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.adminList.setObjectName("adminList")
        self.adminList.setColumnCount(3)
        self.adminList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.adminList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminList.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.adminList)
        self.verticalLayout_2.addWidget(self.CardWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(SuperSearch)
        QtCore.QMetaObject.connectSlotsByName(SuperSearch)

    def retranslateUi(self, SuperSearch):
        _translate = QtCore.QCoreApplication.translate
        SuperSearch.setWindowTitle(_translate("SuperSearch", "管理员查询"))
        self.TitleLabel.setText(_translate("SuperSearch", "管理员查询"))
        self.label_2.setText(_translate("SuperSearch", "输入查询工号（ID）："))
        item = self.adminList.horizontalHeaderItem(0)
        item.setText(_translate("SuperSearch", "管理员工号"))
        item = self.adminList.horizontalHeaderItem(1)
        item.setText(_translate("SuperSearch", "管理员用户名"))
        item = self.adminList.horizontalHeaderItem(2)
        item.setText(_translate("SuperSearch", "管理员密码"))
from qfluentwidgets import CardWidget, SearchLineEdit, TableWidget, TitleLabel