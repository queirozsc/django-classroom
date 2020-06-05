# Python imports
# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Libraries imports
# App imports
from courses.models import Course


class CourseList(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = 'courses'

    def get_queryset(self):
        return super(CourseList, self).\
            get_queryset().\
            filter(teacher=self.request.user)
