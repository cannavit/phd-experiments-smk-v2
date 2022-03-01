from django.db import models

# Create your models here.
# Create django model with:
# name, is_active, updated_at, created_at, is_running, is_finished, is_active
class NameExperiments(models.Model):
    
    name_experiments_file = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)


    is_running = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name_experiments_file
    
    def __unicode__(self):
        return self.name_experiments_file
