from django.shortcuts import render,get_object_or_404
from webpages.models import Youtuber
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def youtubers(request):
    all_tuber = Youtuber.objects.order_by('-created_date')
    context = {
        'all_tuber':all_tuber,
    }
    return render(request,'youtubers/tubers.html',context)

@login_required(login_url='login')
def youtuber_detail(request,id):
    tuber = get_object_or_404(Youtuber,pk=id)
    context = {
        'tuber':tuber,
    }
    return render(request,'youtubers/singlepage.html',context)

@login_required(login_url='login')
def search(request):
    all_tuber = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city',flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type',flat=True).distinct()
    category_search = Youtuber.objects.values_list('category',flat=True).distinct()

    if 'keyword' in request.GET:
        print(request.GET)
        print('---1')
        keyword = request.GET['keyword']
        if keyword:
            all_tuber = all_tuber.filter(discription__icontains=keyword)

    if 'city' in request.GET:
        print(request.GET)
        print("---2")
        city = request.GET['city']
        if city:
            all_tuber = all_tuber.filter(city__iexact=city)

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            all_tuber = all_tuber.filter(camera_type__iexact=camera_type)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            all_tuber = all_tuber.filter(category__iexact=category)                


    context ={
        'all_tuber':all_tuber,
        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_search':category_search,
    }
    return render(request,'youtubers/search.html',context)
