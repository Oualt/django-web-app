"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views # import views.py de l'application listings pour pouvoir l'appeler dans les urlspatterns
from django.shortcuts import redirect # permet de rediriger vers une autre url

urlpatterns = [
    path("", lambda request: redirect('bands/')), # redirige vers band_list si on ne met rien dans l'url
    path("admin/", admin.site.urls),
    path("bands/", views.band_list, name='band-list'), # correspond a def band_list(request) dans views.py
    path('bands/<int:id>/', views.band_detail, name='band-detail'), # permet de récupérer l'id du groupe dans l'url
    path('bands/add/', views.band_create, name='band-create'), # permet de créer un groupe
    path('bands/<int:id>/change/', views.band_update, name='band-update'), # permet de modifier un groupe
    path('bands/<int:id>/delete/', views.band_delete, name='band-delete'), # permet de supprimer un groupe
    path("about-us/", views.about),
    path("contact-us/", views.contact, name='contact'),
    path("email-envoye/", views.email_envoye, name='email-envoye'),
    path('listings/add/', views.listing_create, name='listing-create'), # permet de créer une annonce
]
