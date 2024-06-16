from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('show-more/', views.show_more, name='show_more'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)