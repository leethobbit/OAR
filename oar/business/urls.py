from django.urls import path
from iommi import Form
from iommi import Table

# from oar.animals.models import Animal  # noqa: ERA001
# from oar.people.models import Person  # noqa: ERA001
from .models import Location

app_name = "business"

urlpatterns = [
    path("", Table(auto__model=Location).as_view()),
    path("create_location/", Form.create(auto__model=Location).as_view()),
]
