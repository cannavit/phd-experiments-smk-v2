from django.contrib import admin
from .models import ActiveExperiments

# import variables from  settings.py.
from django.conf import settings
import requests
import json

# import messsage from django
from django.contrib import messages

# import all atacks from chaos. 
from .utils.chaos_network import Network_Blackhole

def getTokenChaos():

    url = "https://api.gremlin.com/v1/users/auth?getCompanySession=true"
    payload = 'email='+ settings.CHAOS_EMAIL +'&password=' + settings.CHAOS_PASSWORD

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)


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

        if obj.chaos_test == 'Network BlackHole':
            
            atackRespone = Network_Blackhole(tokenBearer['header'])

            if atackRespone.status_code == 201:
                messages.success(request, str(obj.id) + " Atack Id :" + atackRespone.text + " URL: " + atackRespone.url)
            else:
                messages.error(request, str(obj.id) + 'Atack not created')
                break

        break



# Register your models here.
# Show all field in admin page
class ActiveExperimentsAdmin(admin.ModelAdmin):
    list_display = ('id','chaos_test', 'criterial',
                    'test', 'experiment', 'is_active')
    list_filter = ('id','chaos_test', 'criterial',
                   'test', 'experiment', 'is_active')
    search_fields = ('id','chaos_test', 'criterial',
                     'test', 'experiment', 'is_active')
    ordering = ('id','chaos_test', 'criterial', 'test', 'experiment', 'is_active')
    filter_horizontal = ()
    list_per_page = 25

    actions = [run_experiment]


# Declarate admin view
admin.site.register(ActiveExperiments, ActiveExperimentsAdmin)
