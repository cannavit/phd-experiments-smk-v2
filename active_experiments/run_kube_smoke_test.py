import json
from django.conf import settings
import requests




class kubeSmokeTest():


    #! Cluster Coverage experiments: 

    def check_memory(namespace):

        url =  settings.KUBE_SMOKE_TEST_HOST +  "/cluster-coverage/check-memory?runTests=true$namespace=" + namespace

        headers = {
            'accept': 'application/json'
        }

        payload={
            'namespace': namespace,
            'runTests': True
        }

        response = requests.request("GET", url, headers=headers, data=payload)

    
        return json.loads(response.text)


    def check_disk(namespace):

        url =  settings.KUBE_SMOKE_TEST_HOST +  "/cluster-coverage/check-disk?runTests=true$namespace=" + namespace

        headers = {
            'accept': 'application/json'
        }

        payload={
            'namespace': namespace,
            'runTests': True
        }

        response = requests.request("GET", url, headers=headers, data=payload)

    
        return json.loads(response.text)


