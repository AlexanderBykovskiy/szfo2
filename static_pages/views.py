from django.shortcuts import render, get_object_or_404
from .models import *


def static_page_view(request, slug):

    page_object = get_object_or_404(StaticPageModel, slug=slug)

    context = {
        'page_object': page_object,
    }

    if (slug == 'contacts'):
        return render(request, 'contacts.html', context)
    else:
        return render(request, 'index.html', context)
