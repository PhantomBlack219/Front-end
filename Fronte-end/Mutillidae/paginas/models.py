from django.db import models

# Create your models here.
from email.policy import default
from django.db import models

# Create your models here.
class Aindice(models.Model):
    Aindice = models.CharField(max_length=200, default="A1")
    nombreA = models.CharField(max_length=11000)

    def get_indiceA(self):
        return self.Aindice
    def get_nombreA(self):
        return self.nombreA
        
    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.Aindice +' '+self.nombreA, self.id)

class Owasp(models.Model):
    nombre = models.CharField(max_length=200, default="OWASP")
    año = models.CharField(max_length=1000)
    def get_nombre(self):
        return self.nombre
    def get_año(self):
        return self.año 
    
    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.nombre, self.id)


