from django.contrib.auth.models import User
from django.db import models

from quiz_app.models import Quiz


class Foydalanuvchi(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, null=True)
    baho = models.FloatField()
    quiz = models.ForeignKey(Quiz, models.SET_NULL, null=True )
    def __str__(self):
        return self.user.username