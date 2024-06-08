from django.shortcuts import render
from .models import *


def index(request):
    autors_bucket = AutorsBucket.objects.order_by('-id')
    compositions = Compositions.objects.order_by('-id')
    busket = Busket.objects.order_by('-id')
    return render(request, 'main/index.html', {
        'autors_bucket': autors_bucket,
        'compositions': compositions,
        'busket': busket
    })