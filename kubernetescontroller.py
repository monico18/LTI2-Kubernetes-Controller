from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, Qt ,QThread, QTimer
from PyQt5.QtGui import QDesktopServices
from ui_main import Ui_MainWindow
from login import Ui_LoginPage
from pod_config import Ui_PodConfig
from container_info import Ui_ContainerInfo
from deployment_config import Ui_DeploymentConfig
from service_config import Ui_ServiceConfig
from ingress_config import Ui_IngressConfig
from ingressRulesInfo import Ui_IngressRulesInfo
from servicePortInfo import Ui_ServicePortInfo
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
import speech_recognition as sr
import pyttsx3
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import librosa
import numpy as np
from python_speech_features import mfcc
from sklearn.svm import SVC
import joblib
import pyaudio
import wave


api_directory = os.path.join(os.path.dirname(__file__), 'Swagger', 'python-client')
sys.path.append(api_directory)

api_path = os.path.join(api_directory, 'api.py')

spec = importlib.util.spec_from_file_location("api", api_path)
api = importlib.util.module_from_spec(spec)

spec.loader.exec_module(api)

class SpeechRecognitionThread(QThread):
    recognized = pyqtSignal(str)
    error = pyqtSignal(str)

    def run(self):
        recognizer = sr.Recognizer()
        retry_count = 3 
        for attempt in range(retry_count):
            try:
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.2)
                    audio = recognizer.listen(source)
                    text = recognizer.recognize_google(audio)
                    self.recognized.emit(text.lower())
                    return
            except sr.RequestError as e:
                self.error.emit(f"Could not request results; {e}")
                return
            except sr.UnknownValueError:
                self.error.emit("Google Speech Recognition could not understand audio")
                return
            except Exception as e:
                self.error.emit(f"Attempt {attempt+1}/{retry_count} failed: {e}")
                time.sleep(2)  # Wait before retrying

        self.error.emit("All attempts to recognize speech have failed.")

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,ip_add, api_key, api_port):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        #Auth
        self.ip_address = ip_add
        self.api_key = api_key
        self.api_port = api_port
        self.api_instance = api.configure_api(self.api_key, self.ip_address, self.api_port)
        
        #Selecteds
        self.selected_pod = None
        self.selected_deployment = None
        self.selected_service = None
        self.selected_ingress = None
        self.selected_namespace = None

        #Connect Pages
        self.btn_page_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.btn_page_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_page_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.btn_page_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.btn_page_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))
        self.btn_page_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6))
        self.btn_page_7.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_7))

        #Dashboard
        self.dashboard_node_layout = QtWidgets.QHBoxLayout(self.groupBox)
        self.dashboard_pod_layout = QtWidgets.QHBoxLayout(self.groupBox_Pod)
        
        self.plot_dashboard()
        
        self.namespace_combo.currentIndexChanged.connect(self.update_pod_plots)
        
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.plot_dashboard)
        self.update_timer.start(30000)
        

        #Pages
        self.pod_config_page = None
        self.container_info_page = None
        self.deployment_config_page = None
        self.service_config_page = None
        self.service_port_info_page = None
        self.ingress_config_page = None
        self.ingress_rules_info_page = None
        
        #Namespace
        self.namespaceTable.clicked.connect(self.handle_namespacetable_item_clicked)
        self.btn_refresh_namespace_table.clicked.connect(self.refresh_table_namespaces)
        self.btn_add_namespace.clicked.connect(self.add_new_namespace)
        self.btn_delete_namespace.clicked.connect(self.rem_namespace)
        
        self.btn_delete_namespace.setEnabled(False)
        
        #Pods
        self.podsTable.clicked.connect(self.handle_podtable_item_clicked)
        self.btn_refresh_pod_table.clicked.connect(self.refresh_table_pods)
        self.btn_add_pod.clicked.connect(self.open_pod_config_page)
        self.btn_delete_pod.clicked.connect(self.open_pod_config_page)
        self.btn_pod_container_details.clicked.connect(self.open_pod_config_page)
        
        self.btn_delete_pod.setEnabled(False)
        self.btn_pod_container_details.setEnabled(False)
        
        #Deployments
        self.deploymentTable.clicked.connect(self.handle_deploytable_item_clicked)
        self.btn_refresh_deployments_table.clicked.connect(self.refresh_table_deployments)
        self.btn_add_deployment.clicked.connect(self.open_deployment_config_page)
        self.btn_delete_deployment.clicked.connect(self.open_deployment_config_page)
        
        self.btn_delete_deployment.setEnabled(False)

        #Services
        self.servicesTable.clicked.connect(self.handle_servicetable_item_clicked)
        self.btn_refresh_services_table.clicked.connect(self.refresh_table_service)
        self.btn_add_service.clicked.connect(self.open_service_config_page)
        self.btn_delete_service.clicked.connect(self.open_service_config_page)
        self.btn_service_port.clicked.connect(self.open_service_config_page)
        
        self.btn_delete_service.setEnabled(False)
        self.btn_service_port.setEnabled(False)
        
        #Ingress
        self.ingressTable.clicked.connect(self.handle_ingresstable_item_clicked)
        self.btn_refresh_ingress_table.clicked.connect(self.refresh_table_ingress)
        self.btn_add_ingress.clicked.connect(self.open_ingress_config_page)
        self.btn_delete_ingress.clicked.connect(self.open_ingress_config_page)
        self.btn_ingress_rules.clicked.connect(self.open_ingress_config_page)
        
        self.btn_delete_ingress.setEnabled(False)
        self.btn_ingress_rules.setEnabled(False)
        
        self.refresh_table_node()
        self.refresh_table_namespaces()
        self.refresh_table_pods()
        self.refresh_table_deployments()
        self.refresh_table_service()
        self.refresh_table_ingress()
        
        self.btn_hear_me.clicked.connect(self.recognize_speech)

    def recognize_speech(self):
        self.listening_dialog = QtWidgets.QMessageBox(self)
        self.listening_dialog.setWindowTitle("Listening")
        self.listening_dialog.setText("The system is now listening. Please speak.")
        self.listening_dialog.setStandardButtons(QtWidgets.QMessageBox.NoButton)
        
        self.listening_dialog.setStyleSheet("background-color: white; color: black;")
        self.listening_dialog.show()

        self.speech_thread = SpeechRecognitionThread()
        self.speech_thread.recognized.connect(self.handle_recognition_result)
        self.speech_thread.error.connect(self.handle_recognition_error)
        self.speech_thread.finished.connect(self.listening_dialog.close)
        self.speech_thread.start()

    def handle_recognition_result(self, text):
        print("Did you say: ", text)
        self.listening_dialog.setText(f"Did you say: {text}?")
        QTimer.singleShot(1000, self.listening_dialog.hide)
        self.speak_text(text)
        
        if "dashboard" in text:
            self.stackedWidget.setCurrentWidget(self.page_1)
        elif "nodes" in text:
            self.stackedWidget.setCurrentWidget(self.page_2)
        elif "namespaces" in text or "name spaces" in text:
            self.stackedWidget.setCurrentWidget(self.page_3)
        elif "pods" in text or "pause" in text:
            self.stackedWidget.setCurrentWidget(self.page_4)
        elif "create pause" in text or "create pods" in text or "create the pause" in text or "create the pods" in text:
            self.btn_add_pod.click()
        elif "deployments" in text:
            self.stackedWidget.setCurrentWidget(self.page_5)
        elif "create deployment" in text or "create the deployment" in text:
            self.btn_add_deployment.click()
        elif "services" in text:
            self.stackedWidget.setCurrentWidget(self.page_6)
        elif "create service" in text or "create the service" in text:
            self.btn_add_service.click()
        elif "ingresses" in text:
            self.stackedWidget.setCurrentWidget(self.page_7)
        elif "create ingress" in text or "create the ingress" in text:
            self.btn_add_ingress.click()
        elif "wizard" in text:
            self.stackedWidget.setCurrentWidget(self.page_8)

    def handle_recognition_error(self, error_message):
        print(error_message)
        self.listening_dialog.setText(f"Error: {error_message}")
        QTimer.singleShot(1000, self.listening_dialog.hide)

    def speak_text(self, command):
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
    
    def update_pod_plots(self):
        selected_namespace = self.namespace_combo.currentText()
        self.clear_layout(self.dashboard_pod_layout.layout())
        self.plot_pods_cpu(namespace=selected_namespace)
        self.plot_pods_mem(namespace=selected_namespace)
    
    def plot_dashboard(self):
        # Clear previous widgets
        self.clear_layout(self.dashboard_node_layout.layout())
        self.clear_layout(self.dashboard_pod_layout.layout())

        self.plot_cpu_usage()
        self.plot_memory_usage()

        self.populate_namespace_combo()
        self.plot_pods_cpu()
        self.plot_pods_mem()

    def plot_cpu_usage(self):
        node_info_str = api.nodes_info(self.ip_address, self.api_key, self.api_port)
        node_info = json.loads(node_info_str)
        names = [node["name"] for node in node_info["nodes_info"]]
        cpu_usages = []
        for node in node_info["nodes_info"]:
            cpu_usage_str = node["cpu_usage"]
            if 'n' in cpu_usage_str:
                cpu_usages.append(int(cpu_usage_str.strip('n')) / 1e9)  
            elif 'u' in cpu_usage_str:
                cpu_usages.append(int(cpu_usage_str.strip('u')) / 1e6) 

        # Set the background color
        if len(names) != len(cpu_usages):
            raise ValueError("The lengths of names and cpu_usages lists do not match.")
        
        background_color = (45 / 255, 45 / 255, 45 / 255) 
        plt.rcParams['figure.facecolor'] = background_color

        # Create CPU Usage Bar Chart
        fig_cpu, ax_cpu = plt.subplots(figsize=(5, 3))  # Smaller figure size
        ax_cpu.set_facecolor(background_color)
        sns.barplot(x=names, y=cpu_usages, ax=ax_cpu, color="lightgray")
        ax_cpu.set_title('Current CPU Usage per Node', color='white')
        ax_cpu.set_xlabel('Node', color='white')
        ax_cpu.set_ylabel('CPU Usage (Cores)', color='white')
        ax_cpu.tick_params(axis='x', colors='white')
        ax_cpu.tick_params(axis='y', colors='white')
        fig_cpu.tight_layout()

        # Create a Canvas to embed the plots
        canvas_cpu = FigureCanvas(fig_cpu)

        # Add the plot to the group box
        self.dashboard_node_layout.layout().addWidget(canvas_cpu)   

    def plot_memory_usage(self):
        node_info_str = api.nodes_info(self.ip_address, self.api_key, self.api_port)
        node_info = json.loads(node_info_str)
        names = [node["name"] for node in node_info["nodes_info"]]
        memory_usages = []

        for node in node_info["nodes_info"]:
            mem_usage_str = node["memory_usage"]
            
            if 'Ki' in mem_usage_str:
                mem_usage = int(mem_usage_str.strip('Ki')) / 1024  
            elif 'Mi' in mem_usage_str:
                mem_usage = int(mem_usage_str.strip('Mi'))  
            elif 'Bi' in mem_usage_str:
                mem_usage = int(mem_usage_str.strip('Bi')) / (1024 ** 2)  
            else:
                mem_usage = 0  
            
            memory_usages.append(mem_usage)

        # Set the background color
        background_color = (45 / 255, 45 / 255, 45 / 255)  # RGB(45, 45, 45) in normalized form
        plt.rcParams['figure.facecolor'] = background_color

        # Create Memory Usage Bar Chart
        fig_memory, ax_memory = plt.subplots(figsize=(5, 3))  # Smaller figure size
        ax_memory.set_facecolor(background_color)
        sns.barplot(x=names, y=memory_usages, ax=ax_memory, color="lightgray")
        ax_memory.set_title('Current Memory Usage per Node', color='white')
        ax_memory.set_xlabel('Node', color='white')
        ax_memory.set_ylabel('Memory Usage (Mi)', color='white')
        ax_memory.tick_params(axis='x', colors='white')
        ax_memory.tick_params(axis='y', colors='white')
        fig_memory.tight_layout()

        # Create a Canvas to embed the plots
        canvas_memory = FigureCanvas(fig_memory)

        # Add the plot to the group box
        self.dashboard_node_layout.layout().addWidget(canvas_memory)
        
    def plot_pods_cpu(self, namespace="default"):
        # Retrieve pod CPU usage information
        pods_cpu_info_str = api.pods_info(self.ip_address, self.api_key, self.api_port, namespace)
        pods_cpu_info = json.loads(pods_cpu_info_str)

        pod_names = []
        container_names = []
        cpu_usages = []

        for pod in pods_cpu_info["pods_info"]:
            pod_name = pod["name"]
            for container in pod["container_info"]:
                cpu_usage_str = container["usage"]["cpu"]
                if 'n' in cpu_usage_str:
                    cpu_usage = int(cpu_usage_str.strip('n')) / 1e9  # Convert from nanocores to cores
                elif 'u' in cpu_usage_str:
                    cpu_usage = int(cpu_usage_str.strip('u')) / 1e6  # Convert from microcores to cores
                else:
                    cpu_usage = 0
                if cpu_usage > 0:
                    pod_names.append(pod_name)
                    container_names.append(container["name"])
                    cpu_usages.append(cpu_usage)
        if len(pod_names) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("No pods found in the selected namespace.")
            msg.setWindowTitle("No Pods")
            msg.exec_()
            return
                
        if len(pod_names) != len(container_names) or len(container_names) != len(cpu_usages):
            raise ValueError("The lengths of pod_names, container_names, and cpu_usages lists do not match.")
    
        background_color = (45 / 255, 45 / 255, 45 / 255)
        
        data = pd.DataFrame({
            "Pod": pod_names,
            "Container": container_names,
            "CPU Usage (Cores)": cpu_usages
        })

        # Create the catplot for CPU usage
        g = sns.catplot(
            data=data,
            x="Pod",
            y="CPU Usage (Cores)",            
            hue="Container",
            kind="bar",
            height=3,
            aspect=3
        )
        g.fig.patch.set_facecolor(background_color)
        for ax in g.axes.flat:
            ax.set_facecolor(background_color)
        # Set plot titles and labels
        g.fig.suptitle('CPU Usage by Pod and Container', color='white')
        g.set_xlabels('Pod', color='white')
        g.set_ylabels('CPU Usage (Cores)', color='white')
        plt.xticks(color='white', rotation=0)
        plt.yticks(color='white')

        legend = plt.legend(title='Container', title_fontsize='13', fontsize='10', facecolor=background_color, edgecolor=background_color)
        plt.setp(legend.get_texts(), color='white')
        plt.setp(legend.get_title(), color='white')
        
        # Adjust plot layout
        plt.tight_layout()

        # Create a Canvas to embed the plot
        canvas = FigureCanvas(g.fig)

        # Add the plot to the pod information layout
        self.dashboard_pod_layout.layout().addWidget(canvas)

    def plot_pods_mem(self, namespace="default"):
        # Retrieve pod memory usage information
        pods_mem_info_str = api.pods_info(self.ip_address, self.api_key, self.api_port, namespace)
        pods_mem_info = json.loads(pods_mem_info_str)

        pod_names = []
        container_names = []
        memory_usages = []

        for pod in pods_mem_info["pods_info"]:
            pod_name = pod["name"]
            for container in pod["container_info"]:
                pod_names.append(pod_name)
                container_names.append(container["name"])
                mem_usage_str = container["usage"]["memory"]
                if 'Ki' in mem_usage_str:
                    mem_usage = int(mem_usage_str.strip('Ki')) / 1024  # Convert from Ki to Mi
                elif 'Mi' in mem_usage_str:
                    mem_usage = int(mem_usage_str.strip('Mi'))  # Already in Mi
                elif 'Bi' in mem_usage_str:
                    mem_usage = int(mem_usage_str.strip('Bi')) / (1024 ** 2)  # Convert from Bi to Mi
                else:
                    mem_usage = 0 
                    
        if len(pod_names) == 0:
            # Display message box if there are no pods
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("No pods found in the selected namespace.")
            msg.setWindowTitle("No Pods")
            msg.exec_()
            return

        background_color = (45 / 255, 45 / 255, 45 / 255)
        # Create a DataFrame for the data
        data = pd.DataFrame({
            "Pod": pod_names,
            "Container": container_names,
            "Memory Usage (Mi)": mem_usage
        })


        # Create the catplot for memory usage
        g = sns.catplot(
            data=data,
            x="Pod",
            y="Memory Usage (Mi)",
            hue="Container",
            kind="bar",
            height=3,
            aspect=2
            )
        
        g.fig.patch.set_facecolor(background_color)
        for ax in g.axes.flat:
            ax.set_facecolor(background_color)
            
        # Set plot titles and labels
        g.fig.suptitle('Memory Usage by Pod and Container', color='white')
        g.set_xlabels('Pod', color='white')
        g.set_ylabels('Memory Usage (Mi)', color='white')
        plt.xticks(color='white', rotation=0)
        plt.yticks(color='white')

        # Add legend
        legend = plt.legend(title='Container', title_fontsize='13', fontsize='10', facecolor=background_color, edgecolor=background_color)
        plt.setp(legend.get_texts(), color='white')
        plt.setp(legend.get_title(), color='white')
        
        # Adjust plot layout
        plt.tight_layout()

        # Create a Canvas to embed the plot
        canvas = FigureCanvas(g.fig)

        # Add the plot to the pod information layout
        self.dashboard_pod_layout.layout().addWidget(canvas)

    def populate_namespace_combo(self):
        namespaces_json_str = api.list_namespaces(self.api_instance)
        namespaces_json = json.loads(namespaces_json_str)
        namespaces = [namespace["name"] for namespace in namespaces_json["namespaces"]]
        
        self.namespace_combo.clear()
        self.namespace_combo.addItems(namespaces)

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            
    def rem_namespace(self):
        api.delete_namespace(self.api_instance, self.selected_namespace["name"])
        time.sleep(3)
        self.refresh_table_namespaces()
        self.btn_delete_namespace.setEnabled(False)
        
    def add_new_namespace(self):
        namespace_name = self.line_namespace.text().lower()
        try:

            namespace_payload = {
                "apiVersion": "v1",
                "kind": "Namespace",
                "metadata": {
                    "name": namespace_name
                },
                "spec": {
                    "finalizers": ["kubernetes"]
                }
            }

            # Call the API to create the namespace
            api.create_namespace(self.api_instance, namespace_payload)
            self.refresh_table_namespaces()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))
    
    def open_ingress_config_page(self):
        sender = self.sender()
        if sender == self.btn_delete_ingress:
            api.delete_ingress(self.ip_address, self.api_key, self.api_port, self.selected_ingress["name"], self.selected_ingress["namespace"] )
            time.sleep(3)
            self.refresh_table_ingress()
            self.btn_delete_ingress.setEnabled(False)
        if sender == self.btn_add_ingress:
            self.ingress_config_page = IngressPage(self.api_instance, self.ip_address, self.api_key, self.api_port)
            self.ingress_config_page.configSaved.connect(self.handleConfigSaved)
            self.ingress_config_page.show()
        if sender == self.ingress_rules_info_page:
            rules = self.selected_ingress.get('rules', [])
            if not rules:
                QtWidgets.QMessageBox.critical(self, "Error", "The selected ingress has no rules.")
                return
            
            self.ingress_rules_info_page = IngressRulesInfo()
            self.ingress_rules_info_page.fill_ingress_rules_info(self.selected_ingress)
            self.ingress_rules_info_page.show()
    
    def open_service_config_page(self):
        sender = self.sender()  
        if sender == self.btn_delete_service:
            api.delete_service(self.api_instance, self.selected_service["name"], self.selected_service["namespace"] )
            time.sleep(3)
            self.refresh_table_service()
            self.btn_delete_service.setEnabled(False)
        if sender == self.btn_add_service:
            self.service_config_page = ServicePage(self.api_instance, self.ip_address, self.api_key, self.api_port)
            self.service_config_page.configSaved.connect(self.handleConfigSaved)
            self.service_config_page.show()
        if sender == self.btn_service_port:
            ports = self.selected_service.get('ports', [])
            if not ports:
                QtWidgets.QMessageBox.critical(self, "Error", "The selected service has no ports.")
                return
            self.service_port_info_page = ServicePortInfo()
            self.service_port_info_page.fill_service_port_info(self.selected_service)
            self.service_port_info_page.show()
            
    def open_deployment_config_page(self):
        sender = self.sender()  
        if sender == self.btn_delete_deployment:           
            if self.selected_deployment:
                api.delete_deployment(self.ip_address, self.api_key, self.api_port, self.selected_deployment["name"], self.selected_deployment["namespace"])
                time.sleep(3)
                self.refresh_table_deployments()
                self.btn_delete_deployment.setEnabled(False)
        elif sender == self.btn_add_deployment:
            self.deployment_config_page = DeploymentPage(self.api_instance, self.ip_address, self.api_key, self.api_port)
            self.deployment_config_page.configSaved.connect(self.handleConfigSaved)
            self.deployment_config_page.show()
    
    def open_pod_config_page(self):
        sender = self.sender()  
           
        if sender == self.btn_delete_pod:           
            api.delete_pod(self.api_instance, self.selected_pod["name"], self.selected_pod["namespace"])
            time.sleep(3)
            self.refresh_table_pods()
            self.btn_delete_pod.setEnabled(False)
        if sender == self.btn_add_pod:
            self.pod_config_page = PodPage(self.api_instance)
            self.pod_config_page.configSaved.connect(self.handleConfigSaved)
            self.pod_config_page.show()
        if sender == self.btn_pod_container_details:
            containers = self.selected_pod.get('containers', [])
            ports = []
            for container in containers:
                container_ports = container.get('ports')
                if container_ports is not None:
                    ports.extend(container_ports)

            if not ports:
                QtWidgets.QMessageBox.critical(self, "Error", "The selected pod has no containers.")
                return
            self.container_info_page = ContainerInfo()
            self.container_info_page.fill_container_info(self.selected_pod)
            self.container_info_page.show()
    
    def handleConfigSaved(self):
        if self.pod_config_page:
            self.pod_config_page.hide()
            self.refresh_table_pods()
        if self.deployment_config_page:
            self.deployment_config_page.hide()
            self.refresh_table_deployments()
        if self.service_config_page:
            self.service_config_page.hide()
            self.refresh_table_service()
        if self.ingress_config_page:
            self.ingress_config_page.hide()
            self.refresh_table_ingress()

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
            response= api.list_deployments(self.ip_address, self.api_key, self.api_port)
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
            
    def refresh_table_service(self):
        try:
            response = api.list_service(self.api_instance)
            services_data = json.loads(response)
            self.servicesTable.setRowCount(0) 
            for row ,service in enumerate(services_data["services"]):
                
                name=service.get('name', '')
                namespace = service.get('namespace', '')
                label = service.get('label', '')           
                num_ports = service.get('num_ports', '') 

                self.servicesTable.insertRow(row)

                self.servicesTable.setItem(row, 0, QtWidgets.QTableWidgetItem(name))
                self.servicesTable.setItem(row, 1, QtWidgets.QTableWidgetItem(namespace))
                self.servicesTable.setItem(row, 2, QtWidgets.QTableWidgetItem(label))
                self.servicesTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(num_ports)))


                for col in range(4):
                    item = self.servicesTable.item(row, col)
                    if item:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)


                for col in range(4):
                    self.servicesTable.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.Stretch)
                    
        except Exception as e:
            print(f"Error populating Services: {e}")
            
    def refresh_table_ingress(self):
        try:
            response = api.list_ingress(self.ip_address, self.api_key, self.api_port)
            ingress_data = json.loads(response)
            self.ingressTable.setRowCount(0) 
            for row ,ingress in enumerate(ingress_data["ingresses"]):
                name=ingress.get('name', '')
                namespace = ingress.get('namespace', '')
                num_rules = ingress.get('num_rules', '') 

                self.ingressTable.insertRow(row)

                self.ingressTable.setItem(row, 0, QtWidgets.QTableWidgetItem(name))
                self.ingressTable.setItem(row, 1, QtWidgets.QTableWidgetItem(namespace))
                self.ingressTable.setItem(row, 2, QtWidgets.QTableWidgetItem(num_rules))


                for col in range(3):
                    item = self.ingressTable.item(row, col)
                    if item:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)


                for col in range(3):
                    self.ingressTable.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.Stretch)
                    
        except Exception as e:
            print(f"Error populating Services: {e}")
                
    def handle_namespacetable_item_clicked(self,item):
        self.btn_delete_namespace.setEnabled(True) 
        row = item.row()
        name = self.namespaceTable.item(row,0).text()
        self.selected_namespace = api.list_selected_namespace(self.api_instance, name)  
        self.selected_namespace = json.loads(self.selected_namespace)     
                
    def handle_podtable_item_clicked(self, item):
        self.btn_delete_pod.setEnabled(True)
        self.btn_pod_container_details.setEnabled(True)
        row = item.row()
        name = self.podsTable.item(row,0).text()
        namespace = self.podsTable.item(row,1).text()
        self.selected_pod = api.list_selected_pod(self.api_instance,name,namespace)
        self.selected_pod = json.loads(self.selected_pod)
    
    def handle_deploytable_item_clicked(self, item):
        self.btn_delete_deployment.setEnabled(True)
        row = item.row()
        name = self.deploymentTable.item(row,0).text()
        namespace = self.deploymentTable.item(row,1).text()
        self.selected_deployment = api.list_selected_deployment(self.ip_address, self.api_key, name, namespace)
        self.selected_deployment = json.loads(self.selected_deployment)
        
    def handle_servicetable_item_clicked(self, item):
        self.btn_delete_service.setEnabled(True)
        self.btn_service_port.setEnabled(True)
        row = item.row()
        name = self.servicesTable.item(row,0).text()
        namespace = self.servicesTable.item(row,1).text()
        self.selected_service = api.list_selected_service(self.api_instance, name, namespace)
        self.selected_service = json.loads(self.selected_service)
       
    def handle_ingresstable_item_clicked(self,item):
        self.btn_delete_ingress.setEnabled(True)
        self.btn_ingress_rules.setEnabled(True)
        row = item.row()
        name = self.ingressTable.item(row,0).text()
        namespace = self.ingressTable.item(row,1).text()
        self.selected_ingress = api.list_selected_ingress(self.ip_address, self.api_key, name, namespace)
        self.selected_ingress = json.loads(self.selected_ingress)     
            
