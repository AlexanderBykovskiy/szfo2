from django.shortcuts import render, get_object_or_404
from .models import *
from feedback.forms import FeedbackForm


def index_page_view(request):

    page_object = get_object_or_404(StaticPageModel, slug='index')

    context = {
        'page_object': page_object,
    }

    return render(request, 'index-page.html', context)


def static_page_view(request, slug):
    page_object = get_object_or_404(StaticPageModel, slug=slug)

    context = {
        'page_object': page_object,
    }

    if slug == 'contacts':

        if request.method == 'POST':
            feedback_form = FeedbackForm(request.POST)
            if feedback_form.is_valid():
                print(feedback_form.cleaned_data)
                try:
                    feedback_form.save()
                    feedback_form = FeedbackForm()
                    context['is_sent_feedback'] = True
                except:
                    feedback_form.add_error(None, 'Ошибка отправки формы обратной связи.')
        else:
            feedback_form = FeedbackForm()

        context['feedback_form'] = feedback_form
        return render(request, 'contacts.html', context)

    else:
        return render(request, 'static-page.html', context)
