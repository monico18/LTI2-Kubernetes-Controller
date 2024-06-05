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
               
    return api_instance

def list_nodes(api_instance):
    try:
        api_response = api_instance.list_core_v1_node().to_dict()

        filtered_response = {
            "nodes": [
                {
                    "name": node["metadata"]["name"],
                    "pod_CIDR": node["spec"]["pod_cidr"],
                    "node_info": node["status"]["node_info"]["os_image"]
                }
                for node in api_response.get("items", [])
            ]
        }

        return json.dumps(filtered_response, indent=4)
    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_node: %s\n" % e)

def list_namespaces(api_instance):
    try:
        api_response = api_instance.list_core_v1_namespace().to_dict()
        
        excluded_namespaces = {"kube-system", "kube-public", "kube-node-lease", "kubernetes-dashboard"}

        filtered_response = {
            "namespaces": [
                {
                    "name": namespace["metadata"]["name"],
                    "status": namespace["status"]["phase"],
                }
                for namespace in api_response.get("items", [])
                if namespace["metadata"]["name"] not in excluded_namespaces
            ]
        }

        return json.dumps(filtered_response, indent=4)
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
        
        excluded_namespaces = {"svclb-traefik-298db33a-gf4v8", "local-path-provisioner-6c86858495-cf6vs",
                               "coredns-6799fbcd5-bq7qm", "traefik-7d5f6474df-l69l8", 
                               "svclb-traefik-298db33a-skzkj", "dashboard-metrics-scraper-5657497c4c-7hp6p",
                               "svclb-traefik-298db33a-ngjxt", "metrics-server-54fd9b65b-55hj7",
                               "kubernetes-dashboard-78f87ddfc-v825n"}

        filtered_response = {
            "pods": [
                {
                    "name": pod["metadata"]["name"],
                    "namespace": pod['metadata']["namespace"],
                    "num_containers": str(len(pod["spec"]["containers"])),
                    "status": pod["status"]["phase"],
                    "pod_ip": pod["status"]["pod_ip"],
                }
                for pod in api_response.get("items", [])
                if pod["metadata"]["name"] not in excluded_namespaces
            ]
        }

        return json.dumps(filtered_response, indent=4)
    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_pod_for_all_namespaces: %s\n" % e)

def list_selected_pod(api_instance, name,namespace):
    try:
        api_response = api_instance.read_core_v1_namespaced_pod(name=name,namespace=namespace).to_dict()

        filtered_response = {
                    "name": api_response["metadata"]["name"],
                    "namespace": api_response['metadata']["namespace"],
                    "containers": api_response["spec"]["containers"],
                }
        
        return json.dumps(filtered_response, indent=4)
    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_pod_for_all_namespaces: %s\n" % e)       
    
def create_pod(api_instance,namespace, json_content):
    try:        
        api_instance.create_core_v1_namespaced_pod(namespace=namespace,body=json_content).to_dict()
        
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
        api_instance.delete_core_v1_namespaced_pod(name,namespace).to_dict()

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_pod_for_all_namespaces: %s\n" % e)
        
def list_deployments(ip_add, api_key):
    try:
        configuration = swagger_client.Configuration()
        configuration.host = f"https://{ip_add}:6443"
        configuration.verify_ssl = False
        configuration.api_key['authorization'] = api_key
        configuration.api_key_prefix['authorization'] = 'Bearer'

        api_instance = swagger_client.AppsV1Api(swagger_client.ApiClient(configuration))
        
        api_response = api_instance.list_apps_v1_deployment_for_all_namespaces().to_dict()
                
        excluded_deploys = {"traefik","dashboard-metrics-scraper","kubernetes-dashboard", 
                               "coredns","local-path-provisioner","metrics-server"}

        filtered_response = {
            "deploys": [
                {
                    "name": deploy["metadata"]["name"],
                    "namespace": deploy['metadata']["namespace"],
                    "num_replicas": deploy["spec"]["replicas"],
               }
                for deploy in api_response.get("items", [])
                if deploy["metadata"]["name"] not in excluded_deploys
            ]
        }

        return json.dumps(filtered_response, indent=4)

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_replication_controller_for_all_namespaces: %s\n" % e)
        
