from django.db import models
from account.models import User

# Create your models here.


class Production(models.Model):
    nom = models.CharField(max_length=50)
    date = models.DateField()
    quantite = models.FloatField()
    vendue = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="productions")
