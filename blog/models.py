import uuid
from django.utils import timezone
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='posts', null=True)

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='posts', null=True)
    author_name = models.CharField(max_length=30)

    def __str__(self):
        return self.author_name
