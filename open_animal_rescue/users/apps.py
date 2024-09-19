import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "open_animal_rescue.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import open_animal_rescue.users.signals  # noqa: F401
