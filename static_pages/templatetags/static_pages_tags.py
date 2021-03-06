from django import template
from static_pages.models import *
from news.models import NewsModel
from partners.models import PartnersModel


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


@register.inclusion_tag('static_pages/main_mobil_menu.html')
def main_mobil_menu_block(active_page_id=None):
    main_menu_list = MainMenuModel.objects.all()
    return {
        'main_menu_list': main_menu_list,
        'active_page_id': active_page_id,
    }


@register.inclusion_tag('static_pages/page_title.html')
def page_title_block(page_title):
    return {'page_title': page_title}


@register.inclusion_tag('static_pages/data_block.html')
def data_block(block_id):
    try:
        data = ContentBlockModel.objects.get(id=block_id).content
    except ContentBlockModel.DoesNotExist:
        data = None
    return {'data_block': data, 'block_id': block_id}


@register.inclusion_tag('static_pages/pagination.html')
def pagination_block(paginator, page_obj):
    return {
        'paginator': paginator,
        'page_obj': page_obj,
    }


@register.inclusion_tag('static_pages/news_front_block.html')
def news_front_block():
    last_news_list = NewsModel.objects.all()[:6]
    return {
        'last_news_list': last_news_list,
    }


@register.inclusion_tag('static_pages/partners_front_block.html')
def partners_front_block(selector):
    partners_list = PartnersModel.objects.all()
    return {
        'partners_list': partners_list,
        'selector': selector,
    }


@register.inclusion_tag('static_pages/slider_block.html')
def slider_block():
    slider_list = NewsModel.objects.all()[:4]
    if slider_list:
        return {'slider_list': slider_list}
    else:
        return {'slider_list': None}


@register.inclusion_tag('static_pages/og_block.html')
def og_block(og_object):
    return {'og_object': og_object}
