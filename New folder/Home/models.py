from django.db import models
from imageFile.models import Test


class getModel(models.Model):
    # id 		= models.IntegerField()
    id = models.AutoField(primary_key=True)  # NOT NULL AUTO_INCREMENT,PRIMARY KEY
    username = models.CharField(max_length=50, unique=True) # UNIQUE VALUE FIELD
    password = models.CharField(max_length=50, unique=True)  # (default='DEFAULT VALUE' or  default='') , null=True
    email_address = models.EmailField(max_length=100, null=True)
    phone_number = models.IntegerField(null=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
"""
def __str__(self):
    return self.username
    
class Meta:
    managed = False
    db_table = 'manufacturer_name'
"""
# Create your models here.
