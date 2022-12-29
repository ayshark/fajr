from django.shortcuts import render, redirect

from rest_framework import viewsets
from .serializer import TrackerSerializer
from .models import Tracker
from .forms import TrackerForm

class TrackerViewSet(viewsets.ModelViewSet):
    queryset = Tracker.objects.all().order_by('date')
    serializer_class = TrackerSerializer

def read_data(request):
    records = Tracker.objects.all().order_by('date')
    context = {
        'records': records #omitting context or keeping it empty won't render the table
    }
    return render(request, r'C:\\Users\Aysha\Desktop\\misc\django2\\fajr\\fajr\\tracker\\templates\\tracker\\read.html', context)
    # return render(request, 'templates/tracker/read.html', context)

def create_data(request):
    form = TrackerForm()

    if request.method == 'POST':
        form = TrackerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read-data')
    context = {
        'form': form,
    }

    return render(request, r'C:\\Users\Aysha\Desktop\\misc\django2\\fajr\\fajr\\tracker\\templates\\tracker\\create.html', context)

def edit_data(request, pk):    
    record = Tracker.objects.get(id=pk)
    form = TrackerForm(instance = record)

    if request.method == 'POST':
        form = TrackerForm(request.POST, instance = record)
        if form.is_valid():
            form.save()
            return redirect('read-data')

    context = {
        'form': form,
        'record': record,
    }

    return render(request, r'C:\\Users\Aysha\Desktop\\misc\django2\\fajr\\fajr\\tracker\\templates\\tracker\\edit.html', context)

def delete_data(request, pk):
    record = Tracker.objects.get(id=pk)
    records = Tracker.objects.all().order_by('date')
    y = record.delete()
    redirect('read-data')

    # if request.method == 'POST': 
    #     y = record.delete()
    #     return redirect('read-data')

    context = {
        'record': record,
        'records': records,
        'deleted': y,
    }
    return render(request, r'C:\\Users\Aysha\Desktop\\misc\django2\\fajr\\fajr\\tracker\\templates\\tracker\\read.html', context)


    #C:\\Users\Aysha\Desktop\\misc\django2\\fajr\\fajr\\tracker\\templates\\tracker\\read.html