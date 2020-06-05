# Python imports
# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Libraries imports
# App imports
from topics.models import Topic


class TopicList(LoginRequiredMixin, ListView):
    model = Topic
    context_object_name = 'topics'

    def get_queryset(self):
        return super(TopicList, self).\
            get_queryset().\
            filter(course__teacher=self.request.user).\
            order_by('name', 'updated_at').\
            distinct('name')
