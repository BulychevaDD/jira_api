from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    name = models.CharField('Name', max_length=64, unique=True)
    users = models.ManyToManyField(User, verbose_name='Users')

    def __str__(self):
        return self.name


class Task(models.Model):
    create_datetime = models.DateTimeField('Created', auto_now_add=True)
    update_datetime = models.DateTimeField('Updated', auto_now=True)

    name = models.CharField('Name', max_length=64)
    description = models.TextField('Description')
    project = models.ForeignKey(Project, verbose_name='Project', related_name='tasks', on_delete=models.CASCADE)
    is_done = models.BooleanField('Is done', default=False)

    class Meta:
        unique_together = ('project', 'name', )

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='User', related_name='comments', on_delete=models.CASCADE)
    content = models.TextField('Content')
    task = models.ForeignKey(Task, verbose_name='Task', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:32]
