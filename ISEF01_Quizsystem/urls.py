"""
URL configuration for ISEF01_Quizsystem project.

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
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_view, name='home'),
    path("frage-erstellen/", include("FrageErstellen.urls")),
    path("login/", include("Login.urls")),
    path("logout/", include("Logout.urls")),
    path("meine-inhalte/", include("MeineInhalte.urls")),
    path("frage/<int:frage_id>/", include("FrageAnzeigen.urls")),
    path("frage/<int:frage_id>/edit/", include("FrageBearbeiten.urls")),
    path("frage/<int:frage_id>/antwort/", include("AntwortErstellen.urls")),
    path("frage/<int:frage_id>/antwort/<int:antwort_id>/edit/",
         include("AntwortBearbeiten.urls")),
    path("startseite/", include("Startseite.urls")),
    path("quiz/", include("Quiz.urls")),
]
