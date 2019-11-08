from django.db import models


class Database(models.Model):
    id=models.CharField(max_length=10,primary_key=True,default="")
    Fname = models.CharField(max_length=200,default="")
    Lname = models.CharField(max_length=200,default="")
    Email = models.CharField(max_length=200,default="")
    city = models.CharField(max_length=200,default="")
    Add = models.CharField(max_length=200,default="")
    Country = models.CharField(max_length=200,default="")
    Zip = models.CharField(max_length=6,default="")
    Phone = models.CharField(max_length=10,default="")
    Text = models.TextField(max_length=200,default="")


    def __str__(self):
        return self.Fname


