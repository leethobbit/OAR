from django.shortcuts import get_object_or_404
from django.urls import path
from iommi import Form
from iommi import Page
from iommi import html

import oar.people.views as people_views

from .models import Person
from .models import Role

app_name = "people"

# Menu

# Tables


# Pages
class PeopleIndex(Page):
    header = html.h1("People and Roles")

    people = people_views.people_table
    roles = people_views.roles_table


# Forms


def edit_person(request, person_pk):
    person = get_object_or_404(Person, pk=person_pk)
    return Form.edit(auto__instance=person)


def delete_person(request, person_pk):
    person = get_object_or_404(Person, pk=person_pk)
    return Form.delete(auto__instance=person)


def edit_role(request, role_pk):
    role = get_object_or_404(Role, pk=role_pk)
    return Form.edit(auto__instance=role)


def delete_role(request, role_pk):
    role = get_object_or_404(Role, pk=role_pk)
    return Form.delete(auto__instance=role)


urlpatterns = [
    path("", PeopleIndex().as_view(), name="people-list"),
    path(
        "create/",
        Form.create(
            auto__model=Person,
        ).as_view(),
    ),
    path("<person_pk>/edit/", edit_person),
    path("<person_pk>/delete/", delete_person),
    path("roles/", people_views.roles_table.as_view(), name="roles-list"),
    path(
        "roles/create/",
        Form.create(
            auto__model=Role,
        ).as_view(),
    ),
    path("roles/<role_pk>/edit/", edit_role),
    path("roles/<role_pk>/delete/", delete_role),
]