class IngressRulesInfo(QtWidgets.QMainWindow, Ui_IngressRulesInfo):
    def __init__(self):
        super(IngressRulesInfo, self).__init__()
        self.setupUi(self)
        self.btn_exit.clicked.connect(self.close)

    def fill_ingress_rules_info(self, selected_ingress):
        ingress_rules_text = ""
        rules = selected_ingress.get('rules', [])
        for rule in rules:
            ingress_rules_text += "Host: {}\n".format(rule.get('host', ''))
            ingress_rules_text += "Paths:\n"
            paths = rule.get('paths', [])
            for path in paths:
                ingress_rules_text += "  Path: {}\n".format(path.get('path', ''))
                ingress_rules_text += "  Service Name: {}\n".format(path.get('service_name', ''))
                ingress_rules_text += "  Service Port: {}\n".format(path.get('service_port', ''))
            ingress_rules_text += "\n"

        self.ingress_rules_info.setPlainText(ingress_rules_text)
 
class IngressPage(QtWidgets.QMainWindow, Ui_IngressConfig):
    configSaved = pyqtSignal()
    def __init__(self, api_instance, ip_address, api_key, api_port):
        super(IngressPage, self).__init__()
        self.setupUi(self)
        self.api_instance = api_instance
        self.ip_address = ip_address
        self.api_key = api_key
        self.api_port = api_port
        
        self.rules = []

        # Populate namespaces dropdown
        response = api.list_namespaces(self.api_instance)
        namespace_data = json.loads(response)
        namespace_options = [ns.get('name', '') for ns in namespace_data["namespaces"]]
        self.namespaces.addItems(namespace_options)

        # Populate path types dropdown
        path_types = ["Prefix", "Exact", "ImplementationSpecific"]
        self.path_types.addItems(path_types)

        # Connect buttons
        self.btn_apply_ingress.clicked.connect(self.save_configuration)
        self.btn_cancel_ingress.clicked.connect(self.close)
        self.btn_add_rule.clicked.connect(self.add_rule_to_table)
        self.btn_remove_rule.clicked.connect(self.remove_selected_rule)


        for col in range(5):
            self.rulesTable.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.Stretch)

    def add_rule_to_table(self):
        host = self.line_host.text()
        path = self.line_path.text()
        path_type = self.path_types.currentText()
        service_name = self.line_service_name.text()
        port = self.line_port.text()
        
        if not host or not path or not service_name or not port:
            self.show_error("Please fill in all rule fields.")
            return
        
        if not port.isdigit():
            self.show_error("Port must be a number.")
            return
        
        row_count = self.rulesTable.rowCount()
        self.rulesTable.insertRow(row_count)
        self.rulesTable.setItem(row_count, 0, QtWidgets.QTableWidgetItem(host))
        self.rulesTable.setItem(row_count, 1, QtWidgets.QTableWidgetItem(path)) 
        self.rulesTable.setItem(row_count, 2, QtWidgets.QTableWidgetItem(path_type))
        self.rulesTable.setItem(row_count, 3, QtWidgets.QTableWidgetItem(service_name))
        self.rulesTable.setItem(row_count, 4, QtWidgets.QTableWidgetItem(port))
        
        self.rules.append({
            "host": host,
            "path": path,
            "pathType": path_type,
            "serviceName": service_name,
            "servicePort": int(port)
        })
        
        self.clear_rule_fields()

    def remove_selected_rule(self):
        selected_items = self.rulesTable.selectedItems()
        if not selected_items:
            return

        removed_row = selected_items[0].row()
        host = self.rulesTable.item(removed_row, 0).text()
        path = self.rulesTable.item(removed_row, 1).text()
        self.rules = [r for r in self.rules if r["host"] != host or r["path"] != path]
        self.rulesTable.removeRow(removed_row)

    def save_configuration(self):
        name = self.line_name.text().lower()
        namespace = self.namespaces.currentText()

        if not name or not self.rules:
            self.show_error("Please provide a name and at least one rule.")
            return

        params = {
            "apiVersion": "networking.k8s.io/v1",
            "kind": "Ingress",
            "metadata": {
                "name": name,
                "namespace": namespace
            },
            "spec": {
                "rules": [
                    {
                        "host": rule["host"],
                        "http": {
                            "paths": [
                                {
                                    "path": rule["path"],
                                    "pathType": rule["pathType"],
                                    "backend": {
                                        "service": {
                                            "name": rule["serviceName"],
                                            "port": {
                                                "number": rule["servicePort"]
                                            }
                                        }
                                    }
                                }
                            ]
                        }
                    } for rule in self.rules
                ]
            }
        }

        api.create_ingress(self.ip_address, self.api_key, self.api_port, namespace, params)
        self.configSaved.emit()
        self.close()

    def clear_rule_fields(self):
        self.line_host.clear()
        self.line_path.clear()
        self.line_service_name.clear()
        self.line_port.clear()

    def show_error(self, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec_() 

class ServicePortInfo(QtWidgets.QMainWindow, Ui_ServicePortInfo):
    def __init__(self):
        super(ServicePortInfo, self).__init__()
        self.setupUi(self)
        self.btn_exit.clicked.connect(self.close)

    def fill_service_port_info(self, selected_service):
        service_port_text = ""
        ports = selected_service.get('ports', [])
        for port in ports:
            service_port_text += "Name: {}\n".format(port.get('name', ''))
            service_port_text += "Port: {}\n".format(port.get('port', ''))
            service_port_text += "Target Port: {}\n".format(port.get('target_port', ''))
            service_port_text += "Protocol: {}\n".format(port.get('protocol', ''))
            service_port_text += "Node Port: {}\n".format(port.get('node_port', ''))
            service_port_text += "\n"

        self.service_port_info.setPlainText(service_port_text)

class ServicePage(QtWidgets.QMainWindow, Ui_ServiceConfig):
    configSaved = pyqtSignal()
    def __init__(self, api_instance, ip_address, api_key, api_port):
        super(ServicePage, self).__init__()
        self.setupUi(self)
        self.api_instance = api_instance
        self.ip_address = ip_address
        self.api_key = api_key
        self.api_port = api_port
        
        self.ports = []

        response = api.list_namespaces(self.api_instance)
        namespace_data = json.loads(response)
        namespace_options = []
        for namespaces in namespace_data["namespaces"]:
            name = namespaces.get('name', '')
            namespace_options.append(name)
            
        response_labels = api.list_deployments(self.ip_address, self.api_key, self.api_port)
        labels_data = json.loads(response_labels)
        labels_options = set()
        for labels in labels_data['deploys']:
            label = labels.get('label', '')
            labels_options.add(label)
            
        protocol_options = ["TCP","UDP","SCTP"]
        load_balancer_options = ["ClusterIP ","NodePort","LoadBalancer","ExternalName","Headless"]

        self.namespaces.addItems(namespace_options)
        self.deploy_labels.addItems(sorted(labels_options))
        self.protocol.addItems(protocol_options)
        self.load_balancer_type.addItems(load_balancer_options)
        
        self.btn_apply_service.clicked.connect(self.save_configuration)
        self.btn_cancel_service.clicked.connect(self.close)
        self.btn_add_port.clicked.connect(self.add_port_to_table)
        self.btn_remove_port.clicked.connect(self.remove_selected_port)

        for col in range(4):
            self.portsTable.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.Stretch)
            
    def add_port_to_table(self):
        port_name = self.line_port_name.text()
        port = self.line_port.text()
        protocol = self.protocol.currentText()
        target_port = self.line_target_port.text()
        
        if not port_name or not port or not target_port:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please fill in all port fields..")
            msg_box.exec_()
            return
        
        if not port.isdigit() or not target_port.isdigit():
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Port and Target Port must be numbers.")
            msg_box.exec_()
            return
        
        row_count = self.portsTable.rowCount()
        self.portsTable.insertRow(row_count)
        self.portsTable.setItem(row_count, 0, QtWidgets.QTableWidgetItem(port_name))
        self.portsTable.setItem(row_count, 1, QtWidgets.QTableWidgetItem(protocol)) 
        self.portsTable.setItem(row_count, 2, QtWidgets.QTableWidgetItem(port))
        self.portsTable.setItem(row_count, 3, QtWidgets.QTableWidgetItem(target_port))
        
        self.ports.append({
            "name": port_name,
            "port": int(port),
            "protocol": protocol,
            "targetPort": int(target_port)
        })
        
        self.line_port_name.clear()
        self.line_port.clear()
        self.line_target_port.clear()
            
    def remove_selected_port(self):
        selected_items = self.portsTable.selectedItems()
        if not selected_items:
            return

        for item in selected_items:
            removed_row = item.row()
            port_name = self.portsTable.item(removed_row, 0).text()
            self.ports = [p for p in self.ports if p["name"] != port_name]
            self.portsTable.removeRow(removed_row)

    def save_configuration(self):
        name = self.line_name.text().lower()
        label = self.line_label.text().lower()
        namespace = self.namespaces.currentText()
        deploy_label = self.deploy_labels.currentText()
        load_balancer = self.load_balancer_type.currentText()

        if not name or not label:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please fill in all required fields.")
            msg_box.exec_()
            return

        if not self.ports:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please add at least one port.")
            msg_box.exec_()
            return

        params = {
            "apiVersion": "v1",
            "kind": "Service",
            "metadata": {
                "name": name,
                "namespace": namespace,
                "labels": {
                    "app": label
                }
            },
            "spec": {
                "selector": {
                    "app": deploy_label
                },
                "ports": self.ports,
                "type": load_balancer
            }
        }

        api.create_service(self.api_instance, namespace, params)

        self.configSaved.emit()
        self.close()

