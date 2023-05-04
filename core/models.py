from django.db import models

from django.urls import reverse 
class Mickey(models.Model):
    price =models.IntegerField("")
    name = models.CharField(max_length=149) 
    brand = models.CharField(max_length=151)
    def __str__(self):
        return self.name
    
    def kurish(self):
        return reverse('open',kwargs={'post_id':self.pk})
    
class Product(models.Model):
    name=models.CharField(max_length=100)    
    brand=models.CharField(max_length=150)

class Meta:
    verbose_name= "Mahsulot"
    verbose_name_plural = "Mahsulotlar"  

def __str__(self):
    return self.name     

def list_page(self):
    return reverse('View_list',kwargs={'list_id':self.pk})