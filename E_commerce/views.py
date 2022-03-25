from django.shortcuts import redirect, render

from app.models import slider, Banner,Main_Category

def BASE(request):
    return render(request,'base.html')


def HOME(request):
    sliders = slider.objects.all().order_by('-id')[0:3]
    banners = Banner.objects.all().order_by('-id')[0:3]
    main_category = Main_Category.objects.all().order_by('-id')
    context = {
        'sliders':sliders,
        'banners':banners,
        'main_category': main_category


    }
    return render(request, 'index.html',context)