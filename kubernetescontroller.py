from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QDesktopServices
from ui_main import Ui_MainWindow
from login import Ui_LoginPage
import sys
import json
import os
import subprocess
import re
import warnings
import paramiko
import requests
import urllib3
import importlib.util

api_directory = os.path.join(os.path.dirname(__file__), 'Swagger', 'python-client')
sys.path.append(api_directory)

api_path = os.path.join(api_directory, 'api.py')

spec = importlib.util.spec_from_file_location("api", api_path)
api = importlib.util.module_from_spec(spec)

spec.loader.exec_module(api)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,ip_add, api_key):
        super(MainWindow, self).__init__()
        self.setupUi(self)


        #Auth
        self.ip_address = ip_add
        self.api_key = api_key

        api_instance = api.configure_api(self.api_key, self.ip_address)
        api.list_nodes(api_instance)

        #Connect Pages
        self.btn_page_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.btn_page_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_page_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.btn_page_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.btn_page_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))
        self.btn_page_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6))
        self.btn_page_7.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_7))


class LoginPage(QtWidgets.QMainWindow, Ui_LoginPage):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.setupUi(self)
        self.ip_add.setFocus()
        self.pushButton.clicked.connect(self.login)

        self.stacked_widget = None

    def set_stacked_widget(self, stacked_widget):
        self.stacked_widget = stacked_widget

    def login(self):
        ip_add = self.ip_add.text()
        username = self.username.text()
        password = self.password.text()

        if ip_add == "10.0.4.149":

            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(ip_add, username= username, password= password)

            command = f"sudo -S -p '' kubectl -n kube-system create token admin-user"  
            stdin, stdout, stderr = ssh_client.exec_command(command)
            stdin.write(password + '\n')
            stdin.flush()
            output = stdout.read().decode()

            self.hide()
            self.main_window = MainWindow(ip_add , output)
            self.main_window.showMaximized()
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Invalid Username")
            msg_box.exec_()
            return


if __name__ == "__main__":
    warnings.filterwarnings("ignore", category=urllib3.exceptions.InsecureRequestWarning)

    app = QtWidgets.QApplication(sys.argv)
    login_page = LoginPage()
    login_page.show()
    sys.exit(app.exec_())
