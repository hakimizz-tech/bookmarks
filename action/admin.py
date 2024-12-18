from django.contrib import admin
from action.models import Action


# Register your models here.

@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ['user', 'verb', 'target', 'created' ]
    list_filter =  ['created']
    search_fields = ['verbs']