from iommi import Action
from iommi import Page
from iommi import Table
from iommi import html

from oar.animals.models import Animal
from oar.animals.models import MedicalRecord
from oar.animals.models import Species
from oar.core import EditTable

# Tables
animal_table = EditTable(
    auto__model=Animal,
    title="Animals",
    actions__create_animal=Action(
        attrs__href="/animals/create/",
        attrs__class={"btn": True, "btn-success": True},
    ),
    columns__name__cell__url=lambda row, **_: row.get_absolute_url(),
    # Search filters
    columns__name__filter__include=True,
    columns__status__filter__include=True,
    columns__species__filter__include=True,
    # Turn on edit feature for columns
    columns__status__field__include=True,
    # Columns to remove from view
    columns__intake_date__include=False,
    columns__intake_type__include=False,
    columns__intake_condition__include=False,
    columns__outcome_date__include=False,
    columns__outcome_type__include=False,
    columns__updated_at__include=False,
    columns__animal_photo__include=False,
    # Style attributes
    columns__starting_weight__display_name="Weight",
    # TODO Figure out how to change text color for query form.
)

species_table = EditTable(
    auto__model=Species,
    title="Species",
    actions__create_species=Action(
        attrs__href="/animals/species/create/",
        attrs__class={"btn": True, "btn-info": True},
    ),
    # Search filters
    columns__name__filter__include=True,
    # Turn on edit feature for columns
    columns__is_ohio_native__field__include=True,
    # Style attributes
    columns__is_ohio_native__display_name="Ohio Native?",
    columns__class_name__display_name="Class",
)

# Forms


# Pages
class AnimalPage(Page):
    title = html.h1(lambda params, **_: params.animal.name)
    actions__create_animal = Action(
        attrs__href="/animals/create/",
    )
    medical_records = Table(
        auto__model=MedicalRecord,
        rows=lambda params, **_: MedicalRecord.objects.filter(animal=params.animal),
    )


class SpeciesPage(Page):
    pass
