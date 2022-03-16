import time
from django.contrib import admin
from .models import ActiveExperiments, TestResults
from .run_kube_smoke_test import kubeSmokeTest

# import variables from  settings.py.
from django.conf import settings
import requests
import json

# import messsage from django
from django.contrib import messages

# import all atacks from chaos.
from .utils.chaos_network import Network_Blackhole


CHAOS_TEST_BODY = {
    "targetDefinition":
        {"strategy":
            {"labels": {},
             "k8sObjects": [
                {
                    "clusterId": "changeit",
                    "uid": "b82c1f26-f2a3-4c0a-855e-a5daed03bf81",
                    "namespace": "smoke-test",
                    "name": "teastore-webui",
                    "kind": "DEPLOYMENT",
                    "labels": {},
                    "annotations": {},
                    "availableContainers": [],
                    "targetType":"Kubernetes"
                }
            ],
                "percentage": 100,
                "containerSelection": {
                "selectionType": "ANY",
                "containerNames": []
            }
            }},
    "impactDefinition": {"cliArgs": ["shutdown2", "-d", "0", "-r"]}}


def getTokenChaos():

    url = "https://api.gremlin.com/v1/users/auth?getCompanySession=true"
    payload = 'email=' + settings.CHAOS_EMAIL + \
        '&password=' + settings.CHAOS_PASSWORD

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)


def run_attack(CHAOS_TEST_BODY_TEMP, tokenBearer):

    url = "https://api.gremlin.com/v1/kubernetes/attacks/new?teamId=" + settings.CHAOS_TEAM_ID

    headers = {
        'Content-Type': 'application/json;charset=utf-8',
        'Authorization': tokenBearer
    }

    payload = json.dumps(CHAOS_TEST_BODY_TEMP)

    response = requests.request("POST", url, headers=headers, data=payload)

    return response


def attack_status(tokenBearer, attackId):

    url = "https://api.gremlin.com/v1/kubernetes/attacks/" + \
        attackId + "?teamId=" + settings.CHAOS_TEAM_ID

    headers = {
        'accept': 'application/json',
        'Authorization': tokenBearer
    }

    payload = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    response = json.loads(response.text)

    try:
        print(response['attackId'])
        urlAttack = 'https://api.gremlin.com/v1/attacks/' + \
            response['attackId'] + "?teamId=" + settings.CHAOS_TEAM_ID

        responseAttack = requests.request(
            "GET", urlAttack, headers=headers, data={})

        response = json.loads(responseAttack.text)

    except:
        print("Attack not found")
        # stateAttack = response['stage']

    return response['stage']


@admin.action(description='Run the experiments')
def run_experiment(modeladmin, request, queryset):

    tokenBearer = getTokenChaos()

    if len(tokenBearer) > 10:
        # Print message in the admin page
        messages.success(request, "Token: " + tokenBearer['header'])

    print(tokenBearer)

    # Get the Data Selected when was active the action
    for obj in queryset:
        print(obj.chaos_test)

        CHAOS_TEST_BODY_TEMP = CHAOS_TEST_BODY

        CHAOS_TEST_BODY_TEMP['impactDefinition']['cliArgs'][0] = obj.chaos_test

        # TODO here is possible add the numbers of the pods
        CHAOS_TEST_BODY_TEMP['targetDefinition']['strategy']["k8sObjects"][0]['namespace'] = obj.namespace

        print(CHAOS_TEST_BODY_TEMP, tokenBearer)

        attackResponse = run_attack(
            CHAOS_TEST_BODY_TEMP, tokenBearer['header'])

        print(attackResponse.text)

        if attackResponse.status_code == 201:
            messages.success(
                request, "Attack: " + obj.chaos_test + " is running, code: " + attackResponse.text)
        else:
            messages.error(
                request, "Attack Error: " + obj.chaos_test + " ERROR: " + attackResponse.reason)
            break

        for i in range(0, 2000, 1):

            statusRespone = attack_status(
                tokenBearer['header'], attackResponse.text)

            print('STATUS ATTACK: ' + str(i) + ' ' + statusRespone)

            if statusRespone == 'Successful':
                messages.success(
                    request, "Attack: " + obj.chaos_test + " is finished, code: " + attackResponse.text)
                break

            elif statusRespone == 'Pending':
                # TODO Run here the smoke test librery

                if obj.test == 'check_memory':

                    response = kubeSmokeTest.check_memory(obj.namespace)
                    save_experiment_data(response,obj.criterial,obj.test, obj)
                    
                elif obj.test == 'check_disk':

                    response = kubeSmokeTest.check_memory(obj.namespace)
                    save_experiment_data(response,obj.criterial,obj.test, obj)

                    print(response)

                messages.warning(
                    request, "Attack: " + obj.chaos_test + " is pending, code: " + attackResponse.text)

            else:
                messages.error(
                    request, "Attack Error: " + obj.chaos_test + " ERROR: " + attackResponse.reason)
                break

            time.sleep(2)


# Register your models here.
# Show all field in admin page
class ActiveExperimentsAdmin(admin.ModelAdmin):

    list_display = ( 'id','chaos_test', 'criterial',
                    'test', 'experiment', 'is_active')
    list_filter = ( 'chaos_test', 'criterial',
                   'test', 'experiment', 'is_active')
    search_fields = ( 'chaos_test', 'criterial',
                     'test', 'experiment', 'is_active')
    ordering = ( 'chaos_test', 'criterial',
                'test', 'experiment', 'is_active')
    filter_horizontal = ()
    list_per_page = 25

    actions = [run_experiment]


# Declarate admin view
admin.site.register(ActiveExperiments, ActiveExperimentsAdmin)


# Register TestResults model
class TestResultsAdmin(admin.ModelAdmin):

    list_display = ('id', 'testId', 'fullName', 'testSuccess',
                    'numberOfRepetions', 'criterial', 'test', 'failureMessages', 'duration')
    list_filter = ( 'testId', 'fullName', 'testSuccess',
                   'numberOfRepetions', 'criterial', 'test', 'failureMessages', 'duration')
    search_fields = ( 'testId', 'fullName', 'testSuccess',
                     'numberOfRepetions', 'criterial', 'test', 'failureMessages', 'duration')
    ordering = ( 'testId', 'fullName', 'testSuccess',
                'numberOfRepetions', 'criterial', 'test', 'failureMessages', 'duration')
    filter_horizontal = ()
    list_per_page = 25


admin.site.register(TestResults, TestResultsAdmin)



def save_experiment_data(response,test_criterial,test_name, obj):

    for test in response['testResults']:
        testResultModel = TestResults.objects.filter(
            testId=response['testId'],
            fullName=test['fullName'],
        )
        if testResultModel.count() == 0:
            TestResults.objects.create(
                testId=response['testId'],
                fullName=test['fullName'],
                experiment_id=obj.id,
                testSuccess=test['status'],
                numberOfRepetions=0,
                criterial=test_criterial,
                test=test_name,
                failureMessages=test['failureMessages'],
                duration=test['duration']
            )
        else:
            print(test)