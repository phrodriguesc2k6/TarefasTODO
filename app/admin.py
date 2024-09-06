from django.contrib import admin

from app.models import list

class listAdmin(admin.ModelAdmin):
    list_display = ('model', 'Name', 'Create_At', 'Description', 'Deadline', 'Finished_At')
    search_fields = ('Name',)

admin.site.register(list, listAdmin)