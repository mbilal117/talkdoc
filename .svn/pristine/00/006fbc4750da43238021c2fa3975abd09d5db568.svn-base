from django.db import models
from django.contrib.auth.models import User
from TalkDoc.models import UserType


# Create your models here.

class UserExtended(models.Model):
    user = models.OneToOneField(User, unique=True)
    user_type = models.ForeignKey(UserType)

    def __unicode__(self):
        return unicode(self.user)
