from django.db import models

# Create your models here.

# Create Django model with:
#  name, date_created, date_modified, passTest, criterial, test, logs, idTest
class Test(models.Model):

    name = models.CharField(max_length=200)

    passTest = models.BooleanField(default=False)
    criterial = models.IntegerField(default=0)
    test = models.TextField()
    logs = models.TextField()
    idTest = models.IntegerField(default=0)


    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    