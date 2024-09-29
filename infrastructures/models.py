from django.db import models
from django.contrib.auth.models import AbstractUser

class Infrastructure(models.Model):
    nom = models.CharField(max_length=100)
    localisation = models.CharField(max_length=100)
    type_infrastructure = models.CharField(max_length=50)
    date_creation = models.DateField()

    def __str__(self):
        return self.nom

class Incident(models.Model):
    infrastructure = models.ForeignKey(Infrastructure, on_delete=models.CASCADE)
    description = models.TextField()
    date_signalement = models.DateField()
    est_resolu = models.BooleanField(default=False)

    def __str__(self):
        return f"Incident sur {self.infrastructure.nom}"

class Intervention(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    date_intervention = models.DateField()
    details = models.TextField()

    def __str__(self):
        return f"Intervention sur l'incident {self.incident.id}"


class Utilisateur(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Citoyen', 'Citoyen'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Citoyen')
