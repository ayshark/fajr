from django.shortcuts import render, redirect

from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import TrackerSerializer
from .models import Tracker
from .forms import TrackerForm



 #creating API endpoints using APIView

class TrackerAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    #list view
    def get(self, request):
        record = Tracker.objects.all().order_by('date')
        serializer = TrackerSerializer(record, many = True)
        return Response(
            serializer.data,
            status = status.HTTP_200_OK)
        
    
    def post(self, request):
        data = {
            'date': request.data.get('date'),
            'daily_status': request.data.get('daily_status')
        }
        serializer = TrackerSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, 
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

class TrackerDetailAPIView(APIView):
    permisssion_classes = [permissions.IsAuthenticated]

    def get_record(self, id):
        try:
            return Tracker.objects.get(id = id)
        except:
            return None

    def get(self, request, id):
        record = self.get_record(id)
        if not record:
            return Response(
                    {'res': 'Object does not exist'},
                    status = status.HTTP_400_BAD_REQUEST
            )
        serializer = TrackerSerializer(record)
        return Response(
            serializer.data, 
            status = status.HTTP_200_OK
        )
    
    def delete(self, request, id):
        record = self.get_record(id)
        if not record:
            return Response(
                {'res': 'Object does not exist'},
                status = status.HTTP_400_BAD_REQUEST
            )
        record.delete()
        return Response(
            {'res': 'Record deleted'},
            status = status.HTTP_200_OK
        )

    def put(self, request, id):
        record = self.get_record(id)
        if not record:
            return Response(
                {'res': 'Object does not exist'},
                status = status.HTTP_400_BAD_REQUEST
            )
        data = {
            'date': request.data.get('date'),
            'daily_status': request.data.get('daily_status')
        }
        serializer = TrackerSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )



# UI view

class TrackerViewSet(viewsets.ModelViewSet):
    queryset = Tracker.objects.all().order_by('date')
    serializer_class = TrackerSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

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

   