from django.db import models

# Create your models here.

class Employee(models.Model):
    eid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    sal=models.FloatField()
    city=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.eid},{self.name},{self.sal},{self.city}"