class DeploymentPage(QtWidgets.QMainWindow, Ui_DeploymentConfig):
    configSaved = pyqtSignal()
    def __init__(self, api_instance, ip_address, api_key, api_port):
        super(DeploymentPage, self).__init__()
        self.setupUi(self)
        self.api_instance = api_instance
        self.ip_address = ip_address
        self.api_key = api_key
        self.api_port = api_port
        
        response = api.list_namespaces(self.api_instance)
        namespace_data = json.loads(response)
        namespace_options = []
        for row, namespaces in enumerate(namespace_data["namespaces"]):
            name = namespaces.get('name', '')
            namespace_options.append(name)

        self.namespaces.addItems(namespace_options)
        
        self.all_pods = {}
        image_options = ["nginx", "httpd", "mysql", "redis", "mongo", "alpine", "busybox", "node", "python", "k8s.gcr.io/pause"]
        self.container_images.addItems(image_options)
                
        self.btn_apply_deploy.clicked.connect(self.save_configuration)
        self.btn_cancel_deploy.clicked.connect(self.close)
        self.btn_add_cont.clicked.connect(self.add_container_to_table)
        self.btn_remove_cont.clicked.connect(self.remove_selected_container)

        self.selected_pod = []
        for col in range(2):
            self.containersTable.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.Stretch)
                    
        
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
        
        for col in range(2):
            item = self.containersTable.item(row_count, col)
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
        replicas = self.line_replicas.text()

        if not replicas.isdigit() or int(replicas) < 1:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please insert a valid number of replicas (1 or more)")
            msg_box.exec_()
            return

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

        api.create_deployment(self.ip_address,self.api_key, self.api_port, namespace, params)

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
        self.selected_pod = None
        self.name = None
        self.namespace = None

        response= api.list_namespaces(self.api_instance)
        namespace_data = json.loads(response)
        namespace_options = []
        for row ,namespaces in enumerate(namespace_data["namespaces"]):
            name = namespaces.get('name', '')
            namespace_options.append(name)

        self.namespaces.addItems(namespace_options)
        
        image_options = ["nginx", "httpd", "mysql", "redis", "mongo", "alpine", "node", "python"]

        self.container_images.addItems(image_options)
        
        self.btn_apply.clicked.connect(self.save_configuration)
        self.btn_cancel.clicked.connect(self.close)
        self.btn_add_cont.clicked.connect(self.add_container_to_table)
        self.btn_remove_cont.clicked.connect(self.remove_selected_container)
        
        for col in range(2):
                    self.containersTable.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.Stretch)
    
    def populate_pod_data(self, selected_pod):
        self.selected_pod = selected_pod
        namespace_index = self.namespaces.findText(selected_pod["namespace"])
        if namespace_index != -1:
            self.namespace = selected_pod["namespace"]
            self.namespaces.setCurrentIndex(namespace_index)
            self.namespaces.setEnabled(False)

        self.line_name.setText(selected_pod["name"])
        self.line_name.setEnabled(False)
        self.name = selected_pod["name"]
        
        label = selected_pod["label"]
        self.line_label.setText(label)
        self.line_label.setEnabled(False)

        self.containersTable.setRowCount(0) 
        for container in selected_pod["containers"]:
            row_count = self.containersTable.rowCount()
            self.containersTable.insertRow(row_count)

            image_name = container["name"]
            container_port = str(container["ports"][0]["container_port"])

            self.containersTable.setItem(row_count, 0, QtWidgets.QTableWidgetItem(image_name))
            self.containersTable.setItem(row_count, 1, QtWidgets.QTableWidgetItem(container_port))

            for col in range(2):
                item = self.containersTable.item(row_count, col)
                if item:
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)   

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
                    item = self.containersTable.item(row_count, col)
                    if item:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)

    def remove_selected_container(self):
        selected_items = self.containersTable.selectedItems()
        if not selected_items:
            return

        for item in selected_items:
            self.containersTable.removeRow(item.row())
    
    def construct_patch_operation(self, containers):
        patch_operation = [
            {
                "op": "replace",
                "path": "/spec/containers",
                "value": containers
            }
        ]
        return patch_operation
    
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

        if self.selected_pod != None:
            patch_operation = self.construct_patch_operation(containers)
            print(patch_operation)
            api.update_pod(self.api_instance, self.name, self.namespace, patch_operation)
        else:
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
        self.ssh_port.setText("22")
        self.api_port.setText("6443")

    def set_stacked_widget(self, stacked_widget):
        self.stacked_widget = stacked_widget

    def login(self):
        ip_add = self.ip_add.text()
        username = self.username.text()
        password = self.password.text()
        ssh_port = self.ssh_port.text()
        api_port = self.api_port.text()
        
        if self.ip_add.text() == "10.0.4.149":
            # self.authenticate_voice()

            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(ip_add, username=username, password=password, port=ssh_port)

            command = f"sudo -S -p '' kubectl -n kube-system create token admin-user"
            stdin, stdout, stderr = ssh_client.exec_command(command)
            stdin.write(password + '\n')
            stdin.flush()
            output = stdout.read().decode()

            self.hide()
            self.main_window = MainWindow(ip_add, output, api_port)
            self.main_window.showMaximized()
        # else:
        #     msg_box = QtWidgets.QMessageBox()
        #     msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        #     msg_box.setWindowTitle("Authentication Error")
        #     msg_box.setText("Voice authentication failed. Please try again.")
        #     msg_box.exec_()
        #     return
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Invalid Username")
            msg_box.exec_()
            return

    # def authenticate_voice(self):
    #     model = joblib.load('voice_auth_model.pkl')

    #     sample_rate = 16000
    #     duration = 3  
    #     audio_data = self.record_audio(sample_rate, duration)

    #     mfcc_features = mfcc(audio_data, sample_rate)

    #     flattened_features = mfcc_features.flatten()

    #     expected_features = 2600  
    #     if len(flattened_features) < expected_features:
    #         pad_width = expected_features - len(flattened_features)
    #         flattened_features = np.pad(flattened_features, (0, pad_width), mode='constant')
    #     else:
    #         flattened_features = flattened_features[:expected_features]

    #     features = flattened_features.reshape(1, -1)

    #     prediction_proba = model.predict_proba(features)
    #     probability_of_authorized = prediction_proba[0][1]  

    #     print(prediction_proba)
    #     print(probability_of_authorized)

    #     threshold = 0.75

        
    #     if probability_of_authorized >= threshold:
    #         self.handle_voice_auth_result(True)
    #     else:
    #         self.handle_voice_auth_result(False)

    # def record_audio(self, sample_rate, duration):
    #     chunk_size = 1024
    #     audio_format = pyaudio.paFloat32
    #     channels = 1

    #     audio = pyaudio.PyAudio()
    #     stream = audio.open(format=audio_format, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk_size)

    #     frames = []
    #     for _ in range(0, int(sample_rate / chunk_size * duration)):
    #         data = stream.read(chunk_size)
    #         frames.append(np.frombuffer(data, dtype=np.float32))

    #     stream.stop_stream()
    #     stream.close()
    #     audio.terminate()

    #     audio_data = np.hstack(frames)
    #     return audio_data
        
    # def handle_voice_auth_result(self, authenticated):
    #     if authenticated:
    #         ip_add = self.ip_add.text()
    #         username = self.username.text()
    #         password = self.password.text()
    #         ssh_port = self.ssh_port.text()
    #         api_port = self.api_port.text()

    #         ssh_client = paramiko.SSHClient()
    #         ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #         ssh_client.connect(ip_add, username=username, password=password, port=ssh_port)

    #         command = f"sudo -S -p '' kubectl -n kube-system create token admin-user"
    #         stdin, stdout, stderr = ssh_client.exec_command(command)
    #         stdin.write(password + '\n')
    #         stdin.flush()
    #         output = stdout.read().decode()

    #         self.hide()
    #         self.main_window = MainWindow(ip_add, output, api_port)
    #         self.main_window.showMaximized()
    #     else:
    #         msg_box = QtWidgets.QMessageBox()
    #         msg_box.setIcon(QtWidgets.QMessageBox.Critical)
    #         msg_box.setWindowTitle("Authentication Error")
    #         msg_box.setText("Voice authentication failed. Please try again.")
    #         msg_box.exec_()
    #         return

if __name__ == "__main__":
    warnings.filterwarnings("ignore", category=urllib3.exceptions.InsecureRequestWarning)

    app = QtWidgets.QApplication(sys.argv)
    login_page = LoginPage()
    login_page.show()
    sys.exit(app.exec_())
