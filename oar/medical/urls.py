from django.shortcuts import get_object_or_404
from django.urls import path
from iommi import Form

import oar.medical.views as medical_views

from .models import MedicalUpdate

app_name = "medical"

# Menu

# Tables

# Pages

# Forms


def edit_medical_update(request, medical_update_pk):
    medical_update = get_object_or_404(MedicalUpdate, pk=medical_update_pk)
    return Form.edit(auto__instance=medical_update)


def delete_medical_update(request, medical_update_pk):
    medical_update = get_object_or_404(MedicalUpdate, pk=medical_update_pk)
    return Form.delete(auto__instance=medical_update)


urlpatterns = [
    path("", medical_views.medical_update_table.as_view(), name="medical-list"),
    path(
        "create/",
        Form.create(
            auto__model=MedicalUpdate,
        ).as_view(),
    ),
    path("<medical_update_pk>/edit/", edit_medical_update),
    path("<medical_update_pk>/delete/", delete_medical_update),
]
