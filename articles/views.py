from multiprocessing import context
import random
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dinner(request, name):
    menus = [{'name':'초밥','price':15000},{'name':'파스타', 'price':10000},{'name':'잔치국수', 'price': 5000}, {'name':'스테이크', 'price':30000}]
    pick = random.choice(menus)
    context = {
        'pick' : pick,
        'name' : name,
        'menus' : menus,
    }
    
    return render(request, 'dinner.html', context)

def review(request):
    return render(request, 'review.html')

def create_review(request):
    content = request.POST.get('content')
    print(request.POST)
    context = {
        'content' : content,
    }
    return render(request, 'review_result.html', context)