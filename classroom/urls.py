# Python imports
# Django imports
from django.urls import path
# Libraries imports
# App imports
from classroom.views.course import CourseList
from classroom.views.topic import TopicList

urlpatterns = [
    path('turmas/', CourseList.as_view(), name='course-list'),
    path('disciplinas/', TopicList.as_view(), name='topic-list')
]
