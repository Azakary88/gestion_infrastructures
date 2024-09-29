from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Incident, Infrastructure, Utilisateur


class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['infrastructure', 'description', 'date_signalement']

class UtilisateurForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'password1', 'password2', 'role']

class InfrastructureForm(forms.ModelForm):
    class Meta:
        model = Infrastructure
        fields = ['nom', 'localisation', 'type_infrastructure', 'date_creation']