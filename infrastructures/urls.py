from django.contrib import admin
from django.urls import path, include
from infrastructures import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.accueil, name='accueil'),  # Page d'accueil
    path('infrastructures/', views.list_infrastructures, name='list_infrastructures'),  # Liste des infrastructures
    path('signaler/', views.signaler_incident, name='signaler_incident'),  # Page de signalement
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Page de connexion
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Page de déconnexion
    path('admin/', admin.site.urls),  # Interface d'administration
    path('accounts/', include('django.contrib.auth.urls')),  # Inclusion des URLs d'authentification
    path('register/', views.register, name='register'),  # Route pour l'inscription
    path('ajouter/', views.ajouter_infrastructure, name='ajouter_infrastructure'),  # Route pour ajouter une infrastructurepath('ajouter/', views.ajouter_infrastructure, name='ajouter_infrastructure'),  # Route pour ajouter une infrastructure
    path('incidents/', views.incident_list, name='incident_list'), 
]
