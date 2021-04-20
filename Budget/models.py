from django.db import models
from django.contrib.auth.models import User

class Asset(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    purpose = models.CharField(max_length=100)
    totalamount = models.DecimalField(max_digits=1000,decimal_places=3)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.purpose
    


class Cost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    asset = models.ForeignKey(Asset,on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=1000,decimal_places=3)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
    