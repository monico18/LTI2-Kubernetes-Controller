from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QDesktopServices
from ui_main import Ui_MainWindow
from login import Ui_LoginPage
from pod_config import Ui_PodConfig
from container_info import Ui_ContainerInfo
from deployment_config import Ui_DeploymentConfig
from service_config import Ui_ServiceConfig
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
        self.selected_deployment = None

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
        self.container_info_page = None
        self.deployment_config_page = None
        
        #Pods
        self.podsTable.clicked.connect(self.handle_podtable_item_clicked)
        self.btn_refresh_pod_table.clicked.connect(self.refresh_table_pods)
        self.btn_add_pod.clicked.connect(self.open_pod_config_page)
        self.btn_delete_pod.clicked.connect(self.open_pod_config_page)
        self.btn_pod_container_details.clicked.connect(self.open_pod_config_page)
        
        self.btn_update_pod.setEnabled(False)
        self.btn_delete_pod.setEnabled(False)
        self.btn_pod_container_details.setEnabled(False)
        
        #Deployments
        self.deploymentTable.clicked.connect(self.handle_deploytable_item_clicked)
        self.btn_refresh_deployments_table.clicked.connect(self.refresh_table_deployments)
        self.btn_add_deployment.clicked.connect(self.open_deployment_config_page)
        self.btn_delete_deployment.clicked.connect(self.open_deployment_config_page)
        
        self.btn_update_deployment.setEnabled(False)
        self.btn_delete_deployment.setEnabled(False)

        
        self.refresh_table_node()
        self.refresh_table_namespaces()
        self.refresh_table_pods()
        self.refresh_table_deployments()
    
    def open_deployment_config_page(self):
        sender = self.sender()  
        if sender == self.btn_delete_deployment:           
            if self.selected_deployment:
                api.delete_deployment(self.ip_address, self.api_key, self.selected_deployment["name"], self.selected_deployment["namespace"])
                time.sleep(3)
                self.refresh_table_deployments()
                self.btn_update_deployment.setEnabled(False)
                self.btn_delete_deployment.setEnabled(False)
        elif sender == self.btn_add_deployment:
            self.deployment_config_page = DeploymentPage(self.api_instance, self.ip_address, self.api_key)
            self.deployment_config_page.configSaved.connect(self.handleConfigSaved)
            self.deployment_config_page.show()
    
    def open_pod_config_page(self):
        sender = self.sender()  
           
        if sender == self.btn_delete_pod:           
            print(self.selected_pod)
            api.delete_pod(self.api_instance, self.selected_pod["name"], self.selected_pod["namespace"])
            time.sleep(3)
            self.refresh_table_pods()
            self.btn_update_pod.setEnabled(False)
            self.btn_delete_pod.setEnabled(False)
        # if sender == self.btn_update_dhcp: 
        #     if self.selected_node is None:
        #         QtWidgets.QMessageBox.critical(self, "Error", "No node selected.")
        #         return
        #     if self.selected_dhcp is not None:
        #         if not self.dhcp_config_page:
        #             self.dhcp_config_page = DhcpPage(self.ip_address, self.username, self.password)
        #             self.dhcp_config_page.configSaved.connect(self.handleConfigSaved)
        #         self.dhcp_config_page.populate_dhcp_data(self.selected_dhcp)
        #         self.dhcp_config_page.show()
        if sender == self.btn_add_pod:
            self.pod_config_page = PodPage(self.api_instance)
            self.pod_config_page.configSaved.connect(self.handleConfigSaved)
            self.pod_config_page.show()
        if sender == self.btn_pod_container_details:
            self.container_info_page = ContainerInfo()
            self.container_info_page.fill_container_info(self.selected_pod)
            self.container_info_page.show()
    
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
                label = pods.get('label', '')
                num_containers = pods.get('num_containers', '')
                status = pods.get('status', '')
                pod_ip = pods.get('pod_ip', '')

                self.podsTable.insertRow(row)

                self.podsTable.setItem(row, 0, QtWidgets.QTableWidgetItem(name))
                self.podsTable.setItem(row, 1, QtWidgets.QTableWidgetItem(namespace))
                self.podsTable.setItem(row, 2, QtWidgets.QTableWidgetItem(label))
                self.podsTable.setItem(row, 3, QtWidgets.QTableWidgetItem(num_containers))
                self.podsTable.setItem(row, 4, QtWidgets.QTableWidgetItem(status))
                self.podsTable.setItem(row, 5, QtWidgets.QTableWidgetItem(pod_ip))



                for col in range(6):
                    item = self.podsTable.item(row, col)
                    if item:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)


                for col in range(6):
                    self.podsTable.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.Stretch)
        except Exception as e:
            print(f"Error populating Nodes: {e}")
   
    def refresh_table_deployments(self):
        try:
            response= api.list_deployments(self.ip_address, self.api_key)
            deploys_data = json.loads(response)
            self.deploymentTable.setRowCount(0) 
            for row ,deploy in enumerate(deploys_data["deploys"]):
                
                name=deploy.get('name', '')
                namespace = deploy.get('namespace', '')
                label = deploy.get('label', '')           
                num_replicas = deploy.get('num_replicas', '')  

                self.deploymentTable.insertRow(row)

                self.deploymentTable.setItem(row, 0, QtWidgets.QTableWidgetItem(name))
                self.deploymentTable.setItem(row, 1, QtWidgets.QTableWidgetItem(namespace))
                self.deploymentTable.setItem(row, 2, QtWidgets.QTableWidgetItem(label))
                self.deploymentTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(num_replicas)))


                for col in range(4):
                    item = self.deploymentTable.item(row, col)
                    if item:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)


                for col in range(4):
                    self.deploymentTable.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.Stretch)
        except Exception as e:
            print(f"Error populating Deployments: {e}")
            
    def handle_podtable_item_clicked(self, item):
        self.btn_update_pod.setEnabled(True)
        self.btn_delete_pod.setEnabled(True)
        self.btn_pod_container_details.setEnabled(True)
        row = item.row()
        name = self.podsTable.item(row,0).text()
        namespace = self.podsTable.item(row,1).text()
        self.selected_pod = api.list_selected_pod(self.api_instance,name,namespace)
        self.selected_pod = json.loads(self.selected_pod)
    
    def handle_deploytable_item_clicked(self, item):
        self.btn_update_deployment.setEnabled(True)
        self.btn_delete_deployment.setEnabled(True)
        row = item.row()
        name = self.deploymentTable.item(row,0).text()
        namespace = self.deploymentTable.item(row,1).text()
        self.selected_deployment = api.list_selected_deployment(self.ip_address, self.api_key, name, namespace)
        self.selected_deployment = json.loads(self.selected_deployment)
        

