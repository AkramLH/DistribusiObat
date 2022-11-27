from django.db import models

class TypeObat(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Obat(models.Model):
    name = models.CharField(max_length=100)
    type_obat = models.ForeignKey(TypeObat, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name