# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'SpyJacketGUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, QProcess
import subprocess
import runDiscord

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 70, 671, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        #LED Icon
        self.LedButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.LedButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/IRLED_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LedButton.setIcon(icon)
        self.LedButton.setIconSize(QtCore.QSize(78, 78))
        self.LedButton.setFlat(True)
        self.LedButton.setObjectName("LedButton")
        #self.LedButton.clicked.connect(self.clickLed)
        self.gridLayout.addWidget(self.LedButton, 1, 0, 1, 1)

        #Maps Icon
        self.MapsButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.MapsButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Icons/gougle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MapsButton.setIcon(icon1)
        self.MapsButton.setIconSize(QtCore.QSize(78, 78))
        self.MapsButton.setFlat(True)
        self.MapsButton.setObjectName("MapsButton")
        self.MapsButton.clicked.connect(self.clickMaps)
        self.gridLayout.addWidget(self.MapsButton, 1, 3, 1, 1)

        #Spotify Icon
        self.SpotifyButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SpotifyButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Icons/spotrify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SpotifyButton.setIcon(icon2)
        self.SpotifyButton.setIconSize(QtCore.QSize(78, 78))
        self.SpotifyButton.setFlat(True)
        self.SpotifyButton.setObjectName("SpotifyButton")
        #self.SpotifyButton.clicked.connect(self.clickSpotify)
        self.gridLayout.addWidget(self.SpotifyButton, 0, 1, 1, 1)

        #Doom Icon
        self.DoomButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.DoomButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Icons/doom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DoomButton.setIcon(icon3)
        self.DoomButton.setIconSize(QtCore.QSize(78, 78))
        self.DoomButton.setFlat(True)
        self.DoomButton.setObjectName("DoomButton")
        self.DoomButton.clicked.connect(self.clickDOOM)
        self.gridLayout.addWidget(self.DoomButton, 0, 3, 1, 1)

        #Raspberry Button
        self.RasButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.RasButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Icons/RasIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RasButton.setIcon(icon4)
        self.RasButton.setIconSize(QtCore.QSize(78, 78))
        self.RasButton.setFlat(True)
        self.RasButton.setObjectName("RasButton")
        self.RasButton.clicked.connect(self.clickRasp)
        self.gridLayout.addWidget(self.RasButton, 1, 2, 1, 1)

        #Discord Icon
        self.DiscordButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.DiscordButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Icons/discordy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DiscordButton.setIcon(icon5)
        self.DiscordButton.setIconSize(QtCore.QSize(78, 78))
        self.DiscordButton.setFlat(True)
        self.DiscordButton.setObjectName("DiscordButton")
        self.DiscordButton.clicked.connect(self.clickDiscord)
        self.gridLayout.addWidget(self.DiscordButton, 0, 4, 1, 1)

        #Camera Icon
        self.CamButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CamButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../Icons/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CamButton.setIcon(icon6)
        self.CamButton.setIconSize(QtCore.QSize(78, 78))
        self.CamButton.setFlat(True)
        self.CamButton.setObjectName("CamButton")
        #self.CamButton.clicked.connect(self.clickCam)
        self.gridLayout.addWidget(self.CamButton, 1, 1, 1, 1)

        #Wireshark Icon
        self.WireSharkButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.WireSharkButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../Icons/WS_PNG.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.WireSharkButton.setIcon(icon7)
        self.WireSharkButton.setIconSize(QtCore.QSize(78, 78))
        self.WireSharkButton.setFlat(True)
        self.WireSharkButton.setObjectName("WireSharkButton")
        self.WireSharkButton.clicked.connect(self.clickWireShark)
        self.gridLayout.addWidget(self.WireSharkButton, 0, 0, 1, 1)

        #VPN Icon
        self.VpnButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.VpnButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../Icons/protonvpn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VpnButton.setIcon(icon8)
        self.VpnButton.setIconSize(QtCore.QSize(78, 78))
        self.VpnButton.setFlat(True)
        self.VpnButton.setObjectName("VpnButton")
        self.VpnButton.clicked.connect(self.clickProtonVPN)
        self.gridLayout.addWidget(self.VpnButton, 0, 2, 1, 1)

        #Background
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-100, -20, 1011, 511))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Backgrounds/itl.cat_vaporwave-wallpaper_25196.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.gridLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def clickDiscord(self):
        subprocess.Popen(['/snap/bin/discord'])

    def clickWireShark(self):
        subprocess.Popen(['/usr/bin/wireshark'])

    def clickProtonVPN(self):
        subprocess.Popen(['/usr/bin/protonVPN'])

    def clickDOOM(self):
        subprocess.Popen(['/usr/games/chocolate-doom'])

    def clickMaps(self):
        os.system("google-earth-pro")

    def clickRasp(self):
        sys.exit()

    #def clickLed(self):
    #    os.system("python LED_GUI.py")

    #def clickCam(self):
    #    os.system("python Camera.py")

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())