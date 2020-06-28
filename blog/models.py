from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel, SoftDeletableModel

User = get_user_model()


class Author(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Post(TimeStampedModel, SoftDeletableModel):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(blank=True)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"id": self.id})
