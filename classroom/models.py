import re
import requests
from allauth.account.signals import user_logged_in
from allauth.socialaccount.models import SocialToken
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.shortcuts import get_object_or_404


class CourseManager(models.Manager):
    def search(self, user_id, course_name):
        user = get_object_or_404(User, pk=user_id)
        return self.get_queryset().filter(
            teacher=user,
            name__icontains=course_name
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

    def __str__(self):
        return self.name

    @property
    def mnemonic(self):
        """
        Extracts mnemonic from course's name
        >>> mnemonic('EMPVS - 1º Ano A')
        '1A'

        Useful for generate dynamic avatars from https://avatars.dicebear.com/
        """
        regex = re.compile('\d')
        match = regex.search(self.name)
        if match is None:
            return '00'
        digit = self.name[match.start()]

        keyword = ' Ano '
        before_keyword, keyword, after_keyword = self.name.partition(keyword)
        letter = after_keyword[0]
        return "{0}{1}".format(digit, letter)

    @property
    def avatar_url(self):
        return "https://avatars.dicebear.com/v2/initials/%s.svg" % self.mnemonic

    class Meta:
        unique_together = ['id', 'teacher']
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['name']

@receiver(user_logged_in)
def retrieve_google_classroom_data(request, user, **kwargs):
    """After login, retrieve Google Classroom data"""
    # get the user's authorization token
    token = SocialToken.objects.filter(account__user=user, account__provider='google')
    # save courses' data
    url = 'https://classroom.googleapis.com/v1/courses/'
    print(url)
    headers = {
        'content-type': 'application/json',
    }
    response = requests.get(
        url,
        params={'access_token': token[0].token},
        headers=headers)
    courses = response.json()['courses']
    Course.objects.filter(teacher=user).delete()
    for course in courses:
        Course.objects.create(
            id=course['id'],
            teacher=user,
            name=course['name'],
            section=course['section'],
            state=course['courseState'],
            link=course['alternateLink'],
            teachers_email=course['teacherGroupEmail'],
            course_email=course['courseGroupEmail'],
            created_at=course['creationTime'],
            updated_at=course['updateTime']
        )
