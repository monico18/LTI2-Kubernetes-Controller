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
        return json.dumps(api_response)
    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_node: %s\n" % e)

def list_namespaces(api_instance):
    try:
        api_response = api_instance.list_core_v1_namespace().to_dict()
        with open('namespaces.json', 'w') as f:
            json.dump(api_response, f, indent=4)
    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_namespace: %s\n" % e)

def list_pods(api_instance):
    try:
        api_response = api_instance.list_core_v1_pod_for_all_namespaces().to_dict()
        with open('pods.json', 'w') as f:
            json.dump(api_response, f, indent=4)
    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_pod_for_all_namespaces: %s\n" % e)

def list_replication_controllers(api_instance):
    try:
        api_response = api_instance.list_core_v1_replication_controller_for_all_namespaces().to_dict()
        with open('replication_controllers.json', 'w') as f:
            json.dump(api_response, f, indent=4)
    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_replication_controller_for_all_namespaces: %s\n" % e)

def list_service_accounts(api_instance):
    try:
        api_response = api_instance.list_core_v1_service_account_for_all_namespaces().to_dict()
        with open('service_accounts.json', 'w') as f:
            json.dump(api_response, f, indent=4)
    except ApiException as e:
        print("Exception when calling CoreV1Api->list_core_v1_service_account_for_all_namespaces: %s\n" % e)
