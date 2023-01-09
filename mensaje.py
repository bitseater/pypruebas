#!/usr/bin/env python

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from PyQt6.QtWidgets import QApplication,  QMessageBox, QWidget, QHBoxLayout,  QPushButton


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QMessageBox')
        self.setGeometry(100, 100, 300, 100)

        layout = QHBoxLayout()
        self.setLayout(layout)

        btn_question = QPushButton('Question')
        btn_question.clicked.connect(self.question)

        btn_info = QPushButton('Information')
        btn_info.clicked.connect(self.info)

        btn_warning = QPushButton('Warning')
        btn_warning.clicked.connect(self.warning)

        btn_critical = QPushButton('Critical')
        btn_critical.clicked.connect(self.critical)

        layout.addWidget(btn_question)
        layout.addWidget(btn_info)
        layout.addWidget(btn_warning)
        layout.addWidget(btn_critical)

        self.show()

    def info(self):
        QMessageBox.information(
            self,
            'Information',
            'This is important information.'
        )

    def warning(self):
        QMessageBox.warning(
            self,
            'Warning',
            'This is a warning message.'
        )

    def critical(self):
        QMessageBox.critical(
            self,
            'Critical',
            'This is a critical message.'
        )

    def question(self):
        answer = QMessageBox.question(
            self,
            'Confirmation',
            'Do you want to quit?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.Yes:
            QMessageBox.information(
                self,
                'Information',
                'You selected Yes. The program will be terminated.',
                QMessageBox.StandardButton.Ok
            )
            self.close()
        else:
            QMessageBox.information(
                self,
                'Information',
                'You selected No.',
                QMessageBox.StandardButton.Ok
            )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())