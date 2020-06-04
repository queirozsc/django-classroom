import requests
from django.db import models
from django.contrib.auth.models import User
from allauth.account.signals import user_logged_in
from django.dispatch import receiver, Signal


class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            teacher_id=get_user(),
            name__icontains=query
        )

class Course(models.Model):

    id = models.CharField(max_length=12, primary_key=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Turma', max_length=100)
    section = models.CharField('Séries', max_length=100)
    state = models.CharField('Situação', max_length=30)
    link = models.CharField('Link', max_length=100)
    teachers_email = models.CharField('Email professores', max_length=100)
    course_email = models.CharField('Email turma', max_length=100)
    created_at = models.DateTimeField("Criada em")
    updated_at = models.DateTimeField("Última atualização")

    objects = CourseManager()

    class Meta:
        unique_together = ['id', 'teacher']

def on_login(request, user, **kwargs):
    api_endpoint = 'https://classroom.googleapis.com/v1/courses'
    response = requests.get(api_endpoint)
    courses = response.json()