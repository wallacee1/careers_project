from django.shortcuts import render
from django.http import HttpResponse

from requisitions.models import Requisition
from hiringsupervisors.models import Hiringsupervisors

def index(request):
    requisitions = Requisition.objects.order_by('-dateofrequisition').filter(is_published=True)[:3]

    context = {
        'requisitions': requisitions
    }


    return render(request, 'pages/index.html', context)

def about(request):
    # Get all hiringsupervisors
    hiringsupervisors = Hiringsupervisors.objects.order_by('-hiredate')
    
    context = {
        'hiringsupervisors': hiringsupervisors,
    }
    return render(request, 'pages/about.html', context)
