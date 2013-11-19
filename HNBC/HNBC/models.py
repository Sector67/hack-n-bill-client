from django.contrib.auth.models import User
from django.db import models


class RFIDKey(models.Model):
    code = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, null=True, blank=True,)

    def __unicode__(self):
        return self.code