class DeploymentPage(QtWidgets.QMainWindow, Ui_DeploymentConfig):
    configSaved = pyqtSignal()
    def __init__(self, api_instance, ip_address, api_key):
        super(DeploymentPage, self).__init__()
        self.setupUi(self)
        self.api_instance = api_instance
        self.ip_address = ip_address
        self.api_key = api_key
        
        self.selected_pods = []
        self.labels = set()

        response = api.list_namespaces(self.api_instance)
        namespace_data = json.loads(response)
        namespace_options = []
        for row, namespaces in enumerate(namespace_data["namespaces"]):
            name = namespaces.get('name', '')
            namespace_options.append(name)

        self.namespaces.addItems(namespace_options)
        
        self.all_pods = {}
        response_pods = api.list_pods(self.api_instance)
        pods_data = json.loads(response_pods)
        for pod in pods_data.get("pods", []):
            name = pod.get('name', '')
            namespace = pod.get('namespace', '')
            if namespace not in self.all_pods:
                self.all_pods[namespace] = []
            self.all_pods[namespace].append(pod)
        
        self.update_pods_for_namespace()
        
        self.btn_apply_deploy.clicked.connect(self.save_configuration)
        self.btn_cancel_deploy.clicked.connect(self.close)
        self.btn_add_pod.clicked.connect(self.add_pod_to_table)
        self.btn_remove_pod.clicked.connect(self.remove_selected_pod)

        self.selected_pod = []
        for col in range(5):
            self.podsTable.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.Stretch)
            
        self.namespaces.currentIndexChanged.connect(self.update_pods_for_namespace)
        
        
    def update_pods_for_namespace(self):
        self.pods.clear()
        namespace = self.namespaces.currentText()
        if namespace in self.all_pods:
            for pod in self.all_pods[namespace]:
                self.pods.addItem(pod['name'], pod)
                
    def add_pod_to_table(self):
        namespace = self.namespaces.currentText()
        pod_name = self.pods.currentText()
        if not pod_name:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please select a Pod.")
            msg_box.exec_()
            return
        
        selected_pod = next((pod for pod in self.all_pods[namespace] if pod['name'] == pod_name), None)
        self.labels.add(selected_pod.get('label', {}))
        if selected_pod:
            self.selected_pods.append(selected_pod)
            row_count = self.podsTable.rowCount()
            self.podsTable.insertRow(row_count)
            self.podsTable.setItem(row_count, 0, QtWidgets.QTableWidgetItem(pod_name))
            self.podsTable.setItem(row_count, 1, QtWidgets.QTableWidgetItem(namespace))
            self.podsTable.setItem(row_count, 2, QtWidgets.QTableWidgetItem(selected_pod.get('label', ' ')))
            self.podsTable.setItem(row_count, 3, QtWidgets.QTableWidgetItem(selected_pod.get('pod_ip', 'N/A')))
            self.podsTable.setItem(row_count, 4, QtWidgets.QTableWidgetItem(selected_pod.get('status', 'Unknown')))
            self.podsTable.setItem(row_count, 5, QtWidgets.QTableWidgetItem(selected_pod.get('num_containers', '0')))
            
            for col in range(6):
                    item = self.podsTable.item(row_count, col)
                    if item:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        else:
            QtWidgets.QMessageBox.critical(self, "Error", f"Pod '{pod_name}' not found in namespace '{namespace}'.")
            
    def remove_selected_pod(self):
        selected_items = self.podsTable.selectedItems()
        if not selected_items:
            return

        for item in selected_items:
            removed_row = item.row()
            namespace = self.podsTable.item(removed_row, 1).text()
            label = self.podsTable.item(removed_row, 2).text() 
            
            print(label)
            print(self.labels)
            if label in self.labels:
                self.labels.remove(label)
            
            self.podsTable.removeRow(removed_row)

    def save_configuration(self):
        if not self.selected_pods:
            QtWidgets.QMessageBox.critical(self, "Error", "Please add at least one Pod to the table.")
            return

        name = self.line_name.text().lower()
        label = self.line_label.text().lower()
        namespace = self.namespaces.currentText()
        replicas = self.line_replicas.text()

        if not replicas.isdigit() or int(replicas) < 1:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please insert a valid number of replicas (1 or more)")
            msg_box.exec_()
            return

        containers = []
        for pod in self.selected_pods:
            pod_name = pod.get('name')
            pod_namespace = pod.get('namespace')
            pod_info_str = api.list_selected_pod(self.api_instance, pod_name, pod_namespace)
            pod_info = json.loads(pod_info_str)
            
            if pod_info:
                for container in pod_info.get('containers', []):
                    container_ports = container.get('ports', [])
                    if container_ports is None:
                        container_ports = []

                    container_info = {
                        "name": container.get('name'),
                        "image": container.get('image'),
                        "ports": [
                            {
                                "containerPort": port.get('container_port')
                            }
                            for port in container_ports
                        ]
                    }
                    containers.append(container_info)
                    
        if len(self.labels) != 1:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("All selected Pods must have the same label.")
            msg_box.exec_()
            return

        if not containers:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("The selected Pods have no containers.")
            msg_box.exec_()
            return
        
        params = {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {
                "name": name,
                "namespace": namespace,
                "labels": {
                    "app": label
                }
            },
            "spec": {
                "replicas": int(replicas),
                "selector": {
                    "matchLabels": {
                        "app": name
                    }
                },
                "template": {
                    "metadata": {
                        "labels": {
                            "app": name
                        }
                    },
                    "spec": {
                        "containers": containers
                    }
                }
            }
        }

        api.create_deployment(self.ip_address,self.api_key, namespace, params)

        self.configSaved.emit()
        self.close()

