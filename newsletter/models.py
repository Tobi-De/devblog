from django.db import models
from model_utils.models import TimeStampedModel


class Signup(TimeStampedModel):
    email = models.EmailField()

    def __str__(self):
        return self.email
