from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

def index(request):
    return redirect(reverse('bus_stations'))

def reading_csv(file):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        bus_stations_list = []
        for row in reader:
            bus_stations_list.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    return bus_stations_list

def bus_stations(request):
    content_list = reading_csv('data-398-2018-08-30.csv')
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(content_list, 10)
    page = paginator.get_page(page_num)
    data = page.object_list
    context = {
        'bus_stations': data,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
