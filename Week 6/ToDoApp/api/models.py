from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    pass


class TaskList(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_on = models.DateTimeField(auto_now=False)
    status = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'TaskList'
        verbose_name_plural = 'TaskLists'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.name, self.description, self.created_at, self.due_on, self.status)

