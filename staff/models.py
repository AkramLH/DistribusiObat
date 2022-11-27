from django.db import models
from django.contrib.auth.models import User

class Pustus(models.Model):
    nama = models.CharField(max_length=50)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nama
    
    
class Staff(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField(null=True)
    nip = models.IntegerField(null=True)
    password = models.CharField(max_length=50)
    pustu_id = models.ForeignKey(Pustus, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name