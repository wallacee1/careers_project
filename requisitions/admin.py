from django.contrib import admin

from .models import Requisition

class RequisitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'lowwage', 'highwage', 'dateofrequisition', 'manager')
    list_display_links = ('id', 'title')
    list_filter = ('title',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'dateofrequisition', 'lowwage', 'highwage',)
    list_per_page: 25

admin.site.register(Requisition, RequisitionAdmin)