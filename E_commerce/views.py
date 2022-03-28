from django.shortcuts import redirect, render

from app.models import slider, Banner,Main_Category,Product

def BASE(request):
    return render(request,'base.html')


def HOME(request):
    sliders = slider.objects.all().order_by('-id')
    banners = Banner.objects.all().order_by('-id')
    main_category = Main_Category.objects.all().order_by('-id')
    product = Product.objects.filter(section__name='Top Deals Of The Day')
    context = {
        'sliders':sliders,
        'banners':banners,
        'main_category': main_category,
        'product' : product


    }
    return render(request, 'index.html',context)

def Error404(request):
    return render(request,'404.html')