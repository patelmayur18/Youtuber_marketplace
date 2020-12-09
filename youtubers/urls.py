from django.urls import path

from .views import youtubers,youtuber_detail,search

urlpatterns = [
    path('', youtubers,name='youtubers'),
    path('search', search,name='search'),
    path('<int:id>', youtuber_detail,name='youtuber_detail'),
    
]
