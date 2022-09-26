from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import department_choices, title_choices

from .models import Requisition

def index(request):
    requisitions = Requisition.objects.order_by('-dateofrequisition').filter(is_published=True)

    paginator = Paginator(requisitions, 6)
    page = request.GET.get('page')
    paged_requisitions = paginator.get_page(page)

    context = {
        'requisitions': paged_requisitions
    }

    return render(request, 'requisitions/requisitions.html', context)

def requisition(request, requisition_id):
    requisition = get_object_or_404(Requisition, pk=requisition_id)

    context = {
        'requisition': requisition
    }
    return render(request, 'requisitions/requisitions.html', context)

def search(request):
    queryset_list = Requisition.objects.order_by('-dateofrequisition')

    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description_icontains=keywords)

    #Department
    if 'department' in request.GET:
        department = request.GET['department']
        if department:
            queryset_list = queryset_list.filter(department_iexact=department)

    #PositionTitle
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title_iexaxt=title)
    context = {
        'department_choices': department_choices,
        'title_choices': title_choices,
        'requisitions': queryset_list,
        'values': request.GET
    }    
    return render(request, 'requisitions/search.html', context)