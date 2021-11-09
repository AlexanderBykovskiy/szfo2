from django import template
from static_pages.models import *


register = template.Library()


@register.simple_tag()
def get_main_menu():
    return MainMenuModel.objects.all()


@register.inclusion_tag('static_pages/main_menu.html')
def main_menu_block(active_page_id=None):
    main_menu_list = MainMenuModel.objects.all()
    return {
        'main_menu_list': main_menu_list,
        'active_page_id': active_page_id,
    }
