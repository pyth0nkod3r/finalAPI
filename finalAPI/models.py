from django.db import models

# Create your models here.


# Manager Model
class UserModel(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    phoneNo = models.IntegerField()

