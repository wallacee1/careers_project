from django.shortcuts import render
from django.http import HttpResponse


from requisitions.models import Requisition
from manager.models import Manager

def index(request):
    requisitions = Requisition.objects.order_by('-dateofrequisition').filter(is_published=True)[:3]
    return render(request, 'pages/index.html')

def about(request):
    # Get all managers
    manager = Manager.objects.order_by('-hiredate')
    
    context = {
        'manager': manager,
    }
    return render(request, 'pages/about.html', context)
