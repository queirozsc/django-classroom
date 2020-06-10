# Python imports
# Django imports
from django.db import models
# Libraries imports
# App imports
from classroom.models.course import Course


class Topic(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField('Disciplina', max_length=100)
    created_at = models.DateTimeField("Criada em", auto_now_add=True)
    updated_at = models.DateTimeField("Última atualização")

    def __str__(self):
        return self.name

    @property
    def avatar_url(self):
        return "https://avatars.dicebear.com/v2/initials/%s.svg" % self.name

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ["name"]