from django.utils.html import format_html
from iommi import Page
from iommi import html

from oar.core import EditTable

from .models import Location
from .models import Meeting

location_table = EditTable(
    auto__model=Location,
    title="Locations",
)

meeting_table = EditTable(
    auto__model=Meeting,
    title="Meetings",
    # Turn on edit feature for columns
    # Columns to remove from view
    columns__minutes__include=False,
    # Styling attributes
    columns__meeting_url__cell__format=lambda value, **_: format_html(
        "<a href={} target='_blank'>{}</a>",
        value,
        value,
    ),
    columns__meeting_url__display_name="Meeting URL",
    create_form__fields__title__input__attrs__placeholder="Title",
    create_form__fields__meeting_url__input__attrs__placeholder=(
        "Google Drive link goes here."
    ),
)


class BusinessPage(Page):
    """
    The homepage for the Business module.
    """

    title = html.h1("Business Home")
    locations = location_table
    meetings = meeting_table
