from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QDesktopServices
from ui_main import Ui_MainWindow
from login import Ui_LoginPage
from pod_config import Ui_PodConfig
import sys
import json
import os
import subprocess
import re
import warnings
import paramiko
import requests
import urllib3
import time
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
        self.api_instance = api.configure_api(self.api_key, self.ip_address)
        
        #Selecteds
        self.selected_pod = None

        #Connect Pages
        self.btn_page_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.btn_page_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_page_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.btn_page_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.btn_page_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))
        self.btn_page_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6))
        self.btn_page_7.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_7))

        
        #Pages
        self.pod_config_page = None
        
        #Pods
        self.podsTable.clicked.connect(self.handle_podtable_item_clicked)
        self.btn_refresh_pod_table.clicked.connect(self.refresh_table_pods)
        self.btn_add_pod.clicked.connect(self.open_pod_config_page)
        self.btn_delete_pod.clicked.connect(self.open_pod_config_page)
        
        self.btn_update_pod.setEnabled(False)
        self.btn_delete_pod.setEnabled(False)

        
        self.refresh_table_node()
        self.refresh_table_namespaces()
        self.refresh_table_pods()
    
    def open_pod_config_page(self):
        sender = self.sender()  
           
        if sender == self.btn_delete_pod:           
            print(self.selected_pod)
            api.delete_pod(self.api_instance, self.selected_pod["name"], self.selected_pod["namespace"])
            time.sleep(3)
            self.refresh_table_pods()
        # if sender == self.btn_update_dhcp: 
            # if self.selected_node is None:
                # QtWidgets.QMessageBox.critical(self, "Error", "No node selected.")
                # return
            # if self.selected_dhcp is not None:
            #     if not self.dhcp_config_page:
            #         self.dhcp_config_page = DhcpPage(self.ip_address, self.username, self.password)
            #         self.dhcp_config_page.configSaved.connect(self.handleConfigSaved)
            #     self.dhcp_config_page.populate_dhcp_data(self.selected_dhcp)
            #     self.dhcp_config_page.show()
        if sender == self.btn_add_pod:
            self.pod_config_page = PodPage(self.api_instance)
            self.pod_config_page.configSaved.connect(self.handleConfigSaved)
            self.pod_config_page.show()
    
    def handleConfigSaved(self):
        if self.pod_config_page:
            self.pod_config_page.hide()
            self.refresh_table_pods()

    def refresh_table_node(self):
        try:
            response= api.list_nodes(self.api_instance)
            nodes_data = json.loads(response)
            self.nodesTable.setRowCount(0) 
            for row ,nodes in enumerate(nodes_data["nodes"]):
                
                name=nodes.get('name', '')
                pod_cidr = nodes.get('pod_CIDR', '')           
                node_info = nodes.get('node_info', '')  

                self.nodesTable.insertRow(row)

                self.nodesTable.setItem(row, 0, QtWidgets.QTableWidgetItem(name))
                self.nodesTable.setItem(row, 1, QtWidgets.QTableWidgetItem(pod_cidr))
                self.nodesTable.setItem(row, 2, QtWidgets.QTableWidgetItem(node_info))


                for col in range(3):
                    item = self.nodesTable.item(row, col)
                    if item:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)


                for col in range(3):
                    self.nodesTable.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.Stretch)
        except Exception as e:
            print(f"Error populating Nodes: {e}")
            
    def refresh_table_namespaces(self):
        try:
            response= api.list_namespaces(self.api_instance)
            namespace_data = json.loads(response)
            self.namespaceTable.setRowCount(0) 
            for row ,namespaces in enumerate(namespace_data["namespaces"]):
                
                name=namespaces.get('name', '')
                status = namespaces.get('status', '')           

                self.namespaceTable.insertRow(row)

                self.namespaceTable.setItem(row, 0, QtWidgets.QTableWidgetItem(name))
                self.namespaceTable.setItem(row, 1, QtWidgets.QTableWidgetItem(status))


                for col in range(2):
                    item = self.namespaceTable.item(row, col)
                    if item:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)


                for col in range(2):
                    self.namespaceTable.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.Stretch)
        except Exception as e:
            print(f"Error populating Nodes: {e}")

    def refresh_table_pods(self):
        try:
            response= api.list_pods(self.api_instance)
            pods_data = json.loads(response)
            self.podsTable.setRowCount(0) 
            for row ,pods in enumerate(pods_data["pods"]):
                
                name= pods.get('name', '')
                namespace = pods.get('namespace', '')    
                num_containers = pods.get('num_containers', '')
                status = pods.get('status', '')
                pod_ip = pods.get('pod_ip', '')

                self.podsTable.insertRow(row)

                self.podsTable.setItem(row, 0, QtWidgets.QTableWidgetItem(name))
                self.podsTable.setItem(row, 1, QtWidgets.QTableWidgetItem(namespace))
                self.podsTable.setItem(row, 2, QtWidgets.QTableWidgetItem(num_containers))
                self.podsTable.setItem(row, 3, QtWidgets.QTableWidgetItem(status))
                self.podsTable.setItem(row, 4, QtWidgets.QTableWidgetItem(pod_ip))



                for col in range(5):
                    item = self.podsTable.item(row, col)
                    if item:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)


                for col in range(5):
                    self.podsTable.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.Stretch)
        except Exception as e:
            print(f"Error populating Nodes: {e}")
            
    def handle_podtable_item_clicked(self, item):
        self.btn_update_pod.setEnabled(True)
        self.btn_delete_pod.setEnabled(True)
        row = item.row()
        name = self.podsTable.item(row,0).text()
        namespace = self.podsTable.item(row,1).text()
        self.selected_pod = api.list_selected_pod(self.api_instance,name,namespace)
        self.selected_pod = json.loads(self.selected_pod)

            
