from django.shortcuts import get_object_or_404
from django.urls import path
from iommi import Form
from iommi import Page
from iommi import Table
from iommi import html

from oar.animals.models import Animal
from oar.animals.models import MedicalRecord
from oar.animals.models import Species
from oar.people.models import Person

app_name = "animals"

# Menu

# Tables

# Pages


def animal_page(request, animal):
    animal = get_object_or_404(Animal, name=animal)

    class AnimalPage(Page):
        title = html.h1(animal.name)
        medical_records = Table(auto__rows=MedicalRecord.objects.filter(animal=animal))
        foster = Table(auto__rows=Person.objects.filter(animal=animal))

    return AnimalPage()


# URLs

urlpatterns = [
    path(
        "",
        Table(auto__model=Animal, title="Animals").as_view(),
        name="animal-list",
    ),
    path(
        "species/",
        Table(
            auto__model=Species,
            title="Species",
            columns__name__cell__url=lambda value, **_: value.get_absolute_url(),
        ).as_view(),
        name="species-list",
    ),
    path(
        "create_or_edit/<int:pk>",
        Form.create_or_edit(
            auto__model=Species,
            instance=lambda **_: None,
        ).as_view(),
    ),
    path(
        "create_animal/",
        Form.create(
            auto__model=Animal,
            auto__exclude=["intake_date", "outcome_date", "outcome_type", "updated_at"],
        ).as_view(),
    ),
    path("pages/<animal>/", animal_page),
]
