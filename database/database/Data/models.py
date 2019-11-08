from django.db import models


class Database(models.Model):
    Fname = models.CharField(max_length=200)
    Lname = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    Add = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    Zip = models.CharField(max_length=6)
    Phone = models.CharField(max_length=10)
    Text = models.CharField(max_length=200)


    def __str__(self):
        return self.Fname


