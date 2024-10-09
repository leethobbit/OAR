from django.urls import path
from iommi import Form

import oar.business.views as business_views

from .models import Feedback
from .models import Location

app_name = "business"

urlpatterns = [
    path("", business_views.BusinessPage().as_view()),
    path("feedback/", Form.create_or_edit(auto__model=Feedback).as_view()),
    path("create_location/", Form.create(auto__model=Location).as_view()),
]
