from django.db import models

# Create your models here.
class user(models.Model):
    firstname=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    dob=models.DateField()
    gender=models.CharField(max_length=20)

class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)

    

    
