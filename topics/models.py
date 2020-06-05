from django.db import models
from courses.models import Course


class Topic(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField('Turma', max_length=100)
    section = models.CharField('Séries', max_length=100)
    state = models.CharField('Situação', max_length=30)
    link = models.CharField('Link', max_length=100)
    teachers_email = models.CharField('Email professores', max_length=100)
    course_email = models.CharField('Email turma', max_length=100)
    created_at = models.DateTimeField("Criada em")
    updated_at = models.DateTimeField("Última atualização")
    mnemonic = models.CharField(max_length=4, null=True, blank=True)