from django.db import models
from django.contrib.sessions.models import Session


class SparqlResult(models.Model):
    result = models.TextField()

class SparqlIntegerReuslt(models.Model):
    value = models.IntegerField()