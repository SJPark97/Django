import imp
import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def greeting(request):
    today = datetime.datetime(2022, 8, 8, 10, 2)

    foods = []
    # foods = ['apple', 'chicken', 'burger']
    six_foods = [food for food in foods if len(food) > 6]
    context = {
        'name' : 'justin', 
        'foods' : foods,
        'six_foods' : six_foods,
        'today' : today
    }
    return render(request, 'greeting.html', context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    # print(request)
    # print(type(request))
    # print(request.GET)
    department = request.GET.get('department')
    name = request.GET.get('name')
    if department == '대전 2반':
        if name == '김영주':
            message = '교수님이시군요!'
        else:
            message = '교육생이시군요!'
    else:
        message = '다른 반이시군요!'
    context = {
        'message' : message,
    }
    return render(request, 'catch.html', context)


def show(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'show.html', context)


