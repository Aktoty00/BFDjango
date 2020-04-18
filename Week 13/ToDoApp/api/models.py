import logging
from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.validators import validate_file_size, validate_extension

logger = logging.getLogger(__name__)


class MyUser(AbstractUser):
    def _try_create_profile_for_user(self, created):
        if created:
            Profile.objects.get_or_create(user=self)

    def save(self, *args, **kwargs):
        logger.info(f'MyUser before saving')
        created = self.id is None
        super(MyUser, self).save(*args, **kwargs)
        self._try_create_profile_for_user(created)
        logger.info(f'MyUser after saving')


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(default='')
    address = models.TextField(default='')


class TaskList(models.Model):
    STATUS = (
        ("to do", "to do"),
        ("in process", "in process"),
        ("done", "done")
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_on = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, max_length=200, default="to do")
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)
    photo = models.ImageField(upload_to='taskList_photos',
                              validators=[validate_file_size,
                                          validate_extension],
                              null=True, blank=True)
    document = models.FileField(upload_to='taskList_documents',
                              validators=[validate_file_size, validate_extension],
                              null=True, blank=True)

    class Meta:
        verbose_name = 'TaskList'
        verbose_name_plural = 'TaskLists'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.name, self.description, self.created_at, self.due_on, self.status)

