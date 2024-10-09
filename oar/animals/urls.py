from django.shortcuts import get_object_or_404
from django.urls import path
from iommi import Form
from iommi import Page
from iommi import Table
from iommi import html

import oar.animals.views as animal_views
from oar.animals.models import Animal
from oar.animals.models import MedicalRecord
from oar.animals.models import Species

app_name = "animals"

# Menu

# Tables

# Pages

# Forms


def edit_animal(request, animal_pk):
    animal = get_object_or_404(Animal, pk=animal_pk)
    return Form.edit(auto__instance=animal)


def delete_animal(request, animal_pk):
    animal = get_object_or_404(Animal, pk=animal_pk)
    return Form.delete(auto__instance=animal)


def edit_species(request, species_pk):
    species = get_object_or_404(Species, pk=species_pk)
    return Form.edit(auto__instance=species)


def delete_species(request, species_pk):
    species = get_object_or_404(Species, pk=species_pk)
    return Form.delete(auto__instance=species)


def animal_page(request, animal_pk):
    animal = get_object_or_404(Animal, pk=animal_pk)

    class AnimalPage(Page):
        title = html.h1(animal.name)
        medical_records = Table(auto__rows=MedicalRecord.objects.filter(animal=animal))

    return AnimalPage()


# URLs

urlpatterns = [
    path("", animal_views.animal_table.as_view(), name="animal-list"),
    path("species/", animal_views.species_table.as_view(), name="species-list"),
    path(
        "species/create/",
        Form.create(
            auto__model=Species,
        ).as_view(),
    ),
    path(
        "create/",
        Form.create(
            auto__model=Animal,
            auto__exclude=["intake_date", "outcome_date", "outcome_type", "updated_at"],
        ).as_view(),
    ),
    path("<animal_pk>/", animal_page),
    path("<animal_pk>/edit/", edit_animal),
    path("<animal_pk>/delete/", delete_animal),
    path("species/<species_pk>/edit/", edit_species),
    path("species/<species_pk>/delete/", delete_species),
]
