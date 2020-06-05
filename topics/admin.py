# Python imports
# Django imports
from django.contrib import admin
# Libraries imports
# App imports
from .models import Topic


class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'updated_at']
    search_fields = ['name']

admin.site.register(Topic, TopicAdmin)