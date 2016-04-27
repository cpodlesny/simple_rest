from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200, blank=False)
    text = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return self.title
