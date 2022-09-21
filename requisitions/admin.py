from django.contrib import admin

from .models import Requisition

class RequisitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'positiontitle', 'is_published', 'wagerange', 'dateofrequisition', 'hiringsupervisors')
    list_display_links = ('id', 'positiontitle')
    list_filter = ('positiontitle',)
    list_editable = ('is_published',)
    search_fields = ('positiontitle', 'description', 'dateofrequisition', 'wagerange')
    list_per_page: 25

admin.site.register(Requisition, RequisitionAdmin)