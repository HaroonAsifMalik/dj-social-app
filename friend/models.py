from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q

# Create your models here.
class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_friends')

    def clean(self):
        duplicate_friendship = Friend.objects.filter(Q(user=self.user, friend=self.friend) | Q(user=self.friend, friend=self.user)).exists()

        if self.user == self.friend:
            raise ValidationError("A user cannot be friends with themselves.")
        
        if duplicate_friendship:
            raise ValidationError("A friendship request already exists from the other user.")
