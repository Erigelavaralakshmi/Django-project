from django.db import models
from typing import Iterable
from enum import Enum 
# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 

    class Meta:
        abstract = True

class Department(Base):
    name = models.CharField(max_length=32)
    date_of_creation = models.DateField(auto_now_add=True)
    employee_count = models.PositiveBigIntegerField(default=0)
    active = models.BooleanField(default=True)


class Employee(Base):

    class DESIGNATION(Enum):
        EXECUTIVE = 'executive'
        SENIOR = 'senior'
        MIDDLE = 'middle'
        JUNIOR = 'junior'
       
        @classmethod
        def choices(cls):
            return [(key.value, key.name) for key in cls]
        
    name  = models.CharField(max_length=32, db_index=True)
    id_number = models.IntegerField(unique=True, null=False, db_index=True)
    date_of_joining = models.DateField()
    salary = models.FloatField(null=True)
    active = models.BooleanField(default=True)
    designation = models.CharField(max_length=16, choices=DESIGNATION.choices, null=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, related_name='employee', null=True)

    class Meta:
        db_table_comment = "This contains Employee data"
