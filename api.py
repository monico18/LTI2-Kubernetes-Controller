import json

# Data provided
data = {
    "kind": "APIResourceList",
    "groupVersion": "v1",
    "resources": [
        {"name": "bindings", "singularName": "binding", "namespaced": True, "kind": "Binding", "verbs": ["create"]},
        {"name": "componentstatuses", "singularName": "componentstatus", "namespaced": False, "kind": "ComponentStatus", "verbs": ["get", "list"], "shortNames": ["cs"]},
        {"name": "configmaps", "singularName": "configmap", "namespaced": True, "kind": "ConfigMap", "verbs": ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"], "shortNames": ["cm"], "storageVersionHash": "qFsyl6wFWjQ="},
        {"name": "endpoints", "singularName": "endpoints", "namespaced": True, "kind": "Endpoints", "verbs": ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"], "shortNames": ["ep"], "storageVersionHash": "fWeeMqaN/OA="},
        {"name": "events", "singularName": "event", "namespaced": True, "kind": "Event", "verbs": ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"], "shortNames": ["ev"], "storageVersionHash": "r2yiGXH7wu8="},
        {"name": "limitranges", "singularName": "limitrange", "namespaced": True, "kind": "LimitRange", "verbs": ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"], "shortNames": ["limits"], "storageVersionHash": "EBKMFVe6cwo="},
        {"name": "namespaces", "singularName": "namespace", "namespaced": False, "kind": "Namespace", "verbs": ["create", "delete", "get", "list", "patch", "update", "watch"], "shortNames": ["ns"], "storageVersionHash": "Q3oi5N2YM8M="},
        {"name": "namespaces/finalize", "singularName": "", "namespaced": False, "kind": "Namespace", "verbs": ["update"]},
        {"name": "namespaces/status", "singularName": "", "namespaced": False, "kind": "Namespace", "verbs": ["get", "patch", "update"]},
        {"name": "nodes", "singularName": "node", "namespaced": False, "kind": "Node", "verbs": ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"], "shortNames": ["no"], "storageVersionHash": "XwShjMxG9Fs="},
        {"name": "nodes/proxy", "singularName": "", "namespaced": False, "kind": "NodeProxyOptions", "verbs": ["create", "delete", "get", "patch", "update"]},
        {"name": "nodes/status", "singularName": "", "namespaced": False, "kind": "Node", "verbs": ["get", "patch", "update"]},
        {"name": "persistentvolumeclaims", "singularName": "persistentvolumeclaim", "namespaced": True, "kind": "PersistentVolumeClaim", "verbs": ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"], "shortNames": ["pvc"], "storageVersionHash": "QWTyNDq0dC4="},
        {"name": "persistentvolumeclaims/status", "singularName": "", "namespaced": True, "kind": "PersistentVolumeClaim", "verbs": ["get", "patch", "update"]},
        {"name": "persistentvolumes", "singularName": "persistentvolume", "namespaced": False, "kind": "PersistentVolume", "verbs": ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"], "shortNames": ["pv"], "storageVersionHash": "HN/zwEC+JgM="},
        {"name": "persistentvolumes/status", "singularName": "", "namespaced": False, "kind": "PersistentVolume", "verbs": ["get", "patch", "update"]},
        {"name": "pods", "singularName": "pod", "namespaced": True, "kind": "Pod", "verbs": ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"], "shortNames": ["po"], "categories": ["all"], "storageVersionHash": "xPOwRZ+Yhw8="},
        {"name": "pods/attach", "singularName": "", "namespaced": True, "kind": "PodAttachOptions", "verbs": ["create", "get"]},
        {"name": "pods/binding", "singularName": "", "namespaced": True, "kind": "Binding", "verbs": ["create"]},
        {"name": "pods/ephemeralcontainers", "singularName": "", "namespaced": True, "kind": "Pod", "verbs": ["get", "patch", "update"]},
        {"name": "pods/eviction", "singularName": "", "namespaced": True, "group": "policy", "version": "v1", "kind": "Eviction", "verbs": ["create"]},
        {"name": "pods/exec", "singularName": "", "namespaced": True, "kind": "PodExecOptions", "verbs": ["create", "get"]},
        {"name": "pods/log", "singularName": "", "namespaced": True, "kind": "Pod", "verbs": ["get"]},
        {"name": "pods/portforward", "singularName": "", "namespaced": True, "kind": "PodPortForwardOptions", "verbs": ["create", "get"]},
        {"name": "pods/proxy", "singularName": "", "namespaced": True, "kind": "PodProxyOptions", "verbs": ["create", "delete", "get", "patch", "update"]},
        {"name": "pods/status", "singularName": "", "namespaced": True, "kind": "Pod", "verbs": ["get", "patch", "update"]},
        {"name": "podtemplates", "singularName": "podtemplate", "namespaced": True, "kind": "PodTemplate", "verbs": ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"], "storageVersionHash": "LIXB2x4IFpk="},
        {"name": "replicationcontrollers", "singularName": "replicationcontroller", "namespaced": True, "kind": "ReplicationController", "verbs": ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"], "shortNames": ["rc"], "categories": ["all"], "storageVersionHash": "Jond2If31h0="},
        {"name": "replicationcontrollers/scale", "singularName": "", "namespaced": True, "group": "autoscaling", "version": "v1", "kind": "Scale", "verbs": ["get", "patch", "update"]},
        {"name": "replicationcontrollers/status", "singularName": "", "namespaced": True, "kind": "ReplicationController", "verbs": ["get", "patch", "update"]},
        {"name": "resourcequotas", "singularName": "resourcequota", "namespaced": True, "kind": "ResourceQuota", "verbs": ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"], "shortNames": ["quota"], "storageVersionHash": "8uhSgffRX6w="},
        {"name": "resourcequotas/status", "singularName": "", "namespaced": True, "kind": "ResourceQuota", "verbs": ["get", "patch", "update"]},
        {"name": "secrets", "singularName": "secret", "namespaced": True, "kind": "Secret", "verbs": ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"], "storageVersionHash": "S6u1pOWzb84="},
        {"name": "serviceaccounts", "singularName": "serviceaccount", "namespaced": True, "kind": "ServiceAccount", "verbs": ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"], "shortNames": ["sa"], "storageVersionHash": "pbx9ZvyFpBE="},
        {"name": "serviceaccounts/token", "singularName": "", "namespaced": True, "group": "authentication.k8s.io", "version": "v1", "kind": "TokenRequest", "verbs": ["create"]},
        {"name": "services", "singularName": "service", "namespaced": True, "kind": "Service", "verbs": ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"], "shortNames": ["svc"], "categories": ["all"], "storageVersionHash": "0/CO1lhkEBI="},
        {"name": "services/proxy", "singularName": "", "namespaced": True, "kind": "ServiceProxyOptions", "verbs": ["create", "delete", "get", "patch", "update"]},
        {"name": "services/status", "singularName": "", "namespaced": True, "kind": "Service", "verbs": ["get", "patch", "update"]}
    ]
}

schema = []
for resource in data["resources"]:
    schema.append({
        "Resource Name": resource["name"],
        "Singular Name": resource["singularName"],
        "Namespaced": resource["namespaced"],
        "Kind": resource["kind"],
        "Verbs": resource["verbs"],
        "Short Names": resource.get("shortNames", []),
        "Categories": resource.get("categories", []),
        "Group": resource.get("group", ""),
        "Version": resource.get("version", "")
    })

# Write schema to JSON file
with open("k8s_resources_schema.json", "w") as file:
    json.dump(schema, file, indent=4)