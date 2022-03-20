import json
from django.conf import settings
import requests


class kubeSmokeTest():

    #! Cluster Coverage experiments:

    def check_memory(namespace):

        url = settings.KUBE_SMOKE_TEST_HOST + \
            "/cluster-coverage/check-memory?runTests=true$namespace=" + namespace

        headers = {
            'accept': 'application/json'
        }

        payload = {
            'namespace': namespace,
            'runTests': True
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return json.loads(response.text)

    def check_disk(namespace):

        url = settings.KUBE_SMOKE_TEST_HOST + \
            "/cluster-coverage/check-disk?runTests=true$namespace=" + namespace

        headers = {
            'accept': 'application/json'
        }

        payload = {
            'namespace': namespace,
            'runTests': True
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return json.loads(response.text)

    def check_nodes(namespace):

        url = settings.KUBE_SMOKE_TEST_HOST + \
            "/cluster-coverage/check-nodes?runTests=true$namespace=" + namespace

        headers = {
            'accept': 'application/json'
        }

        payload = {
            'namespace': namespace,
            'runTests': True
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return json.loads(response.text)

    #! ingress-coverage

    def check_ingress(namespace):

        url = settings.KUBE_SMOKE_TEST_HOST + \
            "/cluster-coverage/check-ingress?runTests=true$namespace=" + namespace

        headers = {
            'accept': 'application/json'
        }

        payload = {
            'namespace': namespace,
            'runTests': True
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return json.loads(response.text)

    #! resource-up

    def volumes_free_space(namespace):

        url = settings.KUBE_SMOKE_TEST_HOST + \
            "/cluster-coverage/volumes-free-space?runTests=true$namespace=" + namespace

        headers = {
            'accept': 'application/json'
        }

        payload = {
            'namespace': namespace,
            'runTests': True
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return json.loads(response.text)

    def volumes_exist_files(namespace):

        url = settings.KUBE_SMOKE_TEST_HOST + \
            "/cluster-coverage/volumes-exist-space?runTests=true$namespace=" + namespace

        headers = {
            'accept': 'application/json'
        }

        payload = {
            'namespace': namespace,
            'runTests': True
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return json.loads(response.text)

    #! Service Coverage

    def check_pods_running(namespace):

        url = settings.KUBE_SMOKE_TEST_HOST + \
            "/cluster-coverage/check-pods-running?runTests=true$namespace=" + namespace

        headers = {
            'accept': 'application/json'
        }

        payload = {
            'namespace': namespace,
            'runTests': True
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return json.loads(response.text)
