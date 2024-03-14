from django.urls import path
from . import views

urlpatterns = [
    path('', views.datatable_main,name='datatable'),
]
