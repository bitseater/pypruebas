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
from PyQt6.QtWidgets import QApplication, QWidget,  QLineEdit,  QFormLayout,  QHBoxLayout

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Widget Demo')

        # create an input pane
        layout = QHBoxLayout()
        self.setLayout(layout)

        # person pane
        person_pane = QWidget(self)
        form_layout = QFormLayout()
        person_pane.setLayout(form_layout)
        form_layout.addRow('First Name:', QLineEdit(person_pane))
        form_layout.addRow('Last Name:', QLineEdit(person_pane))
        form_layout.addRow('Date of Birth:', QLineEdit(person_pane))
        form_layout.addRow('Email Address:', QLineEdit(person_pane))
        form_layout.addRow('Phone Number:', QLineEdit(person_pane))
        layout.addWidget(person_pane)

        # address pane
        address_pane = QWidget(self)
        form_layout = QFormLayout()
        address_pane.setLayout(form_layout)
        form_layout.addRow('Street:', QLineEdit(address_pane))
        form_layout.addRow('City:', QLineEdit(address_pane))
        form_layout.addRow('State/Province:', QLineEdit(address_pane))
        form_layout.addRow('Zip Code:', QLineEdit(address_pane))
        form_layout.addRow('Country:', QLineEdit(address_pane))
        layout.addWidget(address_pane)

        # show the window
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())