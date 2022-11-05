from django.db import models


class App(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    image = models.CharField(max_length=128, null=False, blank=False)
    envs = models.CharField(max_length=128, null=False, blank=False)
    command = models.CharField(max_length=128, null=False, blank=False)


class History(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    envs = models.CharField(max_length=128, null=False, blank=False)
    startAt = models.DateField(null=True, blank=False)
