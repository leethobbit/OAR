import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "oar.users"
    verbose_name = _("Users")

    def ready(self):
        from iommi import register_style

        from config.style import set_base_style

        with contextlib.suppress(ImportError):
            import oar.users.signals  # type: ignore  # noqa: F401, PGH003

        my_style = set_base_style()
        register_style("my_style", my_style)
