import os
from pathlib import Path
import environ
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from static_pages.models import StaticPageModel
from .models import *


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


class ArticlesList(ListView):
    model = ArticlesModel
    paginate_by = 24
    template_name = 'articles.html'
    context_object_name = 'articles_list'

    def get_queryset(self):
        return ArticlesModel.objects.filter(published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        page_object = get_object_or_404(StaticPageModel, id='articles')

        og_object = {
            'title': page_object.header,
            'description': page_object.page_description,
            'site_name': env('DOMAIN'),
        }

        page_object.og = og_object

        context['page_object'] = page_object
        return context


class ArticlesItem(DetailView):
    model = ArticlesModel
    template_name = 'articles-item.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'article_item'

    def get_object(self, **kwargs):
        obj = super().get_object()
        if obj.published:
            return obj
        else:
            raise Http404('Статья не найдена')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        og_object = {
            'title': self.object.header,
            'description': self.object.short_content,
            'image': self.object.cover,
            'type': 'article',
            'url': self.object.get_absolute_url(),
            'site_name': env('DOMAIN'),
        }

        context['page_object'] = {
            'id': 'articles',
            'header': self.object.header,
            'og': og_object,
        }
        return context


class PublicationsList(ListView):
    model = PublicationsModel
    paginate_by = 24
    template_name = 'publications.html'
    context_object_name = 'publications_list'

    def get_queryset(self):
        return PublicationsModel.objects.filter(published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        page_object = get_object_or_404(StaticPageModel, id='publications')

        og_object = {
            'title': page_object.header,
            'description': page_object.page_description,
            'site_name': env('DOMAIN'),
        }

        page_object.og = og_object

        context['page_object'] = page_object
        return context

# class PublicationsItem(DetailView):
#    model = PublicationsModel
#    template_name = 'publications-item.html'
#    slug_url_kwarg = 'slug'
#    context_object_name = 'publication_item'

#    def get_object(self, **kwargs):
#        obj = super().get_object()
#        if obj.published:
#            return obj
#        else:
#            raise Http404('Публикация не найдена')

#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['page_object'] = {
#            'id': 'publications',
#            'header': self.object.header
#        }
#        return context
