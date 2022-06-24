from django.db import models

# Crée ici vos modèle de base de données

class History(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.TextField()
    result = models.CharField(max_length=50, default='None')
    error = models.BooleanField(default=False)
