"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Employee(models.Model):

    name = models.CharField(max_length=50)
    start_salary = models.DecimalField(max_digits=9, decimal_places=2, default=0.0, null=False)
    current_salary = models.DecimalField(max_digits=9, decimal_places=2, default=0.0, null=False)
    years_of_experience = models.IntegerField(null=False, default=0)
    date_of_joining = models.DateTimeField()
    created_dt = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_dt = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table='employee'
