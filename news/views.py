from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import *
from static_pages.models import StaticPageModel


class NewsList(ListView):
    model = NewsModel
    template_name = 'news.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return NewsModel.objects.filter(published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        page_object = get_object_or_404(StaticPageModel, id='news')
        context['page_object'] = page_object
        return context
