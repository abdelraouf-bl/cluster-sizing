from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='billing'),
    path('', views.index, name='virtual-reality'),
    path('', views.index, name='tables'),
    path('', views.index, name='rtl'),
    path('', views.index, name='profile')
]
