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
            "species": MenuItem(url="/animals/species"),
            "people": MenuItem(url="/people"),
            "medical": MenuItem(url="/medical"),
            "business": MenuItem(url="/business"),
            "admin": MenuItem(
                url="/admin",
                include=lambda request, **_: request.user.is_authenticated,
            ),
            "login": MenuItem(
                display_name="Log in",
                url="/accounts/login/",
                include=lambda request, **_: not request.user.is_authenticated,
            ),
            "signup": MenuItem(
                display_name="Signup",
                url="/accounts/signup/",
                include=lambda request, **_: not request.user.is_authenticated,
            ),
            "log_out": MenuItem(
                display_name="Logout",
                url="/accounts/logout/",
                include=lambda request, **_: request.user.is_authenticated,
            ),
            "feedback": MenuItem(
                display_name="Feedback",
                url="business/feedback/",
            ),
        },
    )
