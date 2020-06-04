from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'section', 'state', 'link', 'updated_at']
    search_fields = ['name', 'section']

admin.site.register(Course, CourseAdmin)