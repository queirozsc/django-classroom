# Python imports
# Django imports
from django.contrib import admin
# Libraries imports
# App imports
from classroom.models.course import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'section', 'state', 'link', 'updated_at']
    search_fields = ['name', 'section']


admin.site.register(Course, CourseAdmin)
