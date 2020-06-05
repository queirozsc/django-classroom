from django.urls import path
from topics.views import TopicList

urlpatterns = [
    # path('', views.index, name='index')
    path('', TopicList.as_view(), name='list')
]