from iommi import Action
from iommi import Column
from iommi import EditTable

# This file will contain base iommi object defintions.


class Action(Action):
    pass


class EditTable(EditTable):
    """
    Extended EditTable definition for OAR. Adds edit and delete columns,
    and enhances table styling.
    """

    class Meta:
        columns__edit = Column.edit()
        columns__delete = Column.delete()
        # Search filters
        # Turn on edit feature for columns
        # Style attributes
        attrs__class = {
            "table-hover": True,
            "table-bordered": True,
            "grid gap-3": True,
        }
