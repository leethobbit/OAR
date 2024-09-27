from iommi import Action
from iommi import Page
from iommi import Table
from iommi import html

from oar.animals.models import MedicalRecord

# Tables


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