class PodPage(QtWidgets.QMainWindow, Ui_PodConfig):
    configSaved = pyqtSignal()
    def __init__(self,api_instance):
        super(PodPage,self).__init__()
        self.setupUi(self)
        self.api_instance = api_instance

        response= api.list_namespaces(self.api_instance)
        namespace_data = json.loads(response)
        namespace_options = []
        for row ,namespaces in enumerate(namespace_data["namespaces"]):
            name = namespaces.get('name', '')
            namespace_options.append(name)

        self.namespaces.addItems(namespace_options)
        
        image_options = ["nginx", "httpd", "mysql", "redis", "mongo", "alpine", "busybox", "node", "python", "k8s.gcr.io/pause"]

        self.container_images.addItems(image_options)
        
        self.btn_apply.clicked.connect(self.save_configuration)
        self.btn_cancel.clicked.connect(self.close)
    
    def save_configuration(self):
        name = self.line_name.text()
        namespace = self.namespaces.currentText()
        image = self.container_images.currentText()
        container_port = self.line_container_port.text()
    
        if (int(container_port) <0 and int(container_port)>65535):
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please insert a valid port")
            msg_box.exec_()
            return
                
        params = {
                "apiVersion": "v1",
                "kind": "Pod",
                "metadata": {
                    "name": name,
                    "namespace": namespace,
                    "labels": {
                    "app": name
                    }
                },
                "spec": {
                    "containers": [
                    {
                        "name": image,
                        "image": image+":latest",
                        "ports": [
                        {
                            "containerPort": int(container_port)
                        }
                        ]
                    }
                    ]
                }
                }

        api.create_pod(self.api_instance, namespace,params)

        self.configSaved.emit()
        self.close()
        
class LoginPage(QtWidgets.QMainWindow, Ui_LoginPage):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.setupUi(self)
        self.ip_add.setFocus()
        self.pushButton.clicked.connect(self.login)

        self.stacked_widget = None
        self.ip_add.setText("10.0.4.149")
        self.username.setText("ubuntu")
        self.password.setText("ubuntu")

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
