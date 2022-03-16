from django.db import models

# Create your models here.
# Create django model with:
# chaos_test, criterial, test, experiment, is_active, updated_at, created_at


class ActiveExperiments(models.Model):

    chaos_test = models.CharField(max_length=200)
    criterial = models.CharField(max_length=200)
    test = models.TextField()
    experiment = models.CharField(max_length=200)
    namespace = models.TextField()
    is_active = models.BooleanField(default=False)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # testSuccess = models.BooleanField(default=False)

    # numberOfRepetions = models.IntegerField(default=0)

    def __str__(self):
        return self.chaos_test

    def __unicode__(self):
        return self.chaos_test


class TestResults(models.Model):

    # Use ForeignKey to link to the active_experiments model
    experiment = models.ForeignKey(ActiveExperiments, on_delete=models.CASCADE)

    # Bool TestResults
    testSuccess = models.CharField(max_length=200)
    numberOfRepetions = models.IntegerField(default=0)

    criterial = models.CharField(max_length=200)
    test = models.TextField()

    testId = models.CharField(max_length=200)

    fullName = models.CharField(max_length=1000)

    failureMessages = models.TextField()

    duration = models.IntegerField(default=0)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
