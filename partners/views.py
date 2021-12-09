from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from static_pages.models import StaticPageModel
from .models import *


class PartnersList(ListView):
    model = PartnersModel
    paginate_by = 24
    template_name = 'partners.html'
    context_object_name = 'partners_list'

    def get_queryset(self):
        return PartnersModel.objects.filter(published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        page_object = get_object_or_404(StaticPageModel, id='partners')
        context['page_object'] = page_object
        return context


class PartnersItem(DetailView):
    model = PartnersModel
    template_name = 'partners-item.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'partner_item'

    def get_object(self, **kwargs):
        obj = super().get_object()
        if obj.published:
            return obj
        else:
            raise Http404('Запись не найдена')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_object'] = {
            'id': 'partners',
            'header': self.object.header
        }
        return context
