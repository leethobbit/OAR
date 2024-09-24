# Imports here
from config.menu import create_main_navbar

menu = create_main_navbar().refine_done()


class GlobalMenu:
    def __init__(self, request):
        self.request = request

    def __str__(self):
        return menu.bind(request=self.request).__html__()


def get_global_menu(request):
    return {
        "menu": GlobalMenu(request),
    }
