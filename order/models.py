from django.db import models


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
# Create your models here.

