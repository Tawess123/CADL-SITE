import django.utils.timezone
from django.db import models
from django.utils import timezone
# Create your models here.
class Presence(models.Model):
    user = models.CharField('Nom', max_length=50)
    user_id = models.CharField('Numéro de carte', max_length=50)
    is_present = models.BooleanField('Présent')
    hour_of_presence = models.DateTimeField('Heure de la présence', default=django.utils.timezone.now)
    def __bool__(self):
        return self.is_present
    def __str__(self):
        return self.user