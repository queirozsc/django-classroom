from django.urls import path
from courses.views import CourseList

urlpatterns = [
    # path('', views.index, name='index')
    path('', CourseList.as_view(), name='list')
]