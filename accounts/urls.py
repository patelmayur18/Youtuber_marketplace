from django.urls import path

from .views import dashboard,login,register,logout

urlpatterns = [
    path('dashboard/', dashboard,name='dashboard'),
    path('login/', login,name='login'),
    path('register/', register,name='register'),
    path('logout/', logout,name='logout'),
]
