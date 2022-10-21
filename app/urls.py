from django.urls import path
from . import views

urlpatterns = [
    path("", views.calcnormal),
    path("calc/", views.calculate)
]