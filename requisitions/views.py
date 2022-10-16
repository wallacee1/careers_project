from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import title

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
    return render(request, 'requisitions/requisition.html', context)

def search(request):
  queryset_list = Requisition.objects.order_by('-dateofrequisition')

  # Keywords
  if 'keywords' in request.GET:
   keywords = request.GET['keywords']
   if keywords:
     queryset_list = queryset_list.filter(description__icontains=keywords)

  # Title
  if 'title' in request.GET:
    title = request.GET['title']
    if title:
      queryset_list = queryset_list.filter(title__iexact=title)

  context = {
    'title': title,
    'values': request.GET
  }