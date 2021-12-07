from django.db import models

# Create your models here.
from django.urls import reverse


class QuestionBank(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    question = models.TextField(max_length=500)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('q:home')
