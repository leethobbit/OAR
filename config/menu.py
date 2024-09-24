from iommi import Menu
from iommi import MenuItem


def create_main_navbar():
    """
    This function is used to generate the navbar seen on most pages. Modifications here
    will propogate throughout the app unless overridden elsewhere.
    """
    return Menu(
        sub_menu={
            "home": MenuItem(url="/"),
            "animals": MenuItem(url="/animals"),
            "people": MenuItem(url="/people"),
            "medical": MenuItem(url="/medical"),
            "business": MenuItem(url="/business"),
            "speciestest": MenuItem(url="/animals/species"),
            "admin": MenuItem(url="/iommi-admin"),
            "login": MenuItem(
                display_name="Log in",
                url="/iommi-admin/login/?next=/",
                include=lambda request, **_: not request.user.is_authenticated,
            ),
            "log_out": MenuItem(
                display_name="Log out",
                url="/iommi-admin/logout/",
                include=lambda request, **_: request.user.is_authenticated,
            ),
        },
    )