def create_deployment(ip_add, api_key, namespace, json_contents):
    try:
        configuration = swagger_client.Configuration()
        configuration.host = f"https://{ip_add}:6443"
        configuration.verify_ssl = False
        configuration.api_key['authorization'] = api_key
        configuration.api_key_prefix['authorization'] = 'Bearer'

        api_instance = swagger_client.AppsV1Api(swagger_client.ApiClient(configuration))
        
        api_response = api_instance.create_apps_v1_namespaced_deployment(namespace, json_contents).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_replication_controller_for_all_namespaces: %s\n" % e)
        
def update_deployment(ip_add, api_key, name, namespace, json_contents):
    try:
        configuration = swagger_client.Configuration()
        configuration.host = f"https://{ip_add}:6443"
        configuration.verify_ssl = False
        configuration.api_key['authorization'] = api_key
        configuration.api_key_prefix['authorization'] = 'Bearer'

        api_instance = swagger_client.AppsV1Api(swagger_client.ApiClient(configuration))
        
        api_response = api_instance.patch_apps_v1_namespaced_deployment_with_http_info(name, namespace, json_contents).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_replication_controller_for_all_namespaces: %s\n" % e)
        
def delete_deployment(ip_add, api_key, name, namespace):
    try:
        configuration = swagger_client.Configuration()
        configuration.host = f"https://{ip_add}:6443"
        configuration.verify_ssl = False
        configuration.api_key['authorization'] = api_key
        configuration.api_key_prefix['authorization'] = 'Bearer'

        api_instance = swagger_client.AppsV1Api(swagger_client.ApiClient(configuration))
        
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

def list_ingress(ip_add, api_key):
    try:
        configuration = swagger_client.Configuration()
        configuration.host = f"https://{ip_add}:6443"
        configuration.verify_ssl = False
        configuration.api_key['authorization'] = api_key
        configuration.api_key_prefix['authorization'] = 'Bearer'

        api_instance = swagger_client.NetworkingV1Api(swagger_client.ApiClient(configuration))
        
        api_response = api_instance.list_networking_v1_ingress_for_all_namespaces().to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_service_account_for_all_namespaces: %s\n" % e)
        
def create_ingress(ip_add, api_key, namespace, json_contents):
    try:
        configuration = swagger_client.Configuration()
        configuration.host = f"https://{ip_add}:6443"
        configuration.verify_ssl = False
        configuration.api_key['authorization'] = api_key
        configuration.api_key_prefix['authorization'] = 'Bearer'

        api_instance = swagger_client.NetworkingV1Api(swagger_client.ApiClient(configuration))
        
        api_response = api_instance.create_networking_v1_namespaced_ingress_with_http_info(namespace, json_contents).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_service_account_for_all_namespaces: %s\n" % e)
        
def patch_ingress(ip_add, api_key, name, namespace, json_contents):
    try:
        configuration = swagger_client.Configuration()
        configuration.host = f"https://{ip_add}:6443"
        configuration.verify_ssl = False
        configuration.api_key['authorization'] = api_key
        configuration.api_key_prefix['authorization'] = 'Bearer'

        api_instance = swagger_client.NetworkingV1Api(swagger_client.ApiClient(configuration))
        
        api_response = api_instance.patch_networking_v1_namespaced_ingress_with_http_info(name, namespace, json_contents).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_service_account_for_all_namespaces: %s\n" % e)
        
def delete_ingress(ip_add, api_key, name, namespace, json_contents):
    try:
        configuration = swagger_client.Configuration()
        configuration.host = f"https://{ip_add}:6443"
        configuration.verify_ssl = False
        configuration.api_key['authorization'] = api_key
        configuration.api_key_prefix['authorization'] = 'Bearer'

        api_instance = swagger_client.NetworkingV1Api(swagger_client.ApiClient(configuration))
        
        api_response = api_instance.delete_networking_v1_namespaced_ingress_with_http_info(name, namespace, json_contents).to_dict()
        print(json.dumps(api_response, indent=4))

    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_service_account_for_all_namespaces: %s\n" % e)