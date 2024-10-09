from iommi import Asset
from iommi import Style
from iommi.style_bootstrap5 import bootstrap5


def set_base_style():
    """
    Sets the style for iommi - all global style changes should go here.
    """
    return Style(
        bootstrap5,
        base_template="base.html",
        root__assets={
            "oar_main_css": Asset.css(
                attrs__href="https://bootswatch.com/5/darkly/bootstrap.min.css",
                attrs__crossorigin="anonymous",
            ),
            "oar_custom_css": Asset.css(attrs__href="/static/css/custom.css"),
        },
        DebugMenu={
            "attrs__class": {
                "bg-light": True,
                "text-secondary-emphasis": True,
            },
        },
    )
