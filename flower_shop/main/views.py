from django.shortcuts import render
from .models import *


def index(request):
    autors_bucket = AutorsBucket.objects.all()
    compositions = Compositions.objects.all()
    busket = Busket.objects.all()
    return render(request, 'main/index.html', {
        'autors_bucket': autors_bucket,
        'compositions': compositions,
        'busket': busket
        })