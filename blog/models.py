import uuid
from django.utils import timezone
from django.db import models


class TimesStampedModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
    

class Category(TimesStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Post(TimesStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, 
                                 related_name='posts', null=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    

class Comment(TimesStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='posts', null=True)
    text = models.TextField()

    def __str__(self):
        return self.text


















    











