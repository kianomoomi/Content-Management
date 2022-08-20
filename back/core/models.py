from django.db import models
from django.contrib.auth.models import User


def content_directory_path(instance, filename):
    return f'{instance.title}_{instance.file_format}_{filename}'


class Content(models.Model):
    users = models.ManyToManyField(User)
    title = models.CharField(max_length=20)
    file_format = models.CharField(
        max_length=1,
        choices=[
            ('V', 'Video'),
            ('A', 'Audio'),
            ('D', 'Document')
        ]
    )
    file = models.FileField(upload_to=content_directory_path)
    extra = models.JSONField()

    class Meta:
        unique_together = (('title', 'file_format'),)
