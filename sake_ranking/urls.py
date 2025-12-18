from django.urls import path
from . import views

urlpatterns=[
    path("", views.sake_ranking, name="sake_ranking"),
]