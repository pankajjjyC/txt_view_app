from django.db import models

# Create your models here.

class txt_file(models.Model):#used    
    id = models.IntegerField(primary_key=True)
    txtfile=models.FileField() 
