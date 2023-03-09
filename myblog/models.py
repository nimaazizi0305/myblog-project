from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class categories(models.Model):
    titel=models.CharField(max_length=150)

    def __str__(self):
        return self.titel

class Posts(models.Model):
    title=models.CharField(max_length=150)
    text=RichTextField()
    created=models.DateTimeField(default=timezone.now)
    auth=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(categories,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detial', kwargs={'pk': self.pk})












