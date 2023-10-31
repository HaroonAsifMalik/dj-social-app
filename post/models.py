from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    date = models.DateField(auto_now=True)

class ResponseAgainstPost(models.Model):
    post = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share = models.BooleanField(default=False)
    like = models.BooleanField(default=False)
    comment = models.CharField(max_length=100, null=True, blank=True)