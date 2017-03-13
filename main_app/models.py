from __future__ import unicode_literals

from django.db import models
class saved_url(models.Model):
    link_vid=models.CharField(max_length=500)


    def __str__(self):
      return self.link_vid
