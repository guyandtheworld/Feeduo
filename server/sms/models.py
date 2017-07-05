from django.core.validators import MaxValueValidator
from django.db import models


class SMS(models.Model):
    number = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(9999999999)])
    message_body = models.CharField(max_length=140)