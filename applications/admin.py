from django.contrib import admin

from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'requisition', 'email', 'apply_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'requisition')
  list_per_page = 25

admin.site.register(Application, ApplicationAdmin)