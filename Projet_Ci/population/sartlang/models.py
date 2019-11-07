from django.db import models
from django.db.models import Sum
# Create your models here.

class Population(models.Model):
    nom = models.CharField(max_length=255)
    nbabts = models.PositiveIntegerField(default=0)
    
    @property
    def pourcentage(self):
        pourcentag = self.nbabts / 100
        return pourcentag
    
    
    @property
    def pourcentage(self):
        total = Population.objects.all().aggregate(une_sum = Sum('nbabts'))
        pourcentag = (self.nbabts/total['une_sum'])*100
        return round(pourcentag, 2) 
    
    def __str__(self):
        return self.nom
