from django.contrib import admin

from oar.animals.models import Animal
from oar.animals.models import MedicalRecord
from oar.animals.models import Species


# Register your models here.
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    """
    This customized admin view makes reviewing things in the site easier!
    """

    list_display = ("name", "description", "status", "species", "age", "donation_fee")
    list_filter = ("status",)


admin.site.register(MedicalRecord)
admin.site.register(Species)
