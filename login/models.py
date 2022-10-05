from django.db import models

# Create your models here.
class Login(models.Model):
    account_name= models.CharField(max_length=10)
    password_name = models.CharField(max_length=10)

    def __str__(Self):
        return Self.account_name
    
