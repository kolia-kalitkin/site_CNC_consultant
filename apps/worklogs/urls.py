from django.urls import path
from apps.worklogs import views

urlpatterns = [
    path('', views.create, name='worklogs'),
]