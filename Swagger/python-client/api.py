from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import json

def configure_api(api_key,ip_add):
    configuration = swagger_client.Configuration()
    configuration.host = f"https://{ip_add}:6443"
    configuration.verify_ssl = False
    configuration.api_key['authorization'] = api_key
    configuration.api_key_prefix['authorization'] = 'Bearer'

    api_instance = swagger_client.CoreV1Api(swagger_client.ApiClient(configuration))
    api_instance.list_networking_v1_ingress_for_all_namespaces_with_http_info
    
    api_instance.list_networking_v1_ingress_for_all_namespaces_with_http_info
        
    return api_instance

def list_nodes(api_instance):
    try:
        api_response = api_instance.list_core_v1_node().to_dict()

        filtered_response = {
            "nodes": [
                {
                    "name": node["metadata"]["name"],
                    "addresses": node["status"]["addresses"],
                    "allocatable": node["status"]["allocatable"],
                    "conditions": node["status"]["conditions"],
                    "images": node["status"]["images"],
                    "node_info": node["status"]["node_info"]
                }
                for node in api_response.get("items", [])
            ]
        }

        print(json.dumps(filtered_response, indent=4))

        return json.dumps(api_response, indent=4)
    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_node: %s\n" % e)

def list_namespaces(api_instance):
    try:
        api_response = api_instance.list_core_v1_namespace().to_dict()
        
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_namespace: %s\n" % e)

def create_namespace(api_instance,json_content):
    try:
        #SE DER ERRO NO json_content, ver se o erro não é no create_core, pois lá nunca é "chamado" o body
        #Em principio não é preciso que isto funciona como IS
        api_response = api_instance.create_core_v1_namespace(json_content).to_dict()
        
        print(json.dumps(api_response, indent=4))

    except ApiException as e :
        print("Exception when calling CoreV1Api->list_core_v1_namespace: %s\n" % e)

def update_namespace(api_instance,name,json_content):
    try:
        api_response = api_instance.patch_core_v1_namespace(name,json_content).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e :
        print("Exception when calling CoreV1Api->list_core_v1_namespace: %s\n" % e)

def delete_namespace(api_instance,name):
    try:
        api_response = api_instance.delete_core_v1_namespace(name).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e :
        print("Exception when calling CoreV1Api->list_core_v1_namespace: %s\n" % e)

def list_pods(api_instance):
    try:
        api_response = api_instance.list_core_v1_pod_for_all_namespaces().to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_pod_for_all_namespaces: %s\n" % e)

def create_pod(api_instance,namespace, json_content):
    try:
        api_response = api_instance.create_core_v1_namespaced_pod(namespace,json_content).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_pod_for_all_namespaces: %s\n" % e)
        
def update_pod(api_instance,name ,namespace, json_content):
    try:
        api_response = api_instance.patch_core_v1_namespaced_pod(name,namespace,json_content).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_pod_for_all_namespaces: %s\n" % e)
        
def delete_pod(api_instance,name ,namespace):
    try:
        api_response = api_instance.delete_core_v1_namespaced_pod(name,namespace).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_pod_for_all_namespaces: %s\n" % e)
        
def list_deployments(api_instance, namespace):
    try:
        api_response = api_instance.list_apps_v1_namespaced_deployment_with_http_info(namespace).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_replication_controller_for_all_namespaces: %s\n" % e)
        
def create_deployment(api_instance, namespace, json_contents):
    try:
        api_response = api_instance.create_apps_v1_namespaced_deployment_with_http_info(namespace, json_contents).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_replication_controller_for_all_namespaces: %s\n" % e)
        
def update_deployment(api_instance, name, namespace, json_contents):
    try:
        api_response = api_instance.patch_apps_v1_namespaced_deployment_with_http_info(name, namespace, json_contents).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_replication_controller_for_all_namespaces: %s\n" % e)
        
def delete_deployment(api_instance, name, namespace):
    try:
        api_response = api_instance.delete_apps_v1_namespaced_deployment_with_http_info(name, namespace).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_replication_controller_for_all_namespaces: %s\n" % e)        

def list_service(api_instance):
    try:
        api_response = api_instance.list_core_v1_service_account_for_all_namespaces().to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_service_account_for_all_namespaces: %s\n" % e)
        
def create_service(api_instance, namespace, json_content):
    try:
        api_response = api_instance.create_core_v1_namespaced_service(namespace, json_content).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_service_account_for_all_namespaces: %s\n" % e)

def patch_service(api_instance, name, namespace, json_content):
    try:
        api_response = api_instance.patch_core_v1_namespaced_service(name, namespace, json_content).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_service_account_for_all_namespaces: %s\n" % e)
        
def delete_service(api_instance, name, namespace, json_content):
    try:
        api_response = api_instance.delete_core_v1_namespaced_service(name, namespace, json_content).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_service_account_for_all_namespaces: %s\n" % e)

def list_ingress(api_instance):
    try:
        api_response = api_instance.list_networking_v1_ingress_for_all_namespaces_with_http_info().to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_service_account_for_all_namespaces: %s\n" % e)
        
def create_ingress(api_instance, namespace, json_contents):
    try:
        api_response = api_instance.create_networking_v1_namespaced_ingress_with_http_info(namespace, json_contents).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_service_account_for_all_namespaces: %s\n" % e)
        
def patch_ingress(api_instance, name, namespace, json_contents):
    try:
        api_response = api_instance.patch_networking_v1_namespaced_ingress_with_http_info(name, namespace, json_contents).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_service_account_for_all_namespaces: %s\n" % e)
        
def delete_ingress(api_instance, name, namespace, json_contents):
    try:
        api_response = api_instance.delete_networking_v1_namespaced_ingress_with_http_info(name, namespace, json_contents).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_service_account_for_all_namespaces: %s\n" % e)