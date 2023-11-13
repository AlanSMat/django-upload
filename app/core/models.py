from django.db import models

class Sample(models.Model):
    attachement = models.FileField()