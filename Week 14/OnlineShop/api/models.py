import logging

from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.validators import validate_file_size, validate_file_extension, validate_image_extension

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


class CategoryList(models.Model):
    NAME = (
        ('home', 'home'),
        ('School', 'School'),
        ('Uni', 'Uni'),
        ('Dorm', 'Dorm'),
    )
    name = models.CharField(choices=NAME, max_length=200, default="home")
    desc = models.CharField(max_length=500, null=True)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)
    photo = models.ImageField(upload_to='Category_photos',
                              validators=[validate_file_size,
                                          validate_image_extension],
                              null=True, blank=True)
    document = models.FileField(upload_to='Category_documents',
                                validators=[validate_file_size, validate_file_extension],
                                null=True, blank=True)

    class Meta:
        verbose_name = 'CategoryList'
        verbose_name_plural = 'CategoryLists'

    def __str__(self):
        return 'Category name: {}'.format(self.name)


class ProductList(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    category = models.ForeignKey(CategoryList, on_delete=models.CASCADE, related_name='products', default=1)

    class Meta:
        verbose_name = 'ProductList'
        verbose_name_plural = 'ProductLists'

    def __str__(self):
        return 'Product name: {}'.format(self.name)

