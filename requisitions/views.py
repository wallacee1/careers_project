from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices

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

  # Keywords
  #if 'keywords' in request.GET:
  #  keywords = request.GET['keywords']
  #  if keywords:
  #    queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET
  }