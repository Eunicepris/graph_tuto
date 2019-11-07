from django.shortcuts import render
from django.db.models import Avg, Max, Min
from . import models

# Create your views here.

def home(request):
    population = models.Population.objects.all().order_by('-nbabts')
    data={
        'population': population,
    }
    return render(request, 'index.html', data)

def statistique(request):
    population = models.Population.objects.all().order_by('-nbabts')
    moy = models.Population.objects.all().aggregate(Avg('nbabts'))
    grd = models.Population.objects.all().aggregate(Max('nbabts'))
    pti = models.Population.objects.all().aggregate(Min('nbabts'))
    data={
        'population': population,
        'moy': moy,
        'grd': grd,
        'pti': pti,
    }
    return render(request, 'statistique.html', data)