class ContainerInfo(QtWidgets.QMainWindow, Ui_ContainerInfo):
    def __init__(self):
        super(ContainerInfo,self).__init__()
        self.setupUi(self)
        self.btn_exit.clicked.connect(self.close)
        
    def fill_container_info(self, selected_pod):
        container_text = ""
        containers = selected_pod.get('containers', [])
        for container in containers:
            container_text += "Name: {}\n".format(container.get('name', ''))
            container_text += "Image: {}\n".format(container.get('image', ''))
            container_text += "Ports:\n"
            ports = container.get('ports', [])
            for port in ports:
                container_text += "  Container Port: {}\n".format(port.get('container_port', ''))
            container_text += "\n"
            container_text += "\n"  
        self.container_info.setPlainText(container_text)

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
        self.btn_add_cont.clicked.connect(self.add_container_to_table)
        self.btn_remove_cont.clicked.connect(self.remove_selected_container)
        
        for col in range(2):
                    self.containersTable.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.Stretch)
    
    def refresh_container_table(self):
        try:
            self.containersTable.setRowCount(0)
            for row, deploy in enumerate(deploys_data["deploys"]):
                name = deploy.get('name', '')
                container_port = deploy.get('container_port', '')

                self.containersTable.insertRow(row)

                self.containersTable.setItem(row, 0, QtWidgets.QTableWidgetItem(name))
                self.containersTable.setItem(row, 1, QtWidgets.QTableWidgetItem(container_port))

                for col in range(2):
                    item = self.containersTable.item(row, col)
                    if item:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)

                for col in range(2):
                    self.containersTable.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.Stretch)
        except Exception as e:
            print(f"Error populating Deployments: {e}")

    def add_container_to_table(self):
        image = self.container_images.currentText()
        container_port = self.line_container_port.text()

        if not container_port.isdigit() or not (0 <= int(container_port) <= 65535):
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please insert a valid port")
            msg_box.exec_()
            return

        row_count = self.containersTable.rowCount()
        self.containersTable.insertRow(row_count)
        self.containersTable.setItem(row_count, 0, QtWidgets.QTableWidgetItem(image))
        self.containersTable.setItem(row_count, 1, QtWidgets.QTableWidgetItem(container_port))
        
        for col in range(3):
                    item = self.podsTable.item(row_count, col)
                    if item:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)

    def remove_selected_container(self):
        selected_items = self.containersTable.selectedItems()
        if not selected_items:
            return

        for item in selected_items:
            self.containersTable.removeRow(item.row())
    
    def save_configuration(self):
        name = self.line_name.text().lower()
        label = self.line_label.text().lower()
        namespace = self.namespaces.currentText()
        containers = []
        row_count = self.containersTable.rowCount()
    
        for row in range(row_count):
            image_item = self.containersTable.item(row, 0)
            port_item = self.containersTable.item(row, 1)
            
            if image_item is None or port_item is None:
                continue
            
            image = image_item.text()
            container_port = port_item.text()
            
            if not container_port.isdigit() or not (0 <= int(container_port) <= 65535):
                msg_box = QtWidgets.QMessageBox()
                msg_box.setIcon(QtWidgets.QMessageBox.Critical)
                msg_box.setWindowTitle("Error")
                msg_box.setText(f"Please insert a valid port for row {row + 1}")
                msg_box.exec_()
                return
            
            containers.append({
                "name": image,
                "image": f"{image}:latest",
                "ports": [
                    {
                        "containerPort": int(container_port)
                    }
                ]
            })
    
        if not containers:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please add at least one container")
            msg_box.exec_()
            return
                
        params = {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "name": name,
                "namespace": namespace,
                "labels": {
                    "app": label
                }
            },
            "spec": {
                "containers": containers
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
