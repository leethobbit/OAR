from django.contrib import admin

from oar.business.models import Feedback
from oar.business.models import Location
from oar.business.models import Meeting


# Register your models here.
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    This customized admin view makes reviewing things in the site easier!
    """

    list_display = ("name", "email_address", "feedback_type", "feedback")
    list_filter = ("feedback_type",)


admin.site.register(Location)
admin.site.register(Meeting)
