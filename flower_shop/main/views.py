from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseServerError
from django.views.generic import ListView
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


class Search(ListView):
    template_name = 'main/results.html'
    context_object_name = 'results'
    def get_queryset(self):
        q = self.request.GET.get('q')
        # Создаем QuerySet для каждой модели
        autors_query = AutorsBucket.objects.filter(name__icontains=q)
        compositions_query = Compositions.objects.filter(name__icontains=q)
        bucket_query = Busket.objects.filter(name__icontains=q)
        # Объединяем QuerySetы
        combined_query = autors_query.union(compositions_query, bucket_query)
        return combined_query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

@csrf_exempt
@require_POST
def show_more(request):
    try:
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
        more_items_data = [
            {
                'name': item['fields']['name'],
                'price': item['fields']['price'],
                'photo_url': item['fields']['photo']
            }
            for item in deserialized_items
        ]

        return JsonResponse({'more_items': more_items_data})
    except Exception as e:
        # Выводим подробную информацию об ошибке
        import traceback
        traceback.print_exc()
        return HttpResponseServerError(f"An error occurred: {str(e)}")
    

@csrf_exempt
@require_POST
def show_more_compositions(request):
    try:
        initial_count = 3
        additional_count = 9
        all_items = list(Compositions.objects.all())
        initial_items = all_items[:initial_count]
        remaining_items = all_items[initial_count:]

        if len(remaining_items) > additional_count:
            more_items = remaining_items[:additional_count]
        else:
            more_items = remaining_items

        serialized_items = serializers.serialize('json', more_items)
        deserialized_items = json.loads(serialized_items)
        more_items_data = [
            {
                'name': item['fields']['name'],
                'price': item['fields']['price'],
                'photo_url': item['fields']['photo']
            }
            for item in deserialized_items
        ]

        return JsonResponse({'more_items': more_items_data})
    except Exception as e:
        # Выводим подробную информацию об ошибке
        import traceback
        traceback.print_exc()
        return HttpResponseServerError(f"An error occurred: {str(e)}")
    

@csrf_exempt
@require_POST
def show_more_busket(request):
    try:
        initial_count = 3
        additional_count = 9
        all_items = list(Busket.objects.all())
        initial_items = all_items[:initial_count]
        remaining_items = all_items[initial_count:]

        if len(remaining_items) > additional_count:
            more_items = remaining_items[:additional_count]
        else:
            more_items = remaining_items

        serialized_items = serializers.serialize('json', more_items)
        deserialized_items = json.loads(serialized_items)
        more_items_data = [
            {
                'name': item['fields']['name'],
                'price': item['fields']['price'],
                'photo_url': item['fields']['photo']
            }
            for item in deserialized_items
        ]

        return JsonResponse({'more_items': more_items_data})
    except Exception as e:
        # Выводим подробную информацию об ошибке
        import traceback
        traceback.print_exc()
        return HttpResponseServerError(f"An error occurred: {str(e)}")