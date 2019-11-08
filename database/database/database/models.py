from django.db import models


class Database(models.Model):
    ID= models.IntegerField(primary_key='true')
    Fname = models.CharField(max_length=200)
    Lname = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    Add = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    Zip = models.IntegerField(max_length=6)
    Phone = models.IntegerField(max_length=6)
    Text = models.CharField(max_length=200)
    Data = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.Fname