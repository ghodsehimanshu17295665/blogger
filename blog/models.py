import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from .manager import UserManager


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


class User(AbstractUser, TimesStampedModel):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Post(TimesStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, 
                                 related_name='posts', null=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, 
                             related_name='posts') 
    
    def __str__(self):
        return self.title
    

class Comment(TimesStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='posts', null=True)
    text = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, 
                             related_name='comments')

    def __str__(self):
        return self.text
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_principal = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


# UserProfile.objects = UserAccountManager()



