from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    text=models.CharField(max_length=255)
    date=models.DateTimeField()
    fee=models.BigIntegerField()
    amount=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.fee} - {self.date}"
class Income(models.Model):
    text=models.CharField(max_length=255)
    date=models.DateTimeField()
    fee=models.BigIntegerField()
    amount=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.PROTECT)