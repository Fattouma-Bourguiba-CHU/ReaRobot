from django.db import models
from django.db.models import CharField

# Create your models here.
class Patient(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = CharField(max_length=50)
    num_cin =  CharField(max_length=50)
    email = CharField(max_length=50)
    phone = CharField(max_length=15)
    birth_date = CharField(max_length=50)
    gender = CharField(max_length=50)
    address = CharField(max_length=100)
    care_unity = CharField(max_length=50)
    release_date = CharField(max_length=50)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
     
