from django.contrib import admin
from .models import NameExperiments
import os
from django.contrib import messages


from active_experiments.models import ActiveExperiments

# Register your models here.
# Show all field in admin page.
@admin.action(description='Import CSV file experiments')
def import_cvs_experiments(modeladmin, request, queryset):

    print('')
    # queryset.update(status='p')

    # Get the Data Selected when was active the action
    for obj in queryset:
        print(obj.name_experiments_file)

        # Import one file .csv with the name file.

        # Check if one file exist in one directory.
        if os.path.isfile('experiments_files/'+obj.name_experiments_file):
            print('File exist')

            with open('experiments_files/'+obj.name_experiments_file) as f:
                contents = f.read()
                # Convert String  to List
                c = 0
                contents2 = contents.split('\n')
                for data in contents2:
                    c = c + 1
                    if c > 1:
                        # Convert String  to List
                        row = data.split(',')
                        print(row)
                        
                        # delete blank spaces of one string 
                        count =  ActiveExperiments.objects.filter(
                            chaos_test=row[0].strip(),
                            criterial=row[1].strip(),
                            test=row[2].strip(),
                            experiment=row[3].strip(),
                        ).count()   

                        stringMessage = row[0].strip() + ' ' + row[1].strip() + ' ' + row[2].strip() + ' ' + row[3].strip()

                        if count == 0:
                            # Add new data in ActiveExperiments

                            if row[0].strip() == "":
                                messages.error(request, "One black row. Not is possible load it")
                            else:
                                ActiveExperiments.objects.create(
                                    chaos_test=row[0].strip(),
                                    criterial=row[1].strip(),
                                    test=row[2].strip(),
                                    experiment=row[3].strip(),
                                    body=row[4].strip(),
                                    is_active=True
                                )
    
                                messages.success(request, "Upload Experiment: "+ stringMessage)

                        else:
                            messages.warning(request, "Experiment already exist: "+ stringMessage)
                            

        else: 
            print('File not exist')
            messages.error(request, "File not exist: "+ obj.name_experiments_file)

class NameExperimentAdmin(admin.ModelAdmin):

    list_display = ('name_experiments_file', 'is_active', 'is_running', 'is_finished', 'is_active')
    list_filter = ('name_experiments_file', 'is_active', 'is_running', 'is_finished', 'is_active')
    search_fields = ('name_experiments_file', 'is_active', 'is_running', 'is_finished', 'is_active')
    ordering = ('name_experiments_file', 'is_active', 'is_running', 'is_finished', 'is_active')
    filter_horizontal = ()
    list_per_page = 25
    
    actions = [import_cvs_experiments]

# Declarate admin view
admin.site.register(NameExperiments, NameExperimentAdmin)