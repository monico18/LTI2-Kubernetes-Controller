from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = swagger_client.Configuration()
configuration.api_key['authorization'] = 'eyJhbGciOiJSUzI1NiIsImtpZCI6InRaNkNNOWhXNzJ1VjVyU045SVZ4d1gtVHBEcFpVczBGOEZZTjF4Sm4xZTQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiLCJrM3MiXSwiZXhwIjoxNzE1NzcwNjQ4LCJpYXQiOjE3MTU3NjcwNDgsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsInNlcnZpY2VhY2NvdW50Ijp7Im5hbWUiOiJhZG1pbi11c2VyIiwidWlkIjoiOGQ1MmFlMzEtMWJmYy00MDM0LWE5Y2ItMGYxOGQ1NjEyM2Y3In19LCJuYmYiOjE3MTU3NjcwNDgsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDprdWJlLXN5c3RlbTphZG1pbi11c2VyIn0.KOw8vu6sCSCJ8h2CEVO0IWAoatvsADBHn4hPfI0MuUl6ORJ9ngX3u5ElGfENAm5ENxQUHM99qD-hxP7Bw9ZbKq60IOEIve05pcJ5mfk7oX3QL7yoo-HLMfT2tgmO6DogBEOfWGUP2IHIBYXEIWJ0QgYf39cgZ5CNx3sKAp7SodT6Pyigw2hyBoF6P9BEZEIn1pmk_Ua8fLqiuiNZuEW-Os019sscpZBiikZHtzZAyCUuj3IwtvSGiGZS6p1t6JMt8xbyX3jthua9i44cW4KtNW5Ve_RrUPBXohfcDTknqO4KLtoqUXbkcdD9IxzSB2RUW0pp3W_kme4z_JeOLKULFQ'
configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CoreV1Api(swagger_client.ApiClient(configuration))

try:
    #list nodes
    api_response = api_instance.list_core_v1_node()
    pprint(api_response)
    #list namespaces
    api_response = api_instance.list_core_v1_namespace()
    pprint(api_response)
    #list pods
    api_response = api_instance.list_core_v1_namespace()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WellKnownApi->get_service_account_issuer_open_id_configuration: %s\n" % e)
