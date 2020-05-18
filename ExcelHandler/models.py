from django.db import models
# from django_cleanup import cleanup


# @cleanup.ignore
class TestExcel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, null=True)
    age = models.CharField(max_length=250, null=True)
    gender = models.CharField(max_length=250, null=True)
