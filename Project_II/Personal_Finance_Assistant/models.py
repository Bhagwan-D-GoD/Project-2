from django.db import models

# Create your models here.
class User_Info(models.Model):
    user_id = models.CharField(primary_key=True,max_length=10,)
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=10000)
    
    def __str__(self):
        return self.user_name