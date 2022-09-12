import email
from django.db import models

# Create your models here.
CHOICES=(
    ("1","python"),
    ("2","django"),
    ("3","devops"),
    ("4","others")
)
class Students(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    courses=models.CharField(max_length=30,choices=CHOICES,default="1")
    jdate=models.DateField()

