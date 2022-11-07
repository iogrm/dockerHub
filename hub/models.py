from django.db import models


class App(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    image = models.CharField(max_length=128, null=False, blank=False)
    envs = models.CharField(max_length=128, null=False, blank=False)
    command = models.CharField(max_length=128, null=False, blank=False)


class Container(models.Model):
    containerId = models.CharField(max_length=128, null=False, blank=False)
    name = models.CharField(max_length=128, null=False, blank=False)
    image = models.CharField(max_length=128, null=False, blank=False)
    command = models.CharField(max_length=128, null=False, blank=False)
    createdAt = models.DateField(null=True, blank=False)
    envs = models.CharField(max_length=128, null=False, blank=False)
    appName = models.CharField(max_length=128, null=False, blank=False)
