from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('show-more/', views.show_more, name='show_more'),
    path('show-more-compositions/', views.show_more_compositions, name='show_more-compositions'),
    path('show-more-busket/', views.show_more_busket, name='show_more-busket'),
    path('search/', views.Search.as_view(), name="search" )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)