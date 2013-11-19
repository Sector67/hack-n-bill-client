from django.contrib.auth.models import User
from django.utils.timezone import utc
from django.db import models

import datetime

def now():
    return datetime.datetime.utcnow().replace(tzinfo=utc)


# The RFID key object
class RFIDKey(models.Model):
    code = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, null=True, blank=True,)

    def __unicode__(self):
        return self.code


# An object to store transaction data
class RFIDLog(models.Model):
    key = models.ForeignKey('RFIDKey')
    time = models.DateTimeField(default=datetime.datetime.utcnow().replace(tzinfo=utc), blank=True)
    meta = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.time)
