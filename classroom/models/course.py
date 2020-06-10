# Python imports
import re
# Django imports
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Libraries imports
# App imports

class Course(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField('Turma', max_length=100)
    section = models.CharField('Séries', max_length=100)
    state = models.CharField('Situação', max_length=30)
    link = models.CharField('Link', max_length=100)
    teachers_email = models.CharField('Email professores', max_length=100)
    course_email = models.CharField('Email turma', max_length=100)
    created_at = models.DateTimeField("Criada em")
    updated_at = models.DateTimeField("Última atualização")
    mnemonic = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def avatar_url(self):
        return "https://avatars.dicebear.com/v2/initials/%s.svg" % self.mnemonic

    class Meta:
        unique_together = ['id', 'teacher']
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['mnemonic', 'name']

@receiver(pre_save, sender="classroom.Course")
def generate_mnemonic(sender, instance, **kwargs):
    """
    Extracts mnemonic from course's name
    >>> mnemonic('EMPVS - 1º Ano A')
    '1A'

    Useful for generate dynamic avatars from https://avatars.dicebear.com/
    """
    regex = re.compile('\d')
    match = regex.search(instance.name)
    if match is None:
        return '00'
    digit = instance.name[match.start()]

    keyword = ' Ano '
    before_keyword, keyword, after_keyword = instance.name.partition(keyword)
    letter = after_keyword[0]
    instance.mnemonic = "{0}{1}".format(digit, letter)
