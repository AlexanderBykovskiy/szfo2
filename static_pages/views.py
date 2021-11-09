from django.shortcuts import render


def static_page_view(request, slug):
    context = {
        'title': slug,
        'page_id': slug,
    }
    return render(request, 'index.html', context)
