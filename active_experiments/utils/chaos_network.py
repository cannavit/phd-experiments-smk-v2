import requests


def Network_Blackhole(bearerToken):

    url = "https://api.gremlin.com/v1/kubernetes/attacks/new?teamId=9109c912-2e8f-4ba5-89c9-122e8fbba5c1"

    payload = "{\"targetDefinition\":{\"strategy\":{\"labels\":{},\"k8sObjects\":[{\"clusterId\":\"changeit\",\"createdAt\":\"2022-02-23T13:16:22Z\",\"uid\":\"c31cd4ec-747d-4a0c-ba4d-6bd796ab9dda\",\"namespace\":\"smoke-test\",\"name\":\"teastore-registry\",\"kind\":\"DEPLOYMENT\",\"labels\":{},\"annotations\":{},\"availableContainers\":[],\"targetType\":\"Kubernetes\"},{\"clusterId\":\"changeit\",\"createdAt\":\"2022-02-23T13:16:22Z\",\"uid\":\"f8d7d3ea-4632-4f5a-837b-5cda44f7cfb3\",\"namespace\":\"smoke-test\",\"name\":\"teastore-image\",\"kind\":\"DEPLOYMENT\",\"labels\":{},\"annotations\":{},\"availableContainers\":[],\"targetType\":\"Kubernetes\"}],\"percentage\":100,\"containerSelection\":{\"selectionType\":\"ANY\",\"containerNames\":[]}}},\"impactDefinition\":{\"cliArgs\":[\"blackhole\",\"-l\",\"60\",\"-h\",\"^api.gremlin.com\",\"-p\",\"^53\"],\"providers\":[]}}"
    
    headers = {
        'Content-Type': 'application/json;charset=utf-8',
        'Authorization': bearerToken
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response

# print(response.text)
