from django.db import models

# Create your models here.
# Create django model with:
# chaos_test, criterial, test, experiment, is_active, updated_at, created_at
class ActiveExperiments(models.Model):

    chaos_test = models.CharField(max_length=200)
    criterial = models.CharField(max_length=200)
    test = models.TextField()
    experiment = models.CharField(max_length=200)
    body = models.TextField()
    is_active = models.BooleanField(default=False)
    
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.chaos_test

    def __unicode__(self):
        return self.chaos_test

