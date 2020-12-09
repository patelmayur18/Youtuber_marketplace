from django.shortcuts import render,redirect
from .models import Hiretuber
from django.contrib import  messages
# Create your views here.

    # first_name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    # tuber_id = models.IntegerField()
    # tuber_name = models.CharField(max_length=200)
    # email = models.CharField(max_length=100)
    # city = models.CharField(max_length=200)
    # phone = models.CharField(max_length=15)
    # state = models.CharField(max_length=200)
    # message = models.TextField(blank=True)
    # user_id = models.IntegerField(blank=True)
def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        email = request.POST['email']
        city = request.POST['city']
        phone = request.POST['phone']
        state = request.POST['state']
        message = request.POST['message']
        user_id = request.POST['user_id']

        hiretuber = Hiretuber(first_name=first_name,last_name=last_name,tuber_id=tuber_id,tuber_name=tuber_name,
                              email=email,city=city,phone=phone,state=state,message=message,user_id=user_id)
        hiretuber.save()
        messages.success(request,"Thanks for reching out")
        return redirect('home')
                              