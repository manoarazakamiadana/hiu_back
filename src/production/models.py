from django.db import models
from account.models import User

# Create your models here.


class Production(models.Model):
    quantite = models.FloatField()
    reste = models.FloatField()
    unite = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="productions")
