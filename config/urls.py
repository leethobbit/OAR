# ruff: noqa
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views import defaults as default_views
from django.views.generic import TemplateView

from iommi import Form, Page, Table, html

from .menu import create_main_navbar
from oar.animals.models import Animal, Species
from oar.business.models import Location


class IndexPage(Page):
    header = html.h1("Welcome to Open Animal Rescue!")
    logo = html.img(
        attrs__src="static/images/dragon-4417431_1280.png",
        attrs__style__width="50%",
    )

    animals = Table(auto__model=Animal, page_size=5)
    species = Table(auto__model=Species, title="Species", page_size=5)
    location = Table(auto__model=Location, page_size=5)
    # create_animal = Form(auto__model=Animal)


urlpatterns = [
    path("", IndexPage().as_view(), name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("oar.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("animals/", include("oar.animals.urls", namespace="animals")),
    path("business/", include("oar.business.urls", namespace="business")),
    # ...
    # Media files
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
