from django.db import models
# from django_cleanup import cleanup


# @cleanup.ignore
class ImageModel(models.Model):
    # id 		= models.IntegerField()
    id = models.AutoField(primary_key=True)
    uploadedDate = models.DateTimeField(auto_now_add=True)
    userName = models.CharField(max_length=50, null=True)
    imageColumn = models.ImageField(upload_to='imageFolder/', null=True)


class Test(models.Model):
    # id 		= models.IntegerField()
    id = models.AutoField(primary_key=True)
    testName = models.CharField(max_length=50, null=True)