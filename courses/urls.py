# Python imports
# Django imports
from django.urls import path
# Libraries imports
# App imports
from courses.views import CourseList

urlpatterns = [
    # path('', views.index, name='index')
    path('', CourseList.as_view(), name='list')
]