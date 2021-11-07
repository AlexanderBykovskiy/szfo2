from django.http import HttpResponseNotFound


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
