from django.shortcuts import redirect, render

from app.models import slider, Banner

def BASE(request):
    return render(request,'base.html')


def HOME(request):
    sliders = slider.objects.all()
    banners = Banner.objects.all()
    context = {
        'sliders':sliders,
        'banners':banners

    }
    return render(request, 'index.html',context)