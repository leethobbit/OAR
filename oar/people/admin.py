from django.contrib import admin

from oar.people.models import Person
from oar.people.models import Role

admin.site.register(Person)
admin.site.register(Role)
