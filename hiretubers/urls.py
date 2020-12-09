from django.urls import path

from .views import hiretuber

urlpatterns = [
    path('hiretuber/', hiretuber,name='hiretuber'),
]
