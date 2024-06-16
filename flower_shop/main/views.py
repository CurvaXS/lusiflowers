from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core import serializers
import json

from .models import *
from .forms import FeedbackForm

def index(request):
    initial_count = 3
    autors_bucket = AutorsBucket.objects.order_by('-id')[:initial_count]
    compositions = Compositions.objects.order_by('-id')[:initial_count]
    busket = Busket.objects.order_by('-id')[:initial_count]
    comment = Feedback.objects.order_by('-id')
    
    
    error = ''
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.name_id = request.user.id
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверна!'

    form = FeedbackForm()
    
    return render(request, 'main/index.html', {
        'autors_bucket': autors_bucket,
        'compositions': compositions,
        'busket': busket,
        'form': form,
        'error': error,
        "comment":comment
    })

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseServerError
@csrf_exempt
@require_POST
def show_more(request):
    try:
        # Ваш код обработки запроса
        initial_count = 3
        additional_count = 9
        all_items = list(AutorsBucket.objects.all())
        initial_items = all_items[:initial_count]
        remaining_items = all_items[initial_count:]

        if len(remaining_items) > additional_count:
            more_items = remaining_items[:additional_count]
        else:
            more_items = remaining_items

        serialized_items = serializers.serialize('json', more_items)
        deserialized_items = json.loads(serialized_items)
        more_items_data = [{'name': item['fields']['name'], 'price': item['fields']['price']} for item in deserialized_items]

        return JsonResponse({'more_items': more_items_data})
    except Exception as e:
        # Выводим подробную информацию об ошибке
        import traceback
        traceback.print_exc()
        return HttpResponseServerError(f"An error occurred: {str(e)}")