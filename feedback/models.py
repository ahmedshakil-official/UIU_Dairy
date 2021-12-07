from django.db import models

# Create your models here.


class Feedback(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    feedback = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name + ' ' + self.last_name