from django.urls import path
from .views import CrearListaUser

urlpatterns = [
    path('', CrearListaUser.as_view()),
]