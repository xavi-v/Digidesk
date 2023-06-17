from django.db import models

# Create your models here.
class Digimon(models.Model):
  name = models.CharField(max_length = 128, help_text = " Ingrese el nombre del Digimon: ")
  img = models.CharField(max_length = 256, help_text = "ingrese la imagen: ")
  level = models.CharField(max_length = 128, help_text = "ingrese el lvl por favor: ")
  
def __str__(self):
  return f"*{self.name}*"


  