from django.db import models
from django.contrib.auth.models import User

class stockportfolio(models.Model):
    stocksymbol=models.CharField(max_length=15)
    stockname=models.CharField(max_length=100)
    quantity=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
     
    def __str__(self):
        return self.user