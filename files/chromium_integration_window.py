# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QSize, QPoint
from browser_integration import browserIntegration
import platform
import os
from newopen import Open
from functools import partial
import osCommands
import sys


os_type = platform.system()

home_address = str(os.path.expanduser("~"))


class ChromiumIntegrationWindow(QWidget):
    def __init__(self, persepolis_setting):
        super().__init__()

        self.persepolis_setting = persepolis_setting
        icons = ':/' + \
            str(self.persepolis_setting.value('settings/icons')) + '/'
        self.setWindowIcon(QIcon.fromTheme('persepolis', QIcon(':/icon.svg')))
        self.setWindowTitle('Browser integration')

        window_verticalLayout = QVBoxLayout(self)

        # labels
        self.label1 = QLabel()

        self.label2 = QLabel()

        self.site_label = QLabel(self)
        self.site_label.setTextFormat(QtCore.Qt.RichText)
        self.site_label.setAlignment(QtCore.Qt.AlignCenter)
        self.site_label.setOpenExternalLinks(True)
        self.site_label.setTextInteractionFlags(
            QtCore.Qt.TextBrowserInteraction)

        self.label3 = QLabel()

        self.label4 = QLabel()

        self.label5 = QLabel()

        for i in self.label1, self.label2, self.site_label, self.label3,  self.label4, self.label5:
            window_verticalLayout.addWidget(i)

    # chromium
        chromium_verticalLayout = QVBoxLayout()

        self.chromium_pushButton = QPushButton()
        self.chromium_pushButton.clicked.connect(
            partial(self.chromiumPressed, 'chromium'))
        self.chromium_label = QLabel()

        chromium_verticalLayout.addWidget(self.chromium_pushButton)
        chromium_verticalLayout.addWidget(self.chromium_label)

    # chrome

        self.chrome_pushButton = QPushButton()
        self.chrome_pushButton.clicked.connect(
            partial(self.chromiumPressed, 'chrome'))

        self.chrome_label = QLabel()

        chromium_verticalLayout.addWidget(self.chrome_pushButton)
        chromium_verticalLayout.addWidget(self.chrome_label)

    # Firefox
        firefox_verticalLayout = QVBoxLayout()

        self.firefox_pushButton = QPushButton()
        self.firefox_pushButton.clicked.connect(
            partial(self.chromiumPressed, 'firefox'))

        self.firefox_label = QLabel()
        firefox_verticalLayout.addWidget(self.firefox_pushButton)
        firefox_verticalLayout.addWidget(self.firefox_label)


    # opera
        opera_verticalLayout = QVBoxLayout()

        self.opera_pushButton = QPushButton()
        self.opera_pushButton.clicked.connect(
            partial(self.chromiumPressed, 'opera'))

        self.opera_label = QLabel()

        opera_verticalLayout.addWidget(self.opera_pushButton)
        opera_verticalLayout.addWidget(self.opera_label)

    # vivaldi

        self.vivaldi_pushButton = QPushButton()
        self.vivaldi_pushButton.clicked.connect(
            partial(self.chromiumPressed, 'vivaldi'))

        self.vivaldi_label = QLabel()

        opera_verticalLayout.addWidget(self.vivaldi_pushButton)
        opera_verticalLayout.addWidget(self.vivaldi_label)



        


    # chromium_chrome_horizontalLayout
        chromium_chrome_horizontalLayout = QHBoxLayout()

        chromium_chrome_horizontalLayout.addLayout(chromium_verticalLayout)
        chromium_chrome_horizontalLayout.addLayout(firefox_verticalLayout)
        chromium_chrome_horizontalLayout.addLayout(opera_verticalLayout)

        window_verticalLayout.addLayout(chromium_chrome_horizontalLayout)

    # ok button
        self.ok_pushButton = QPushButton()
        self.ok_pushButton.setIcon(QIcon(icons + 'ok'))

        ok_horizontalLayout = QHBoxLayout()

        ok_horizontalLayout.addStretch(1)
        ok_horizontalLayout.addWidget(self.ok_pushButton)

        self.ok_pushButton.clicked.connect(self.close)

        window_verticalLayout.addLayout(ok_horizontalLayout)


# lables text

        self.label1.setText(
            'Browser integration can help you download very easy!\nJust click on download link in your browser\nand then download starts in Persepolis!\nPersepolis can integrate into Firefox and chromium and chrome')
        self.label2.setText(
            'For Firefox please visit our site and read guides:\n')
        self.site_label.setText(
            "<a href=https://persepolisdm.github.io>https://persepolisdm.github.io</a>")
        self.label3.setText('\nFor Chrome/Chromium :')
        self.label4.setText(
            '\t1. First make sure that Chrome or Chromium is installed')
        self.label5.setText('\t2. Then press appropriate button here:\n')

        self.chrome_pushButton.setText('Chrome')
        self.chromium_pushButton.setText('Chromium')
        self.firefox_pushButton.setText('Firefox')
        self.opera_pushButton.setText('Opera')
        self.vivaldi_pushButton.setText('Vivaldi')

        self.ok_pushButton.setText('OK')

        # window size and position
        size = self.persepolis_setting.value(
            'ChromiumIntegrationWindow/size', QSize(363, 300))
        position = self.persepolis_setting.value(
            'ChromiumIntegrationWindow/position', QPoint(400, 300))

        self.resize(size)
        self.move(position)

    def chromiumPressed(self, browser):

        browserIntegration(browser)

        if browser == 'chromium':
            self.chromium_label.setText('Done!')
        elif browser == 'chrome':
            self.chrome_label.setText('Done!')
        elif browser == 'firefox':
            self.firefox_label.setText('Done!')
        elif browser == 'opera':
            self.opera_label.setText('Done!')
        elif browser == 'vivaldi':
            self.vivaldi_label.setText('Done!')



    def changeIcon(self, icons):
        icons = ':/' + str(icons) + '/'
        self.ok_pushButton.setIcon(QIcon(icons + 'ok'))

    def closeEvent(self, event):
        # saving window size and position
        self.persepolis_setting.setValue(
            'ChromiumIntegrationWindow/size', self.size())
        self.persepolis_setting.setValue(
            'ChromiumIntegrationWindow/position', self.pos())
        self.persepolis_setting.sync()
        self.destroy()
