from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
from .models import Task

def index(request):
    art = Task.objects.get(title='index')
    return render(request, 'main/index.html', {"article": art})

def demand(request):
    art = Task.objects.get(title='demand')
    return render(request, 'main/demand.html', {"article": art})

def geography(request):
    art = Task.objects.get(title='geography')
    return render(request, 'main/geography.html', {"article": art})

def skills(request):
    art = Task.objects.get(title='skills')
    return render(request, 'main/skills.html', {"article": art})

def rv(request):
    art = Task.objects.get(title='rv')
    return render(request, 'main/rv.html', {"article": art})


def rv(request):
    url = 'https://api.hh.ru/vacancies?text=сисадмин+OR+системный%20администор+OR+system%20admin+OR+сис%20админ+OR+системный%20админ+OR+администратор%20систем+OR+системний%20адміністратор&date_from=2022-12-01&date_to=2022-12-31'
    response = requests.get(url).text
    vacancies = sorted(json.loads(response)["items"], key = lambda vac: int(vac['published_at'][8:10]), reverse=True)[:10]
    full_vac=[]
    for vacancy in vacancies:
        response = requests.get(f'https://api.hh.ru/vacancies/{vacancy["id"]}').text
        full_vac.append(json.loads(response))
    return render(request, 'main/rv.html', {'vacancies':full_vac})

