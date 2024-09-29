from django.shortcuts import render, redirect
from .models import Infrastructure, Incident
from .forms import IncidentForm, InfrastructureForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .forms import UtilisateurForm


def accueil(request):
    return render(request, 'accueil.html')

def est_admin(user):
    return user.is_authenticated and user.role == 'Admin'  # Vérifie si l'utilisateur est connecté et est un admin

@login_required  # Assure-toi que l'utilisateur est connecté
@user_passes_test(est_admin)
def ajouter_infrastructure(request):
    if request.method == 'POST':
        form = InfrastructureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_infrastructures')  # Redirige vers la liste des infrastructures
    else:
        form = InfrastructureForm()
    return render(request, 'infrastructures/ajouter_infrastructure.html', {'form': form})

def signaler_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incident_list')
    else:
        form = IncidentForm()
    return render(request, 'infrastructures/signalement.html', {'form': form})

def incident_list(request):
    incidents = Incident.objects.all()  # Récupère tous les incidents
    return render(request, 'infrastructures/incident_list.html', {'incidents': incidents})

def register(request):
    if request.method == 'POST':
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige vers la page de connexion après l'inscription
    else:
        form = UtilisateurForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def list_infrastructures(request):
    if request.user.is_authenticated:
        user_role = request.user.role  # Assurez-vous que l'attribut `role` existe
        # Votre logique pour récupérer et afficher les infrastructures
    else:
        # Gérer le cas où l'utilisateur n'est pas authentifié
        # Rediriger vers la page de connexion ou afficher un message
        return redirect('login_url')  # Remplacez 'login_url' par votre URL de connexion

    # Continuez avec votre logique si l'utilisateur est authentifié
    return render(request, 'infrastructures/list.html', context)

@login_required
def list_infrastructures(request):
    infrastructures = Infrastructure.objects.all()
    return render(request, 'infrastructures/list.html', {'infrastructures': infrastructures})
# Create your views here.
