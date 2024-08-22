from django.db import models

class Employee(models.Model):
    cusid = models.CharField(max_length=200)
    serialno = models.CharField(max_length=200)
    type = models.DateField()


    class Meta:
        db_table = 'Amc_tbl'
