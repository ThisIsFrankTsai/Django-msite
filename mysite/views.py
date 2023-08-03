from django.shortcuts import render
from django.http import Http404,HttpResponse
from mysite.models import Product
import random


# Create your views here.

def about(request):
    quotes = ['平凡的腳步也可以走完偉大的行程。',   
    '每天醒來，敲醒自己的不是鐘聲，而是夢想。',
    '沒有口水與汗水，就沒有成功的淚水。',
    '別想一下造出大海，必須先由小河川開始。']

    quote = random.choice(quotes)

    return render(request, 'about.html', locals())

def listing(request):

    products = Product.objects.all().order_by('-price').exclude(qty=0)
    products2 = Product.objects.filter(qty=0)

    return render(request,'list.html',locals())

def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')
    #return HttpResponse('找不到指定的品項編號')
    #return HttpResponseNotFound('<h1>Page not found</h1>')
    return render(request, 'disp.html', locals())

def home(request):
    quotes = ['平凡的腳步也可以走完偉大的行程。',   
    '每天醒來，敲醒自己的不是鐘聲，而是夢想。',
    '沒有口水與汗水，就沒有成功的淚水。',
    '別想一下造出大海，必須先由小河川開始。']

    quote = random.choice(quotes)

    return render(request, 'home.html', locals())
