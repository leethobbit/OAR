from iommi import Action

from oar.core import EditTable

from .models import MedicalUpdate

# Tables
medical_update_table = EditTable(
    auto__model=MedicalUpdate,
    title="Q Updates",
    actions__create_q_update=Action(
        display_name="Create New Update",
        attrs__href="/update/create/",
        attrs__class={"btn": True, "btn-info": True},
    ),
    # Search filters
    # Turn on edit feature for columns
    # Style Attributes
)
