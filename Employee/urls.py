from django.http import request
from django.urls import path

from . import views

urlpatterns = [
    path("empregister", views.empregister, name="empregister"),
    path("details", views.details, name="details"),
    path("employeeProfile", views.employeeProfile, name="employeeProfile"),
    path("edit", views.edit, name="edit"),
    path("update", views.update, name="update"),
    path("employeeEdit", views.employeeEdit, name="employeeEdit"),
    path("employeeUpdate", views.employeeUpdate, name="employeeUpdate"),
    path("delete", views.destroy, name="delete"),
]
