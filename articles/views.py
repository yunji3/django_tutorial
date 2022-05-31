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