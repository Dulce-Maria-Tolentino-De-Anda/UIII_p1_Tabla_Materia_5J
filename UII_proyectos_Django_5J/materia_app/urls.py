from django.urls import path
from materia_app import views
urlpatterns = [
    path("", views.inicio_vista, name="inicio_visita")
]
