from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='requisitions'),
    path('<int:requisition_id>', views.requisition, name='requisition'),
    path('search', views.search, name='search'),
]