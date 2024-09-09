from django.contrib import admin
from app.models import list
from app.models import TimeScale

class listAdmin(admin.ModelAdmin):
    list_display = ('model', 'Name', 'Create_At', 'Description', 'Deadline', 'TimeScale', 'Finished_At')
    search_fields = ('Name',)

admin.site.register(list, listAdmin)

class adminTimeScale(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(TimeScale, adminTimeScale)