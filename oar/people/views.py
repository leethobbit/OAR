from iommi import Action

from oar.core import EditTable

from .models import Person
from .models import Role

# Tables
people_table = EditTable(
    auto__model=Person,
    title="People",
    actions__create_person=Action(
        attrs__href="/people/create/",
        attrs__class={"btn": True, "btn-info": True},
    ),
    # Search filters
    # Turn on edit feature for columns
    # Style Attributes
)

roles_table = EditTable(
    auto__model=Role,
    title="Roles",
    actions__create_role=Action(
        attrs__href="/people/roles/create/",
        attrs__class={"btn": True, "btn-info": True},
    ),
)
