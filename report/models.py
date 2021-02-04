from django.db import models

# Create your models here.
class Report(models.Model):
    code = models.CharField(max_length = 5)
    title = models.CharField(max_length = 30)
    contents = models.TextField()