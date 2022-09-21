from django.contrib import admin

from .models import Hiringsupervisors

class HiringsupervisorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hiredate')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Hiringsupervisors, HiringsupervisorsAdmin)
