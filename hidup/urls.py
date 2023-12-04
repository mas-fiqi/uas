from django.urls import path
from . import views

urlpatterns = [
    path('hidup/', views.hidup, name='hidup'),
]