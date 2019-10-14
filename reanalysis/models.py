from django.db import models

# Create your models here.

class era5(models.Model):
    dataname = models.CharField(max_length=200)
    chartname = models.CharField(max_length=200)
    intime = models.CharField(max_length=200)
    def __str__(self):
    	return self.intime