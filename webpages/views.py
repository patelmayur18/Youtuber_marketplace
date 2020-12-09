from django.shortcuts import render
from django.http import  HttpResponse
from .models import Slider,Team,Youtuber
from django.contrib.auth.decorators import  login_required
# Create your views here.
@login_required(login_url='login')
def home(request):
    sliders = Slider.objects.all()
    members = Team.objects.all()
    fetured_youtuber = Youtuber.objects.filter(is_featured=True)
    youtubers = Youtuber.objects.order_by('-created_date')
    context={
        'sliders':sliders,
        'members':members,
        'fetured_youtuber':fetured_youtuber,
        'youtubers':youtubers,
    }

    return render(request,'webpages/index.html',context)

@login_required(login_url='login')
def about(request):
    members = Team.objects.all()
    context ={
         'members':members
     }
    return render(request,'webpages/about.html',context)

@login_required(login_url='login')
def contact(request):
    return render(request,'webpages/contact.html')

@login_required(login_url='login')
def services(request):
    return render(request,'webpages/services.html')        